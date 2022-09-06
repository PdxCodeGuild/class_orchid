import pprint
import re
import requests
import json
import PySimpleGUI as sg
import csv
import os


layout = [
    [sg.Text("would you like to enter the recipe book?", size = 10)],
    [sg.Button("DONE")],
    [sg.Button("OK")]

]

window = sg.Window("demo", layout)


layout2 = [
    [sg.Button("OK")],
    [sg.Button("DONE")],
    [sg.Text("Please enter the food you want to search for:")],
    [sg.Input("")],
    

    ]

window2 = sg.Window("demo_2", layout2)

while True:
    event, values = window2.read()
    if event == "OK":
        value = values[0]

    params = {
    "type" :"public",
     "app_id" : "1cdc9597", 
    "app_key" : "60b438b2284a5c3d5ae7d03e81caac11",
    "q" : "type of food",

}



    type_of_food_requested = value
    params.update({"q": [type_of_food_requested]})
    #print(params)

    response = requests.get("https://api.edamam.com/api/recipes/v2", params=params, headers = {'accept' : 'application/json'})
    response = json.loads(response.text)

    hits = response["hits"]



    w1 = hits[1]
    


    rec = f"Here is the ingrediant list:", w1["recipe"]["ingredientLines"]
    link = f'Here is the link for the instructions:', w1["recipe"] ["url"]
    #print(f"Here is the ingrediant list:", w1["recipe"]["ingredientLines"])
    #print(f'Here is the link for the instructions:', w1["recipe"] ["url"])
        
    if event == "DONE" or event == sg.WIN_CLOSED:
        break
window.close()


rec= str(rec)
rec.split(",")



final_layout =[  
[sg.Text(rec, size= (20,20))],
[sg.Button("DONE")],
[sg.Text(link, size= (20,20))]

]

final_window = sg.Window("demo_2", final_layout, size = (400,400), finalize=True)


while True:
    event, values = final_window.read()

    if event == "DONE" or event == sg.WIN_CLOSED:
        break
window.close()
    