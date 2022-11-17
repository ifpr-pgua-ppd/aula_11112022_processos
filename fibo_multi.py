
import concurrent.futures
import time
import sys

def fibo(n):
    if(n>1):
        return fibo(n-1)+fibo(n-2)
    return n

def main():

    inicio = time.time()
    n_processos = int(sys.argv[1])
    n_elementos = int(sys.argv[2])

    executor = concurrent.futures.ProcessPoolExecutor(max_workers=n_processos)

    #submetendo as tarefas
    respostas = []
    for n in range(n_elementos):
        processo = executor.submit(fibo,n=n)
        respostas.append(processo)
    
    #iniciando a execução e aguardando a finalização
    executor.shutdown(wait=True)

    #processando as respostas de cada execução
    #e armazenando o resultado em uma lista
    elementos = []
    for resp in concurrent.futures.as_completed(respostas):
        elementos.append(resp.result())
    
    #ordenando os elementos
    elementos = sorted(elementos)
    print(elementos)
    fim = time.time()
    
    print(f"Tempo total:{fim-inicio}")

main()