from functools import reduce

# --- Data ---
students = [
    {"name": "Aru", "course": "B.Sc", "fees": 25000},
    {"name": "Priya", "course": "B.Com", "fees": 20000},
    {"name": "Karthik", "course": "B.Tech", "fees": 50000},
   {"name": "gani", "course": "B.Sc", "fees": 25000},
    {"name": "ravi", "course": "B.Com", "fees": 20000},
    {"name": "Kalai", "course": "B.Tech", "fees": 50000} 
]

faculty = [
 {"name": "mahesh", "subject": "Maths", "salary": 45000},
    {"name": "ravi", "subject": "Physics", "salary": 40000},
    {"name": "rani", "subject": "English", "salary": 65000},
 {"name": " raju", "subject": "computer science", "salary": 55000},
    {"name": "ramu", "subject": "commerce", "salary": 70000},
    {"name": "surendhar", "subject": "English", "salary": 25000}
]
# Function to get details
def get_details():
    print("\n--- Students ---")
    list(map(lambda s: print(f"Name: {s['name']}, Course: {s['course']}, Fees: ₹{s['fees']}"), students))
    
    print("\n--- Faculty ---")
    list(map(lambda f: print(f"Name: {f['name']}, Subject: {f['subject']}, Salary: ₹{f['salary']}"), faculty))

# Sorted data
sorted_students = sorted(students, key=lambda s: s['fees'], reverse=True)
sorted_faculty = sorted(faculty, key=lambda f: f['salary'], reverse=True)

# Filtered data (students with fees > 25000, faculty with salary > 40000)
high_fee_students = list(filter(lambda s: s['fees'] > 25000, students))
high_salary_faculty = list(filter(lambda f: f['salary'] > 40000, faculty))

# Total fees & salary
total_fees = reduce(lambda acc, s: acc + s['fees'], students, 0)
total_salary = reduce(lambda acc, f: acc + f['salary'], faculty, 0)

# --- Output ---
get_details()

print("\n--- Sorted Students by Fees ---")
print(sorted_students)

print("\n--- Sorted Faculty by Salary ---")
print(sorted_faculty)

print("\n--- High Fee Students (> ₹25000) ---")
print(high_fee_students)

print("\n--- High Salary Faculty (> ₹40000) ---")
print(high_salary_faculty)

print(f"\nTotal Fees Collected: ₹{total_fees}")
print(f"Total Salary Paid: ₹{total_salary}")
