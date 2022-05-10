# -------------------- Setting --------------------

from tkinter import font

from click import style
from dash import Dash, dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import pickle
from PIL import Image
import io
import base64

def get_vis1_fig(data):
    fig1 = go.Figure(data=[go.Sankey(
        valueformat=".0f",
        valuesuffix=" punks",
        # Define nodes
        node=dict(
            pad=15,
            thickness=15,
            line=dict(color="black", width=0.5),
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
VIS_DATA_PATH = './data'

# -------------------- Visualization Figures --------------------
# Vis1 - Sankey Diagram --------------------
# dataset for vis1
data1 = json.load(open('../../data/vis1_data.json'))

# fig for vis1
fig1 = get_vis1_fig(data1)

fig1.update_layout(
    plot_bgcolor='rgba(255,255,255,0.1)',
    width=1000,
    height=600,
    title='<br>Sankey Diagram: Distribution of CryptoPunks with Different Attributes',
    titlefont=dict(size=20, family='PT Sans Narrow'),
)


# -------------------- App --------------------
# Build the app
app = Dash(__name__)
app.layout = html.Div([
    # Banner display
    html.Div(
        className="header-title",
        children=[
            html.H1(
                id="title1",
                children="A Glance into NFT Ethics: On Ethics of CryptoPunk",
            ),
            html.H2(
                id="title2",
                children="STATS 401 Project II",
            ),
        ],
    ),
    # Visualization grid
    html.Div(
        html.Div(children=[
            html.H3(children='Visualization 1.'),

            # html.Div(children='The Sankey diagram visualizes the distribution of CryptoPunk with different attributes.'),

            dcc.Graph(id="graph-1",
                        className="div-card", figure=fig1),
            dcc.Tooltip(id="graph-tooltip-1"),
        ]),
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port=8051)
