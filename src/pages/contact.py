import dash
from dash import html

header = html.H1('Contact')

layout = html.Div([
  header,
])

dash.register_page("contact", layout=layout, path="/contact")
