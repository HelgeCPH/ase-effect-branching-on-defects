import csv
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


x_data = [2, 6, 12, 1, 23, 10, 8]  # merges per week
y_data = [5, 9, 3, 7, 11, 4, 7]  # defects per week
# Plot
plt.scatter(x_data, y_data)
plt.title("Project name")
plt.xlabel("merges per week")
plt.ylabel("defects per week")
plt.savefig("plot.png")

ρ, p = stats.spearmanr(x_data, y_data)
print(ρ, p)

df = pd.read_csv("frequencies_per_week.csv")
df["created_week"] = pd.to_datetime(df["created_week"], utc=True)
corr_index = df.corr(method="spearman")["bugs_per_week"]["merges_per_week"]
title = f"Project name (ρ={corr_index:3f})"
df.plot(x="merges_per_week", y="bugs_per_week", kind="scatter", title=title)
plt.savefig("plot.png")
