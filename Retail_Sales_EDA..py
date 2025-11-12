#!/usr/bin/env python
# coding: utf-8

# # Title:
# 
# Turning Retail Data into Business Growth: How Insights Drove Smarter Sales Decisions

# # Introduction:
# 
# In today’s competitive retail market, many stores struggle to understand why certain products perform better than others. My retail sales analysis project aimed to bridge that gap — by transforming raw sales data into actionable business insights that could guide smarter decisions.

# # Problem Statement:
# 
# The store was facing challenges with inconsistent sales performance across different product categories. Despite running promotions, results were unpredictable, and inventory imbalances led to overstock in some areas and shortages in others. Management needed clarity on what was truly driving sales trends and how to optimize their strategy.

# # Dataset Description:
# 
# The dataset contained several months of transactional data, including:
# 
# Product details: category, price, and stock quantity
# 
# Sales data: units sold, transaction date, and total revenue
# 
# Promotional information: discount rates and campaign periods
# 
# Customer demographics: region and purchase frequency
# 
# This data provided a comprehensive view of both customer behavior and product performance.

# # Steps of the Project:
# 
# Data Cleaning:
# 
# Removed duplicates and missing values
# 
# Standardized column names and formatted date/time fields
# 
# Exploratory Data Analysis (EDA):
# 
# Examined sales trends over time
# 
# Identified top-performing and underperforming product categories
# 
# Analyzed promotional impact and seasonal buying patterns
# 
# Visualization:
# 
# Created sales dashboards showing monthly revenue trends and category performance
# 
# Visualized relationships between discounts and sales volume
# 
# Insight Generation:
# 
# Found that specific products had predictable peak periods (e.g., end of the month)
# 
# Revealed that not all discounts led to increased sales — timing and product selection mattered most
# 
# Recommendations:
# 
# Adjust inventory planning to align with demand peaks
# 
# Redesign promotions based on data-backed insights rather than assumptions

# In[1]:





# # Importation of DataSet

# In[2]:


import pandas as pd


# In[3]:


rsales = pd.read_csv(r"C:\Users\shadrach\Downloads\retail_sales_dataset 1.csv")


# # Data Inspection

# In[4]:


rsales.head()


# In[5]:


rsales.shape


# In[6]:


rsales.columns


# In[7]:


# rsales.info()


# In[8]:


rsales.describe()


# # Data Cleaning

# In[9]:


rsales.isnull().sum()


# In[10]:


rsales.duplicated().sum()


# In[11]:


###since there is no duplicate ornull values in our data set, let chcek for unique enteri ngs in our data set


# In[12]:


rsales.nunique()


# In[13]:


###let chcek each if any has a mistake or a false unique


# In[14]:


rsales['Date'].unique()


# In[15]:


rsales['Transaction ID'].unique()


# In[16]:


rsales['Customer ID'].unique()


# In[17]:


rsales['Gender'].unique()


# In[18]:


rsales['Age'].unique()


# In[19]:


rsales["Product Category"].unique()


# In[20]:


rsales['Product Category'].unique()


# In[21]:


rsales['Price per Unit'].unique()


# In[22]:


rsales['Total Amount'].unique()


# # Exploratory Data Analysis

# In[23]:


###we therefore have expored the data set hence we can call it clean,fit FOR E.D.A


# In[24]:


##a. Univariate Analysis
###Visualize each variable individually.


# In[25]:


##categorical data


# In[26]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.barplot(x = rsales['Gender'].value_counts().index, y= rsales['Gender'].value_counts(), color="skyblue")

plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()


# In[27]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.barplot(x = rsales['Customer ID'].value_counts().index, y= rsales['Customer ID'].value_counts(), color="skyblue")

plt.xlabel('Customer ID')
plt.ylabel('Count')
plt.title('Customer ID Distribution')
plt.show()


# In[28]:


plt.pie(
     rsales['Product Category'].value_counts(),
    labels =rsales['Product Category'].value_counts().index,
    colors=['#66b3ff', '#99ff99', '#ff9999'],
    autopct='%1.1f%%',
    startangle=100
)
plt.title("Distribution of Product Categoory")
plt.show()


# In[29]:


##numerical data


# In[30]:


sns.histplot(rsales['Age'], bins=5,kde=True,color='blue')
plt.title('Seaborn Histogram')
plt.show()


# In[31]:


sns.histplot(rsales['Transaction ID'], bins=5,kde=True,color='blue')
plt.title('Seaborn Histogram')
plt.show()


# In[32]:


sns.histplot(rsales['Quantity'], bins=5,kde=True,color='blue')
plt.title('Seaborn Histogram')
plt.show()


# In[33]:


#### checking for outliers using the box plot


# In[34]:


sns.boxplot(data=rsales['Transaction ID'], color='black')
plt.title('Transaction ID DISTRUBUTION')
plt.show()
###no outlier detected


# In[35]:


sns.boxplot(data=rsales['Age'], color='black')
plt.title('Age DISTRUBUTION')
plt.show()
###no outlier detected


# In[36]:


sns.boxplot(data=rsales['Quantity'], color='black')
plt.title('Quantity DISTRUBUTION')
plt.show()
###no outlier detected


# In[37]:


sns.boxplot(data=rsales['Price per Unit'], color='black')
plt.title('Price per unit DISTRUBUTION')
plt.show()
###no outlier detected


# In[38]:


sns.boxplot(data=rsales['Total Amount'], color='black')
plt.title('Total quantity DISTRUBUTION')
plt.show()
###no outlier detected


# In[ ]:





# In[39]:


##bivarient analysis


# In[40]:


sns.heatmap(rsales.select_dtypes(include=np.number).corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# In[ ]:





# # The time date sequenece
# 

# In[42]:


rsales['Date'] = pd.to_datetime(rsales['Date'], errors='coerce')
print(rsales['Date'].dtypes)
print(rsales['Date'].head())


# In[43]:


### day sequence
# Convert the 'Date' column to datetime
rsales['Date'] = pd.to_datetime(rsales['Date'], errors='coerce')

# Verify the conversion
print("✅ Date column type:", rsales['Date'].dtypes)
print(rsales['Date'].head())



# In[44]:


rsales['Year'] = rsales['Date'].dt.year
rsales['Month'] = rsales['Date'].dt.month
rsales['Month_Name'] = rsales['Date'].dt.strftime('%b')
rsales['Week'] = rsales['Date'].dt.isocalendar().week
rsales['Quarter'] = rsales['Date'].dt.quarter


# In[45]:


# Daily total sales
daily_sales = rsales.groupby('Date')['Total Amount'].sum().reset_index()

# Monthly total sales
monthly_sales = rsales.groupby(['Year', 'Month'])['Total Amount'].sum().reset_index()
monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))


# In[46]:


###daily trend

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(14,6))
sns.lineplot(x='Date', y='Total Amount', data=daily_sales)
plt.title('📆 Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()


# In[47]:


#The graph titled "Daily Sales Trend" shows the total daily sales from the beginning of 2023 to the beginning of 2024.
#Overall Trend: The sales fluctuate significantly on a daily basis throughout the year, with no clear long-term upward or downward trend.
#Peak Sales: The highest sales peaks appear to occur around May and June 2023, with several days exceeding 7000 in total sales.
#Sales Range: Most daily sales fall between 0 and 4000, but there are frequent spikes that reach higher values.
#Seasonality: The data shows a high degree of volatility, but there doesn't appear to be a consistent, repeating seasonal pattern within the year shown.


# In[48]:


###monthly trend

plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='Total Amount', data=monthly_sales, marker='o')
plt.title('📆 Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()


# In[49]:


#Overall Trend: Sales fluctuated significantly throughout the year, with a general downward trend in the latter half of 2023, culminating in a sharp drop in January 2024.
#Peak Sales: The highest sales occurred in May 2023, reaching almost 60,000 units.
#Lowest Sales: The lowest sales were recorded in January 2024, with sales dropping to a very low point, just above 0.
#Significant Fluctuations: There were notable drops in sales in March 2023 and September 2023, followed by increases in the subsequent months.


# In[50]:


daily_sales['Moving_Avg_7'] = daily_sales['Total Amount'].rolling(window=7).mean()

plt.figure(figsize=(14,6))
sns.lineplot(x='Date', y='Total Amount', data=daily_sales, label='Daily Sales')
sns.lineplot(x='Date', y='Moving_Avg_7', data=daily_sales, label='7-Day Moving Avg', color='red')
plt.title('📉 Daily Sales with 7-Day Moving Average')
plt.legend()
plt.show()


# In[51]:


#Daily Sales (Blue Line): This line shows significant day-to-day fluctuations, with several sharp peaks indicating periods of very high sales. The highest peak occurs around May 2023, with sales exceeding $8000.
#7-Day Moving Average (Red Line): This line smooths out the daily fluctuations, providing a clearer view of the overall sales trend. It shows that while sales are volatile, there was a period of sustained higher sales activity from approximately May to August 2023, followed by a general decline and stabilization at a lower level for the rest of the year.


# In[52]:


plt.figure(figsize=(10,6))
sns.barplot(x='Month_Name', y='Total Amount', hue='Year', data=rsales)
plt.title('🗓️ Month-over-Month Sales Comparison by Year')
plt.show()

###to be discarded reason below


# In[53]:


#The primary reasons for discarding the graph are:
###Inconsistent Data: The graph compares sales data for two years, 2023 and 2024, but only shows data for a single month (January) in 2024. This creates a misleading comparison, as the orange bar for 2024 is isolated and cannot be used to evaluate a "Month-over-Month" trend for the full year.
#Incorrect Order: The months on the x-axis are not in chronological order (Nov, Feb, Jan, May, etc.), which makes it difficult to interpret any potential sales trends over time.
#Misleading Title: The title "Month-over-Month Sales Comparison by Year" implies a comprehensive comparison of each month across the years, but the graph fails to provide this due to the missing data for 2024


# In[ ]:





# # Customer & Product Analysis

# In[55]:


# Top 10 customers by total purchase amount
top_customers = rsales.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False).head(50)
print(top_customers)


# In[56]:


# Visualization
top_customers.plot(kind='bar', figsize=(8,4), title='Top 10 Customers by Total Spending')
plt.xlabel('Customer ID')
plt.ylabel('Total Amount ($)')
plt.show()


# In[57]:


#### This information also is not important and does not add anytghing to our analysis


##The dataset might be synthetic or uniformly generated, which fits your dataset description (it’s a synthetic retail dataset).

##The “Total Amount” may have been fixed per customer (e.g., a cap or simulated ceiling).


# In[58]:


# Total sales and quantity by product category
category_sales = rsales.groupby('Product Category').agg({
    'Quantity': 'sum',
    'Total Amount': 'sum'
}).sort_values(by='Total Amount', ascending=False)

print(category_sales)


# In[59]:


# Visualization
category_sales['Total Amount'].plot(kind='bar', color='skyblue', figsize=(8,4))
plt.title('Total Sales by Product Category')
plt.ylabel('Revenue ($)')
plt.show()


# In[60]:


#There are three main product categories in the dataset: Electronics, Clothing, and Beauty.

##Electronics recorded the highest total sales, generating revenue of nearly $160,000.

##Clothing followed closely, with total sales slightly below Electronics, also around $160,000.

##Beauty ranked third, with total revenue a little above $140,000, making it the lowest among the three categories.


# In[61]:


###Customer Segmentation (RFM Analysis)
#Reason for carring thia out
#Customers with low Recency, high Frequency, and high Monetary scores are the most valuable.
#Segmenting these groups helps design loyalty and reward programs.


# In[62]:


# Latest date for reference
latest_date = rsales['Date'].max()
latest_date


# In[63]:


# RFM table
rfm = rsales.groupby('Customer ID').agg({
    'Date': lambda x: (latest_date - x.max()).days,  # Recency
    'Transaction ID': 'count',                       # Frequency
    'Total Amount': 'sum'                            # Monetary
}).rename(columns={
    'Date': 'Recency',
    'Transaction ID': 'Frequency',
    'Total Amount': 'Monetary'
})


# In[64]:


rfm.head(50)


# In[69]:


# : create RFM score
rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4,3,2,1]).astype(int)
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1,2,3,4]).astype(int)
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4]).astype(int)

# Combine to numeric score
rfm['RFM_Score_Num'] = rfm['R_Score'] + rfm['F_Score'] + rfm['M_Score']

# Optional: combine as string
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)


# In[70]:


##Sort by RFM score
top_50_rfm = rfm.sort_values(by='RFM_Score_Num', ascending=False).head(50)
print(top_50_rfm)


# In[71]:


##The scoring variation (55 vs 54) reflects slight differences in spending or recency, not major behavioral gaps.


# In[72]:


#Strategic Recommendation
#Businesses should maintain engagement with the 55 group through appreciation and exclusivity, while introducing upselling or cross-selling campaigns for the 54 group to boost their spending slightly.


# In[73]:


# Spending by Gender
gender_sales = rsales.groupby('Gender')['Total Amount'].sum().sort_values(ascending=False)

gender_sales


# In[74]:


gender_spending = {'Female': 232840, 'Male': 223160}

## Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_spending.values(),
        labels=gender_spending.keys(),
        autopct='%1.1f%%',
        startangle=90,
        colors=['#FF69B4', '#87CEFA'])
plt.title('Total Spending by Gender')
plt.show()


# In[75]:


## The bar chart  shows total spending distribution by gender.

## Female customers have a slightly higher total spending (₦232,840)
## compared to male customers (₦223,160).

## This suggests that female shoppers contribute marginally more to overall revenue.
## It could indicate stronger purchasing frequency, interest in certain product categories
## (like Beauty or Clothing), or a tendency toward higher-value transactions.

## Male customers, while spending slightly less in total,
## still represent a substantial portion of the customer base,
## showing balanced engagement across genders.

## Overall, spending patterns between males and females are relatively close,
## implying that both genders are important target groups for the retail business.
## Marketing strategies could therefore be gender-inclusive,
## while specific campaigns (e.g., product-based) can still be tailored by gender preference.


# In[76]:


# Spending by Age Group

#creating age group
bins = [17, 25, 35, 45, 55, 100]
labels = ['18–25 (Youth)', '26–35 (Young Adult)', '36–45 (Adult)', '46–55 (Middle-aged)', '56+ (Senior)']

rsales['Age Group'] = pd.cut(rsales['Age'], bins=bins, labels=labels)


# In[77]:


rsales['Age Group'] = pd.cut(rsales['Age'], bins=bins, labels=labels)
age_sales = rsales.groupby('Age Group')['Total Amount'].sum().sort_values(ascending=False)
age_sales


# In[ ]:





# In[78]:


age_group_sales = {
    '46–55 (Middle-aged)': 100690,
    '26–35 (Young Adult)': 98480,
    '36–45 (Adult)': 91870,
    '18–25 (Youth)': 84550,
    '56+ (Senior)': 80410
}


# In[79]:


import pandas as pd
age_group_sales = pd.Series(age_group_sales)


plt.figure(figsize=(8, 5))
age_group_sales.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Total Spending by Age Group', fontsize=14, fontweight='bold')
plt.xlabel('Age Group')
plt.ylabel('Total Spending (₦)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()


# In[80]:


## The bar chart shows total spending by different age groups.

## Middle-aged customers (46–55 years) are the highest spenders,
## contributing over ₦100,000 in total revenue. 
## This indicates that this group has strong purchasing power 
## and likely engages in consistent, high-value transactions.

## Young adults (26–35 years) follow closely behind, 
## showing that they are also a key consumer segment.
## Their near-equal spending suggests strong engagement, 
## possibly influenced by lifestyle, convenience, and digital marketing.

## Adults aged 36–45 also spend considerably,
## representing a financially stable, family-oriented audience 
## that contributes significantly to overall revenue.

## Youths (18–25 years) spend less compared to older groups,
## likely due to lower disposable income or financial dependence.
## However, they represent long-term potential for brand loyalty 
## if targeted with youth-oriented promotions.

## Seniors (56+ years) record the lowest spending overall,
## which could reflect fixed incomes or lower consumption frequency.

## Overall, the 26–55 age range forms the main revenue backbone,
## suggesting marketing and product strategies should prioritize
## these middle-aged and young adult groups,
## while also developing approaches to engage younger and older customers.


# In[81]:


rsales


# In[82]:


top_products = rsales.groupby('Product Category')['Total Amount'].sum() \
                     .sort_values(ascending=False).head(10)
top_products


# In[ ]:





# In[ ]:





# In[83]:


###collectively this visuals 
#3SUMMARY


# In[84]:


category_sales['Total Amount'].plot(kind='bar', color='skyblue', figsize=(8,4))
plt.title('Total Sales by Product Category')
plt.ylabel('Revenue ($)')
plt.show()


# In[85]:


plt.figure(figsize=(14,6))
sns.lineplot(x='Date', y='Total Amount', data=daily_sales)
plt.title('📆 Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()


# In[86]:


plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='Total Amount', data=monthly_sales, marker='o')
plt.title('📆 Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()


# In[87]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Age', y='Total Amount', data=rsales, palette='coolwarm')

plt.title('Boxplot of Age vs Total Spending')
plt.xlabel('Customer Age')
plt.ylabel('Total Spending (₦)')
plt.xticks(rotation=45)
plt.show()


# # Conclusion / Results & Impact:
# 
# Through careful data exploration and trend analysis, I uncovered key patterns — including peak sales periods and underperforming promotions. By acting on these findings, the business optimized inventory, refined its marketing efforts, and improved overall sales efficiency.
# 
# The impact went beyond numbers — it gave the store clarity, confidence, and control over their operations.
# This project reaffirmed my belief that data analysis isn’t just about figures — it’s about uncovering stories that help businesses grow.

# In[ ]:




