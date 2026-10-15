import time
# V0

def terminal():
    path = '/'
    paths = []
    while True:
        response = input("user$ ")
        parts = response.split()
        if response == 'exit':
            time.sleep(0.5)
            print("bye")
            time.sleep(1)
            break
        if response == 'pwd':
            print(f'path : {path}')
        if len(parts) == 2 and parts[0] == 'cd':
            path = str(path) + str(parts[1])

terminal()            
