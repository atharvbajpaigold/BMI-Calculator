from tkinter import *
from tkinter import ttk
root = Tk()

g = IntVar()
lgbtq = ["Male","Female"]
root.geometry("1000x700")
def bmi():
    a = int(entry.get())
    b= int(entry2.get())
    c = b/100
    B = round(float(a / c** 2), 1)
    label7.config(text=B)
    label7.place(x=100,y=550)\


#main heading
label = Label(root,
              text='BMI Calculator',
              font=('Arial',25,'bold'),
              fg='white',
              bg='black')
label.pack()
#MH
label7 =  Label(root,
              text='BMI SCREEN',
              font=('Arial',15,'bold'),
              fg='white',
              bg='black')
label7.place(x=100,y=550)
#enter weight
lbl1 = Label(root,
             text='* Enter Your Weight In KG (Down Below) ',
             font=('Arial',15,'bold'))
lbl1.place(x=0 , y=150)
#enter weight text

l = PhotoImage(file='guu.png')
lll = Label(image=l)
lll.place(x=470,y=80)
l2 = PhotoImage(file='guu2.png')
lll2 = Label(image=l)
lll2.place(x=900,y=80)
#entry box for weight
entry = Entry(root,
              font=('Arial',15,'bold'),
              )
entry.place(x=0,y=190)
#entry box for weight

#enter age text
lbl2 = Label(root,
             text='* Enter Your Height In CM Down Below ',
             font=('Arial',15,'bold'))
lbl2.place(x=0 , y=280)
#enter age text


#entry box for height
entry2 = Entry(root,
              font=('Arial',15,'bold'),
              )
entry2.place(x=0,y=320)
#entry box for height


sb = Button(root,command=bmi,text='Submit',font = ('Arial',15,'bold'))
sb.place(x=100,y=400)

for index in range(len(lgbtq)):
    rb = Radiobutton(root,
                     text=lgbtq[index],
                    font=('Arial',15,'bold'),
                    variable=g,
                    value=index,
                    )   
    rb.pack(anchor=W)

   
root.mainloop()
























