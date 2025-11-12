from dash import html
import dash_bootstrap_components as dbc

def buttons():
    button = html.Div(
        [
            html.A(
                dbc.Button(
                    html.Img(src="/assets/insta.jpeg", style={"width": "30px","borderRadius": "50%"}),
                    style={
                        "backgroundColor": "transparent",
                        "border": "none",
                        "padding": "0",
                        "outline": "none",
                        "boxShadow": "none"
                    },
                    className="me-1"
                ),
                href="https://instagram.com",
                target="_blank",
                
            ),
            html.A(
                dbc.Button(
                    html.Img(src="/assets/whatsapp.png", style={"width": "30px","borderRadius": "50%"}),
                    style={
                        "backgroundColor": "transparent",
                        "border": "none",
                        "padding": "0",
                        "outline": "none",
                        "boxShadow": "none"
                    },
                    className="me-1"
                ),
                href="https://www.whatsapp.com/",
                target="_blank",
            ),
            html.A(   
                dbc.Button(
                    html.Img(src="/assets/github2.png", style={"width": "30px","borderRadius": "50%"}),
                    style={
                        "backgroundColor": "transparent",
                        "border": "none",
                        "padding": "0",
                        "outline": "none",
                        "boxShadow": "none"
                    },
                    className="me-1"
                ),
                href="https://github.com/kazukito4",
                target="_blank",
            ),    
        ],
        style={
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "gap": "300px",
            "marginTop": "50px",
        }
    ) 
    return button
