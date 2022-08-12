# -------------------- Setting --------------------

from dash import Dash, dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json


def get_vis1_fig(data):
    fig1 = go.Figure(data=[go.Sankey(
        valueformat=".0f",
        valuesuffix=" punks",
        # Define nodes
        node=dict(
            pad=15,
            thickness=15,
            line=dict(color="black", width=0.2),
            label=data['node']['name'],
            color=data["node"]['color'],
        ),
        # Add links
        link=dict(
            source=data['link']['source'],
            target=data['link']['target'],
            value=data['link']['value'],
            color=data['link']['color'],
        ))])
    return fig1


# PATHs
# The directory where the visualization data for each visualization is stored
VIS_DATA_PATH = '../../data/vis'

# -------------------- Visualization Figures --------------------
# Vis1 - Sankey Diagram --------------------
# dataset for vis1
data1 = json.load(open(f'{VIS_DATA_PATH}/vis1_data.json'))

# fig for vis1
fig1 = get_vis1_fig(data1)

fig1.update_layout(
    plot_bgcolor='rgba(255,255,255,0.1)',
    height=700,
    # title='<br>Sankey Diagram: Distribution of CryptoPunks with Different Attributes',
    titlefont=dict(size=20, family='PT Sans Narrow'),
)


# -------------------- App --------------------
# Build the app
app = Dash(__name__)
app.layout = html.Div(
    id="grid-container",
    className="grid-container",
    children=[
        # Header
        html.Div(
            id='header',
            className="header",
            children=[
                html.P(
                    children='Visualizing NFT Ethics',
                )
            ]
        ),
        # Title display
        html.Div(
            id="title",
            className="title",
            children=[
                html.H2(
                    children="Figure 1: Sankey Diagram",
                ),
                html.P(
                    children="Distribution of CryptoPunks with Different Attributes",
                )
            ]
        ),
        # Visualization grid
        html.Div(
            id="graph",
            className="graph",
            children=[
                dcc.Graph(id="graph-1", figure=fig1, config={'displayModeBar': False}),
                dcc.Tooltip(id="graph-tooltip-1"),
            ]
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port=8051)
