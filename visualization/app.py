# -------------------- Setting --------------------

from dash import Dash, dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

from utils import (
    get_vis1_fig,
    get_vis3_fig,
)


# PATHs
# The directory where the dune data is stored
DUNE_DATA_PATH = '../dune_data'

# The directory where the cryptopunk data with attributes info is stored
CSV_PATH = '../cp'

# The directory where the three databases are stored
DATABASE_PATH = '../database'

# The directory where the cryptopunk images is stored
PUNK_IMG_PATH = '../punk_imgs'

# The directory where the visualization data for each visualization is stored
VIS_DATA_PATH = '../vis_data'

# The directory where the scraped tweets data is stored
TWEET_PATH = '../tweets'

# -------------------- Visualization Figures --------------------
# Vis1 - Sankey Diagram --------------------
# dataset for vis1
data1 = json.load(open(VIS_DATA_PATH + '/vis1_data.json'))

# fig for vis1
fig1 = get_vis1_fig(data1)

fig1.update_layout(
    plot_bgcolor='rgba(255,255,255,0.1)',
    width=1000,
    height=600,
)


# Vis3 - Bubble Chart --------------------
# dataset for vis3
data3 = pd.read_csv('{}/vis3_data.csv'.format(VIS_DATA_PATH),
                    header=0, index_col=0)

# df3 = df3[df3['date'] > '2021-01-01']
data3 = data3[data3['price'] < 700]

# fig for vis3
fig3 = get_vis3_fig(data3)

# turn off native plotly.js hover effects - make sure to use
# hoverinfo="none" rather than "skip" which also halts events.

fig3.update_traces(hoverinfo="none", hovertemplate=None)

fig3.update_layout(
    xaxis=dict(title='Date'),
    yaxis=dict(title='ETH Price'),
    plot_bgcolor='rgba(255,255,255,0.1)',
    width=1000,
    height=600,
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
                id="title",
                children="On Ethics of Ethereum NFT",
            ),
            # html.Div(
            #     id="learn_more",
            #     children=[
            #         html.Img(className="logo",
            #                  src=app.get_asset_url("logo.png"))
            #     ],
            # ),
        ],
    ),
    # Visualization grid
    html.Div(
        id="grid",
        children=[
            # vis1
            html.Div(children=[
                html.H2(children='Visualization 1'),

                html.Div(children='Sankey Diagram.'),

                dcc.Graph(id="graph-1",
                          className="div-card", figure=fig1),
                # dcc.Graph(
                #     id='graph-1',
                #     figure=fig1
                # )
            ]),

            # vis3
            html.Div(children=[
                html.H2(children='Visualization 3'),

                html.Div(children='Bubble Chart.'),
                
                dcc.Graph(id="graph-3", className="div-card",
                          figure=fig3),
                # dcc.Graph(
                #     id='graph-3',
                #     figure=fig3
                # ),
                dcc.Tooltip(id="graph-tooltip"),
            ])

        ]),
])

# Define callback to update graph


@ app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    [Input("graph-3", "hoverData")]
)
# hover to display punk image
def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    # demo only shows the first point, but other points may also be available
    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]

    df_row = data3.iloc[num]
    img_src = df_row['img_url']
    punk_id = df_row['punk_id']
    tx_date = df_row['date']

    children = [
        html.Div([
            html.Img(src=img_src, style={"width": "100%"}),
            html.P(f"Punk ID: {punk_id}", style={"color": "#3347D7"}),
            html.P(f"Date: {tx_date}", style={"color": "#8BD6EA"}),
        ], style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port=8051)
