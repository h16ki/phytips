import dash
from dash import html
# import dash_html_components as html
from dash import dcc
# import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px


# app = dash.Dash(__name__)
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LITERA],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

COMMON_STYLE = {
    "font-family": [
        "Helvetica Neue",
        "Arial",
        "Hiragino Kaku Gothic ProN",
        "Hiragino Sans",
        "Meiryo",
        "sans-serif"
    ],
}

SIDEBAR_STYLE = {
    "width": "16rem",
    "padding": "2rem 1rem",
    # "background-color": "rgb(200,200,203)",
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "right": 0,
}

sidebar = html.Div(
    [
        html.H1("Physics...", id="header", style={"font-size": 15, "color":"rgb(3,175,122)"}),
        html.Div("Category"),
        html.Hr(),
    ],
    style=SIDEBAR_STYLE,
)

CONTENT_STYLE = {
    "margin-left": "2rem",
    # "margin-right": "2rem", 
    "padding": "2rem 1rem",
    "position": "absolute",
    "width": "100%"
}

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

content = html.Div(
    [
        html.P("減衰振動・強制振動"),
        dcc.Graph(
            id="oscillation",
            figure=fig
        )
        
    ],
    id="page-content",
    style=CONTENT_STYLE
)

HEADER_STYLE = {
    "padding": "1rem",
}

header = dbc.Nav(
    children=[
        html.H1("Mechanics plots...", id="header"),
    ],
    style=HEADER_STYLE
)


app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=2),
                dbc.Col(content, width=8),
            ]
        ),
    ],
    style=COMMON_STYLE
)

if __name__ == "__main__":
    app.run_server(debug=True)
