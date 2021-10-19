import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LITERA],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

if __name__ == "__main__":
    app.run_server(debug=True)