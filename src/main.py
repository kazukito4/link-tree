from dash import Dash
import dash_bootstrap_components as dbc
from layout.layout_heander import Layout


app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
app.layout = Layout.creat_layout()

if __name__ == "__main__":
    app.run(debug=True)

print("erro")