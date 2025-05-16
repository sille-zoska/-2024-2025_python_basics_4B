# N-tica (tuple)
farby = ("červená", "zelená", "modrá")
print(farby[1])
print(farby[0:2])  # Zobrazí prvé dva prvky
print(farby[1:])  # Zobrazí všetky prvky od druhého po posledný

# Množina (set)
cisla = {1, 2, 3, 3, 2}
print(cisla)  # Duplikáty sa odstránia
print(2 in cisla)  # Skontroluje, či je číslo 2 v množine
print(4 in cisla)  # Skontroluje, či je číslo 4 v množine
print(2 not in cisla)  # Skontroluje, či číslo 2 nie je v množine

# Slovník (dict)
student = {"meno": "Eva", "vek": 17}
print(student["meno"])
print(student["vek"])
print(student.get("meno"))  # Získanie hodnoty pomocou kľúča
print(student.get("vek"))  # Získanie hodnoty pomocou kľúča
