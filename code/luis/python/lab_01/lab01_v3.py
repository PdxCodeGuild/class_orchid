distance_by_unit  = {
    "foot": float(0.3048), # meters
    "mi": float(1609.34),  # 1 milimeters is meters
    "m": 1, # 1 meter is 1 meter
    "km": 1000, # 1 kilometer is 1000 meters
    "yard": float(0.9144), # one yard to meters
    "inch": float(0.0254) # one inch to meters
}

user_input = int(input("What is the distance? "))
user_unit = input("What are the units? ")

if user_unit == "foot":
    total = user_input * distance_by_unit["foot"]
    print(f"{user_input} {user_unit} is {total} m")
elif user_unit == "mi":
    total2 = user_input * distance_by_unit["mi"]
    print(f"{user_input} {user_unit} is {total2} m")
elif user_unit == "m":
    total3 = user_input * distance_by_unit["m"]
    print(f"{user_input} {user_unit} is {total3} m")
elif user_unit == "km":
    total4 = user_input * distance_by_unit["km"]
    print(f"{user_input} {user_unit} is {total4} m")
elif user_unit == "yard":
    total5 = user_input * distance_by_unit["yard"]
    print(f"{user_input} {user_unit} is {total5} m")
elif user_unit == "inch":
    total6 = user_input * distance_by_unit["inch"]
    print(f"{user_input} {user_unit} is {total6} m")