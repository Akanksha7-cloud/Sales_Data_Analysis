#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\AKANKSHA\Downloads\sales_data.csv")
df.head()


# In[2]:


print("Shape of Dataset:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
df.info()


# In[3]:


print("Missing Values:\n")
df.isnull().sum()


# In[4]:


print("Duplicate rows before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate rows after:", df.duplicated().sum())


# In[5]:


product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("Highest Selling Product:", product_sales.index[0])
print("Total Sales:", product_sales.iloc[0])


# In[6]:


top10_products = product_sales.head(10)

plt.figure(figsize=(10,5))
top10_products.plot(kind="bar")

plt.title("Top 10 Highest Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.show()


# In[7]:


city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

print("Highest Selling City:", city_sales.index[0])
print("Total Sales:", city_sales.iloc[0])


# In[8]:


top10_cities = city_sales.head(10)

plt.figure(figsize=(10,5))
top10_cities.plot(kind="bar")

plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.show()


# In[10]:


df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Day"] = df["Order Date"].dt.day


# In[11]:


year_sales = df.groupby("Year")["Sales"].sum()

print(year_sales)

plt.figure(figsize=(8,5))
year_sales.plot(kind="line", marker="o")

plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.grid(True)
plt.show()


# In[12]:


daily_sales = df.groupby("Day")["Sales"].sum()

plt.figure(figsize=(10,5))
daily_sales.plot(kind="line", marker="o")

plt.title("Daily Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.grid(True)
plt.show()


# In[13]:


plt.figure(figsize=(8,5))

plt.scatter(df["Price Each"],
            df["Quantity Ordered"])

plt.title("Price Each vs Quantity Ordered")
plt.xlabel("Price Each")
plt.ylabel("Quantity Ordered")

plt.grid(True)
plt.show()


# In[14]:


corr = df["Price Each"].corr(df["Quantity Ordered"])

print("Correlation:", corr)


# In[15]:


numeric_df = df[["Quantity Ordered",
                 "Price Each",
                 "Sales"]]

plt.figure(figsize=(8,5))

sns.heatmap(numeric_df.corr(),
            annot=True)

plt.title("Correlation Heatmap")

plt.show()


# In[16]:


print("Conclusion:")

print("Highest Selling Product:",
      product_sales.index[0])

print("Highest Selling City:",
      city_sales.index[0])

print("The heatmap and correlation analysis show the relationship between sales, price and quantity.")

print("Yearly and daily trends help understand customer purchasing patterns.")


# In[ ]:




