import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3(
        id = 'intro',
        children = 'PKMN Image Finder: Just type the name of the pokemon :)'
    ),
    dcc.Input(
        id = 'image-retrieve',
        value = 'Pikachu',
        type = 'text'
    ),
    html.Div(
        id = 'pkmn-image'
    ),
])

@app.callback(
    Output(component_id='pkmn-image', component_property='children'),
    [Input(component_id='image-retrieve', component_property='value')]
)
def retrieve_pkmn_image(pkmn_name):
    pkmn_name = pkmn_name.title()
    pkmn_name += '.png'
    if pkmn_name not in os.listdir(os.path.join('assets/pkmn_images')):
        return None
    data = html.Img(
        src = '/assets/pkmn_images/{name}'.format(name=pkmn_name)
    )
    return data

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
