employee_data = "Alice,Developer,30|Bob,Manager,45|Charlie,Designer,25"
# Splitting the employee data by '|' to separate each employee's info
employee_list = employee_data.split('|')

# TODO: For each employee, create a formatted string with stripped details and role eligibility for a junior position
for employee in employee_list:
    attr = employee.split(',')
    name = attr[0]
    role = attr[1]
    age = attr[2]
    eligibility = "Eligible for junior position" if role in ('Developer','Designer') else "not eligible"
    # TODO: Parse the employee data and add eligibility note if applicable
    print(F"Name: {name} - Role: {role} - Age: {age} {eligibility}")
