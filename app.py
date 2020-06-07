import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server=app.server
app.layout = html.Div([ dcc.Graph(figure=fig)])
if __name__ == '__main__':
    app.run_server(debug=Flase)
