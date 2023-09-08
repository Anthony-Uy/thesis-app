# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1("My Dash App"),
#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'}],
#             'layout': {
#                 'title': 'Sample Dash Plot'
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

# import dash
# from dash import Dash, html, dcc
# import pandas as pd

# data = (
#     pd.read_csv("hw_25000.csv")
# )

# app = Dash(__name__)


# if __name__ == '__main__':
#     app.run_server(debug=True)


# import dash
# from dash import dcc, html, Dash
# # import dash_core_components as dcc
# # import dash_html_components as html
# import pandas as pd

# app = dash.Dash(__name__)

# # Read the CSV file into a DataFrame
# data = (pd.read_csv('hw_25000.csv'))

# # Define the layout of your Dash app
# # app.layout = html.Div([
# #     dcc.Graph(
# #         id='scatter-plot',
# #         figure={
# #             'data': [
# #                 # Create a scatter plot using the data from your DataFrame
# #                 {'x': df['Height(Inches)'], 'y': df['Weight(Pounds)'], 'type': 'scatter', 'mode': 'markers', 'name': 'Height vs. Weight'},
# #             ],
# #             'layout': {
# #                 'title': 'Height vs. Weight Scatter Plot',
# #                 'xaxis': {'title': 'Height (inches)'},
# #                 'yaxis': {'title': 'Weight (pounds)'}
# #             }
# #         }
# #     )
# # ])

# app.layout = html.Div(
#     children=[
#         html.H1(children="Height Weight Analytics"),
#         html.P(
#             children=(
#                 "Analyze the behavior of avocado prices and the number"
#                 " of avocados sold in the US between 2015 and 2018"
#             ),
#         ),
#         dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": data["Height[Inches]"],
#                         "y": data["Weight[Pounds]"],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"Height and Weight"},
#             },
#         ),
#         # dcc.Graph(
#         #     figure={
#         #         "data": [
#         #             {
#         #                 "x": data["Date"],
#         #                 "y": data["Total Volume"],
#         #                 "type": "lines",
#         #             },
#         #         ],
#         #         "layout": {"title": "Avocados Sold"},
#         #     },
#         # ),
#     ]
# )

# if __name__ == '__main__':
#     app.run_server(debug=True)



import dash
from dash import dcc,html,Dash
import pandas as pd

app = dash.Dash(__name__)

# Read the CSV file into a DataFrame
df = pd.read_csv('hw_25000.csv')

app.layout = html.Div([
    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                {'x': df[' Height'], 'y': df[' Weight'], 'type': 'scatter', 'mode': 'markers', 'name': 'Height vs. Weight'},
            ],
            'layout': {
                'title': 'Height vs. Weight Scatter Plot',
                'xaxis': {'title': 'Height (inches)'},
                'yaxis': {'title': 'Weight (pounds)'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


# import dash
# from dash import dcc,html,Dash
# import pandas as pd
# import numpy as np

# app = dash.Dash()

# df = pd.read_csv('trees.csv')
# # print(df.head())
# c1_array = df[' Girth'].to_numpy()
# c2_array = df[' Height'].to_numpy()

# app.layout = html.Div([
#     html.H1("CSV Data Display"),
#     dcc.Graph(
#         id='datatable',
#         figure = {
#             'data' : [
#                 # {'x' : df['Index'], 'y' : df['Girth'], 'type':'bar', 'name':'First Chart'}
#                 {'x' : c1_array, 'y' : c2_array, 'type':'bar', 'name':'First Chart'}

#             ],
#             'layout' :{
#                 'title' :'Simple Chartk'
#             }
#         }
#     ),
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
