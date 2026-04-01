from functools import reduce

# Sample data
faculty = [
    {"name": "Dr. Kumar", "salary": 55000},
    {"name": "Pf. Meena", "salary": 62000},
    {"name": " pf.Arjun", "salary": 58000}
]

students = [
    {"name": "Anita", "fees": 45000},
    {"name": "Ravi", "fees": 47000},
    {"name": "Priya", "fees": 50000}
]

# Calculate total salary
total_salary = reduce(lambda acc, f: acc + f["salary"], faculty, 0)

# Calculate total fees collected
total_fees = reduce(lambda acc, s: acc + s["fees"], students, 0)

print(f"Total Salary Paid: ₹{total_salary}")
print(f"Total Fees Collected: ₹{total_fees}")

