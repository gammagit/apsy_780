import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('rts_expt.csv')
print(df.head())

# Draw a lineplot of RTs
# sns.lineplot(df, x='trial', y='rt')
sns.boxplot(df, x='condition', y='rt')
plt.title('RT comparisons across conditions')
plt.xlabel('Conditions')
plt.ylabel('RTs (ms)')
plt.show()