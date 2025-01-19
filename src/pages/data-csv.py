import dash
from dash import Dash, callback, dash_table, dcc, html, Input, Output
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

# used for reading and for showing in ui
filename = 'data-goldstandard/rsvnet_hospitalization_us_only.csv'

# load data
df = pd.read_csv(f'./data/{filename}')
df['date'] = pd.to_datetime(df['date']) # ensure 'date' is in datetime format

### chart

# template themes dict for toggling to match app color scheme
templates = {
  'light': 'plotly_white',
  'dark': 'plotly_dark',
}

def themed_figure(theme = 'light'):
  return px.scatter(df, x='date', y='value', title=filename, template=templates[theme])

chart = dcc.Graph(
  id='csv-chart',
  className='figure',
  figure=themed_figure(),
  config={
    'modeBarButtonsToRemove': ['select', 'lasso2d'],
    'displaylogo': False,
  },
)

### data table

def grid_class(theme = 'light'):
  return 'ag-theme-quartz' if theme == 'light' else 'ag-theme-quartz-dark'

grid = dag.AgGrid(
  id="csv-data-grid",
  className=grid_class(),
  rowData=df.to_dict("records"),
  columnDefs=[{"field": i, 'filter': True} for i in df.columns],
  columnSize="sizeToFit",
  dashGridOptions={'pagination': True},
)

### layout

layout = html.Div([
  html.H1('Data CSV'),
  dmc.Stack([chart, grid])
])

## callbacks

# match chart and table colors to current color scheme setting
@callback(
  Output('csv-chart', 'figure'),
  Output('csv-data-grid', 'className'),
  Input('theme-store', 'data'),
)
def align_chart_theme(theme):
  return themed_figure(theme), grid_class(theme)

# sync data in data table with that of chart
@callback(
  Output('csv-data-grid', 'rowData'),
  Input('csv-chart', 'relayoutData')
)
def sync_table(relayout_data):
  if not relayout_data or 'xaxis.range[0]' not in relayout_data:
    return df.to_dict('records')
  
  x_start = pd.to_datetime(relayout_data['xaxis.range[0]'])
  x_end = pd.to_datetime(relayout_data['xaxis.range[1]'])
  
  filtered_df = df[(x_start <= df['date']) & (df['date'] <= x_end)]
  return filtered_df.to_dict('records')

dash.register_page("data-csv", layout=layout, path="/data-csv")
