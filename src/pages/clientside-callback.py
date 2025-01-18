import dash
from dash import clientside_callback, ClientsideFunction, dcc, html, Input, Output
import dash_mantine_components as dmc

header = html.H1('Clientside Callback')

layout = html.Div([
  header,
  dcc.Markdown('click the button. check the console.'),
  dmc.Button('Click me', id='clicker'),

  dcc.Store(id='click-count')
])

clientside_callback(
  ClientsideFunction(
    namespace='clientside',
    function_name='local_script_callback'
  ),
  Output('click-count', 'data'),
  Input('clicker', 'n_clicks'),
)

dash.register_page('clientside-callback', layout=layout, path='/clientside-callback')
