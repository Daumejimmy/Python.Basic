# Definition von Variablen mit unterschiedlichen Datentypen
x = 5               # Integer
name = "Max"       # String

# Mehrere Variablenzuweisung in einer Zeile
a, b, c = 5, 4, "Tim"

# Ändern des Wertes einer Variable
alter = 30          # Integer
gewicht = 14.5      # Float
name = "Alex"       # String
gewicht = 15        # Wert von "gewicht" wird von 14.5 auf 15 geändert

# Definition einer Funktion
def meine_funktion():
    lokal = "Ich bin lokal"
    print(lokal)

# Änderung einer globalen Variablen innerhalb einer Funktion
def set_global_var():
    global global_var
    global_var = "Global"
