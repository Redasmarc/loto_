from tkinter import *
import random
from PIL import Image, ImageTk

sarasas1 = []
sarasas2 = []

def tavo_skaiciai():
    sarasas1.clear()
    for i in range(6):
        skaicius = random.randint(1, 37)
        sarasas1.append(skaicius)
    l_sarasas1 = Label(root, text="")
    l_sarasas1.grid(row=1, column=0, padx=0, pady=5)
    l_sarasas1.config(text=f"Tavo bilieto skaiciai: {sarasas1}")
    return sarasas1


def istraukti_skaiciai():
    sarasas2.clear()
    for i in range(6):
        skaicius = random.randint(1, 37)
        sarasas2.append(skaicius)
    l_sarasas2 = Label(root, text="")
    l_sarasas2.grid(row=6, column=0, padx=0, pady=0)
    l_sarasas2.config(text=f"Laimingi skaiciai: {sarasas2}")
    return sarasas2

def tikrinam():
    tinka = set(sarasas1) & set(sarasas2)
    if len(tinka) == 6:
        tikrina.config(text="Atspejai 6 skaicius ir laimejai didiji priza 100_000 LT!", bg='green')
    elif len(tinka) == 5:
        tikrina.config(text="Atspejai 5 skaicius ir laimejai buta Palangoje!", bg='green')
    elif len(tinka) == 4:
        tikrina.config(text="Atspejai 4 skaicius ir laimejai automobili Fiat Punto!", bg='green')
    elif len(tinka) == 3:
        tikrina.config(text="Atspejai 3 skaicius ir laimejai kelione i JAE! Viskas iskaiciuota!", bg='green')
    elif len(tinka) == 2:
        tikrina.config(text="Atspejai 2 skaicius, deja, nieko nelaimejai.", bg='red')
    elif len(tinka) == 1:
        tikrina.config(text="Atspejai tik 1 skaiciu, deja, nieko nelaimejai.", bg='red')
    else:
        tikrina.config(text="Deja neatspejai nei vieno skaiciaus. Sekmes kita karta.", bg='red')


root = Tk()
root.title("Lotto Zaidimas")
root.geometry("380x260")
root.maxsize(379,252)
background = PhotoImage(file="images/jackpot.png")
bg = Label(image=background)

bg.place(x=0, y=0, relwidth=1, relheight=1) # bg vidury

bilietas = Button(root, text="Isigyti bilieta", command=tavo_skaiciai)
bilietas.grid(row=0, column=0, padx=150, pady=10)

laimingi = Button(root, text="Laimingi skaiciai", command=istraukti_skaiciai)
laimingi.grid(row=4, column=0, padx=150, pady=10)

tikrinti = Button(root, text="Tikrinkite bilieta", command=tikrinam)
tikrinti.grid(row=8, column=0, padx=0, pady=10)

tikrina = Label(root, text='')
tikrina.grid(row=10, column=0, padx=0, pady=0)


root.mainloop()