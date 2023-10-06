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


