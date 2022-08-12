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

def get_vis3_fig(data):
    colorsIdx = {'Dark': '#9d0208', 'Medium': '#dc2f02',
                 'Light': '#f48c06', 'Albino': '#ffba08',
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
                opacity=0.5,
            )
        )
        trace_list.append(trace)

    fig3 = go.Figure(data=trace_list)

    return fig3


# PATHs
# -------------------- Visualization Figures --------------------
# Vis3 - Bubble Chart --------------------
# dataset for vis3
data3 = pd.read_csv('{}/vis3_data.csv'.format('../../../data/vis'),
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
    yaxis=dict(title='Price (ETH)'),
    plot_bgcolor='rgba(255,255,255,0.1)',
    width=1500,
    height=700,
    legend={'itemsizing': 'constant'},
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
            html.H3(children='Visualization 3.'),

            # html.Div(children='The scatter plot visualizes the CryptoPunk transactions in terms of the punk skin tone of each transaction.'),

            dcc.Graph(id="graph-3",
                        className="div-card", figure=fig3),
            dcc.Tooltip(id="graph-tooltip-3"),
        ]),
    ),
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
    
    
    image_path = '../../../old/data/punk_imgs/{}.png'.format(punk_id)
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
    app.run_server(debug=True, host="localhost", port=8053)
