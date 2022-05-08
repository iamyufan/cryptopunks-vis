layout = go.Layout(xaxis={'title': 'Date'}, 
                   yaxis={'title': 'ETH Price'})

fig3 = go.Figure(layout=layout)

colorsIdx = {'Dark': '#A4031F', 'Medium': '#DB9065',
             'Light': '#F2A359', 'Albino': '#F2DC5D',
             'Non-human': '#8DFFCD'}

df3 = df3[df3['price'] < 700]

for year in ['2017', '2018', '2019', '2020', '2021', '2022']:
    df3_year = df3[df3['date'] > year]
    for sc in ['Non-human', 'Albino', 'Light', 'Medium', 'Dark']:
        df3_temp = df3_year[df3_year['punk_skin_tone'] == sc]
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
                opacity=0.8,
            )
        )
        fig3.add_trace(trace)
        
# Make the first trace visible
fig3.data[0].visible = True

# Create and add slider
steps = []
for i in range(len(fig3.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig3.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig3.update_layout(
    sliders=sliders
)