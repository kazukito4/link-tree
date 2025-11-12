from dash import Input, Output, State, html, dcc,callback


@callback(
    Output("input-caixa_de_anotações", "children"),
    Input("button-LINK", "n_clicks"),
    State("input-caixa_de_anotações", "children"),
)



def caixa_de_anotações(n_clicks, current_children):
    if n_clicks is None:
        return current_children

    anotações = html.Div(
        dcc.Textarea(
            placeholder="anotações",
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
    current_children.append(anotações)
    return current_children
