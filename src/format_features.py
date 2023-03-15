def format_features(input_list):
    feature_list = []

    for dictionary in input_list:
        if "features" in dictionary:
            for feature in dictionary["features"]:
                if feature not in feature_list:
                    feature_list.append(feature)


    return [[item] for item in feature_list]