
from dash import Dash, html, dcc, Input, Output, callback, no_update
from pages import index, common, end
import plotly.graph_objs as go
import pandas as pd
from PIL import Image
import io
import base64
import json
from itertools import chain

# Initiate app ===============================================================
app = Dash(__name__, suppress_callback_exceptions=True, url_base_pathname=common.base_url+'/')
app.title = "A Glance into NFT Ethics"      # appears in browser title bar

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

# Visualization 1 ============================================================
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

# load the data source
data1 = json.load(open('./data/vis1_data.json'))

# generate the figure1
fig1 = get_vis1_fig(data1)
fig1.update_layout(
    plot_bgcolor='rgba(255,255,255,0.1)',
    width=800,
    height=600,
    title='Sankey Diagram of the Attributes Distribution',
    titlefont=dict(size=20, family='PT Sans Narrow'),
)

# generate the layout1
layout1 = html.Div(
    children=[
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='four columns div-user-controls figure-description',
                    children=[
                        html.H1('A Glance into NFT Ethics'),
                        html.H2('CryptoPunks Generating Distribution'),
                        html.P(
                            'Knowing the initial amount of CryptoPunks provides insights of the design team’s opinions of equality.'),
                            html.P('This Sankey diagram illustrates the differences in the CryptoPunks genesis with various attributes where 6160 (61.6%) of the punks are with male type and 3840 (38.4%) of the punks are with the female type. Among the 9879 human CryptoPunks, 3031 (30.68%) of the punks with a medium skin tone, 3006 (30.42%) of the punks with a light skin tone, 2824 (28.59%) of the punks with a dark skin tone, and 1018 (10.30%) of the punks with the albino skin tone. Looking at the generation phase, we saw a big difference in the number of CryptoPunks for males and females. And the number varies slightly by skin color. We searched for documentation about the original design of CryptoPunk, but couldn’t find a description of the initial Punk quantity allocation ratio. From the current research, we can’t conclude if this is a reasonable allocation, but there is indeed a number inequality between male and female features.'
                        ),
                        html.Div(style={'margin-top': '20px'}),
                        html.Div(
                            children=[
                                html.Div(
                                    className='bottom-nav',
                                    children=[
                                        html.A(id='', className='', children=[
                                            html.Button('<', id='button-prev', n_clicks=0)
                                        ], href=common.base_url+'/', style={'margin-right': '2rem'}),
                                        html.A(id='', className='', children=[
                                            html.Button('>', id='button-next', n_clicks=0),
                                        ], href=common.base_url+'/vis2'),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='eight columns div-for-charts bg-white figure-right',
                    children=[
                        dcc.Graph(id='example-graph', figure=fig1)
                    ]
                )    
            ]
        )
    ]
)

# Visualization 2 ============================================================
def get_vis2_fig(dark_li, medium_li, light_li, albino_li, 
                 dark_attribute_count_list, medium_attribute_count_list, light_attribute_count_list, albino_attribute_count_list):
    fig = go.Figure()

    fig.add_trace(go.Box(
        x=dark_li,
        y=dark_attribute_count_list,
        name='Dark',
        marker_color='#9d0208'
    ))
    fig.add_trace(go.Box(
        x=medium_li,
        y=medium_attribute_count_list,
        name='Medium',
        marker_color='#dc2f02'
    ))
    fig.add_trace(go.Box(
        x=light_li,
        y=light_attribute_count_list,
        name='Light',
        marker_color='#f48c06'
    ))
    fig.add_trace(go.Box(
        x=albino_li,
        y=albino_attribute_count_list,
        name='Albono',
        marker_color='#ffba08'
    ))

    return fig

# load data
tx_db = pd.read_csv('./data/tx_db.csv', index_col=0)
tx_db.sort_values(by='date', inplace=True)

tx_db_2021 = tx_db[tx_db['date'] > '2020-12-31']
tx_db_2021 = tx_db_2021[tx_db_2021['skin_tone'] != 'Non-human']

def get_grouped_box_data(skin_tone):
    all_li = list(tx_db_2021[(tx_db_2021['skin_tone'] == skin_tone)]['eth_price'])
    dark_li = [
        list(tx_db_2021[(tx_db_2021['skin_tone'] == skin_tone) & (tx_db_2021['attr_count'] == attr_count)]['eth_price']) 
        for attr_count in [1, 2, 3, 4, 5]]
    
    all_attribute_count_list = ['All'] * len(all_li)
    dark_attribute_count_list = [
        len(dark_li[i])
        for i in range(len(dark_li))
    ]

    dark_li = all_li + list(chain(*dark_li))

    dark_attribute_count_list = [
        [f'{attr_count} attributes'] * dark_attribute_count_list[attr_count-1]
        for attr_count in [1, 2, 3, 4, 5]
    ]

    dark_attribute_count_list = all_attribute_count_list + list(chain(*dark_attribute_count_list))
    return dark_li, dark_attribute_count_list

dark_li, dark_attribute_count_list = get_grouped_box_data('Dark')
medium_li, medium_attribute_count_list = get_grouped_box_data('Medium')
light_li, light_attribute_count_list = get_grouped_box_data('Light')
albino_li, albino_attribute_count_list = get_grouped_box_data('Albino')

# generate figure2
fig2 = get_vis2_fig(dark_li, medium_li, light_li, albino_li, 
                    dark_attribute_count_list, medium_attribute_count_list, light_attribute_count_list, albino_attribute_count_list)
fig2.update_layout(
    xaxis=dict(title='Price (ETH)', zeroline=False),
    title='Distribution of the CryptoPunk price by skin tones (after 2021)',
    boxmode='group',
    height=800,
    width=800,
    plot_bgcolor='rgba(0,0,0,0)',
)
fig2.update_xaxes(showline=True, linewidth=2, linecolor='#adb5bd', gridcolor='#adb5bd')
fig2.update_traces(orientation='h') # horizontal box plots

# generate layout2
layout2 = html.Div(
    children=[
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='four columns div-user-controls figure-description',
                    children=[
                        html.H1('A Glance into NFT Ethics'),
                        html.H2('Price Differences of CryptoPunks with Different Skin Tones'),
                        html.P(
                            'To further depict the price differences for CryptoPunks with dif- ferent skin tones, we choose the transaction records starting from Jan 1th 2022, to visualize the price distribution for each skin tone. Moreover, we explore the price distribution of skin tones of punks with different numbers of attributes (i.e., 1, 2, 3, 4, 5), which is illustrated in this figure.'
                        ),
                        html.P(
                            'Specifically, the median prices are 41.99 ETH for the punks with dark skin tone, 43.85 ETH for the punks with medium skin tone, 44.72 ETH for the punks with light skin tone, and 40 ETH for the punks with albino skin tone. Since Albino is a rare Punk attribute (9 in 10000), we hypothesize that the low median price is probably because of their low number of cases in the trade. With the exception of Albino Skin Tone, for the other three primary Skin tones, we found that CryptoPunk with darker colors had a lower median price in the transaction.'
                        ),
                        html.Div(style={'margin-top': '20px'}),
                        html.Div(
                            children=[
                                html.Div(
                                    className='bottom-nav',
                                    children=[
                                        html.A(id='', className='', children=[
                                            html.Button('<', id='button-prev', n_clicks=0)
                                        ], href=common.base_url+'/vis1', style={'margin-right': '2rem'}),
                                        html.A(id='', className='', children=[
                                            html.Button('>', id='button-next', n_clicks=0),
                                        ], href=common.base_url+'/vis3'),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='eight columns div-for-charts bg-white figure-right',
                    children=[
                        dcc.Graph(
                            id='example-graph',
                            figure=fig2
                        )
                    ]
                )
            ]
        )
    ]
)

# Visualization 3 =============================================================
def get_vis3_fig(skin_tone_prices):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=skin_tone_prices['date'], y=skin_tone_prices['Overall'], name="Overall", line=dict(width=1.3, color='#0077b6', dash='dot')))
    fig.add_trace(go.Scatter(x=skin_tone_prices['date'], y=skin_tone_prices['Albino'], name="Albino", line=dict(width=1.3, color='#ffba08')))
    fig.add_trace(go.Scatter(x=skin_tone_prices['date'], y=skin_tone_prices['Light'], name="Light", line=dict(width=1.3, color='#f48c06')))
    fig.add_trace(go.Scatter(x=skin_tone_prices['date'], y=skin_tone_prices['Medium'], name="Medium", line=dict(width=1.3, color='#dc2f02')))
    fig.add_trace(go.Scatter(x=skin_tone_prices['date'], y=skin_tone_prices['Dark'], name="Dark", line=dict(width=1.3, color='#9d0208')))

    fig.update_yaxes(title_text="Price (ETH)")
    fig.update_xaxes(title_text="Date")

    return fig

# load data
skin_tone_prices = tx_db.groupby(['date', 'skin_tone']).agg({"eth_price": ["median"]}).unstack(1)
skin_tone_prices.columns = ['Albino', 'Dark', 'Light', 'Medium', 'Non-human']
skin_tone_prices = skin_tone_prices.reset_index()
skin_tone_prices = skin_tone_prices[skin_tone_prices['date'] > '2021-05-31']

overall_prices = tx_db[tx_db['skin_tone'] != 'Non-human'].groupby(['date']).agg({"eth_price": ["median"]})
overall_prices.columns = ['Overall']
overall_prices = overall_prices.reset_index()
overall_prices = overall_prices[overall_prices['date'] > '2021-05-31']

skin_tone_prices = skin_tone_prices.merge(overall_prices, on='date', how='left')

# generate fig3
fig3 = get_vis3_fig(skin_tone_prices)
fig3.update_layout(
    title="Median Price by Skin Tone vs Time (after 2021)",
    autosize=False,
    width=800,
    height=600,
    plot_bgcolor='rgba(0,0,0,0)',
)
fig3.update_xaxes(showline=True, linewidth=2, linecolor='#adb5bd', gridcolor='#adb5bd')
fig3.update_yaxes(showline=True, linewidth=2, linecolor='#adb5bd', gridcolor='#adb5bd')

# generate layout3
layout3 = html.Div(
    children=[
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='four columns div-user-controls figure-description',
                    children=[
                        html.H1('A Glance into NFT Ethics'),
                        html.H2('Price Difference Trends over Time'),
                        html.P(
                            'We further explore how the price difference among punks with different skin tones changes over time, especially since the CryptoP- unks project began to draw more and more attention from the world in 2021. Figure 4 shows the median prices of CryptoPunks with dif- ferent skin tones after May 31, 2020. We can observe that the overall price trends for punks with various skin tones are very similar; that is, they all follow the overall price trend for the whole CryptoPunk collection. Nevertheless, Figure 4 also indicates that most of the price gap between punks with lighter skin tones and darker skin tones does exist, especially where the most expensive CryptoPunk transactions are often associated with punks with lighter skin tones.'
                        ),
                        html.Div(style={'margin-top': '20px'}),
                        html.Div(
                            children=[
                                html.Div(
                                    className='bottom-nav',
                                    children=[
                                        html.A(id='', className='', children=[
                                            html.Button('<', id='button-prev', n_clicks=0)
                                        ], href=common.base_url+'/vis2', style={'margin-right': '2rem'}),
                                        html.A(id='', className='', children=[
                                            html.Button('>', id='button-next', n_clicks=0),
                                        ], href=common.base_url+'/vis4'),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='eight columns div-for-charts bg-white figure-right',
                    children=[
                        dcc.Graph(id='example-graph', figure=fig3)
                    ]
                )
            ]
        )
    ]
)

# Visualization 4 =============================================================
def get_vis4_fig(data):
    colorsIdx = {'Dark': '#A4031F', 'Medium': '#DB9065',
                 'Light': '#F2A359', 'Albino': '#F2DC5D',
                 'Non-human': '#8DFFCD'}
    trace_list = []
    for sc in ['Non-human', 'Albino', 'Light', 'Medium', 'Dark']:
        df3_temp = data[data['punk_skin_tone'] == sc]
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
    fig = go.Figure(data=trace_list)
    return fig

# load data
data4 = pd.read_csv('./data/vis4_data.csv', header=0, index_col=0)
data4 = data4[data4['price'] < 700]

# generate fig4
fig4 = get_vis4_fig(data4)
fig4.update_traces(hoverinfo="none", hovertemplate=None)
fig4.update_layout(
    xaxis=dict(title='Date'),
    yaxis=dict(title='ETH Price'),
    plot_bgcolor='rgba(255,255,255,0.1)',
    width=800,
    height=600,
    title='Scatter Plot: CryptoPunk Transactions with Punk Skin Tone',
    titlefont=dict(size=20, family='PT Sans Narrow'),
)

# generate layout4
layout4 = html.Div(
    children=[
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='four columns div-user-controls figure-description',
                    children=[
                        html.H1('A Glance into NFT Ethics'),
                        html.H2('Price Difference Trends over Time'),
                        html.P(
                            'Furthermore, we illustrate the CryptoPunks transaction in regard to the punks’ skin tones using a scatter plot, where each scatters denotes a CryptoPunk transaction whose color represents the punk’s skin tone. Similar to the previous figure, we can observe that most transactions associated with punks with darker skin tones generally show lower transaction prices compared to other transactions on the same date.'
                        ),
                        html.Div(style={'margin-top': '20px'}),
                        html.Div(
                            children=[
                                html.Div(
                                    className='bottom-nav',
                                    children=[
                                        html.A(id='', className='', children=[
                                            html.Button('<', id='button-prev', n_clicks=0)
                                        ], href=common.base_url+'/vis3', style={'margin-right': '2rem'}),
                                        html.A(id='', className='', children=[
                                            html.Button('>', id='button-next', n_clicks=0),
                                        ], href=common.base_url+'/vis5'),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='eight columns div-for-charts bg-white figure-right',
                    children=[
                        dcc.Graph(id="graph-4", figure=fig4),
                        dcc.Tooltip(id="graph-tooltip-4"),
                    ]
                )
            ]
        )
    ]
)

# add hover effect
@ app.callback(
    Output("graph-tooltip-4", "show"),
    Output("graph-tooltip-4", "bbox"),
    Output("graph-tooltip-4", "children"),
    [Input("graph-4", "hoverData")]
)

def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]
    
    df_row = data4.iloc[num]
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

# Visualization 5 =============================================================
def get_vis5_fig(sent_year_df):
    fig = go.Figure(data=[
        go.Bar(name='Negative', x=years, y=sent_year_df['neg'], marker=dict(color='#78C1E2')),
        go.Bar(name='Neutral', x=years, y=sent_year_df['neu'], marker=dict(color='#52CB8B')),
        go.Bar(name='Positive', x=years, y=sent_year_df['pos'], marker=dict(color='#FAC261')),
    ])
    # Change the bar mode
    fig.update_layout(barmode='stack', legend=dict(
        yanchor="top",
        y=0.99,
    ))
    return fig

# load data
data_path = './data/vis5_data.csv'

sent_year_df = pd.read_csv(data_path, header=0, index_col=0)

years=['2017', '2018', '2019', '2020', '2021', '2022']
sents=['neg', 'neu', 'pos']

# generate fig5
fig5 = get_vis5_fig(sent_year_df)
fig5.update_traces(hoverinfo="none", hovertemplate=None)
fig5.update_layout(
    xaxis=dict(title='Year'),
    yaxis=dict(title='Percentage of Tweets'),
    plot_bgcolor='rgba(255,255,255,0.1)',
    height=600,
    width=800,
    title='Bar Chart & WordCloud: The Sentiments of Twitter Users Towards NFT Ethics-Related Topics',
)

# generate layout5
layout5 = html.Div(
    children=[
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='four columns div-user-controls figure-description',
                    children=[
                        html.H1('A Glance into NFT Ethics'),
                        html.H2('Twitter Analysis with Bar Chart & Word Cloud'),
                        html.P(
                            'The bar chart and the word cloud visualizations in the figure reflected the sentiments of Twitter users’ attitudes about NFT ethics. The keywords we chose included NFT, ethics, fairness, gender, race, equality, and so on. By clicking on each section, we can see the main discussion word cloud under this section on the right. Even though the NFT trust topic is also important, we believe gender and racial inequities are also an essential part of NFT ethics. However, we found that very few users were tweeting about race and gender equality in NFT topics. Combining the data analysis and conclusions of the previous four sections with the Twitter word cloud we present, we find that gender and racial inequalities do exist in the generation and transaction process, but Twitter users are not talking about these things. This means that the problem is existing, but the attention is missing.'
                        ),
                        html.Div(style={'margin-top': '20px'}),
                        html.Div(
                            children=[
                                html.Div(
                                    className='bottom-nav',
                                    children=[
                                        html.A(id='', className='', children=[
                                            html.Button('<', id='button-prev', n_clicks=0)
                                        ], href=common.base_url+'/vis4', style={'margin-right': '2rem'}),
                                        html.A(id='', className='', children=[
                                            html.Button('>', id='button-next', n_clicks=0),
                                        ], href=common.base_url+'/'),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='eight columns div-for-charts bg-white figure-right',
                    children=[
                        dcc.Graph(id="graph-5", figure=fig5, clear_on_unhover=True),
                        dcc.Tooltip(id="graph-tooltip-5"),
                    ]
                )
            ]
        )
    ]
)

# add hover effect
@app.callback(
    Output("graph-tooltip-5", "show"),
    Output("graph-tooltip-5", "bbox"),
    Output("graph-tooltip-5", "children"),
    Input("graph-5", "hoverData"),
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
        font_color = 'blue'
    elif sent == 'neu':
        Sent = 'Neutral'
        font_color = 'green'
    elif sent == 'pos':
        Sent = 'Positive'
        font_color = 'orange'
    
    image_path = './data/wc_imgs/{}_{}.png'.format(year, sent)
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


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    pathname = pathname[len(common.base_url):]
    if pathname == '/':
        return index.layout
    elif pathname == '/vis1':
        return layout1
    elif pathname == '/vis2':
        return layout2
    elif pathname == '/vis3':
        return layout3
    elif pathname == '/vis4':
        return layout4
    elif pathname == '/vis5':
        return layout5
    elif pathname == '/end':
        return end.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run(debug=True, port=8070)
