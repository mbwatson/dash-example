from dash import Dash, _dash_renderer, dcc, Input, Output, State, callback, clientside_callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from src.components.layout import layout
from src.theme import DEFAULT_THEME

_dash_renderer._set_react_version('18.2.0')

app = Dash(
  __name__,
  external_stylesheets=dmc.styles.ALL,
  use_pages=True,
  pages_folder='src/pages'
)

app.title = 'Dash Dashboard'
app.layout = dmc.MantineProvider(
  theme=DEFAULT_THEME,
  id='mantine-provider',
  children=layout,
)

server = app.server

if __name__ == '__main__':
  app.run_server(debug=True)
