def format_stock_feature(stock, features, original_data):
    stocks_features = []

    for item in stock:
        item_features = []

        for data in original_data:
            if data["item_name"] == item["item_name"]:
                item_features = data["features"]

        for old_feature in item_features:
            for data_feature in features:
                if old_feature == data_feature["feature_name"]:
                    stocks_features.append([
                        item["item_id"], data_feature["feature_id"]
                    ])

    return stocks_features
