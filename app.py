# -------------------- Setting --------------------

from dash import Dash, dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import pickle
from PIL import Image
import io
import base64

from utils import (
    get_vis1_fig,
    get_vis3_fig,
    get_vis4_fig,
)


# PATHs
# The directory where the visualization data for each visualization is stored
VIS_DATA_PATH = './data'

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
    title='<br>Sankey Diagram of CryptoPunks of Different Attributes',
    titlefont=dict(size=20, family='PT Sans Narrow'),
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
    title='<br>Bubble Chart of CryptoPunks Transactions based on Punk Skin Tone',
    titlefont=dict(size=20, family='PT Sans Narrow'),
)


# Vis4 - Network Visualization --------------------
# dataset for vis4
data4_2022 = pickle.load(open(VIS_DATA_PATH + '/vis4_data_2022.pkl', 'rb'))
data4_2021 = pickle.load(open('{}/vis4_data_{}.pkl'.format(VIS_DATA_PATH, '2021'), 'rb'))
data4_2020 = pickle.load(open('{}/vis4_data_{}.pkl'.format(VIS_DATA_PATH, '2020'), 'rb'))
data4_2019 = pickle.load(open('{}/vis4_data_{}.pkl'.format(VIS_DATA_PATH, '2019'), 'rb'))
data4_2018 = pickle.load(open('{}/vis4_data_{}.pkl'.format(VIS_DATA_PATH, '2018'), 'rb'))
data4_2017 = pickle.load(open('{}/vis4_data_{}.pkl'.format(VIS_DATA_PATH, '2017'), 'rb'))


# fig for vis4
fig4 = get_vis4_fig(data4_2022)

# fig4.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             direction="right",
#             x=0.7,
#             y=1.2,
#             showactive=True,
#             buttons=list(
#                 [
#                     dict(
#                         label="2022",
#                         method="update",
#                         args=[{"data": data4_2022}],
#                     ),
#                     dict(
#                         label="2021",
#                         method="update",
#                         args=[{"data": data4_2021}],
#                     ),
#                     dict(
#                         label="2020",
#                         method="update",
#                         args=[{"data": data4_2020}],
#                     ),
#                     dict(
#                         label="2019",
#                         method="update",
#                         args=[{"data": data4_2019}],
#                     ),
#                     dict(
#                         label="2018",
#                         method="update",
#                         args=[{"data": data4_2018}],
#                     ),
#                     dict(
#                         label="2017",
#                         method="update",
#                         args=[{"data": data4_2017}],
#                     ),
#                 ]
#             ),
#         )
#     ]
# )



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
                dcc.Tooltip(id="graph-tooltip-1"),
            ]),

            # vis3
            html.Div(children=[
                html.H2(children='Visualization 3'),

                html.Div(children='Bubble Chart.'),
                
                dcc.Graph(id="graph-3", className="div-card",
                          figure=fig3, clear_on_unhover=True),

                dcc.Tooltip(id="graph-tooltip-3"),
            ]),
            
            # vis4
            html.Div(children=[
                html.H2(children='Visualization 4'),

                html.Div(children='Network Visualization.'),
                
                dcc.Graph(id="graph-4", className="div-card",
                          figure=fig4),
                dcc.Tooltip(id="graph-tooltip-4"),
            ]),

        ]),
])

# Define callback to update graph


@ app.callback(
    Output("graph-tooltip-3", "show"),
    Output("graph-tooltip-3", "bbox"),
    Output("graph-tooltip-3", "children"),
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
    # img_src = df_row['img_url']
    punk_id = df_row['punk_id']
    tx_date = df_row['date']
    
    
    image_path = './data/punk_imgs/{}.png'.format(punk_id)
    im = Image.open(image_path)
    buffer = io.BytesIO()
    im.save(buffer, format="png")
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    im_url = "data:image/png;base64, " + encoded_image


    children = [
        html.Div([
            html.Img(src=im_url, style={"width": "100%"}),
            html.P(f"Punk ID: {punk_id}", style={"color": "black"}),
            html.P(f"{tx_date}", style={"color": "grey"}),
        ], style={'width': '100px', 'white-space': 'normal'})
    ]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port=8051)
