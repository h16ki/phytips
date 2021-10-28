import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import numpy as np
import utils
import plotly.graph_objects as go


# app = dash.Dash(
#     __name__,
#     suppress_callback_exceptions=True,
#     external_stylesheets=[dbc.themes.YETI],
#     meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
# )


CONTENT_STYLE = {
    # "margin-left": "2rem",
    # "margin-right": "5rem",
    "padding": "3rem 2rem",
    # "position": "absolute",
    # "width": "100%",
    # "border": "solid 1px black",
}

# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length")


def damped_driven_harmonic_oscillation(t, x0=1.0, v0=0.0, freq=1.0, damp=0.0, extf=None):
    """
    An exact analytic solution for the harmonic oscillator with damping and driving force.
    $$
      \ddot{x} + \gamma \dot{x} + \omega^2 x = f \cos(\Omega t)
    $$

    Args
    ----
    t: list, numpy.array
    x0: float, default 1.0
    v0: float, default 0.0
    freq: float, default 1.0
    damp: float
    extf: optional, {"fun": "cos" , "amp":0, "freq":0}, "fun" is in ("cos", "sin")

    Return
    ------
    list

    """

    if extf:
        ext_amp = extf.pop("amp")
        ext_freq = extf.pop("freq")
        ext_fun = extf.pop("fun")
        # fun = VALID_FUNS[ext_fun]

    else:
        ext_fun = ext_amp = ext_freq = 0

    # Non-dimensionalization, p = Omega/omega, q = gamma/omega, tau = omega * t
    p = ext_freq / freq
    q = damp / freq
    tau = freq * t

    # Rescale
    nu0 = v0 / freq

    # 3-type homogeneous solution.
    # Overdamped
    if q > 1:
        div = np.sqrt(q ** 2 - 1.0)
        A = 0.5 * ((1.0 + q / div) * x0 + nu0 / div)
        B = 0.5 * ((1.0 - q / div) * x0 - nu0 / div)
        oscillation = A * np.exp(div * tau) + B * np.exp(-div * tau)

    # Underdamped
    elif q < 1:
        div = np.sqrt(1.0 - q ** 2)
        A = x0
        B = (nu0 + q * x0) / div
        oscillation = A * np.cos(div * tau) + B * np.sin(div * tau)

    # Critically-damped
    elif q == 1:
        A = x0
        B = x0 + nu0
        oscillation = A * tau + B

    homo_solution = np.exp(-q * tau) * oscillation

    # Driving oscillation
    if ext_fun == "cos":
        deno = (1 - p ** 2) ** 2 + 4 * q ** 2
        if deno == 0:
            part_solution = ext_amp / (2 * freq ** 2) * tau * np.sin(tau)
        else:
            part_solution = (1 - p ** 2) / deno * ext_amp / freq ** 2 * np.cos(
                p * tau
            ) + (2 * q) / deno * ext_amp / freq ** 2 * np.sin(p * tau)

    elif ext_fun == "sin":
        pass

    else:
        part_solution = 0

    # return homo_solution + part_solution
    sol = homo_solution + part_solution
    data = {
        "freq": freq,
        "damp": damp,
        "Freq": ext_freq,
        "tau": tau,
        "mom": momentum,
        "pos": sol,
        "sol": sol,
        # "amplitude"
    }

    return data


def phenomena(freq, damp, extf):
    periodic_number = 13
    t1 = 2.0 * np.pi * periodic_number / freq
    plots = []
    x0 = np.linspace(-1, 1, 9)
    v0 = np.linspace(-1, 1, 9)
    t = np.linspace(0, t1, 300)
    # for x in x0:
    #     for v in v0:
    #         plot = go.Scatter(
    #             x=t, y=damped_driven_harmonic_oscillation(
    #                 t, x0, v0, freq, damp, extf
    #             ),
    #             line=dict(dash="solid", color="#0076c3"),
    #             visible=False,
    #         )
    #         plots.append(plot)

    osc = damped_driven_harmonic_oscillation(
        t, 1, 0, freq, damp, extf=extf
    )        
    plot = go.Scatter(x=osc["tau"], y=osc["sol"])
    
    layout = go.Layout(template=utils.template)
    fig = go.Figure(data=plot, layout=layout)

    fig.update_layout(
        xaxis_title="$\omega t$ $$h$$",
        yaxis_title="$x(t)$ \(h\)"
    )

    return fig




def phase_space_trajectory(data):
    x = data["pos"]
    p = data["pos"]

    plot = go.Scatter(x=x, y=p)
    layout = go.Layout(template=utils.template)
    fig = go.Figure(data=plot, layout=layout)

    return fig

def universal_resonance_curve():
    pass

def birds_eye_view():
    pass


natural_frequency = html.Div(
    [
        # dbc.Label("Natural frequency $\omega$:", size="sm", width="auto"),
        dbc.FormText("Natural frequency $\omega$:"),
        # dbc.Row(
        #     dbc.Input(
        #         type="text", id="natural_frequency", placeholder="1.0", size="sm"
        #     ),
        #     width="2",
        # )
        dbc.Input(
            type="text", id="natural_frequency", placeholder="1.0", size="sm", #width="auto"
            className="w-25", invalid=False, value=1.0
        )
    ],
    className="my-1"
)

damping_ratio = html.Div(
    [
        # dbc.Label("Damping ratio $\gamma$:", size="sm", width="auto"),
        dbc.FormText("Damping ratio $\gamma$:"),
        # dbc.Col(
            dbc.Input(
                type="text", id="damping_ratio", placeholder="0.0", size="sm", #width="2"
                className="w-25", value=0.0
            ),
            # width="2",
        # )
    ],
    className="my-1"
)


oscillator_properties = dbc.Form(
    [
        dbc.Row(
            [
                dbc.Label("Oscillator properties:"),
                # dbc.Col(natural_frequency),
                # dbc.Col(damping_ratio),
                natural_frequency,
                damping_ratio,
            ],
            # className="p-3"
        )
    ],
    className="mb-5"
)

driving_force_function = dbc.Row(
    [
        dbc.FormText("Function:"),
        # dbc.Col(
            dbc.RadioItems(
                id="driving_force_function",
                options=[
                    {"label": "cos", "value": "cos"},
                    {"label": "sin", "value": "sin"},
                    {"label": "none", "value": "none"}
                ],
                inline=True,
            ),
            # width="auto",
        # )
    ]
)

driving_force_amplitude = html.Div(
    [
        dbc.FormText("Amplitude:"),
        # dbc.Col(
            dbc.Input(placeholder="0.0", type="text", size="sm"),
            # width="auto",
        # )
    ],
    className="my-1"
)

driving_force_frequency = html.Div(
    [
        dbc.FormText("Frequency:"),
        # dbc.Col(
            dbc.Input(placeholder="0.0", type="text", size="sm"),
            # width = "auto",
        # ),
    ],
    className="my-1"
)

driving_force = dbc.Form([
    dbc.Row([
        dbc.Label("Driving force:"),
        # dbc.Col(driving_force_function),
        # dbc.Col(driving_force_amplitude),
        # dbc.Col(driving_force_frequency)
        driving_force_function,
        driving_force_amplitude,
        driving_force_frequency,
    ])
])


redraw_button = html.Div(
    [
       dbc.Button("Redraw", id="redraw_button", color="primary", outline=True,
           className="justify-content-center"
       ), 
    ],
    className="justify-content-center"
)


inputarea = html.Div(
    [
        dbc.Input(placeholder="valid", valid=True),
        dbc.Input(placeholder="invalid", valid=False),
        dbc.Input(placeholder="valid", invalid=True),
        dbc.Input(placeholder="invalid", invalid=False),
    ]
)

content = html.Div(
    [
        inputarea,
        html.H3("振動 $h$"),
        html.Div(
            [
                dcc.Graph(id="motion", figure=phenomena(1, 0, {"fun": "cos", "amp": 1, "freq": 0.8})),
            ],
            style={
                "margin-bottom": "1rem"
            }
        ),
        dbc.Row([
            dbc.Col(oscillator_properties),
            dbc.Col(driving_force),
            dbc.Col(redraw_button),
        ]),
        # oscillator_properties,
        # driving_force,
        html.Div(
            [
                dbc.Button("Submit", id="submit-val", n_clicks=0, color="primary", outline=True),
                html.Div(id="container-button-basic", children="Enter a value and press submit.")
            ]
        )
    ],
    id="page-content",
    style=CONTENT_STYLE,
)


def callback(app):
            
    @app.callback(
        Output("container-button-basic", "children"),
        # Input("submit-val", "n_clicks"),
        [
            Input("submit-val", "n_clicks"),
            State("natural_frequency", "value"),
            State("damping_ratio", "value")
        ]
    )
    def update_button(n_clicks, freq, damp,):
        # print(utils.plot_layout())
        return f"{n_clicks} times pushed. {freq}, {damp}"
    
    @app.callback(
            [
                Output("natural_frequency", "value"),
                Output("natural_frequency", "invalid"),
            ],
        Input("natural_frequency", "value")
    )
    def input_validation_natural_frequency(value):
        try:
            print("ok")
            value = float(value or "1.0")
        except ValueError:
            print("ng")
            isinvalid = True
        else:
            if value < 0:
                isinvalid = True
            else:
                isinvalid = False
                
        return str(value), isinvalid
            
    return content
# @app.callback(
#     Output(component_id='output_div', component_property='children'),
#     [Input(component_id='input_id', component_property='value')]
# )
# def update_output_div(input_value):
#     if input_value:
#         return html.Div(className='output-area', children=[
#             html.Span(input_value)
#         ])
#     else:
#         html.Div()


# def callback(app):
#     app.callback(
#         Output(component_id="output_div", component_property="children"),
#         [
#             Input(component_id="input_id", component_property="value")
#         ]
#     )
#     def update_output_div(input_value):
#         if input_value:
#             return html.Div(className="output-area", children=[
#                 html.Span(input_value)
#             ])
#         else:
#             html.Div()


# app.layout = html.Div(content, style=CONTENT_STYLE)

if __name__ == "__main__":
    app.run_server(debug=True)
