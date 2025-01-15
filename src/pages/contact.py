from dash import html

header = html.H1('Contact')

def create_page():
  layout = html.Div([
    header,
  ])
  return layout