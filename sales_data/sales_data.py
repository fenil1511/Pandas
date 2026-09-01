import pandas as pd

# Raw dataset
data = {
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'customer_type': ['Subscriber', 'Guest', 'Subscriber', 'Subscriber', 'Guest', 'Guest', 'Subscriber', 'Guest', 'Subscriber', 'Guest'],
    'region': ['North', 'West', 'East', 'North', 'South', 'West', 'East', 'South', 'North', 'West'],
    'category': ['Electronics', 'Clothing', 'Furniture', 'Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture'],
    'unit_price': [300.0, 45.0, 150.0, 1200.0, 80.0, 150.0, 450.0, 35.0, 850.0, 200.0],
    'quantity': [2, 3, 1, 1, 4, 2, 1, 5, 1, 2],
    'discount_pct': [0.10, 0.00, 0.15, 0.05, 0.00, 0.10, 0.20, 0.00, 0.05, 0.10],
    'payment_method': ['Credit Card', 'UPI', 'PayPal', 'Credit Card', 'UPI', 'Credit Card', 'PayPal', 'Cash', 'Credit Card', 'UPI']
}

df = pd.DataFrame(data)

# Calculate total net revenue for each order
cat_price=df.groupby(df['category'])['unit_price'].sum()
max_price_by_cat=cat_price.idxmax()
top_value =cat_price.max()
print(f'{max_price_by_cat},{top_value},{df['category'].value_counts().max()}')
print(df['unit_price'].sum())

# Compare Subscriber vs. Guest customers. What is the average order value (total_amount) for each group?
Compare_customers = df.groupby(df['customer_type'])['unit_price'].sum()
print(Compare_customers)


# Which region generated the lowest revenue, and what is its most popular payment method?

lowest_revenue_by_revenue = df.groupby(['region', 'payment_method'])['unit_price'].sum() 
sorted_revenue = lowest_revenue_by_revenue.sort_values(ascending=True)

print(sorted_revenue)


# Find all orders where discount_pct was greater than 0% and paid via Credit Card. How much total discount money did the company give away on these orders?

dis = df[(df['discount_pct'] > 0) & (df['payment_method'] == 'Credit Card')].copy()
dis['discount_amount'] = (dis['unit_price'] * dis['quantity']) * dis['discount_pct']
total_discount_given = dis['discount_amount'].sum()

print(f"Total Discount Given: ${total_discount_given:.2f}")