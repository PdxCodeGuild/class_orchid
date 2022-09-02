from tkinter import *
from PIL import Image, ImageTk
import requests

"""
maybe find a way to turn the button into a pair of dice

i need to find a way to get my quotes to be wrapped or warped to fit my gui???
"""
#the boilerplate when using tkinter and the classes that comes with it
root = Tk()
root.title("DONDA")
root.geometry("825x800")

#assigning my api to a variable to be used in a function i will later create
url = "https://api.kanye.rest" #not sure what my endpoint is at this time

#my get_quote function does just that.. grabs a kanye quote (which are usally fire)
def get_quote():
    response = requests.get(url)
    quote = response.json()['quote']
    return(quote)

# label1=Label(root, text='I miss Mitch')



canvas1 = Canvas(root, width=425, height=425, bg='red')

#im positioning my canvas into my window, if i had two canvas i could literally put them both in the same window by making adjustments ie: c1.pack(side="left") and same for the right 
canvas1.place(x=0,y=0, relwidth=1, relheight=1)

#here im using Image.open which is a module i imported from PIL to bring in my image of little ye that will be assigned to the variable 'img'
img = (Image.open('little_kanye.png'))



#im doing just that with the resize method resizing my image to make it fit into my "825x800" window then using ANTIALIAS to smooth any jagged edges
resize_image = img.resize((800,775),Image.ANTIALIAS)

#just reassigning my little ye that has just been modified to work for my project
new_image = ImageTk.PhotoImage(resize_image)

#now im displaying the image as my canvas to now have labels or buttons put onto, "anchor=NW" is me telling tkinter to start with the most upper left it can get then stretch to the most bottom right
canvas1.create_image(10,10, anchor=NW, image=new_image)

#function created to get a response whatever that might be from clicking the button
def myClick():
    label1.config(text=get_quote())
    label2.config(text=get_quote())


#this is actually getting whatever text you want displayed,to actually display .pack() in terms just places the object with no regards where
my_text = Label(root, text="Mood for the day...", font=("Helvetica", 40), fg='red')
my_text.pack(pady=15)

label1 = Label(root, text=get_quote(), font=("Helvetica", 16))
label1.pack()

space = Label(root, text='OR',font=("Helvetica",70), fg='red')
space.pack()

label2 = Label(root, text=get_quote(), font=("Helvetica", 16))
label2.pack()



#do not put '()' into the function when assigning the command
button1 = Button(root, text="Kayne once said", command=myClick, padx=2, pady=3)
button1.pack()


#this is how you actually move your buttons or labels in the window you've created to make adjustments ex: (600,25)
button1_canvas =canvas1.create_window(600,25,anchor="nw", window=button1)
label1_canvas =canvas1.create_window(20,750, anchor="nw", window=label1)
label2_canvas =canvas1.create_window(20,73, anchor="nw", window=label2)
space =canvas1.create_window(60,350, anchor="nw", window=space)


#this method ongoing loop that tracks even your cursor being moved and the way thats made possible is with root.mainloop()
root.mainloop()