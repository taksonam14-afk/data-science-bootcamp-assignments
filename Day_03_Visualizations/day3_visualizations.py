import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.dpi"] = 150

os.makedirs("Day_03_Visualizations", exist_ok=True)

csv_paths = [
    "retail_sales_visualization_dataset.csv",
    "Day_03_Visualizations/retail_sales_visualization_dataset.csv",
]
df = None
for path in csv_paths:
    if os.path.exists(path):
        df = pd.read_csv(path)
        break

if df is None:
    raise FileNotFoundError("Could not locate retail_sales_visualization_dataset.csv")

df.columns = df.columns.str.strip()
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce").fillna(0)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce").fillna(0)
df["Region"] = df["Region"].fillna("Unknown")

# 1. Distribution Chart
fig1, ax1 = plt.subplots(figsize=(8, 4.5))
sns.histplot(data=df, x="Sales", bins=15, kde=True, color="#2b5c8f", ax=ax1)
ax1.set_title("1. Distribution of Sales per Transaction", fontsize=13, weight="bold")
ax1.set_xlabel("Sales ($)")
ax1.set_ylabel("Transaction Count")
plt.tight_layout()
fig1.savefig("Day_03_Visualizations/chart1_distribution.png", dpi=300, bbox_inches="tight")
plt.close(fig1)

# 2. Comparison Chart
cat_sales = df.groupby("Category")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False)
fig2, ax2 = plt.subplots(figsize=(8, 4.5))
sns.barplot(data=cat_sales, x="Category", y="Sales", palette="viridis", ax=ax2)
ax2.set_title("2. Cumulative Sales by Product Category", fontsize=13, weight="bold")
ax2.set_xlabel("Product Category")
ax2.set_ylabel("Total Sales ($)")
plt.tight_layout()
fig2.savefig("Day_03_Visualizations/chart2_comparison.png", dpi=300, bbox_inches="tight")
plt.close(fig2)

# 3. Relationship Chart
fig3, ax3 = plt.subplots(figsize=(8.5, 5))
sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category",
    size="Discount",
    sizes=(40, 180),
    alpha=0.85,
    ax=ax3,
)
ax3.set_title("3. Bivariate Relationship: Sales vs. Profit", fontsize=13, weight="bold")
ax3.set_xlabel("Sales ($)")
ax3.set_ylabel("Profit ($)")
ax3.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
fig3.savefig("Day_03_Visualizations/chart3_relationship.png", dpi=300, bbox_inches="tight")
plt.close(fig3)

# 4. Correlation Heatmap
fig4, ax4 = plt.subplots(figsize=(7, 5))
corr_matrix = df[["Quantity", "Unit_Price", "Discount", "Sales", "Profit"]].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="vlag", center=0, ax=ax4)
ax4.set_title("4. Correlation Heatmap of Numeric Variables", fontsize=13, weight="bold")
plt.tight_layout()
fig4.savefig("Day_03_Visualizations/chart4_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close(fig4)

# 5. Trend Line Chart & Primary Export
time_trend = df.set_index("Date").resample("W")["Sales"].sum().reset_index()
fig5, ax5 = plt.subplots(figsize=(9, 4.5))
ax5.plot(time_trend["Date"], time_trend["Sales"], marker="o", color="#1b9e77", label="Weekly Sales")
ax5.set_title("5. Weekly Aggregate Sales Trend", fontsize=13, weight="bold")
ax5.set_xlabel("Timeline (Weeks)")
ax5.set_ylabel("Sales ($)")
ax5.grid(True, linestyle="--", alpha=0.4)
ax5.legend()
plt.tight_layout()
fig5.savefig("Day_03_Visualizations/weekly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.close(fig5)

print("All Day 3 visualization charts generated and saved successfully.")
