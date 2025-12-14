products = [
    {"product_id": 1, "product_name": "Laptop", "rating": 4.7, "quantity_in_stock": 10, "price": 75000},
    {"product_id": 2, "product_name": "Mouse", "rating": 4.2, "quantity_in_stock": 0, "price": 800},
    {"product_id": 3, "product_name": "Phone", "rating": 4.6, "quantity_in_stock": 5, "price": 35000},
    {"product_id": 4, "product_name": "Keyboard", "rating": 4.8, "quantity_in_stock": 12, "price": 1500},
    {"product_id": 5, "product_name": "Headphones", "rating": 4.3, "quantity_in_stock": 8, "price": 1200}
]
high_rated_in_stock_expensive = []

for product in products :
    if (
        product["rating"] >= 4.5 and 
        product["quantity_in_stock"] > 0 and 
        product["price"] >= 1000
    ):
        high_rated_in_stock_expensive.append((
            product["product_id"],
            product["product_name"],
            product["rating"],
            product["quantity_in_stock"],
            product["price"]

        )

        )
    for item in high_rated_in_stock_expensive:
        print (item)