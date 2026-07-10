import csv
import os
from datetime import datetime

def save_metrics(metrics):

    file_exists = os.path.isfile("system_logs.csv")

    with open("system_logs.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "cpu",
                "ram",
                "disk"
            ])

        writer.writerow([
            datetime.now(),
            metrics["cpu"],
            metrics["ram"],
            metrics["disk"]
        ])