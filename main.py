from processo import Processo
from regiao_critica import RegiaoCritica
from random import randint, shuffle


if __name__ == '__main__':

    arquivo = open("resultado.txt", "w")

    for q in range(200):
        # criação de processos e ordenando aleatoriamente
        fila_processos = [Processo(F"Processo {i + 1}", i, [randint(1, 100) for _ in range(10)]) for i in range(10)]
        shuffle(fila_processos)

        # adicionando/removendo na região crítica
        regiao = RegiaoCritica()

        for processo in fila_processos:
            if processo.pid < 5:
                try:
                    for valor in processo.array:
                        regiao.vetor_add(valor)
                        print(F"{processo.nome} adicinou {valor} na posição {len(regiao.vetor)}", file=arquivo)
                except IndexError as e:
                    print(F"Impossível adicinoar: {e.args}", file=arquivo)
            else:
                for _ in range(len(processo.array)):
                    try:
                        print(F"Processo {processo.nome} removeu o valor {regiao.vetor[-1]}", file=arquivo)
                        regiao.vetor_rem()
                    except IndexError as e:
                        print(F"Impossível {processo.nome} remover: {e}", file=arquivo)

        # exibir elementos da fila
        if regiao.vetor:
            print(F"\nElementos da região crítica: {regiao.vetor}", file=arquivo)
            print(F"Total: {len(regiao.vetor)} elementos", file=arquivo)
        else:
            print("A região crítica está vazia!", file=arquivo)
