import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df["weight"] / ((df["height"] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    fig = sns.catplot(x="variable", y="total", hue="value", data=df_cat, kind="bar", col="cardio").fig
    fig.savefig('catplot.png')  # Make sure the directory to save the file exists
    return fig

# Draw Heat Map
def draw_heat_map():
    df_heat = df[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) &
                 (df["height"] <= df["height"].quantile(0.975)) & (df["weight"] >= df["weight"].quantile(0.025)) &
                 (df["weight"] <= df["weight"].quantile(0.975))]

    corr = df_heat.corr(method='pearson')
    mask = np.triu(corr)

    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, mask=mask, cmap='coolwarm', fmt='.1f', center=0.08, square=True, annot=True, linewidths=1, cbar_kws={"shrink": .5})

    fig.savefig('heatmap.png')  # Make sure the directory to save the file exists
    return fig

# Call the functions
draw_cat_plot()
draw_heat_map()
