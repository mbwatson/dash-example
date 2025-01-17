from dash import callback, dash_table, dcc, html, Input, Output
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

df = pd.read_csv('./data/data-goldstandard/rsvnet_hospitalization_us_only.csv')

header = html.H1('Data')

layout = html.Div([
  header,
  dmc.Stack([
    dcc.Graph(figure=px.histogram(df, x='date', y='value'), id="my-plot"),
    dash_table.DataTable(
      data=df.to_dict('records'),
      page_size=20,
      id="my-table"
    ),
  ])
])

@callback(
  Output("my-table", "data"),
  [Input("my-plot", "clickData")]
)
def on_trace_click(click_data):
    """Listen to click events and update table, passing filtered rows"""
    p = trace_click['points'][0]

    # here, use 'customdata' property of clicked point, 
    # could also use 'curveNumber', 'pointIndex', etc.
    if 'customdata' in p:
        key = p['customdata']['my-key']

    df_f = get_corresponding_rows(df, key)

    return df_f.to_dict('records')

def get_corresponding_rows(df, my_key):
    """Filter df, return rows that match my_key"""
    return df[df['key-column'] == my_key]