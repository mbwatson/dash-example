from dash import Dash, _dash_renderer, dcc, Input, Output, State, callback, clientside_callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from src.pages import home, about, contact, data_csv, data_parquet, not_found
from src.components.layout import layout
from src.theme import DEFAULT_THEME

_dash_renderer._set_react_version('18.2.0')

app = Dash(__name__, external_stylesheets=dmc.styles.ALL)

app.title = 'Dash Dashboard'
app.layout = dmc.MantineProvider(
  theme=DEFAULT_THEME,
  id='mantine-provider',
  children=layout,
)

server = app.server

# routing
@callback(
  Output('page-content', 'children'),
  Input('url', 'pathname'),
)
def display_page(pathname):
  if pathname == '/about':
    return about.layout
  if pathname == '/contact':
    return contact.layout
  if pathname == '/data-csv':
    return data_csv.layout
  if pathname == '/data-parquet':
    return data_parquet.layout
  if pathname == '/':
    return home.layout
  else:
    return not_found.layout

if __name__ == '__main__':
  app.run_server(debug=True)
