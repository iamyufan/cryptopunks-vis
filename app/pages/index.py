from dash import dcc, html, Input, Output, callback
from pages import common
from pages.common import nav


layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='ten columns div-user-controls index-title-container',
                              children=[
                                  html.H1('A Glance into NFT Ethics:',
                                          className='index-subtitle'),
                                  html.H1('On Ethics of CryptoPunks', style={
                                        'background-color': '#1d31ea', 'max-width': '100%'}, className='index-title'),
                                  html.H1('Presented at ChinaVis ‘22', style={},
                                          className='index-subtitle'),
                              ]
                              ),
                     html.Div(className='four columns div-user-controls index-author-container',
                              children=[
                                  html.P('Authors: ', className='index-author',
                                         style={'margin-bottom': '5px', 'font-weight': 'bold'}),
                                  html.P('Yufan Zhang',
                                         className='index-author'),
                                  html.P('Zichao Chen',
                                         className='index-author'),
                                  html.P('Luyao Zhang',
                                         className='index-author'),
                                  html.P('Xin Tong',
                                         className='index-author'),
                              ]
                              ),
                     html.Div(className='ten columns div-user-controls', children=[
                         html.P("As a blockchain-based application, Non-Fungible Token (NFT) has received worldwide attention over the past few years. Digital artwork is the main form of NFT that can be stored on different blockchains. Although the NFT market is rapidly developing, we observed potential ethical and racial fairness issues in the design of NFT artworks due to a lack of ethical guidelines or censorship. Therefore, we investigated CryptoPunks, the most famous collection in the NFT market, to explore and visualize its potential ethical issues. We explored the ethical issues from three aspects: design, trading transactions, and related topics on Twitter. We scraped data from Twitter and Dune Analytics using python libraries, Twitter crawler, and sentiment analysis tools. Our five visualizations implied that 1.6 times more male punks were created in the initial design process than the female ones. And the male ones have a higher average selling price than females; lighter-skinned punks tend to sell for higher prices. The results of our study and visualizations provide a preliminary exploration of CryptoPunks and further inspire future ethical-related investigation and research in the NFT domain.", className='index-description')
                     ]),
                 ]),
        html.Div(className='two columns', children=[
            nav,
        ]),
        html.Div(id='', className='', children=[
            html.Img(src=common.base_url+'/assets/poster.jpg',
                     className='poster-img'),
        ])
    ]
)
