def validate_student(name, age, department):

    if not isinstance(name, str) or not name.strip():
        return False, "Student name is required."

    if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
        return False, "Age must be a positive integer."

    if not isinstance(department, str) or not department.strip():
        return False, "Department is required."

    return True, "Student details are valid."