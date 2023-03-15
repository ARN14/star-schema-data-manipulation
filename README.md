# Python Data Manipulation from a PSQL Database into a STAR schema
## Introduction
This project is a small scale demonstration of data manipulation through interacting with SQL tables using Python.  
The project involves taking a basic unformatted SQL database, reading the data from it, and manipulating it into an SQL star schema.  
A star schema is a method of storing data in SQL tables to optimise for use in data warehouses and for data analysis, it involves one fact table, and multiple dimension tables which all connect to the fact table, making it easy to analyse the specific measurable data in the fact table against many dimensions.  
The project uses:
- PSQL databases
- Python interaction with SQL
- PG8000
- Test driven development
- Pep8 standards

### Original database  
The original database has the following format:
```SQL
items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR,
    features VARCHAR[],
    department VARCHAR,
    amount_in_stock INT
)

staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    department VARCHAR
)

sales (
    sales_id SERIAL PRIMARY KEY,
    item_name VARCHAR,
    salesperson VARCHAR,
    price DECIMAL,
    quantity INT,
    created_at TIMESTAMP
)
```
The first draft of the database is not optimised for data analysis, and requires complex joins to query data.  
### STAR Database  
The database after manipulation and transformation into the star schema has the following format:  
It has one fact table, the fact_sales table:
```SQL
fact_sales (
    sales_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES dim_stock(stock_id),
    salesperson INT REFERENCES dim_staff(staff_id),
    price DECIMAL,
    quantity INT,
    created_at TIMESTAMP DEFAULT NOW()
)
```
The `dim_stock`, and `dim_staff` are joined by id onto the `fact_sales` table.  
`dim_staff` references a `dim_department` table.  
and `dim_stock` connects to the `dim_features` table via a `stock_features` junction table.  
The new database has 6 tables in total.


## Data Manipulation  
The first step to converting into a star schema is to format the raw data from the initial database, ready to be inserted into the new database tables by thee pg8000 module.  
We use one function for each of the new tables that need to be made, making 6 utility functions.   
1. `format_departments`  
accepts a list of dictionaries from the staff table, and returns a list of lists containing the **department_name**.  
1. `format_stock`
accepts a list of dictionaries from the item table, and returns a list containing the **item_name** and the **amount**.  
1. `format_features`
accepts a list of dictionaries of features and returns a list of lists containing the **feature_name**.  
1. `format_staff` 
**accepts**:
a list of dictionaries representing staff data  
a list of dictionaries representing the **new** department data  
**returns**:  
a list of lists containing the **first_name**, **last_name**, and the _correct_ **department_id**  
1. `format_stock_feature`  
**accepts**:  
a list representing the newly inserted stock data  
a list representing the newly inserted feature data  
a list representing the original stock data   
**returns**:  
a list of lists that containing **stock_id**, and **feature_id**  
1. `format_sales`   
**accepts**:  
a list representing the newly inserted stock data  
a list representing the newly inserted staff data  
a list representing the original sales data    
**returns**:    
item_id  
salesperson  
price  
quantity  
created_at    

## Loading
After manipulating the data into the required format, the next step is loading it into the new database.
The `populate_new_database` function handles the following:
- Retrieving raw data from the first database  
- Calling the 6 helper functions to transform the data into the required schema  
- Loading the new formatted data into the star schema database.  

The function uses the pg8000 module to interact with both PSQL databases.  
Running this function will execute a complete ETL operation, extracting raw data, transforming it with Python code by the helper functions, and loading it into the new database.  


## Installation
The project has the following dependancies:
- Python version 3.11.0
- Pytest
- pg8000  

The program needs both an initial database with test data, and the correct tables in a new database.  
The names of these databases should be entered into a `connection_details.py` file, with the following variables:
```
name = ""
database = ""
new_database = ""
```
Input a username, and the name of the two databases.  

Enter the following highlighted commands in the terminal to run the program:
- Setup virtual environment `python -m venv venv`
- Activate environment: `source venv/bin/activate`
- install dependancies (pytest and pg8000)
- Set PYTHONPATH: `export PYTHONPATH=$(pwd)`
- Ensure the tests are working, run: `pytest` 
- run the 'populate_new_database' function: `python src/populate_new_database.py`