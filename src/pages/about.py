from dash import dcc, html

header = html.H1('About')

layout = html.Div([
  header,
  dcc.Markdown("""Lorem ipsum consectetur voluptate commodo aute nulla dolore
    officia magna esse laboris officia sunt laborum aliquip do in magna.
    Commodo consequat sunt quis ut magna laborum esse laborum nostrud non
    eiusmod sint veniam adipisicing cupidatat excepteur."""),
  dcc.Markdown("""aliqua consequat in consequat nostrud ullamco do nulla
    voluptate laboris. Dolor adipisicing sit consequat irure excepteur laborum
    do in non dolor dolore sit quis. Ex dolor ea est et veniam commodo cillum
    nulla sit aute ut dolor mollit ut dolore aute. Consequat duis ullamco
    labore occaecat minim proident non dolor dolore est sit id proident."""),
  dcc.Markdown("""Minim consequat excepteur in do pariatur enim ullamco
    fugiat qui commodo ut amet. Ut commodo laboris aute ex nisi ut dolore
    veniam ad duis do sint. Pariatur deserunt aute aliquip fugiat ea id
    laboris eu culpa dolore proident nulla consectetur consectetur minim.
    Mollit ex elit magna esse quis dolor nisi tempor id ex nostrud. Qui in
    consequat labore minim sit laboris eiusmod eu dolor reprehenderit
    consequat id. Lorem ipsum nulla eiusmod amet magna exercitation do."""),
])
