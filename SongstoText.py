import pandas as pd

# Load the sorted dataset with songs and popularity
dataset_path = 'sorted_dataset_with_popularity.csv'  # Replace with your sorted dataset file path
df_sorted = pd.read_csv(dataset_path)

# Check column names to identify any trailing spaces or issues
df_sorted.columns = df_sorted.columns.str.strip()

# Create a text box style output without fetching URIs (storing it in a variable)
text_box_output = "\n".join([f"{row['Artist']} - {row['Song']}" for index, row in df_sorted.iterrows()])

# Optionally save the output to a text file with utf-8 encoding to handle special characters
with open('songs_list.txt', 'w', encoding='utf-8') as f:
    f.write(text_box_output)

# The formatted data is now stored in 'text_box_output'
# You can now use 'text_box_output' for further processing or handling