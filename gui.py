import tkinter as tk
window = tk.Tk()
frame_a = tk.Frame(master=window, relief = tk.GROOVE, borderwidth = 5)
label_a = tk.Label(master=frame_a, text="Name") #create label_a and assign frame_a to label_a
entry = tk.Entry()
button = tk.Button()
text_box=tk.Text()

frame_b = tk.Frame(master=window, width=100, height=15)
label_b = tk.Label(master=frame_b, text="Surname")


frame_a.pack()
label_a.pack()
frame_b.place(x=5,y=30)
label_b.pack()
entry.pack()
button.pack()
text_box.pack()

#assign entered text from entry to var name
name = entry.get()
#if for example user entered invalid input
#text for reentry could be deleted by
#entry.delete(0, tk.END)

window.mainloop()

#yeah