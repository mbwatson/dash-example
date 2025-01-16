from dash import dcc, html
import dash_mantine_components as dmc

header = html.H1('👋🏼 Welcome')

layout = dmc.Container(
  [
    header,
    html.Hr(),
    dcc.Markdown("""
      Ullamco anim ea ea aliquip cupidatat aliqua culpa laborum ea veniam
      culpa commodo veniam esse labore.

      Eiusmod ea reprehenderit anim proident veniam consequat velit culpa
      elit. Do duis *officia elit ea* eu pariatur dolor eu dolor voluptate
      velit occaecat in. Nisi aute anim aliquip occaecat nulla dolor veniam
      minim. Ut nulla ullamco consectetur cupidatat labore ut laborum
      eiusmod amet esse officia sit commodo magna ea excepteur pariatur.
      Labore non consequat deserunt proident laborum consectetur eu anim ut
      non incididunt laborum."""),
  ],
  fluid=True
)
