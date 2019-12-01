def mass_to_fuel(mass):
    return (mass // 3) - 2

def full_mass_to_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel > 0:
        fuel += full_mass_to_fuel(fuel)
    else:
        return 0
    return fuel

with open("input", "r") as f:
    file_data = f.read()
    modules_mass = file_data.split("\n")
    total_fuel_needed = 0
    for mass in modules_mass:
        if mass:
            total_fuel_needed += full_mass_to_fuel(int(mass))
    print(f"total fuel needed: {total_fuel_needed}")
