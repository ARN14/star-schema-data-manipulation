import pg8000.native as pg
from src.get_data import get_staff_data, get_sales_data, get_items_data
from src.format_features import format_features
from src.format_stock import format_stock
from src.format_stock_feature import format_stock_feature
from connection_details import name, new_database

conn = pg.Connection(name, database=new_database)

def populate_new_database():
    staff_data = get_staff_data()
    sales_data = get_sales_data()
    items_data = get_items_data()

    dim_features = format_features(items_data)
    for feature in dim_features:
        conn.run("INSERT INTO dim_features (feature_name) VALUES (:values)", values=feature[0])

    dim_stock = format_stock(items_data)
    for stock in dim_stock:
        conn.run("INSERT INTO dim_stock (item_name, amount_in_stock) VALUES (:name, :amount)", name=stock[0], amount=stock[1])

    new_features = conn.run("SELECT * FROM dim_features;")
    new_stock = conn.run("SELECT * FROM dim_stock;")

    # print(new_stock)
    # print(new_features)
    # print(items_data)

    stock_features = format_stock_feature(new_stock, new_features, items_data)
    for ids in stock_features:
        print(ids)
        conn.run("INSERT INTO stock_feature_junc (feature_id, stock_id) VALUES (:feature, :stock)", stock=ids[0], feature=ids[1])
    conn.run("SELECT * FROM stock_feature_junc;")


populate_new_database()