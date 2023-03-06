from pydoc import classname
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
from pages import common
from pages.common import nav

links = [
    {'name': '	arXiv:2206.12922',
        'url': 'https://doi.org/10.48550/arXiv.2206.12922'},
]

# Create a list of hyperlinks
link_list = html.Ul([
    html.Li(
        html.A(link['name'], href=link['url'])
    ) for link in links
])


layout = html.Div(
    children=[
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='ten columns div-user-controls',
                    children=[
                        html.H1('A Glance into NFT Ethics: On Ethics of CryptoPunks', style={
                                "padding-left": "7rem", "color": "#fffcfc"}),
                        html.H1('Presented at ChinaVis ‘22', style={
                                "padding-left": "7rem", "font-size": "2rem", "color": "#fffcfc"}),
                        html.H1('Authors: Yufan Zhang, Zichao Chen, Luyao Zhang, Xin Tong', style={
                                "padding-left": "7rem", "font-size": "2rem", "color": "#fffcfc"}),
                    ]
                ),
                html.Div(
                    className='ten columns div-user-controls', 
                    children=[
                        html.H2('Read our paper:'),
                        html.A('arXiv:2206.12922', href='https://doi.org/10.48550/arXiv.2206.12922', style={"padding-left": "1rem", 'font-size': '2rem'}),
                        html.Div(style={'margin-top': '20px'}),
                    ]
                ),
                html.Div(
                    className='ten columns div-user-controls', 
                    children=[
                        html.H2('Contacts:'),
                        html.A('yufanbruce@outlook.com', href='yufanbruce@outlook.com', style={"padding-left": "1rem", 'font-size': '2rem'}),
                        html.Div(style={'margin-top': '20px'}),
                    ]
                ),
            ]
        ),
        html.Div(
            className='two columns', 
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='bottom-nav',
                            children=[
                                html.A(id='', className='', children=[
                                    html.Button('<', id='button-prev', n_clicks=0)
                                ], href=common.base_url+'/vis5', style={'margin-right': '2rem'}),
                                html.A(id='', className='', children=[
                                    html.Button('⇤', id='button-next', n_clicks=0),
                                ], href=common.base_url+'/'),
                            ]
                        )
                    ]
                )
            ]
        ),
        html.Div(
            children=[
                html.Img(src=common.base_url+'/assets/poster.jpg', className='poster-img'),
            ]
        )
    ]
)
