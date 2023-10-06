# write a dash code to build a table with the following features:
# 1. The table should be editable
# 2. The columns of the table should be Weight,height,Age and Temperature
# 3. The table should have a dropdown menu for the column Temperature in range 0-100
# 4. The table should have a dropdown menu for the column Age in range 0-100
# 5. The table should have a dropdown menu for the column Weight in range 0-100 in steps of 5
# 6. The table should have a dropdown menu for the column Height in range 0-100 in steps of 5

# write your code here
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Sample data
# keep the sample data as per column names for 10 entries as mentioned above

data = {
        'Patient_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Weight': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Height': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Age': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
        'Temperature': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]}

# make all the data strings
data = {k: [str(i) for i in v] for k, v in data.items()}

df = pd.DataFrame(data)

print(df)

app = dash.Dash(__name__)

# add a heading to the app and place it in the center of the app
#calculate BMI for each row and plot a bar chart for the same

# write your code here
# BMI = weight/height^2

df['BMI'] = df['Weight'].astype(float)/(df['Height'].astype(float)**2)
print(df)

# add bar chart of the calculated bmi in the dataframe above and place it in the bottom of the app
# do not show the BMI column in the table

app.layout = html.Div([
    html.Img(
        src='assets/header.png', 
        alt='Your Image',
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
            'options': [{'label': i, 'value': i} for i in df['Temperature'].unique()]
        },
        'Age': {
            'options': [{'label': i, 'value': i} for i in df['Age'].unique()]
        },
        'Weight': {
            'options': [{'label': i, 'value': i} for i in df['Weight'].unique()]
        },
        'Height': {
            'options': [{'label': i, 'value': i} for i in df['Height'].unique()]
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
    )
])







if __name__ == '__main__':
    app.run_server(debug=True)







