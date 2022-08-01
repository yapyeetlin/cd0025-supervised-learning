from threading import Thread
from time import sleep
from datetime import datetime 



class thread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.returnVariable = None
        self.counter = 0

    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                self.returnVariable = read_socket(self.returnVariable)
            except KeyboardInterrupt:
                break
        print("Stopping " + self.name)

def read_socket(counter):
    print(f"{datetime.now()} - {counter}")
    sleep(2)
    if not counter: return 1
    else: return counter +1



# Create new threads
thread1 = thread("Thread-1")

# Start new Threads
thread1.start()

sleep(30)
print(thread1.returnVariable)
print ("Exiting Main Thread")
