
import csv
from datetime import datetime

data = [
    ["ID", "Name", "Value", "Date"],
    [1, "Sample A", 100, datetime.now().strftime("%Y-%m-%d")],
    [2, "Sample B", 200, datetime.now().strftime("%Y-%m-%d")],
    [3, "Sample C", 300, datetime.now().strftime("%Y-%m-%d")]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file generated successfully!")
