# employee data
employees = [
    {"name": "test_1", "age": 30, "salary": 50000},
    {"name": "test_2", "age": 25, "salary": 60000},
    {"name": "test_3", "age": 35, "salary": 70000},
    # ...
]

# Define a lambda expression to convert the salary to an hourly wage.
salary_to_hourly = lambda salary: salary / 2080

# Use map() along with the lambda expression to transform the salary of each employee
hourly_wages= list(map(lambda emp : {**emp, "salary": salary_to_hourly(emp["salary"])},employees))

# Define a lambda expression to determine the employment status based on the age of the employee
employment_status=lambda  age : "Junior" if age <30 else "Senior"

# Use map() again this time to add the employment status to each employee dictionary
transformed_employees = list(map(lambda emp: {**emp, "employeement_status":employment_status(emp["age"])},hourly_wages))

# Print the transformed dataset
for emp in transformed_employees:
    print(emp)
