import io
import base64
from dash import Dash, dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import pandas as pd
from PIL import Image

data_path = '../../data/vis5_data.csv'

sent_year_df = pd.read_csv(data_path, header=0, index_col=0)

years=['2017', '2018', '2019', '2020', '2021', '2022']
sents=['neg', 'neu', 'pos']

fig = go.Figure(data=[
    go.Bar(name='Negative', x=years, y=sent_year_df['neg'], marker=dict(color='#E00000')),
    go.Bar(name='Neutral', x=years, y=sent_year_df['neu'], marker=dict(color='#FFBA08')),
    go.Bar(name='Positive', x=years, y=sent_year_df['pos'], marker=dict(color='#3F88C5')),
])
# Change the bar mode
fig.update_layout(barmode='stack', legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=-0.3
))

# turn off native plotly.js hover effects - make sure to use
# hoverinfo="none" rather than "skip" which also halts events.
fig.update_traces(hoverinfo="none", hovertemplate=None)

fig.update_layout(
    xaxis=dict(title='Year'),
    yaxis=dict(title='Percentage of Tweets'),
    plot_bgcolor='rgba(255,255,255,0.1)'
)

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
    html.Div([
        html.H2(children='Visualization 5'),

        html.Div(children='Wordcloud'),
        
        dcc.Graph(id="graph-basic-2", figure=fig, clear_on_unhover=True, style={'width': '50%', 'height': '100%'}),
        dcc.Tooltip(id="graph-tooltip"),
    ]),
])


@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Input("graph-basic-2", "hoverData"),
)
def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    # demo only shows the first point, but other points may also be available
    points = hoverData["points"][0]
    bbox = points["bbox"]
    num1 = points["pointNumber"]        # Year
    num2 = points["curveNumber"]        # Sentiment
    year = years[num1]                  
    sent = sents[num2]
    
    tweets_count = sent_year_df.loc[int(year), sent+'_count']
    
    Sent = ''
    if sent == 'neg':
        Sent = 'Negative'
        font_color = '#E00000'
    elif sent == 'neu':
        Sent = 'Neutral'
        font_color = '#FFBA08'
    elif sent == 'pos':
        Sent = 'Positive'
        font_color = '#3F88C5'
    
    image_path = '../../data/vis5/{}_{}.png'.format(year, sent)
    im = Image.open(image_path)
    buffer = io.BytesIO()
    im.save(buffer, format="png")
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    im_url = "data:image/png;base64, " + encoded_image

    children = [
        html.Div([
            html.Img(
                src=im_url,
                style={"width": "300px"},
            ),
            # html.Img(src=img_src, style={"width": "100%"}),
            html.H4(f"{year}-{Sent}", style={"color": font_color, "font-family":'Courier New'}),
            html.P(f"Amount of Tweets: {tweets_count}", style={"color": "black", "font-family":'Courier New'}),
            # html.P(f"{desc}"),
        ], style={'width': '300px', 'white-space': 'normal'})
    ]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port=8054)
