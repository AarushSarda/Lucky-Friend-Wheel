from tkinter import *
import random

root = Tk()
root.title("Lucky Friend Wheel")
root.geometry("500x500")
root.configure(background = "pink")

input1 = Entry(root)
input1.place(relx = 0.5 , rely = 0.2 , anchor=CENTER)

labelList = Label(root)
labelRN = Label(root)
labelRName = Label(root)
list = []

def addFriend() :
    friend_name = input1.get()
    list.append(friend_name)
    labelList["text"]= "Your Friend List : " + str(list)
    
def RandomName() :
    length = len(list)
    random_number = random.randint(0 , length-1)
    labelRN["text"] = str(random_number)
    generatedRandomNUM = list[random_number]
    labelRName["text"] = str(generatedRandomNUM)
    
btn = Button(root , text = "Add To Your Friend List" , command = addFriend)
btn.place(relx=0.5 , rely=0.3 , anchor=CENTER)

labelList.place(relx=0.5,rely=0.4,anchor=CENTER)

btn2 = Button(root , text = "Who Is Your Lucky Friend" , command = RandomName)
btn2.place(relx=0.5 , rely=0.5 , anchor=CENTER)
labelRN.place(relx=0.5,rely=0.6,anchor=CENTER)
labelRName.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()