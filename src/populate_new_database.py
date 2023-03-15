import pg8000.native as pg
from src.get_data import get_staff_data, get_sales_data, get_items_data
from src.format_features import format_features
from src.format_stock import format_stock
from src.format_stock_feature import format_stock_feature
from src.format_departments import format_departments
from src.format_staff import format_staff
from src.format_sales import format_sales
from connection_details import name, new_database

conn = pg.Connection(name, database=new_database)


def populate_new_database():
    items_data = get_items_data()
    staff_data = get_staff_data()
    sales_data = get_sales_data()

    dim_features = format_features(items_data)
    for feature in dim_features:
        conn.run("INSERT INTO dim_features (feature_name) VALUES (:values)",
                 values=feature[0])

    dim_stock = format_stock(items_data)
    for stock in dim_stock:
        conn.run("""INSERT INTO dim_stock (item_name, amount_in_stock)
                    VALUES (:name, :amount)""",
                 name=stock[0], amount=stock[1])

    new_features = conn.run("SELECT * FROM dim_features;")
    new_stock = conn.run("SELECT * FROM dim_stock;")
    stock_features = format_stock_feature(new_stock, new_features, items_data)
    for ids in stock_features:
        conn.run("""INSERT INTO stock_feature_junc (feature_id, stock_id)
                    VALUES (:feature, :stock)""",
                 feature=ids[0], stock=ids[1])

    dim_department = format_departments(staff_data)
    for department in dim_department:
        conn.run("""INSERT INTO dim_department (department_name)
                    VALUES (:name)""",
                 name=department[0])

    new_departments = conn.run("SELECT * FROM dim_department;")
    dim_staff = format_staff(staff_data, new_departments)
    for staff in dim_staff:
        conn.run("""INSERT INTO dim_staff (first_name,
                    last_name,
                    department_id)
                    VALUES (:first, :last, :id)""",
                 first=staff[0], last=staff[1], id=staff[2])

    new_staff = conn.run("SELECT * FROM dim_staff;")
    fact_sales = format_sales(new_stock, new_staff, sales_data)

    for sale in fact_sales:
        conn.run("""INSERT INTO fact_sales (item_id, salesperson,
                    price, quantity, created_at)
                    VALUES (:id, :salesperson, :price, :quantity, :created)""",
                 id=sale[0], salesperson=sale[1],
                 price=sale[2], quantity=sale[3],
                 created=sale[4])


populate_new_database()
