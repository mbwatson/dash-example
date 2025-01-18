from dash import callback, dcc, Input, Output, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from src.components.theme_toggle import theme_toggle

github_link = dmc.Anchor(
  DashIconify(icon='feather:github', width=20, color='var(--mantine-color-text)'),
  variant='transparent',
  id='github-link',
  href='https://github.com/mbwatson/dash-example/',
  target='_blank',
)

logo = dmc.Anchor('[LOGO]', href='/')

header = dmc.Flex(
  children=[
    dmc.Group([dmc.Burger(id='burger', size='sm', hiddenFrom='sm', opened=False), logo]),
    dmc.Group([github_link, theme_toggle]),
  ],
  justify='space-between',
  style={'flex': 1},
  h='100%',
  px='md',
)
