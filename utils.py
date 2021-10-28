import plotly.graph_objects as go


def plot_layout():
    layout_template = dict(
        layout=go.Layout(
            xaxis=dict(
                ticks="inside", zeroline=False, linewidth=1,
                showline=True, linecolor="#222222", mirror="allticks",
            ),
            yaxis=dict(
                ticks="inside", zeroline=False, linewidth=1,
                showline=True, linecolor="#222222", mirror="allticks",
            ),
            yaxis2=dict(
                gridcolor="#d5d5d5",
                ticks="inside", zeroline=False, linewidth=1,
                showline=True, linecolor="#222222", mirror=False,
                overlaying="y", side="right",
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )
    )
    return layout_template

template = plot_layout()