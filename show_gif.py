from tkinter import *
from PIL import Image, ImageTk

root = Tk()
file = 'gif.gif'

info = Image.open(file)
frames = info.n_frames
print(frames)

im = [ImageTk.PhotoImage(file=file,format=f'gif -index{i}') for i in range(frames)]

gif_label = Label(image=im[0])
gif_label.pack()

anim = None
count = 0
delay = 50

def animation():
    global count, anim
    count = (count + 1) % frames
    gif_label.configure(image=im[count])
    anim = root.after(delay, animation)

def start_animation():
    global anim
    anim = root.after(delay, animation)

def stop_animation():
    global anim
    if anim:
        root.after_cancel(anim)
        anim = None

start_button = Button(text="Start", command=start_animation)
start_button.pack()

stop_button = Button(text="Stop", command=stop_animation)
stop_button.pack()

root.mainloop()






