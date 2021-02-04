import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyoff

# df = px.data.iris() # iris is a pandas DataFrame
# fig = px.scatter(df, x="sepal_width", y="sepal_length")


# data = pd.read_csv("avocado.csv")
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
# data.sort_values("Date", inplace=True)

data = pd.read_csv("data/df_supply_demand.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d %H:%M:%S")
# data.sort_values("Date", inplace=True)

#q2
cols_to_used = ['Date', 'Hour', 'Active drivers', 'Active customers']
q2 = data[cols_to_used]
q2 = q2.groupby(['Hour']).mean().reset_index()

fig = go.Figure()
fig.add_trace(go.Scatter(x=q2['Hour'], y=q2['Active drivers'],
                    mode='lines',
                    name='Supply'))
fig.add_trace(go.Scatter(x=q2['Hour'], y=q2['Active customers'],
                    mode='lines',
                    name='Demand'))

fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1
    )
)

#q3
cols_to_used = ['DayName',
 'Hour',
 'Active drivers',
 'Active customers',
 'SD_Value']
q3 = data[cols_to_used]

# order dataframe based on DayName order, Monday to Sunday
q3['DayName'] = pd.Categorical(q3['DayName'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)

# get the average value of daily supply ('Active drivers') and demand ('Active customers')
q3 = q3.groupby(['DayName','Hour']).mean().reset_index()

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=q3[q3['DayName'] == 'Monday']['Hour'], y=q3[q3['DayName'] == 'Monday']['SD_Value'],
                    mode='lines',
                    name='Monday'))

fig3.add_trace(go.Scatter(x=q3[q3['DayName'] == 'Tuesday']['Hour'], y=q3[q3['DayName'] == 'Tuesday']['SD_Value'],
                    mode='lines',
                    name='Tuesday'))

fig3.add_trace(go.Scatter(x=q3[q3['DayName'] == 'Wednesday']['Hour'], y=q3[q3['DayName'] == 'Wednesday']['SD_Value'],
                    mode='lines',
                    name='Wednesday'))

fig3.add_trace(go.Scatter(x=q3[q3['DayName'] == 'Thursday']['Hour'], y=q3[q3['DayName'] == 'Thursday']['SD_Value'],
                    mode='lines',
                    name='Thursday'))

fig3.add_trace(go.Scatter(x=q3[q3['DayName'] == 'Friday']['Hour'], y=q3[q3['DayName'] == 'Friday']['SD_Value'],
                    mode='lines',
                    name='Friday'))

fig3.add_trace(go.Scatter(x=q3[q3['DayName'] == 'Saturday']['Hour'], y=q3[q3['DayName'] == 'Saturday']['SD_Value'],
                    mode='lines',
                    name='Saturday'))

fig3.add_trace(go.Scatter(x=q3[q3['DayName'] == 'Sunday']['Hour'], y=q3[q3['DayName'] == 'Sunday']['SD_Value'],
                    mode='lines',
                    name='Sunday'))


fig3.update_layout(
    xaxis = dict(
        title_text = 'Hour',
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1
    ),
    yaxis = dict(
        title_text = 'Supply/Demand (SD) Value'
    )
)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Bolt - Supply Data Analysis"


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Bolt Supply Data Analysis", className="header-title"
                ),
                html.P(
                    children="Analyze the sample supply data information"
                    " and the demand from the user who saw a car in the app"
                    " between 14 November 2016 until 18 December 2016",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                # html.Div(
                #     children=[
                #         html.Div(children="Region", className="menu-title"),
                #         dcc.Dropdown(
                #             id="region-filter",
                #             options=[
                #                 {"label": region, "value": region}
                #                 for region in np.sort(data.region.unique())
                #             ],
                #             value="Albany",
                #             clearable=False,
                #             className="dropdown",
                #         ),
                #     ]
                # ),
                # html.Div(
                #     children=[
                #         html.Div(children="Type", className="menu-title"),
                #         dcc.Dropdown(
                #             id="type-filter",
                #             options=[
                #                 {"label": avocado_type, "value": avocado_type}
                #                 for avocado_type in data.type.unique()
                #             ],
                #             value="organic",
                #             clearable=False,
                #             searchable=False,
                #             className="dropdown",
                #         ),
                #     ],
                # ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range", className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    # children=dcc.Graph(
                    #     id="price-chart",
                    #     config={"displayModeBar": False},
                    # ),
                    # className="card",
                    children=dcc.Graph(
                        id="graph1",
                        figure=fig),
                    className="q2",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="graph2",
                        figure=fig3),
                    className="q3",
                ),
                # html.Div(
                #     children=dcc.Graph(
                #         id="volume-chart",
                #         config={"displayModeBar": False},
                #     ),
                #     className="card",
                # ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    [Output("graph1", "figure")],
    [
        Input("date-range", "start_date"),
        Input("date-range", "end_date")
    ],
)

def update_charts(start_date, end_date):
    pass
    # mask = (
    #     & (data.Date >= start_date)
    #     & (data.Date <= end_date)
    # )
    # filtered_data = data.loc[mask, :]
    # price_chart_figure = {
    #     "data": [
    #         {
    #             "x": filtered_data["Date"],
    #             "y": filtered_data["AveragePrice"],
    #             "type": "lines",
    #             "hovertemplate": "$%{y:.2f}<extra></extra>",
    #         },
    #     ],
    #     "layout": {
    #         "title": {
    #             "text": "Average Price of Avocados",
    #             "x": 0.05,
    #             "xanchor": "left",
    #         },
    #         "xaxis": {"fixedrange": True},
    #         "yaxis": {"tickprefix": "$", "fixedrange": True},
    #         "colorway": ["#17B897"],
    #     },
    # }

    # volume_chart_figure = {
    #     "data": [
    #         {
    #             "x": filtered_data["Date"],
    #             "y": filtered_data["Total Volume"],
    #             "type": "lines",
    #         },
    #     ],
    #     "layout": {
    #         "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
    #         "xaxis": {"fixedrange": True},
    #         "yaxis": {"fixedrange": True},
    #         "colorway": ["#E12D39"],
    #     },
    # }
    # return price_chart_figure, volume_chart_figure

if __name__ == "__main__":
    app.run_server(debug=True)
