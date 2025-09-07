import pandas as pd

df = pd.read_csv('rts_expt.csv')

mean_congruent = df[df['condition']=='congruent'].rt.mean()

print(df.head())
print(mean_congruent)