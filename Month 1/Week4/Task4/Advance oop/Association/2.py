# .Create a Doctor and Patient class. Associate one doctor with multiple patients and print the patient details.

class Doctor:
    def __init__(self, name):
        self.name = name
        self.patients = []


class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease


d1 = Doctor("Dr. Verma")

p1 = Patient("Dhruv", 22, "Fever")
p2 = Patient("Ankit", 25, "Cold")

d1.patients.append(p1)
d1.patients.append(p2)

for p in d1.patients:
    print(f"Doctor: {d1.name} -> Patient: {p.name}, Age: {p.age}, Disease: {p.disease}")