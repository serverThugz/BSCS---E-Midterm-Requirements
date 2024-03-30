from tkinter import *
from PIL import Image, ImageTk

after_id = None  # Declare a global variable outside functions

def animate_next_frame():
    global count, after_id
    new_image = imageObject[count]
    label.config(image=new_image)
    count += 1
    if count == frames:
        count = 0
    after_id = loading.after(100, animate_next_frame)  # Assign after_id

def open_new_window():
    pass

def stop_animation():
    global after_id
    if after_id is not None:
        loading.after_cancel(after_id)
    loading.destroy()
    open_new_window()

loading = Tk()
loading.geometry("455x560")

# Create a frame with black background
frame = Frame(loading, bg="black")
frame.place(x=0, y=0, relwidth=1, relheight=1)

gifImage = "C:\\Users\\Me\\PycharmProjects\\Self Development Activity\\LoadingGIF.gif"
openImage = Image.open(gifImage)
tkImage = ImageTk.PhotoImage(openImage)

# Create label with the GIF image and place it inside the frame
label = Label(frame, image=tkImage)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

frames = openImage.n_frames
imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
count = 0

# Start animation
animate_next_frame()
# Stop animation after 3 seconds
loading.after(3000, stop_animation)


loading.mainloop()
