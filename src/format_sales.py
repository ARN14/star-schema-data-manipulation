def format_sales(stock, staff_list, original_data):
    new_sales_data = []

    for sale in original_data:

        item_id = next(
            (item[0] for item in stock
             if item[1] == sale["item_name"]),
            None)
        salesperson = next(
            (staff[0] for staff in staff_list
             if staff[1] +
                " " + staff[2] == sale["salesperson"]),
            None)

        try:
            price = sale["price"]
            quantity = sale["quantity"]
            created_at = sale["created_at"]
        except Exception:
            price = None
            quantity = None
            created_at = None

        sale_data = [item_id, salesperson, price, quantity, created_at]

        if None not in sale_data:
            new_sales_data.append(sale_data)

    return new_sales_data
