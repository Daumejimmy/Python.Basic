# Definiere die Variable "alter"
alter = 44
# Definiere die Variable "student" als True, was bedeutet, dass die Person ein Student ist
student = True

# Überprüfe, ob die Person ein volljähriger Student ist
if alter >= 18 and student:
    print("Du bist ein volljähriger Student")

# Überprüfe, ob die Person entweder jünger als 14 ist oder ein Student ist
if alter < 14 or student:
    print("Du bist entweder jünger als 14 oder ein Student.")

# Überprüfe, ob die Person kein Student ist
if not student:
    print("Du bist kein Student.")

# Überprüfe, ob die Person entweder ein volljähriger Student ist oder jünger als 13
if (alter > 18 and student) or (alter > 13):
    print("Du bist entweder ein volljähriger Student oder jünger als 13.")


# Definiere das Alter der Person
alter1 = 14
# Definiere, ob die Person die Erlaubnis der Eltern hat
erlaubnis_von_eltern = False

# Überprüfe, ob das Alter größer oder gleich 18 ist
if alter1 >= 18:
    print("Du darfst in den Club")

# Falls das Alter zwischen 14 und 17 liegt und die Erlaubnis der Eltern vorliegt
elif alter1 >= 14 and alter1 <= 17 and erlaubnis_von_eltern:
    print("Du darfst in den Club, aber nur mit der Erlaubnis von deinen Eltern.")

# Wenn keine der vorherigen Bedingungen erfüllt ist
else:
    print("Du darfst nicht in den Club.")


# Definiere das Alter der Person
alter1 = 13
# Definiere, ob die Person die Erlaubnis der Eltern hat
erlaubnis_von_eltern = False

# Überprüfe, ob das Alter größer oder gleich 18 ist
if alter1 >= 18:
    print("Du darfst in den Club")

# Überprüfe, ob das Alter zwischen 14 und 17 liegt und die Erlaubnis der Eltern vorliegt
if alter1 >= 14 and alter1 <= 17 and erlaubnis_von_eltern:
    print("Du darfst in den Club, aber nur mit der Erlaubnis von deinen Eltern.")

# Wenn keine der vorherigen Bedingungen erfüllt ist
if alter1 < 14:
    print("Du darfst nicht in den Club.")
