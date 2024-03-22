from tkinter import *






aken=Tk()
aken.geometry("800x400")
aken.title("Tkineri kasutamine")

tekst1="Ruutvõrrandi lahendamine"

pealkiri=Label(aken,
               text=tekst1,
               bg="#bddbf0",
               fg="#04951d",
               font="Arial 20",
               height=3,
               width=len(tekst1))
esForm=Label(aken,
             )



obj=[pealkiri]
for i in obj:
    i.pack()
aken.mainloop()
