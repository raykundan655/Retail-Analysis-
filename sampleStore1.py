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

# 3 Evaluate the performance of different customer segments (Consumer, Corporate, Home Office) based on sales, quantity, and profit.

segment=df_no_outlier.groupby("Segment")[["Sales","Profit","Quantity"]].sum().reset_index()
plt.figure(figsize=(15,7))
plt.subplot(1,3,1)
sns.barplot(x="Segment",y="Sales",data=segment,palette='dark:orange')
plt.grid(False)
plt.xticks(rotation=45)
plt.title("Segment by Sales")



plt.subplot(1,3,2)
sns.barplot(x="Segment",y="Quantity",data=segment,palette='dark:purple')
plt.grid(False)
plt.xticks(rotation=45)
plt.title("Segment by Quantity")



plt.subplot(1,3,3)
sns.barplot(x="Segment",y="Profit",data=segment,palette='dark:blue')
plt.grid(False)
plt.xticks(rotation=45)
plt.title("Segment by Profit")
plt.suptitle("Segment-wise Customer Behavior")
plt.show()




# 4 identifying return frequency by category to assess business impact.

def conv(val):
    if(val=="Yes"):
        return 1
    else:
        return 0

df_no_outlier["returned_flag"]=df_no_outlier["Returned"].apply(conv)
print(df_no_outlier)

returnbase=df_no_outlier.groupby("Category")["returned_flag"].sum()
plt.pie(returnbase.values,labels=returnbase.index,autopct="%.2f%%",colors = ["#A1C9F1", "#FFB5E8", "#B5EAD7"])
plt.legend()
plt.title("Distribution of return order by Category")
plt.show()

# 5 Analyzing shipping time to understand delivery performance and customer experience.

df_no_outlier["shipment_Duration"]=(df_no_outlier["Ship Date"] - df_no_outlier["Order Date"]).dt.days
sns.histplot(x="shipment_Duration",data=df_no_outlier,bins=5,kde=True,color="#2ECC71")
plt.grid(True)
plt.title("Distribution of Shipping Duration")
plt.show()



corr=df_no_outlier.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()

df_no_outlier.to_excel("clean-data.xlsx",index=False)



