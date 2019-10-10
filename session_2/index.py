import time

class Timer():
    def __init__(self):
        self.seconds = 10
    
    def tick(self):
        self.seconds -= 1
    
    def start(self):
        while (self.seconds > 0):
            print(self.seconds)
            time.sleep(1)
            self.tick()
    
    def reset(self):
        self.seconds = 10

clock = Timer()
while True:
    command = input("Moi ban nhap lenh: ")
    if (command == "start"):
        clock.start()
        print("Het gio")
    elif (command == "reset"):
        clock.reset()
    elif (command == "exit"):
        break
    else:
        print("Lenh khong hop le")
