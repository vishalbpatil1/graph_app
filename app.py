import plotly.express as px
df = px.data.iris()
import plotly.graph_objects as go # or plotly.express as px
#fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()
import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
    
])

if __name__ == '__main__':
    app.run_server()
