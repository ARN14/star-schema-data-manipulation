def format_stock(input_list):
    return [[item["item_name"], item["amount"]] for item in input_list if "item_name" in item and "amount" in item]