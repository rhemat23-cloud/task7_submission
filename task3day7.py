students = [
    {"name": "Arun", "fees": 25000},
    {"name": "Priya", "fees": 18000},
    {"name": "Karthik", "fees": 22000}
]

# List of faculty
faculty = [
    {"name": "Dr. Meena", "salary": 55000},
    {"name": "Mr. Raj", "salary": 48000},
    {"name": "Ms. Kavya", "salary": 60000}
]

# Sort students by fees (ascending)
students.sort(key=lambda x: x["fees"])

# Sort faculty by salary (ascending)
faculty.sort(key=lambda x: x["salary"])

print("Students sorted by fees:")
for s in students:
    print(f"{s['name']} - ₹{s['fees']}")

print("\nFaculty sorted by salary:")
for f in faculty:
    print(f"{f['name']} - ₹{f['salary']}")

