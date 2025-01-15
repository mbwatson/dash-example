from dash import Dash, dcc, html, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from src.components.navbar import navbar
from src.pages import home, about, contact
from src.theme import DEFAULT_THEME
import os


assets_path = os.getcwd() +'/src/assets'

app = Dash()
app.title = 'Dash Dashboard'
app.layout = dmc.MantineProvider(
  theme=DEFAULT_THEME,
  id="mantine-provider",
  children=html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dmc.Container(id='page-content', size=1200, style={"margin-top": "2rem"}),
  ])
)

# routing
@app.callback(
  Output('page-content', 'children'),
  [Input('url', 'pathname')]
)
def display_page(pathname):
  if pathname == '/about':
    return about.create_page()
  if pathname == '/contact':
    return contact.create_page()
  else:
    return home.create_page()

# run the app
if __name__ == '__main__':
  app.run(debug=True)
