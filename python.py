import pandas as pd

# Load your data
df = pd.read_csv("data.csv")

# Process the data (e.g., calculate average sales per category)
grouped_data = df.groupby('category')['sales'].mean().reset_index()

# Save the processed data to a JSON file
grouped_data.to_json("data.json", orient="records")
