def format_departments(input_list):
    departments_list = []

    for dictionary in input_list:
        if "department" in dictionary\
                and dictionary["department"]\
                and type(dictionary["department"]) == str\
                and dictionary["department"] not in departments_list:

            departments_list.append(dictionary["department"])

    return [[department] for department in departments_list]
