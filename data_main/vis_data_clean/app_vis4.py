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


mgr_options=['2017', '2018', '2019', '2020', '2021', '2022']
# mgr_options = df["Manager"].unique()

app = Dash()

app.layout = html.Div([
    html.H2("Visualization 4 - Transaction Network"),
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
    data = pickle.load(open('../../data/vis4_data_{}.pkl'.format(Manager), 'rb'))

    return {
        'data': data,
        'layout':go.Layout(
                      showlegend=True,
                      plot_bgcolor='rgba(255,255,255,0.1)',
                      hovermode='closest',
                      width=880,
                      height=800,
                      margin=dict(b=20, l=5, r=5, t=40),
                      xaxis=dict(showgrid=False, zeroline=False,
                                 showticklabels=False),
                      yaxis=dict(showgrid=False, zeroline=False,
                                 showticklabels=False)
                  )
    }


if __name__ == '__main__':
    app.run_server(debug=True, host="localhost", port=8055)