# Definition von Variablen
vorname = "Jimmy"
nachname = "Mueller"

# Zusammenführen der Vor- und Nachnamen
vollstaendiger_name = vorname + " " + nachname

# Ausgabe des vollständigen Namens
print("Der Vollständiger Name:", vollstaendiger_name)

# Einen Teil eines Textes ausschneiden
text = "Python-Programmierung"
teil = text[0:6]  # Die ersten 6 Zeichen des Textes
print("Gesliceter Text:", teil)

# Verwenden von Platzhaltern zur Formatierung von Text
name = "Paul"
alter = 30
text = "Mein Name ist {} und ich bin {} Jahre alt.".format(name, alter)
print(text)

# Verwenden von f-Strings zur Formatierung von Text (Python 3.6+)
text2 = f"Mein Name ist {name} und ich bin {alter} Jahre alt."
print(text2)
