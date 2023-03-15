def format_stock_feature(stock, features, original_data):
    stocks_features = []

    for item in original_data:
        feature_ids = [column[0] for column in features
                       if column[1] in item["features"]]
        stock_id = [column[0]
                    for column in stock
                    if column[1] == item["item_name"]]

        for feature in feature_ids:
            stocks_features.append([feature, stock_id[0]])

    return stocks_features
