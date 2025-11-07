from dash import Dash


from layout.layout_heander import Layout
app = Dash(__name__)
app.layout = Layout.creat_layout()

if __name__ == "__main__":
    app.run(debug=True)

print("erro")