import dash_bootstrap_components as dbc
from dash import html

def recipe_list(title="Recipe List"):
    return dbc.Row(
        dbc.Col(
            html.Div(title, className="text-center p-4 border"),
            width=12
        ),
        className="mb-4"
    )