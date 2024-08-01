
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt# Part 3: Features correlation and density plot
credit_card_fraud_detection_part3 = """
# Features correlation
plt.figure(figsize=(14,14))
plt.title('Credit Card Transactions features correlation plot (Pearson)')
corr = data_df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, linewidths=.1, cmap="Reds")
plt.show()

# Plot the correlated and inverse correlated values
s = sns.lmplot(x='V20', y='Amount', data=data_df, hue='Class', fit_reg=True, scatter_kws={'s':2})
s = sns.lmplot(x='V7', y='Amount', data=data_df, hue='Class', fit_reg=True, scatter_kws={'s':2})
plt.show()

s = sns.lmplot(x='V2', y='Amount', data=data_df, hue='Class', fit_reg=True, scatter_kws={'s':2})
s = sns.lmplot(x='V5', y='Amount', data=data_df, hue='Class', fit_reg=True, scatter_kws={'s':2})
plt.show()

# Features density plot
var = data_df.columns.values

i = 0
t0 = data_df.loc[data_df['Class'] == 0]
t1 = data_df.loc[data_df['Class'] == 1]

sns.set_style('whitegrid')
plt.figure()
fig, ax = plt.subplots(8,4,figsize=(16,28))

for feature in var:
    i += 1
    plt.subplot(8,4,i)
    sns.kdeplot(t0[feature], bw=0.5, label="Class = 0")
    sns.kdeplot(t1[feature], bw=0.5, label="Class = 1")
    plt.xlabel(feature, fontsize=12)
    locs, labels = plt.xticks()
    plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()
"""
