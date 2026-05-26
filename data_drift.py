import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.read_csv(r"D:\Projects\ScholarX\Project 2\train.csv")
current_data = pd.read_csv(r"D:\Projects\ScholarX\Project 2\test.csv")

report = Report(metrics=[DataDriftPreset()])
my_eval = report.run(reference_data=reference_data, current_data=current_data)

my_eval.save_html(r"D:\Projects\ScholarX\Project 2\data_drift_report.html")
print("Data drift report generated and saved as 'data_drift_report.html")

