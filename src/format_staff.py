def format_staff(staff_data, department_data):
    formatted_staff = []

    for staff in staff_data:
        department_id = [row[0] for row in department_data
                         if row[1] == staff["department"]]

        if not department_id:
            continue

        formatted_staff.append(
            [
                staff["first_name"],
                staff["last_name"],
                department_id[0]
            ])

    return formatted_staff
