
import pandas as pd
import json

# Load the CSV file
input_file = 'input.csv'
df = pd.read_csv(input_file)

# Group by 'id' and 'group', and calculate the total minutes per group
grouped_df = df.groupby(['id', 'group'], as_index=False)['min'].sum()

# Save the grouped data to a CSV file
grouped_df.to_csv('output.csv', index=False)

# Prepare data for JSON format
json_data = []
for id_value, group_data in grouped_df.groupby('id'):
    group_dict = {}
    for _, row in group_data.iterrows():
        group_dict[row['group']] = row['min']
    json_data.append({"id": id_value, "group": [group_dict]})

# Save the JSON data to a file
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
