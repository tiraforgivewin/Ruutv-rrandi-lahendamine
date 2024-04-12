from re import A
from tkinter import *

def Answer():
      a=float(textbox1.get())
      b=float(textbox2.get())
      c=float(textbox3.get())
      if a!="" and b!="" and c!="":
            D=b**2-4*a*c
            if D>0:
                x1=((b*-1)+D**(1/2))/2*a
                x2=((b*-1)-D**(1/2))/2*a
                AnswerForm.configure(text="Vastama on "+x1+","+x2)
            elif D==0:
                x=(b*-1)/(2*a)
                AnswerForm.configure(text="Vastama on "+x)
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
             height=1,
             width=len(tekst2)
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


pealkiri.grid(row=0,column=1,columnspan=6)
esimineForm.grid(row=1,column=1)
teineForm.grid(row=1,column=3)
kolmasForm.grid(row=1,column=5)
textbox1.grid(row=1,column=0)
textbox2.grid(row=1,column=2)
textbox3.grid(row=1,column=4)
nupp.grid(row=1,column=6)
AnswerForm.grid(row=9,column=4)
aken.mainloop()
