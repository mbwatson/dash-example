from dash import Dash, html
from src.components.layout import create_layout
import dash_bootstrap_components as dbc

def main() -> None:
  app = Dash(external_stylesheets=[dbc.themes.LUMEN])
  app.title = "Dash Dashboard"
  app.layout = create_layout(app)
  app.run(debug=True)

# Run the app
if __name__ == '__main__':
  main()
