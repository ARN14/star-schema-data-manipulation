def format_sales(stock, staff_list, original_data):
    new_sales_data = []
    
    for sale in original_data:

        item_id = next((item["item_id"] for item in stock if item["item_name"] == sale["item_name"]), None)
        salesperson = next((staff["staff_id"] for staff in staff_list if staff["first_name"] + " " + staff["last_name"] == sale["salesperson"]), None)

        try:
            price = sale["price"]
            quantity = sale["quantity"]
            created_at = sale["created_at"]
        except:
            price = None
            quantity = None
            created_at = None

        sale_data = [item_id, salesperson, price, quantity, created_at]

        if not None in sale_data:
            new_sales_data.append(sale_data)

    return new_sales_data