students = [
    {"name": "Arun", "fees": 60000},
    {"name": "Priya", "fees": 45000},
    {"name": "Karthik", "fees": 75000}
]

faculty = [
    {"name": "Dr. Meena", "salary": 40000},
    {"name": "Mr. Raj", "salary": 28000},
    {"name": "Ms. Anitha", "salary": 35000}
]

# Filter students with fees > 50000
high_fee_students = list(filter(lambda s: s["fees"] > 50000, students))

# Filter faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f["salary"] > 30000, faculty))

print("High Fee Students:", high_fee_students)
print("High Salary Faculty:", high_salary_faculty)

