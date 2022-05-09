from turtle import color, width
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

mgr_options = ['2017', '2018', '2019', '2020', '2021', '2022']

app = dash.Dash()

app.layout = html.Div([
    html.H2("Sales Funnel Report"),
    html.Div(
        [
            dcc.Dropdown(
                id="Manager",
                options=[{
                    'label': i,
                    'value': i
                } for i in mgr_options],
                value='2021'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph', style={'width': '75%'}),
])


@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('Manager', 'value')])
def update_graph(Manager):
    VIS_DATA_PATH = '../../data'
    df_plot = pd.read_csv("{}/vis5/sent_distribution_{}.csv".format(VIS_DATA_PATH, Manager))
    
    trace = go.Bar(x=df_plot['sentiment'], y=df_plot['percentage'])#, color=['#87B9E8', '#E788A1', '#EBD498'])
    # trace = px.bar(df_plot, x='sentiment', y='percentage')#, color=['#87B9E8', '#E788A1', '#EBD498'])

    return {
        'data': [trace],
        'layout':
        go.Layout(
            title='Customer Order Status for {}'.format(Manager),
            barmode='stack',)
    }


if __name__ == '__main__':
    app.run_server(debug=True, host="localhost", port='8052')