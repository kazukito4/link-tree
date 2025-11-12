from dash import Input, Output, State, html, dcc
from main import app

@app.callback(
    Output("input-SAFADA", "children"),
    Input("add-input-OHHH", "n_clicks"),
    State("input-SAFADA", "children"),
)
def caixa(n_clicks, current_children):
    if n_clicks is None:
        return current_children

    porra = html.Div(
        dcc.Textarea(
            placeholder="vai bota",
            style={
                "width": "100%",
                "height": "120px",
                "padding": "10px",
                "borderRadius": "10px",
                "fontSize": "16px"
            }
        ),
        style={
            "background": "white",
            "padding": "10px",
            "borderRadius": "12px",
            "boxShadow": "0 0 10px rgba(0,0,0,0.2)"
        }
    )

    current_children = current_children or []
    current_children.append(porra)
    return current_children
