from dash import html

def buttons():
    button = html.Div(
        [
            html.A(
                html.Img(
                    src="/assets/insta.jpeg",
                    style={"width": "40px", "borderRadius": "50%"}
                ),
                href="https://instagram.com",
                target="_blank",
            ),
            html.A(
                html.Img(
                    src="/assets/whatsapp.png",
                    style={"width": "40px", "borderRadius": "50%"}
                ),
                href="https://www.whatsapp.com/",
                target="_blank",
            ),
            html.A(
                html.Img(
                    src="/assets/github2.png",
                    style={"width": "40px", "borderRadius": "50%"}
                ),
                href="https://github.com/kazukito4",
                target="_blank",
            ),
        ],
        style={
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "gap": "500px",      
            "marginTop": "50px",
        }
    )
    return button
