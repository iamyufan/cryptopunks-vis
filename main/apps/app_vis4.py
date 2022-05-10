import dash
from dash import Dash, dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import pickle
from PIL import Image
import io
import base64


mgr_options = ['2017', '2018', '2019', '2020', '2021', '2022']
# mgr_options = df["Manager"].unique()

app = Dash()

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
    html.H3("Visualization 4."),
    html.Div(
        [
            dcc.Dropdown(
                id="Manager",
                options=[{
                    'label': i,
                    'value': i
                } for i in mgr_options],
                value='2022'),
        ],
        style={'width': '8%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])


@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('Manager', 'value')])
def update_graph(Manager):
    data = pickle.load(
        open('../../data/vis4_data/vis4_data_{}.pkl'.format(Manager), 'rb'))

    return {
        'data': data,
        'layout': go.Layout(
            showlegend=True,
            plot_bgcolor='rgba(255,255,255,0.1)',
            hovermode='closest',
            width=880,
            height=800,
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False,
                       showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False,
                       showticklabels=False),
            title='<br>Circular Network: Transaction Network of CryptoPunk by Year. ',
            titlefont=dict(size=20, family='PT Sans Narrow'),
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True, host="localhost", port=8054)
