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
                answer1 = "Vastama on ", x1, ",", x2
                AnswerForm.configure(text=answer1)
            elif D==0:
                x=(b*-1)/(2*a)
                answer2 =  "Vastama on ", x
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
      if a!="" and b!="" and c!="":
            D=b**2-4*a*c
            if D>0:
                x1=((b*-1)+D**(1/2))/2*a
                x2=((b*-1)-D**(1/2))/2*a
                xmin=-20.0
                xmax=20.0
                dx=0.01
                xlist=mlab.frange(xmin, xmax, dx)
                plt.plot(xlist, ylist, color='b', linestyle='-', marker='')
                ymin=-20.0
                ymax=20.0
                dy=0.01
                ylist=mlab.frange(ymin, ymax, dy)
                plt.show()

            elif D==0:
                x=(b*-1)/(2*a)
            elif D<0:
               AnswerForm.configure(text="Võrrandil pole juuri")    
      else:
          textbox1.configure(bg="#ff1100")
          textbox2.configure(bg="#ff1100")
          textbox3.configure(bg="#ff1100")
    
    


      




aken=Tk()
aken.geometry("800x400")
aken.title("Tkineri kasutamine")

tekst1="Ruutvõrrandi lahendamine"
tekst2="Lahendus"
tekst3 = "Graafik"


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

pealkiri.grid(row=0,column=1,columnspan=6)
esimineForm.grid(row=1,column=1)
teineForm.grid(row=1,column=3)
kolmasForm.grid(row=1,column=5)
textbox1.grid(row=1,column=0)
textbox2.grid(row=1,column=2)
textbox3.grid(row=1,column=4)
nupp.grid(row=1,column=6)
nupp2.grid(row=1,column=7)
AnswerForm.grid(row=9,column=1,columnspan=6)
aken.mainloop()
