from dash import Dash, html
import dash_bootstrap_components as dbc


class Layout():
    def creat_layout():
        imagen=dbc.Container(
            html.Header([
                html.Img(
                    src="/assets/kabum.png",
                    style={
                        "width":"100px",
                        "height":"100px",
                        "display": "flex",
                        "justify-content": "center",
                        "margin": "0 auto",
                        "border": "3px solid blue",
                        "border-radius": "50%",
                        "border-image": "url("") 150 round",
                    },
                    alt="foto do perfil"
            )
        ],style={
                    "paddingTop": "40px",   
                    "textAlign": "center"
                })
        )
        print("erro layout")
        return imagen

print("erro")
    
    # "display": "block",
    # "margin": "0 auto",
    # "border-radius": "50%",