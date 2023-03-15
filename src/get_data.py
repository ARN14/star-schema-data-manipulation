import pg8000.native as pg
from datetime import datetime
from connection_details import name, database

def get_data():
    conn = pg.Connection(name, database=database)

    sales_table = conn.run("SELECT * FROM sales;")

    formatted_sales = []

    for sale in sales_table:
        formatted_time = sale[5].strftime("%Y-%m-%d %H:%M:%S")
        formatted_sales.append({
            "sales_id": sale[0],
            "item_name": sale[1],
            "salesperson": sale[2],
            "price": float(sale[3]),
            "quantity": sale[4],
            "created_at": formatted_time,
            
        })

    items_table = conn.run("SELECT * FROM items;")
    
    formatted_items = []

    for item in items_table:
        formatted_items.append({
            "item_id": item[0],
            "item_name": item[1],
            "features": item[2],
            "department": item[3],
            "amount": item[4]            
        })

    staff_table = conn.run("SELECT * FROM staff;")
    
    formatted_staff = []

    for staff in staff_table:
        formatted_staff.append({
            "staff_id": staff[0],
            "first_name": staff[1],
            "last_name": staff[2],
            "department": staff[3],
        })

    return_list = [formatted_sales, formatted_items, formatted_staff]
    return return_list