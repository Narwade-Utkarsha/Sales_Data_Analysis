# Sales Data Analysis Report

## 1. Introduction

The Sales Data Analysis project is developed using Python, Pandas, and Matplotlib. The main objective is to load sales data, clean the dataset, perform data analysis, and visualize sales information using different charts.

## 2. Tools and Technologies

- Python
- Pandas
- Matplotlib
- CSV Dataset
- Visual Studio Code (VS Code)

## 3. Dataset Description

The dataset contains 100 records and 5 original columns.

| Column Name | Description |
|---|---|
| Order_ID | Unique order identification |
| Product | Product name |
| Quantity | Number of products sold |
| Unit_Price | Price of one product |
| Total_Sales | Total sales amount |

## 4. Data Cleaning

The following operations were performed:

- Loaded the CSV dataset using Pandas.
- Checked missing values.
- Checked duplicate records.
- Removed duplicate records.
- Replaced missing product names with "Unknown".
- Replaced missing numerical values using median.
- Calculated Total_Sales using Quantity and Unit_Price.
- Saved the cleaned dataset as `cleaned_sales_data.csv`.

## 5. Data Analysis

The following sales analysis operations were performed:

- Total Revenue calculation.
- Average Sales calculation.
- Highest Sales identification.
- Lowest Sales identification.
- Best-Selling Product identification.
- Product-wise sales comparison.

## 6. Data Visualization

Matplotlib was used to create the following charts:

### 6.1 Bar Chart
Displays the total sales of different products and helps compare product-wise sales.

### 6.2 Line Chart
Displays product-wise sales values using a line graph to understand differences in sales.

### 6.3 Pie Chart
Displays the percentage contribution of each product to total sales.

The generated chart images are saved as:

- `bar_chart.png`
- `line_chart.png`
- `pie_chart.png`

## 7. Conclusion

This project demonstrates how Python, Pandas, and Matplotlib can be used to load, clean, analyze, and visualize sales data. The charts help present sales information in a simple and understandable way. This project also provides practical experience in data analysis and visualization.

## 8. Future Enhancements

- Create an interactive sales dashboard.
- Analyze monthly and yearly sales.
- Generate automated sales reports.
- Add more advanced data visualizations.
- Use real-world sales datasets for better insights.
