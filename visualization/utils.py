
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


def get_vis3_fig(data):
    colorsIdx = {'Dark': '#A4031F', 'Medium': '#DB9065',
                'Light': '#F2A359', 'Albino': '#F2DC5D',
                'Non-human': '#8DFFCD'}

    trace_list = []
    for sc in ['Non-human', 'Albino', 'Light', 'Medium', 'Dark']:
        df3_temp = data[data['punk_skin_tone'] == sc]
        cols = df3_temp['punk_skin_tone'].map(colorsIdx),
        trace = go.Scatter(
            x=df3_temp['date'],
            y=df3_temp['price'],
            name='SKIN TONE: {}'.format(sc),
            mode="markers",
            marker=dict(
                color=colorsIdx[sc],
                size=df3_temp["bubble_size"],
                line={"width": 0},
                sizeref=1.5,
                sizemode="diameter",
                opacity=0.8,
            )
        )
        trace_list.append(trace)
        
    fig3 = go.Figure(data = trace_list)
    
    return fig3
