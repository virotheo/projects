from tkinter import *
import requests
import webbrowser
import os

ip = requests.get("https://api.ipify.org").text
version = 1.1
coins = 0

# creation sauvegarde si pas présent

if os.path.exists("save.txt"):
      with open("save.txt", "r") as saving:
       try:
            coins = int(saving.read())
       except:
            coins = 0
       saving.close()
else:
     with open("save.txt", "w+") as save:
      save.write("0")
      save.close()

# On définit un gestionnaire d'événements pour le bouton ci-dessous.
def farm():
    global coins
    coins += 5
    coins_show.config(text=coins)

def link_support():
        webbrowser.open_new("https://discord.gg/upM5gf9RxM")

def save():
      with open("save.txt", "w") as saving:
            saving.write(str(coins))

def auto_save():
      save()
      window.after(1000, auto_save)

# On instancie notre fenêtre graphique
window = Tk()
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)
window.title(f"Cookie Clicker V{version}")
window.iconbitmap("logo_cookie.ico")
window.config(background='#91370d')

# créer la boite
frame = Frame(window, bg='#91370d', bd=1, relief=SUNKEN)

label_title = Label(frame, text='Cookie Clicker', font=('courrier', 50 ),bg='#91370d', fg='#ffffff')
label_title.pack()

footer_ip = Label(window, text=f'Your IP : {ip}', font=('courrier', 8  ),bg='#91370d', fg='#ffffff')
footer_ip.pack(side=BOTTOM)

coins_show = Label(frame, text=coins, font=('courrier', 8  ),bg='#91370d', fg='#ffffff')
coins_show.pack()
coins_show.config(text=coins)

upgrade_1 = Button(frame, text='Buy a Kitchen (x1.25)', font=('Courrier', 5),bg='#ffffff', fg='#91370d', command=None)
upgrade_1.pack(pady=5,side=BOTTOM)

upgrade_2 = Button(frame, text='Buy a Furnace (x1.5)', font=('Courrier', 5),bg='#ffffff', fg='#91370d', command=None)
upgrade_2.pack(pady=5,side=BOTTOM)

upgrade_3 = Button(frame, text='Upgrade Furnace (x1.75)', font=('Courrier', 5),bg='#ffffff', fg='#91370d', command=None)
upgrade_3.pack(pady=5,side=BOTTOM)

upgrade_4 = Button(frame, text='Buy Vanilla Cookie Method (x2)', font=('Courrier', 5),bg='#ffffff', fg='#91370d', command=None)
upgrade_4.pack(pady=5,side=BOTTOM)

farm_button = Button(frame, text='Farm', font=('Courrier', 15),bg='#ffffff', fg='#91370d', command=farm)
farm_button.pack(pady=15)

support = Button(window, text='Support Discord', font=('Courrier', 10),bg='#ffffff', fg='#91370d', command=link_support)
support.pack(side=BOTTOM)

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Sauvegarder", command=save)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)
frame.pack()

auto_save()

window.mainloop()
