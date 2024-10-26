# import pandas as pd
# import numpy as np

# np.random.seed(0)

# # Define the columns
# columns = [
#     "Sex",
#     "AgeBaseline",
#     "HistoryDiabetes",
#     "HistoryCHD",
#     "HistoryVascular",
#     "HistorySmoking",
#     "HistoryHTN",
#     "HistoryDLD",
#     "HistoryObesity",
#     "DLDmeds",
#     "DMmeds",
#     "HTNmeds",
#     "ACEIARB",
#     "CholesterolBaseline",
#     "CreatinineBaseline",
#     "eGFRBaseline",
#     "sBPBaseline",
#     "dBPBaseline",
#     "BMIBaseline",
#     "TimeToEventMonths",
#     "EventCKD35",
#     "TIME_YEAR"
# ]

# # Define the data types
# dtypes = [
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "int64",
#     "float64",
#     "float64",
#     "float64",
#     "float64",
#     "float64",
#     "float64",
#     "float64",
#     "int64",
#     "int64",
#     "int64"
# ]

# # Generate the data
# data = {
#     "Sex": np.random.randint(0, 2, size=5000),
#     "AgeBaseline": np.random.randint(40, 80, size=5000),
#     "HistoryDiabetes": np.random.randint(0, 2, size=5000),
#     "HistoryCHD": np.random.randint(0, 2, size=5000),
#     "HistoryVascular": np.random.randint(0, 2, size=5000),
#     "HistorySmoking": np.random.randint(0, 2, size=5000),
#     "HistoryHTN": np.random.randint(0, 2, size=5000),
#     "HistoryDLD": np.random.randint(0, 2, size=5000),
#     "HistoryObesity": np.random.randint(0, 2, size=5000),
#     "DLDmeds": np.random.randint(0, 2, size=5000),
#     "DMmeds": np.random.randint(0, 2, size=5000),
#     "HTNmeds": np.random.randint(0, 2, size=5000),
#     "ACEIARB": np.random.randint(0, 2, size=5000),
#     "CholesterolBaseline": np.random.uniform(3.0, 7.0, size=5000),
#     "CreatinineBaseline": np.random.uniform(40.0, 120.0, size=5000),
#     "eGFRBaseline": np.random.uniform(80.0, 120.0, size=5000),
#     "sBPBaseline": np.random.uniform(120.0, 180.0, size=5000),
#     "dBPBaseline": np.random.uniform(70.0, 110.0, size=5000),
#     "BMIBaseline": np.random.uniform(20.0, 50.0, size=5000),
#     "TimeToEventMonths": np.random.randint(0, 24, size=5000),
#     "EventCKD35": np.random.randint(0, 2, size=5000),
#     "TIME_YEAR": np.random.randint(0, 10, size=5000)
# }

# # Create the DataFrame
# df = pd.DataFrame(data)

# # Save the DataFrame to a JSON file
# df.to_json("data.json", orient="records")
import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(0)

# Define the columns and data types
columns = [
    "Sex",
    "AgeBaseline",
    "HistoryDiabetes",
    "HistoryCHD",
    "HistoryVascular",
    "HistorySmoking",
    "HistoryHTN",
    "HistoryDLD",
    "HistoryObesity",
    "DLDmeds",
    "DMmeds",
    "HTNmeds",
    "ACEIARB",
    "CholesterolBaseline",
    "CreatinineBaseline",
    "eGFRBaseline",
    "sBPBaseline",
    "dBPBaseline",
    "BMIBaseline",
    "TimeToEventMonths",
    "EventCKD35",
    "TIME_YEAR"
]

# Generate the data
data = {
    "Sex": np.random.randint(0, 2, size=5000),
    "AgeBaseline": np.random.randint(40, 80, size=5000),
    "HistoryDiabetes": np.random.randint(0, 2, size=5000),
    "HistoryCHD": np.random.randint(0, 2, size=5000),
    "HistoryVascular": np.random.randint(0, 2, size=5000),
    "HistorySmoking": np.random.randint(0, 2, size=5000),
    "HistoryHTN": np.random.randint(0, 2, size=5000),
    "HistoryDLD": np.random.randint(0, 2, size=5000),
    "HistoryObesity": np.random.randint(0, 2, size=5000),
    "DLDmeds": np.random.randint(0, 2, size=5000),
    "DMmeds": np.random.randint(0, 2, size=5000),
    "HTNmeds": np.random.randint(0, 2, size=5000),
    "ACEIARB": np.random.randint(0, 2, size=5000),
    "CholesterolBaseline": np.random.uniform(3.0, 7.0, size=5000),
    "CreatinineBaseline": np.random.uniform(40.0, 120.0, size=5000),
    "eGFRBaseline": np.random.uniform(80.0, 120.0, size=5000),
    "sBPBaseline": np.random.uniform(120.0, 180.0, size=5000),
    "dBPBaseline": np.random.uniform(70.0, 110.0, size=5000),
    "BMIBaseline": np.random.uniform(20.0, 50.0, size=5000),
    "TimeToEventMonths": np.random.randint(0, 24, size=5000),
    "EventCKD35": np.random.randint(0, 2, size=5000),
    "TIME_YEAR": np.random.randint(0, 10, size=5000)
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_path = "/mnt/data/healthcare_data.csv"
df.to_csv(csv_path, index=False)

print(csv_path)
