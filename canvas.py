from tkinter import *
from tkinter import ttk
import joblib
from PIL import ImageGrab

import imageProcessing
from imageProcessing import *

PATH = r'.\images\\'


def create_canvas(p_width=500, p_height=500, p_brush_size=10):
    root = Tk()
    root.title("Digit recognition")

    cv = Canvas(root,
                width=p_width,
                height=p_height,
                bg='white')
    cv.pack()

    def paint(event):
        color = 'black'
        x1, y1 = (event.x - p_brush_size), (event.y - p_brush_size)
        x2, y2 = (event.x + p_brush_size), (event.y + p_brush_size)
        cv.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def save_image():
        x = root.winfo_rootx()
        y = root.winfo_rooty()
        xx = x + root.winfo_width()
        yy = y + root.winfo_height()
        ImageGrab.grab().crop((x, y, xx, yy)).save(PATH + 'image.jpg')
        resize_image(PATH + 'image.jpg')


    def open_popup():
        save_image()
        top= Toplevel(root)
        top.geometry("250x50")
        top.title("Result")
        Label(top, text= "Rozpoznana liczba to %d" % joblib.load("trained_model.joblib").predict([imageProcessing.image_to_np(PATH + 'image.jpg').flatten()])).place(x=15,y=15)

    cv.bind("<B1-Motion>", paint)
    # cv.bind("<ButtonRelease-1>", save_image)

    ttk.Button(root, text= "check", command= open_popup).pack()

    root.mainloop()



