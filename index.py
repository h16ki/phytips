import dash, os
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import sidebar, footer
import mechanics.oscillation.content as osc
import base64


# mathjax = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML",
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        # {
        #     "href": "https://cdn.jsdelivr.net/npm/katex@0.13.19/dist/katex.min.css",
        #     "rel": "stylesheet",
        #     "integrity": "sha384-beuqjL2bw+6DBM2eOpr5+Xlw+jiH44vMdVQwKxV28xxpoInPHTVmSvvvoPq9RdSh",
        #     "crossorigin": "anonymous"
        # }
    ],
    external_scripts=[
        {
            "type": "text/javascript",
            "id": "MathJax-script",
            "src": "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML",
        }
        # dict(
        #     src="https://cdn.jsdelivr.net/npm/katex@0.13.19/dist/katex.min.js",
        #     integrity="sha384-aaNb715UK1HuP4rjZxyzph+dVss/5Nx3mLImBe9b0EW4vMUkc1Guw4VRyQKBC0eG",
        #     crossorigin="anonymous"
        # ),
        # dict(
        #     src="https://cdn.jsdelivr.net/npm/katex@0.13.19/dist/contrib/auto-render.min.js",
        #     integrity="sha384-+XBljXPPiv+OzfbB3cVmLHf4hdUFHlWNZN5spNQ7rmHTXpd7WvJum6fIACpNNfIR",
        #     crossorigin="anonymous",
        #     onload="renderMathInElement(document.body);"
        # ),
    ],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
# app.scripts.append_script({"external_scripts": mathjax})
app.title = "Phytips"
server = app.server
server.route('/')

COMMON_STYLE = {
    # "font-family": [
    #     "Helvetica Neue",
    #     "Arial",
    #     "M Plus 1p",
    #     "Hiragino Kaku Gothic ProN",
    #     "Hiragino Sans",
    #     "Meiryo",
    #     "sans-serif"
    # ],
}

HEADER_STYLE = {
    "padding": "1rem",
    "padding-bottom": "3rem",
    # "width": "3rem",
    "height": "3rem",
    "display": "flex",
    "align-items": "center",
    "backgound-color": "rgba()",
    # "border":"solid 1px black"
}

img = base64.b64encode(open("assets/logo.png", "rb").read())
header = dbc.Nav(
    children=[
        html.Div(
            children = [
                # html.Img(src=f"data:image/png;base64,{img.decode()}", height="30"),
                dcc.Link(children=html.Img(src=f"data:image/png;base64,{img.decode()}", height="30"), href="/"),
                html.Div("hogehoge $ho$"),
            ],
            style = {
                "displuay": "flex",
                "align-items": "center", 
                "height": "3rem", 
                "top": 0, 
                "position": "fixed"
            }
        ),
        # html.H1("Phytips", id="header", style={"font-size": 16}),
        # html.Img(src=f"data:image/png;base64,{img.decode()}", height="30", style={"border":"solid 1px black"})
    ],
    style=HEADER_STYLE
)

navbar = dbc.Navbar(
    dbc.Container(
        children = [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=f"data:image/png;base64,{img.decode()}", height="30")),
                        dbc.Col(dbc.NavbarBrand("Phytips"))
                    ],
                    align="center"
                ),
                href="/",
                style = {"textDecoration": "none"},
            ),
        ]
    ),
    # color = "white",
    dark = True,
)


# app.layout = html.Div(
#     [
#         navbar,
#         # header,
#         # sidebar.sidebar,
#         # dbc.Row(
#         #     [
#         #         # dbc.Col(sidebar.sidebar, width=3),
#         #         # dbc.Col(osc.content, width=9),
#         #         dbc.Col(osc.callback(app), width=9)
#         #     ]
#         # ),
#         osc.callback(app),
#         footer.footer,
#     ],
#     style=COMMON_STYLE
# )
app.layout = html.Div(
    children = [
        dbc.Row(
            children = [
                dbc.Col(sidebar.sidebar, width=3),
                dbc.Col(osc.callback(app))
            ]
        )
    ],
    style = {
        # "padding": "3rem 1rem",
    }
)

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),
# ])

def foo():
    return 1

if __name__ == '__main__':
    app.run_server()
