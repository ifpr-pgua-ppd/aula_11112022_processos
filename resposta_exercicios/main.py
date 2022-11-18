from produtor import Produtor
from consumidor import Consumidor
from multiprocessing import Queue

def main():

    buffer = Queue(maxsize=2)
    arquivoEntrada = "entrada.txt"

    produtor = Produtor(buffer,arquivoEntrada)
    consumidor = Consumidor(buffer)

    produtor.start()
    consumidor.start()

    produtor.join()
    consumidor.join()

    print("Fim")

main()