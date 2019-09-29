import tkinter as tk 
from gtts import gTTS


def convert():   
        print("Conversion Started.........")  
        filename = save_name.get()
        data = txt.get("1.0","end-1c")    
        audio = gTTS(text=data,lang="en",slow=False)    
        audio.save(filename)
        print("Conversion Done :)")    
    

def new():
    txt.delete("1.0","end-1c")
    save_name.delete(0,"end")

bgcolor="#192A56"
root = tk.Tk()
root.title("PyText-to-Speech")
root.geometry("530x590")
root.resizable(width=False,height=False)
root.config(background=bgcolor)


title_lbl = tk.Label(root,text="PyText-to-Speech Converter",font="Verdana 20",fg="red",bg=bgcolor)
title_lbl.place(x=87,y=10)

lbl = tk.Label(root,text="Enter the text to convert to speech: ",font="Verdana 12",fg="white",bg=bgcolor)
lbl.place(x=5,y=65)

txt=tk.Text(root,height=25,width=40)
txt.place(x=5,y=90)

save_name_lbl = tk.Label(root,text="Save File as ",font="Verdana 12",fg="white",bg=bgcolor)
save_name_lbl.place(x=5,y=520)
filename = tk.StringVar()
save_name = tk.Entry(root,textvariable=filename)
save_name.place(x=115,y=523)


convert_btn = tk.Button(root,text="Convert",command=convert)
convert_btn.place(x=402,y=115)
convert_btn.config(height=2,width=10)

new_btn = tk.Button(root,text="New Entry",command=new)
new_btn.place(x=402,y=160)
new_btn.config(height=2,width=10)

instruction_lbl = tk.Label(root,text="Connect to internet.\n Enter the name with extension.\nYou can also enter the path.",font="Verdana 8",fg="white",bg=bgcolor)
instruction_lbl.place(x=340,y=240)




credit_lbl = tk.Label(root,text="Developed by\nSamiruddin Thunder\nVer 1.0",fg="white",bg=bgcolor,font="Verdana 10")
credit_lbl.place(x=355,y=500)



root.mainloop()

