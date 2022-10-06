'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 18: Mini Capstone - Rainbow Table'''

import PySimpleGUI as sg
import requests
import hashlib

def make_list(count, length):

    url=f"https://makemeapassword.ligos.net/api/v1/alphanumeric/json?c={count}&l={length}&sym=True"
    response = requests.get(url) 

    data = response.json()
    pws = data.get('pws')
    password_dict = {}
    for password in pws:
        password_dict[password] = hashlib.md5(password.encode('utf-8')).hexdigest()
    return password_dict

def decode(hash_in):
    with open('rbow_table.csv', 'r') as file:
        lines = file.read().replace(', ', '\n')
        lines = lines.split('\n')

    if hash_in in lines:
        pw_index = lines.index(hash_in) - 1
        output = lines[pw_index]
        return output
       

# All the stuff inside the window.
sg.theme('DarkPurple')
layout = [  [sg.Text('Welcome to the Rainbow Table creator and hash decoder')],
            [sg.Text('Please Enter the number of passwords you would like to add'), sg.InputText(do_not_clear=False)],
            [sg.Text('Please enter the length of the passwords you would like to add'), sg.InputText(do_not_clear=False)],
            [sg.Text('For decoding, enter the hash you would like to decode.'), sg.InputText(do_not_clear=False)],
            [sg.Button('Send It'), sg.Button('Decode'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Rainbow Table', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    #print(values)
    length = values[1]
    count = values[0]
    hash_in = values[2]

    if event == 'Send It':
        password = make_list(count, length)
        with open('rbow_table.csv', 'a') as f:
            for key in password.keys():
                f.write("%s, %s\n"%(key,password[key]))

    if event == 'Decode':
        pw = decode(hash_in)
        if pw is not None:
            sg.popup_ok(f"The hash value {hash_in} corresponds with a password of {decode(hash_in)}. ")
        else:
            sg.popup_ok("That hash was not found, please try a different one. ")

    elif event == sg.WIN_CLOSED or event == 'Cancel': 
        window.close()
        break

window.close()