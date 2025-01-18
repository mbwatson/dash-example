import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, Input, Output, State, callback, _dash_renderer

theme_toggle = dmc.ActionIcon(
  [
    dmc.Box(DashIconify(icon='feather:moon', width=24, height=24), darkHidden=True),
    dmc.Box(DashIconify(icon='feather:sun', width=24, height=24), lightHidden=True),
  ],
  variant='transparent',
  color='goldenrod',
  id='color-scheme-toggle',
  size='lg',
)

@callback(
  Output('mantine-provider', 'forceColorScheme'),
  Input('color-scheme-toggle', 'n_clicks'),
  State('mantine-provider', 'forceColorScheme'),
  prevent_initial_call=True,
)
def switch_theme(_, theme):
  return 'dark' if theme == 'light' else 'light'

if __name__ == '__main__':
  app.run(debug=True)