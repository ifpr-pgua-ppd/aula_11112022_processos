from multiprocessing import Process, current_process
import time

class MeuProcesso(Process):

    #construtor do processo
    def __init__(self,id):
        Process.__init__(self)
        self.id = id
    
    #método de trabalho do processo
    #enquanto o método estiver executando
    #o process está vivo
    def run(self):
        #acessando o nome do processo
        nome = self.name
        print(f"{nome}...{self.id}")
        time.sleep(3)

def main():
    nome = current_process().name
    print(f"{nome} Iniciando...")
    
    #instanciando os objetos que irão representar
    #processos
    p1 = MeuProcesso(1)
    p2 = MeuProcesso(2)

    #iniciando a execução do processo
    p1.start()
    p2.start()

    #barreira de sincronização
    p1.join()
    p2.join()

    print(f"{nome} FIM!")

main()