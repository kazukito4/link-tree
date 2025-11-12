from dash import Dash, html, Input, Output, State
import dash_bootstrap_components as dbc
from layout.layout_button import buttons

class Layout():
    def creat_layout():
        imagen = dbc.Container(
            [
                html.Header(
                    [
                        html.Img(
                            src="/assets/kabum.png",
                            style={
                                "width": "100px",
                                "height": "100px",
                                "display": "flex",
                                "justify-content": "center",
                                "margin": "0 auto",
                                "border": "3px solid blue",
                                "border-radius": "50%",
                            },
                        ),

                        dbc.Button(
                            "LINK",
                            id="add-input-OHHH",
                            color="secondary",
                            style={"marginLeft": "1000px"}
                        ),

                        html.P(
                            "programador cristão",
                            style={
                                "color": "white",
                                "marginTop": "10px",
                                "fontSize": "18px",
                                "textAlign": "center"
                            }
                        )
                    ],
                    style={
                        "paddingTop": "40px",
                        "textAlign": "center"
                    }
                ),

                dbc.CardBody([
                    buttons()
                ]),
                html.Div(
                    id="input-SAFADA",
                    style={
                        "marginTop": "40px",
                        "display": "flex",
                        "flexDirection": "column",
                        "gap": "20px"
                    }
                )
            ]
        )
        return imagen
