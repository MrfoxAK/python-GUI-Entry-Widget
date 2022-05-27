from tkinter import *

root = Tk()

root.geometry("425x280")
root.title("AK")
def getvals():
    print(f"The name of user is {nameval.get()}")
    print(f"The phone.no of user pass is {phoneval.get()}")
    print(f"The gender of user is {genderval.get()}")
    print(f"The emergency.no of user is {emval.get()}")
    print(f"The paymentmode of user is {payval.get()}")
    print(f"is the user is interested in prefood ? 1 for yes & 0 for no \nUser said : {foodval.get()}")
    with open("myLogs.txt", "a") as f:
        f.write(f"The name of user is : {nameval.get()}\n")
        f.write(f"The phone.no of user pass is  : {phoneval.get()}\n")
        f.write(f"The gender of user is : {genderval.get()}\n")
        f.write(f"The emergency.no of user is : {emval.get()}\n")
        f.write(f"The paymentmode of user is : {payval.get()}\n")
        f.write(f"is the user is interested in prefood ? 1 for yes & 0 for no \nUser said : {foodval.get()}\n")
        # f.write(f"                             \n")

Label(root, text="Welcome to AK Travels", font="comicsansms 15 bold",pady=15).grid(row=0,column=3)
# text for our form
name = Label(root, text="Name :")
phone = Label(root, text="Phone :")
gender = Label(root, text="Gender :")
emergency = Label(root, text="Emergency Contact :")
paymentmode = Label(root, text="Payment Mode :")
#pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)
# tkinter variable for storing entries
nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
emval = StringVar()
payval = StringVar()
foodval = IntVar()
# entries for our form
nameentry = Entry(root,textvariable=nameval)
phentry = Entry(root,textvariable=phoneval)
genentry = Entry(root,textvariable=genderval)
ementry = Entry(root,textvariable=emval)
payentry = Entry(root,textvariable=payval)
# packing the entries
nameentry.grid(row=1,column=3)
phentry.grid(row=2,column=3)
genentry.grid(row=3,column=3)
ementry.grid(row=4,column=3)
payentry.grid(row=5,column=3)
# checkbox & packing
foodservice = Checkbutton(text="Want to prebook your meels?",variable=foodval)
foodservice.grid(row=6, column=3)
# Button & Packing
Button(text="Submit!", command=getvals).grid(row=7,column=3)


root.mainloop()





