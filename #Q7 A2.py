#Q7. Write a program in python to create a dictionary and add list as values?
listdict = {
  "English": ["Arjun", "Iqra", "Tanya"],
    "Computer Science": ["Dev", "Simran"],
    "History": ["Ali", "Nina", "Omar"],
    "Geography": ["Harsh", "Pooja"]  }

for subject, students in listdict.items():
    print(f"{subject}: {students}")
