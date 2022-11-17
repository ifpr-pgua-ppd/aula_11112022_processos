import multiprocessing
import time

def func(id):
    nome = multiprocessing.current_process().name
    print(f"{nome}...{id}")
    time.sleep(30)

def main():
    nome = multiprocessing.current_process().name
    print(f"{nome} - INICIANDO!!")

    #criando processos com a função de trabalho e os parâmetros
    p1 = multiprocessing.Process(target=func,args=(1,))
    p2 = multiprocessing.Process(target=func,args=(2,))

    #iniciando os processos
    p1.start()
    p2.start()

    #barreira de sincronização
    p1.join()
    p2.join()

    print(f"{nome} - FIM!!")

if __name__ == "__main__":
    main()