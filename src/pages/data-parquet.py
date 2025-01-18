import dash
from dash import callback, dash_table, dcc, html, Input, Output
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

df = pd.read_parquet('./data/visualization/data-visualization/models/round1/inc hosp/US/sample/part-0.parquet')

print(df)

header = html.H1('Data Parquet')

layout = html.Div([
  header,
  'Coming soon...',
])

dash.register_page("data-parquet", layout=layout, path="/data-parquet")
