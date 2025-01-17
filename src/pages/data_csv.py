from dash import callback, dash_table, dcc, html, Input, Output
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

df = pd.read_csv('./data/data-goldstandard/rsvnet_hospitalization_us_only.csv')

header = html.H1('Data CSV')

chart = dcc.Graph(figure=px.histogram(df, x='date', y='value'), id="my-plot")

table = dash_table.DataTable(
  data=df.to_dict('records'),
  page_size=20,
  id="my-table")

layout = html.Div([
  header,
  dmc.Stack([chart, table])
])
