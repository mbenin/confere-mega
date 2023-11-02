import argparse

class MegaSena:
    def __init__(self, arquivo):
        # Carrega as apostas do arquivo
        with open(arquivo, 'r') as f:
            self.apostas = [list(map(int, linha.strip().split(','))) for linha in f.readlines()]

    def confere_numeros(self, *numeros):
        # Verifica se há 6 números passados
        if len(numeros) != 6:
            return "Por favor, insira exatamente 6 números."

        resultados = []

        # Confere cada aposta
        for aposta in self.apostas:
            acertos = len(set(numeros) & set(aposta))
            resultados.append(acertos)

        return resultados


if __name__ == "__main__":
    # Define e obtém os argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Confere números da Mega-Sena.')
    parser.add_argument('numeros', metavar='N', type=int, nargs=6,
                        help='seis números da Mega-Sena a serem conferidos')
    args = parser.parse_args()

    mega = MegaSena('apostas.txt')
    resultados = mega.confere_numeros(*args.numeros)

    for idx, acertos in enumerate(resultados, 1):
        print(f"Aposta {idx}: {acertos} acertos")
