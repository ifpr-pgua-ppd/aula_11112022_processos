from multiprocessing import Process, Queue
import random
import time

class Produtor(Process):

    def __init__(self,buffer):
        Process.__init__(self)
        self.buffer = buffer
    
    def produzir(self):
        produto = random.randint(1,1000)
        print(f"{self.name} produziu {produto}")
        self.buffer.put(produto)
        time.sleep(0.5)
    
    def run(self):
        while True:
            self.produzir()

class Consumidor(Process):
    
    def __init__(self,buffer):
        Process.__init__(self)
        self.buffer = buffer
    
    def consumir(self):
        time.sleep(random.randint(3,5))
        produto = self.buffer.get()
        print(f"{self.name} consumiu {produto}")
        
    
    def run(self):
        while True:
            self.consumir()

def main():

    buffer = Queue(maxsize=5)

    produtor = Produtor(buffer)

    consumidor1 = Consumidor(buffer)
    consumidor2 = Consumidor(buffer)
    consumidor3 = Consumidor(buffer)
    
    produtor.start()
    consumidor1.start()
    consumidor2.start()
    consumidor3.start()

main()