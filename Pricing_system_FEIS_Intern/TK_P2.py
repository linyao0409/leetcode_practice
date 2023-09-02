import tkinter as tk
win = tk.Tk()
win.title("Far Easten")
win.geometry("700x500")
win.minsize(500,300)
win.maxsize(1024,768)
#icon
win.iconbitmap("/Users/linyao/python/TK_practice/feis_image.ico")
#col 
win.config(background="grey")
#透明度
win.attributes("-alpha",0.8)
#置頂
win.attributes("-topmost",0) # 1 : True, 0: False



#button
btn = tk.Button(text = "give me pric ered",bg="red")

btn.pack()

win.mainloop()