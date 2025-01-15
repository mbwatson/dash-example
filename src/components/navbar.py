from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from src.components.drawer import drawer

logo = dmc.Anchor(
  "[LOGO]",
  href="/",
  className="navbar--brand",
)

def navlink(label, href):
  return dmc.NavLink(label=label, href=href, variant="subtle")

nav_items = [
  {"label": "Home", "href": "/"},
  {"label": "About", "href": "/about"},
  {"label": "Contact", "href": "/contact"},
]

menu = dmc.Group(
  [navlink(label=item["label"], href=item["href"]) for item in nav_items],
  wrap="no-wrap",
  className="navbar--menu",
)

navbar = dmc.Paper(
  shadow="xs",
  className="navbar",
  children=[
    drawer,
    logo,
    menu,
  ],
)

