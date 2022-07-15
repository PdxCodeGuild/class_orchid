distance = {
    "feet" : 0.3048,
    "mile" : 1609.43,
    "meter" : 1,
    "km" : 1000,
    "yard" : 0.9144,
    "inch" : 0.0254 
}

measurement = input("\nPlease the imput units; feet, mile, meter, km, yard, inch ")


lenght_to_convert = distance[measurement]

orginal_lenght  = input("\nPlease enter the distance ")

output_units = input("\nenter the disired output unit ")
output_units = distance[output_units]
orginal_lenght = int(orginal_lenght)


output = orginal_lenght * lenght_to_convert

final_output = output / output_units

print(f"total distance {final_output}")