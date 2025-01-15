from dash import callback, dcc, html
import dash_mantine_components as dmc
from dash import Input, Output, State, html

import dash_mantine_components as dmc
from dash_iconify import DashIconify

drawer = html.Div(
  [
    dmc.ActionIcon(
      DashIconify(icon="feather:menu", width=16),
      id="drawer-toggle",
      variant="subtle",
      n_clicks=0,
      m="md",
    ),
    dmc.Drawer(
      title="Drawer",
      id="drawer",
      padding="md",
      position="left",
      size=350,
      style={"display": "block"}
    ),
  ]
)

@callback(
  Output("drawer", "opened"),
  Input("drawer-toggle", "n_clicks"),
  prevent_initial_call=True,
)
def sliding_drawer(n_clicks):
  return True
