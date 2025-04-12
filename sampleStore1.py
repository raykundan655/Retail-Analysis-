import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns  


file_path="C:\\Users\\USER\\Downloads\\py\\sample_-_superstore.xlsx"
df=pd.read_excel(file_path,sheet_name="Orders")
return_df=pd.read_excel(file_path,sheet_name="Returns")
# print(df)
print(df.head())
print(df.info())

# cleaning
print(df.isnull().sum())
print(df["Order ID"].duplicated().sum())
df.drop_duplicates(subset="Order ID",keep="first",inplace=True)
print(df["Order ID"].duplicated().sum())

df["Order Date"]=pd.to_datetime(df["Order Date"])
df["Ship Date"]=pd.to_datetime(df["Ship Date"])

print(df.columns)
numeric =["Quantity","Discount","Profit","Sales"]
df[numeric]=df[numeric].apply(pd.to_numeric)

df1=df[df["Profit"]>=0].copy()
print(df1)

# merging two sheet
df1=pd.merge(df1,return_df,on="Order ID",how="left")
print(df1)
df1["Returned"].replace(np.nan,"No",inplace=True)
print(df1)

print(df1.columns)

# outlier detection of profit and removable
Q1=df1["Profit"].quantile(0.25)
Q3=df1["Profit"].quantile(0.75)
IQR=Q3-Q1

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

df_no_outlier=df1[(df1["Profit"]>=lower_bound) & (df1["Profit"]<=upper_bound) ].copy()
print(df_no_outlier)


print(df_no_outlier.describe())

#Objectives

#1  Examine monthly-yearly  patterns in sales to identify peak periods and seasonal trends.


df_no_outlier["Year"]=df_no_outlier["Order Date"].dt.year
df_no_outlier["Month"]=df_no_outlier["Order Date"].dt.month_name()

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']


print(df_no_outlier)
gb_month=df_no_outlier.groupby("Month")["Profit"].sum().reindex(month_order).reset_index()
gb_year=df_no_outlier.groupby("Year")["Profit"].sum().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(x="Month",y="Profit",data=gb_month,color="m")
plt.xticks(rotation=45)
plt.title("Profit Trend Over Month")
plt.grid(True)
plt.show(block=False)
plt.figure(figsize=(6,6))
sns.lineplot(x="Year",y="Profit",data=gb_year,color="red")
plt.title("Profit Trend Over Year")
plt.grid(True)

plt.show()


#2 average profit across different regions to identify high and low-performing areas.


region=df_no_outlier.groupby("Region")["Profit"].mean()
br=sns.barplot(x=region.index,y=region.values,palette="YlGnBu")

plt.title("Average Profit Across region")
br.bar_label(br.containers[0],fmt="%.2f")
br.bar_label(br.containers[1],fmt="%.2f")
br.bar_label(br.containers[2],fmt="%.2f")
br.bar_label(br.containers[3],fmt="%.2f")
plt.ylabel("Average Profit")
plt.show()
