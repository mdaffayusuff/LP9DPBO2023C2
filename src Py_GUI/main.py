from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import Image, ImageTk
import requests
import io

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3))
hunians.append(Rumah("Sekar MK", 5, 2))
hunians.append(Indekos("Bp. Romi", "Cahya"))
hunians.append(Rumah("Satria", 1, 4))

listphoto = []

root = Tk()
root.title("Praktikum DPBO Python")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen atas nama " + hunians[index].get_nama_pemilik() , padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    
    response = requests.get(hunians[index].get_preview())
    image_data = response.content
    image = Image.open(io.BytesIO(image_data))
    new_width = 400
    new_height = 300
    resized_image = image.resize((new_width, new_height))
    photo_detail = ImageTk.PhotoImage(resized_image)
    listphoto.append(photo_detail)
    d_pict = Label(d_frame, image=photo_detail).grid(row=0)

    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w", justify=LEFT).grid(row=1, column=0, sticky="w")
    #d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

def main_page():
    landing_frame.destroy()
    masuk_section.destroy()
    
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

landing_frame = LabelFrame(root, text="Hello", padx=10, pady=10)
landing_frame.pack(padx=10, pady=10)

landing_welcome = Label(landing_frame, text="Welcome back, User").grid(row=0)

response = requests.get("https://cdn.dribbble.com/users/989466/screenshots/16168689/media/66899610428d098a4467516591ce01ae.png")
image_data = response.content
image = Image.open(io.BytesIO(image_data))
new_width = 400
new_height = 300
resized_image = image.resize((new_width, new_height))
photo_detail = ImageTk.PhotoImage(resized_image)
listphoto.append(photo_detail)
detail_pict = Label(landing_frame, image=photo_detail).grid(row=1)


masuk_section = LabelFrame(root)
masuk_section.pack(padx=10, pady=10)
masuk_button = Button(masuk_section, text="Masuk", command=main_page, padx=100)
masuk_button.grid(row=0, column=0)


root.mainloop()
