from dash import Dash, html


class Layout():
    def creat_layout():
        imagen=html.Header([
            html.Img(
                src="/assets/kabum.png",
                style={
                    "display": "block",
                    "width":"300px",
                    "margin": "0 auto",
                    "border-radius": "86%",
                    "border": "10px solid transparent",
                    "padding": "15px",
                    "border-image": "url(border.png) 50 round"
                },
                alt="foto do perfil"
            )
        ])
        print("erro layout")
        return imagen

print("erro")
    