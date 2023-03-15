import pg8000.native as pg
from connection_details import name, database

conn = pg.Connection(name, database=database)


def get_staff_data():

    staff_table = conn.run("SELECT * FROM staff;")

    formatted_staff = []

    for staff in staff_table:
        formatted_staff.append({
            "staff_id": staff[0],
            "first_name": staff[1],
            "last_name": staff[2],
            "department": staff[3],
        })

    return formatted_staff


def get_sales_data():
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

    return formatted_sales


def get_items_data():
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

    return formatted_items
