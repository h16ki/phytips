import dash
# import dash_html_components as html
from dash import html, dcc
# import dash_core_components as dcc
import dash_bootstrap_components as dbc

footer = html.Div(
    children = [
        html.Hr(),
        html.P("F")
    ],
    style = {
        "margin-top": 100,
        # "background-color": "#232311",
        "height": 200,
        # "color": "#ffffff"
    }
)