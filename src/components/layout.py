from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

CONFIG = {
  "MAX_WIDTH": "1600px",
}

layout_css = {
  "max-width": CONFIG["MAX_WIDTH"],
}

title_css = {
  "margin-top": "1rem",
  "text-align": "center",
}

def create_layout(app: Dash) -> html.Div:
  return dbc.Container(
    className="app-root",
    style=layout_css,
    children=[
      dbc.Row(
        dbc.Col(
          html.H1("🌐 " + app.title, style=title_css),
          width={ "size": 6, "offset": 3 },
        )
      ),
      html.Hr(),
      html.Div(children=[
        dcc.Markdown(children="""
          Ullamco anim ea ea aliquip cupidatat aliqua culpa laborum ea veniam
          culpa commodo veniam esse labore.
        """),
        dcc.Markdown(children="""
          Eiusmod ea reprehenderit anim proident veniam consequat velit culpa
          elit. Do duis officia elit ea eu pariatur dolor eu dolor voluptate
          velit occaecat in. Nisi aute anim aliquip occaecat nulla dolor veniam
          minim. Ut nulla ullamco consectetur cupidatat labore ut laborum
          eiusmod amet esse officia sit commodo magna ea excepteur pariatur.
          Labore non consequat deserunt proident laborum consectetur eu anim ut
          non incididunt laborum.
        """),
      ])
    ]
  )