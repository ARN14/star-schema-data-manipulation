def format_staff(staff_data, department_data):
    formatted_staff = []

    for staff in staff_data:
        required_department_id = 0

        for department in department_data:
            if "department_name" in department\
                    and "department_id" in department\
                    and department["department_name"] == staff["department"]:

                required_department_id = department["department_id"]

        if required_department_id != 0\
            and "first_name" in staff\
                and "last_name" in staff:
            formatted_staff.append(
                [
                    staff["first_name"],
                    staff["last_name"],
                    required_department_id
                ])

    return formatted_staff
