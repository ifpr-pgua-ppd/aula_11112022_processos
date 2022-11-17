from threading import Thread
from multiprocessing import Process

class MinhaThread(Thread):

    def __init__(self,lista):
        Thread.__init__(self)
        self.lista = lista

    
    def run(self):
        for a in range(5,10,1):
            self.lista.append(a)
        
        print(f"{self.name} {self.lista}")

class MeuProcesso(Process):

    def __init__(self,lista):
        Process.__init__(self)
        self.lista = lista

    
    def run(self):
        for a in range(5,10,1):
            self.lista.append(a)
        
        print(f"{self.name} {self.lista}")

def main():

    print("Main...(Thread)")
    lista = [1,2,3,4]
    print(f"Main...(Thread){lista}")
    t1 = MinhaThread(lista)
    t1.start()
    t1.join()
    print(f"Main...(Thread){lista}")

    print("Main...(Process)")
    lista = [1,2,3,4]
    print(f"Main...(Process){lista}")
    p1 = MeuProcesso(lista)
    p1.start()
    p1.join()
    print(f"Main...(Process){lista}")

main()