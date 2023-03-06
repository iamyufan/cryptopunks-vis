from dash import html

base_url = "/cryptopunks"


nav = html.Div(
    children=[
        html.Div(className='bottom-nav',
            children=[
                html.A(id='', className='', children=[
                    html.Button('<', id='button-prev', n_clicks=0)
                ], href= base_url+'/', style={'margin-right': '2rem'}),
                html.A(id='', className='', children=[
                    html.Button('>', id='button-next', n_clicks=0),
                ], href= base_url+'/vis1'),
            ]
        )
    ]
)