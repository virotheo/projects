from tkinter import *
import requests
import webbrowser

ip = requests.get("https://api.ipify.org").text
version = 1.0
coins = 0

# On définit un gestionnaire d'événements pour le bouton ci-dessous.
def farm():
    global coins
    coins+=5
    coins_show.config(text=coins)

def link_support():
        webbrowser.open_new("https://discord.gg/upM5gf9RxM")

def save():
      print("saved!")        


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

coins_show = Label(window, text=coins, font=('courrier', 8  ),bg='#91370d', fg='#ffffff')
coins_show.pack()
coins_show.config(text=coins)

farm_button = Button(frame, text='Farm', font=('Courrier', 25),bg='#ffffff', fg='#91370d', command=farm)
farm_button.pack(pady=25, fill=X)

support = Button(window, text='Support Discord', font=('Courrier', 10),bg='#ffffff', fg='#91370d', command=link_support)
support.pack(side=BOTTOM)

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Sauvegarder", command=save)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)
frame.pack()
window.mainloop()