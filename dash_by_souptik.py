# write a dash code to build a table with the following features:
# 1. The table should be editable
# 2. The columns of the table should be Weight,height,Age and Temperature
# 3. The table should have a dropdown menu for all the column in range 0-100

# import libraries
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Create Sample data 10 entries with coloumn names: Patient_ID, Weight, Height, Age, Temperature
data = {
        'Patient_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Weight (Kg)': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Height (inches)': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Age': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Temperature (Celcius)': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]}

# make all the data strings
data = {k: [str(i) for i in v] for k, v in data.items()}

# make data into a dataframe
df = pd.DataFrame(data)

# Create dash interface
app = dash.Dash(__name__)

# create a coloumn in dataframe named BMI using given formula: Weight/Height^2
df['BMI'] = df['Weight (Kg)'].astype(float)/(df['Height (inches)'].astype(float)**2)

# add an image to the app and place it in the top of the app. The image source is 'assets/header.png', with alt='AADS, Tech@Lilly'
# add a heading to the app and place it in the center of the app
# add bar chart of the calculated bmi in the dataframe above and place it in the bottom of the app
# add a footer to the app with the following text: Credits - Souptik, Asit, and Deepankar from AADS, Tech@Lilly
app.layout = html.Div([
    html.Img(
        src='assets/header.png', 
        alt='AADS, Tech@Lilly',
        style={'width': '100%', 'height': 'auto'}  # Set the width to 50%
    ),
    html.H1("Clinical Trial Data", style={'textAlign': 'center'}),
    dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {"name": col, "id": col, "editable": True,"presentation": "dropdown"}
        if col != 'Patient_ID'  # Make all columns editable except 'State'
        else {"name": col, "id": col, "editable": True, "presentation": "dropdown"}
        for col in df.columns
    ],
    dropdown={
        'Temperature': {
            'options': [{'label': i, 'value': i} for i in df['Temperature (Celcius)'].unique()]
        },
        'Age': {
            'options': [{'label': i, 'value': i} for i in df['Age'].unique()]
        },
        'Weight': {
            'options': [{'label': i, 'value': i} for i in df['Weight (Kg)'].unique()]
        },
        'Height': {
            'options': [{'label': i, 'value': i} for i in df['Height (inches)'].unique()]
        }
    },
    editable=True,
    style_cell={'textAlign': 'center'},  # Center-align the content horizontally
    style_data_conditional=[
        {
            'if': {'column_id': 'Temperature'},
            'textAlign': 'center',  # Center-align the content vertically
            'verticalAlign': 'middle'
        },
        {
            'if': {'column_id': 'Age'},
            'textAlign': 'center',  # Center-align the content vertically
            'verticalAlign': 'middle'
        },
        {
            'if': {'column_id': 'Weight'},
            'textAlign': 'center',  # Center-align the content vertically
            'verticalAlign': 'middle'
        },
        {
            'if': {'column_id': 'Height'},
            'textAlign': 'center',  # Center-align the content vertically
            'verticalAlign': 'middle'
        }
    ]
),
    dcc.Graph(
        id='BMI',
        figure={
            'data': [
                {'y': df['BMI'],'x':df['Patient_ID'], 'type': 'bar', 'name': 'BMI'},
            ],
            'layout': {
                'title': 'BMI',
                'xaxis': {'title': 'Patient_ID'},
                'yaxis': {'title': 'BMI'},
                'plot_bgcolor': '#ffffff',
                'showlegend': True,
                'width': '80%'
            }
        }
    ),
    html.H1("Credits - Souptik, Asit, and Deepankar from AADS, Tech@Lilly", style={'textAlign': 'center'})
])

if __name__ == '__main__':
    app.run_server(debug=True)