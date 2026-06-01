from tkinter import *
import requests
import webbrowser
import os
import time


ip = requests.get("https://api.ipify.org").text
version = 1.3
coins = 0

multiplier = 1

# -------------------------
# VARIABLES UPGRADES
# -------------------------
upgrade1_bought = False
upgrade2_bought = False
upgrade3_bought = False
upgrade4_bought = False


# creation sauvegarde si pas présent
if os.path.exists("save.txt"):
      with open("save.txt", "r") as saving:
       try:
            coins = float(saving.read())
       except:
            coins = 0
else:
     with open("save.txt", "w+") as save:
      save.write("0")


# -------------------------
# UPGRADE CHECK FIX
# -------------------------
def upgrade_available():
      if coins >= 200 and not upgrade1_bought:
          upgrade_1['state'] = "normal"

      if coins >= 1000 and not upgrade2_bought:
          upgrade_2['state'] = "normal"

      if coins >= 5000 and not upgrade3_bought:
          upgrade_3['state'] = "normal"

      if coins >= 10000 and not upgrade4_bought:
          upgrade_4['state'] = "normal"


# -------------------------
# FARM
# -------------------------
def farm():
    global coins
    coins += multiplier
    coins_show.config(text=int(coins))


# -------------------------
# SAVE
# -------------------------
def save():
      with open("save.txt", "w") as saving:
            saving.write(str(coins))


def auto_save():
      save()
      window.after(1000, auto_save)
      window.after(1000, upgrade_available)


# -------------------------
# FARM BUTTON
# -------------------------
def check_button():
    farm()


# -------------------------
# UPGRADES BUY FIX
# -------------------------
def up1():
      global coins, multiplier, upgrade1_bought
      if coins >= 500:
            coins -= 500
            multiplier = 2
            upgrade1_bought = True
            upgrade_1['state'] = 'disabled'
            coins_show.config(text=int(coins))

def up2():
      global coins, multiplier, upgrade2_bought
      if coins >= 1000:
            coins -= 1000
            multiplier = 4
            upgrade2_bought = True
            upgrade_2['state'] = 'disabled'
            coins_show.config(text=int(coins))

def up3():
      global coins, multiplier, upgrade3_bought
      if coins >= 5000:
            coins -= 5000
            multiplier = 5
            upgrade3_bought = True
            upgrade_3['state'] = 'disabled'
            coins_show.config(text=int(coins))

def up4():
      global coins, multiplier, upgrade4_bought
      if coins >= 10000:
            coins -= 10000
            multiplier = 10
            upgrade4_bought = True
            upgrade_4['state'] = 'disabled'
            coins_show.config(text=int(coins))


# -------------------------
# SUPPORT
# -------------------------
def link_support():
        webbrowser.open_new("https://discord.gg/upM5gf9RxM")


# -------------------------
# GUI
# -------------------------
window = Tk()
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)
window.title(f"Cookie Clicker V{version}")
window.config(background='#91370d')


frame = Frame(window, bg='#91370d', bd=1, relief=SUNKEN)

label_title = Label(frame, text='Cookie Clicker', font=('courrier', 50), bg='#91370d', fg='#ffffff')
label_title.pack()

footer_ip = Label(window, text=f'Your IP : {ip}', font=('courrier', 8), bg='#91370d', fg='#ffffff')
footer_ip.pack(side=BOTTOM)

coins_show = Label(frame, text=coins, font=('courrier', 8), bg='#91370d', fg='#ffffff')
coins_show.pack()


# -------------------------
# BUTTONS
# -------------------------
upgrade_1 = Button(frame, text='Buy a Kitchen (x1.25)', font=('Courrier', 5), bg='#ffffff', fg='#91370d', command=up1)
upgrade_1.pack(pady=5, side=BOTTOM)
upgrade_1['state'] = 'disabled'

upgrade_2 = Button(frame, text='Buy a Furnace (x1.5)', font=('Courrier', 5), bg='#ffffff', fg='#91370d', command=up2)
upgrade_2.pack(pady=5, side=BOTTOM)
upgrade_2['state'] = 'disabled'

upgrade_3 = Button(frame, text='Upgrade Furnace (x1.75)', font=('Courrier', 5), bg='#ffffff', fg='#91370d', command=up3)
upgrade_3.pack(pady=5, side=BOTTOM)
upgrade_3['state'] = 'disabled'

upgrade_4 = Button(frame, text='Buy Vanilla Cookie Method (x2)', font=('Courrier', 5), bg='#ffffff', fg='#91370d', command=up4)
upgrade_4.pack(pady=5, side=BOTTOM)
upgrade_4['state'] = 'disabled'


farm_button = Button(frame, text='Farm', font=('Courrier', 15), bg='#ffffff', fg='#91370d', command=check_button)
farm_button.pack(pady=15)


support = Button(window, text='Support Discord', font=('Courrier', 10), bg='#ffffff', fg='#91370d', command=link_support)
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
