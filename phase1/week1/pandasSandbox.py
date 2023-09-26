import numpy as np
import matplotlib.pyplot as plt, pandas as pd, os
os.system("cls")

df = pd.read_csv('tips.csv')

## Basic statistics on the dataframe
#print(df.describe())

## Group data by the day of week
## numeric_only arguement prevents string values 
# print(df.groupby(["day"]).sum(numeric_only=True))

## Count
# print(df.groupby(["day"]).count())

# tips_by_day = df.groupby('day')['tip'].sum()
# print(tips_by_day.to_frame("tip (£)").reset_index())

fig, ax = plt.subplots(1,2)
df.hist(column="total_bill",ax=ax[0])
df.hist(column="total_bill",bins=20,ax=ax[1])


table = pd.DataFrame(pd.pivot_table(df,index=["sex","smoker"],aggfunc=np.sum,values=("total_bill")))
print(table)