import dash
from dash import Dash, callback, dash_table, dcc, html, Input, Output
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

# used for reading and for showing in ui
filename = 'data-goldstandard/rsvnet_hospitalization_us_only.csv'

# load data
df = pd.read_csv(f'./data/{filename}')
df['date'] = pd.to_datetime(df['date']) # ensure 'date' is in datetime format

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

table = dash_table.DataTable(
  data=df.to_dict('records'),
  page_size=20,
  id='data-table',
  columns=[{'name': col, 'id': col} for col in df.columns],
  style_header={
    'color': 'var(--color-container-fg)',
    'backgroundColor': 'var(--color-container-bg)',
    'fontWeight': 'bold',
  },
  style_data={
    'color': 'var(--color-container-fg)',
    'backgroundColor': 'var(--color-container-bg)',
    'fontSize': '80%',
  },
)

layout = html.Div([
  html.H1('Data CSV'),
  dmc.Stack([chart, table])
])

# match chart colors to app color scheme setting
@callback(
  Output('csv-chart', 'figure'),
  Input('theme-store', 'data'),
)
def align_chart_theme(theme):
  return themed_figure(theme)

# sync data in data table with that of chart
@callback(
  Output('data-table', 'data'),
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
