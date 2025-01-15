from dash import html
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from src.components.drawer import drawer
from src.components.theme_toggle import theme_toggle

github_link = dmc.Anchor(
  DashIconify(icon="feather:github", width=20, color="var(--mantine-color-text)"),
  variant="transparent",
  id="github-link",
  href="https://github.com/mbwatson/dash-example/",
  target="_blank",
)

logo = dmc.Anchor(
  "[LOGO]",
  href="/",
  className="navbar--brand",
)

def navlink(label, href):
  return dmc.NavLink(label=label, href=href, variant="subtle")

nav_items = [
  {"label": "Home", "href": "/"},
  {"label": "Data", "href": "/data"},
  {"label": "About", "href": "/about"},
  {"label": "Contact", "href": "/contact"},
]

menu = dmc.Flex(
  [navlink(label=item["label"], href=item["href"]) for item in nav_items],
  wrap="no-wrap",
  className="navbar--menu-items",
  justify="flex-end"
)

navbar = dmc.Paper(
  shadow="xs",
  className="navbar",
  children=[
    drawer,
    logo,
    dmc.Flex([menu, github_link, theme_toggle], className="navbar--menu")
  ])

