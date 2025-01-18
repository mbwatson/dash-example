import dash
from dash import Dash, callback, dash_table, dcc, html, Input, Output
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

filename = 'data-goldstandard/rsvnet_hospitalization_us_only.csv'
df = pd.read_csv(f'./data/{filename}')
df['date'] = pd.to_datetime(df['date'])  # ensure 'date' is in datetime format

header = html.H1('Data CSV')

chart = dcc.Graph(
  id='chart',
  figure=px.histogram(df, x='date', y='value', title=filename)
)

table = dash_table.DataTable(
  data=df.to_dict('records'),
  page_size=20,
  id='data-table',
  columns=[{'name': col, 'id': col} for col in df.columns]
)

layout = html.Div([
  header,
  dmc.Stack([chart, table])
])

@callback(
  Output('data-table', 'data'),
  Input('chart', 'relayoutData')
)
def sync_table(relayout_data):
  if not relayout_data or 'xaxis.range[0]' not in relayout_data:
    return df.to_dict('records')
  
  x_start = pd.to_datetime(relayout_data['xaxis.range[0]'])
  x_end = pd.to_datetime(relayout_data['xaxis.range[1]'])
  
  filtered_df = df[(x_start <= df['date']) & (df['date'] <= x_end)]
  return filtered_df.to_dict('records')

dash.register_page("data-csv", layout=layout, path="/data-csv")
