from re import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib import mlab
from math import *

def Answer():
      a=float(textbox1.get())
      b=float(textbox2.get())
      c=float(textbox3.get())
      if a!="" and b!="" and c!="":
            D=b**2-4*a*c
            if D>0:
                x1=((b*-1)+D**(1/2))/2*a
                x2=((b*-1)-D**(1/2))/2*a
                answer1 = "Vastama on ", round(x1, 3), ",",  round(x2, 3)
                AnswerForm.configure(text=answer1)
            elif D==0:
                x=(b*-1)/(2*a)
                answer2 =  "Vastama on ",  round(x, 3)
                AnswerForm.configure(text=answer2)
            elif D<0:
               AnswerForm.configure(text="Võrrandil pole juuri")    
      else:
          textbox1.configure(bg="#ff1100")
          textbox2.configure(bg="#ff1100")
          textbox3.configure(bg="#ff1100")

def Grafik():
      a=float(textbox1.get())
      b=float(textbox2.get())
      c=float(textbox3.get())     
      x0=-b/(2*a)
      y0=a*x0**2+b*x0+c
      x1 = []
      for i in range(-20, 21):
          x1.append(x0 + i)
      y1 = [a * x ** 2 + b * x + c for x in x1]
      plt.figure()
      plt.plot(x1, y1, 'r-d')
      plt.ylabel('y')
      plt.xlabel('x')
      plt.grid(True)
      plt.show()    
    
def Grafik_Libikas():
    x1 = list(range(-9, 0))
    y1 = [-1*(1/8)*(x+9)**2 + 8 for x in x1]    
    x2 = list(range(1, 10))
    y2 = [-1*(1/8)*(x-9)**2 + 8 for x in x2]
    
    x3 = list(range(-9, -7))
    y3 = [7*(x+8)**2 + 1 for x in x3]    
    x4 = list(range(8, 10))
    y4 = [7*(x-8)**2 + 1 for x in x4]

    x5 = list(range(-8, 0))
    y5 = [(1/49)*(x+1)**2 for x in x5]    
    x6 = list(range(1, 9))
    y6 = [(1/49)*(x-1)**2 for x in x6]
    
    x7 = list(range(-8, 0))
    y7 = [-1*(4/49)*(x+1)**2 for x in x7]   
    x8 = list(range(1, 9))
    y8 = [-1*(4/49)*(x-1)**2 for x in x8]
    
    x9 = list(range(-8, -1))
    y9 = [(1/3)*(x+5)**2-7 for x in x9]   
    x10 = list(range(2, 9))
    y10 = [(1/3)*(x-5)**2-7 for x in x10]
    
    x11 = list(range(-2, 0))
    y11 = [-2*(x+1)-2 for x in x11]    
    x12 = list(range(1, 3))
    y12 = [-2*(x-1)-2 for x in x12]
    
    x13 = list(range(-1, 2))
    y13 = [-4*x**2+2 for x in x13]   
    x14 = list(range(-1, 2))
    y14 = [4*x**2-6 for x in x14]
    
    x15 = list(range(-2, 1))
    y15 = [-1.5*x+2 for x in x15]
    x16 = list(range(0, 3))
    y16 = [1.5*x+2 for x in x16]
    
    plt.figure()
    plt.plot(x1, y1, 'r-d', x2, y2, 'r-d', x3, y3, 'r-d', x4, y4, 'r-d',
             x5, y5, 'r-d', x6, y6, 'r-d', x7, y7, 'r-d', x8, y8, 'r-d',
             x9, y9, 'r-d', x10, y10, 'r-d', x11, y11, 'r-d', x12, y12, 'r-d'
             , x13, y13, 'r-d', x14, y14, 'r-d', x15, y15, 'r-d', x16, y16, 'r-d')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
    
def Grafik_Vihmavari():
     x1 = list(range(-12, 13))
     y1 = [-1*(1/18)*x**2 + 12 for x in x1] 
     x2 = list(range(-4, 5))
     y2 = [-1*(1/8)*x**2 + 6 for x in x2] 
     x3 = list(range(-12, -3))
     y3 = [-1*(1/8)*(x+8)**2 + 6 for x in x3] 
     x4 = list(range(4, 13))
     y4 = [-1*(1/8)*(x-8)**2 + 6 for x in x4] 
     x5 = list(range(-4, 2))
     y5 = [1.5*(x+3)**2-10 for x in x5]
     plt.figure()
     plt.plot(x1, y1, 'r-d', x2, y2, 'r-d', x3, y3, 'r-d', x4, y4, 'r-d', x5, y5, 'r-d',)
     plt.ylabel('y')
     plt.xlabel('x')
     plt.grid(True)
     plt.show()
     

def Grafik_Prillid():
     x1 = list(range(-9, 0))
     y1 = [-1*(1/16)*(x+5)**2 + 2 for x in x1] 
     x2 = list(range(1, 10))
     y2 = [-1*(1/16)*(x-5)**2 + 2 for x in x2] 
     x3 = list(range(-9, 0))
     y3 = [(1/4)*(x+5)**2 - 3 for x in x3] 
     x4 = list(range(1, 10))
     y4 = [(1/4)*(x-5)**2 - 3 for x in x4] 
     x5 = list(range(-1, 2))
     y5 = [-0.5*x**2+1.5 for x in x5]
     x6 = list(range(-9, -5))
     y6 = [-1*(x+7)**2+5 for x in x6]
     x7 = list(range(6, 10))
     y7 = [-1*(x-7)**2+5 for x in x7]
     plt.figure()
     plt.plot(x1, y1, 'r-d', x2, y2, 'r-d', x3, y3, 'r-d', x4, y4, 'r-d', x5, y5, 'r-d', x6, y6, 'r-d', x7, y7, 'r-d',)
     plt.ylabel('y')
     plt.xlabel('x')
     plt.grid(True)
     plt.show()



      




aken=Tk()
aken.geometry("800x400")
aken.title("Tkineri kasutamine")

tekst1="Ruutvõrrandi lahendamine"
tekst2="Lahendus"
tekst3 = "Graafik"
tekst4 = "Libikas"
tekst5 = "Vihmavari"
tekst6 = "Prillid"


pealkiri=Label(aken,
               text=tekst1,
               bg="#bddbf0",
               fg="#04951d",
               font="Arial 20",
               height=3,
               width=len(tekst1))
esimineForm=Label(aken, 
             text="x**2+",
             bg="#ffffff",
             fg="#04951d",
             font="Arial 20",
             height=1,
             width=6
             )
teineForm=Label(aken, 
             text="x+",
             bg="#ffffff",
             fg="#04951d",
             font="Arial 20",
             height=1,
             width=6
             )
kolmasForm=Label(aken, 
             text="=0",
             bg="#ffffff",
             fg="#04951d",
             font="Arial 20",
             height=1,
             width=6
             )



AnswerForm=Label(aken, 
             text=tekst2,
             bg="#ffd042",
             fg="#000000",
             font="Arial 20",
             height=3,
             width=30
             )


textbox1=Entry(aken,
               bg="#dee3db",
               fg="#000000",
               font="Arial 20",
               width=5
               )
textbox2=Entry(aken,
               bg="#dee3db",
               fg="#000000",
               font="Arial 20",
               width=5
               )
textbox3=Entry(aken,
               bg="#dee3db",
               fg="#000000",
               font="Arial 20",
               width=5
               )


nupp=Button(aken,
            text=tekst2,
            height=1,
            width=len(tekst2),
            bg="#72d048",
            font="Arial 20",
            command=Answer
            
            )
nupp2=Button(aken,
            text=tekst3,
            height=1,
            width=len(tekst3),
            bg="#72d048",
            font="Arial 20",
            command=Grafik)
nupp3=Button(aken,
            text=tekst4,
            height=1,
            width=len(tekst4),
            bg="#72d048",
            font="Arial 20",
            command=Grafik_Libikas)
nupp4=Button(aken,
            text=tekst5,
            height=1,
            width=len(tekst5),
            bg="#72d048",
            font="Arial 20",
            command=Grafik_Vihmavari)
nupp5=Button(aken,
            text=tekst6,
            height=1,
            width=len(tekst6),
            bg="#72d048",
            font="Arial 20",
            command=Grafik_Prillid)

pealkiri.grid(row=0,column=0,columnspan=7)
esimineForm.grid(row=1,column=1)
teineForm.grid(row=1,column=3)
kolmasForm.grid(row=1,column=5)
textbox1.grid(row=1,column=0)
textbox2.grid(row=1,column=2)
textbox3.grid(row=1,column=4)
nupp.grid(row=1,column=6)
nupp2.grid(row=1,column=7)
nupp3.grid(row=10,column=1,columnspan=2)
nupp4.grid(row=10,column=3,columnspan=2)
nupp5.grid(row=10,column=5,columnspan=2)
AnswerForm.grid(row=9,column=0,columnspan=7)
aken.mainloop()
