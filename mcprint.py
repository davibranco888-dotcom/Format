# mcprint.py

cores = {
    "0": "\033[30m",  # preto
    "1": "\033[34m",  # azul escuro
    "2": "\033[32m",  # verde
    "3": "\033[36m",  # ciano
    "4": "\033[31m",  # vermelho
    "5": "\033[35m",  # roxo
    "6": "\033[33m",  # amarelo
    "7": "\033[37m",  # branco claro
    "8": "\033[90m",  # cinza escuro
    "9": "\033[94m",  # azul claro
    "a": "\033[92m",  # verde claro
    "b": "\033[96m",  # ciano claro
    "c": "\033[91m",  # vermelho claro
    "d": "\033[95m",  # rosa
    "e": "\033[93m",  # amarelo claro
    "f": "\033[97m",  # branco
    "r": "\033[0m"    # reset
}

def mcprint(texto):
    resultado = ""
    i = 0
    while i < len(texto):
        if texto[i] == "§" and i + 1 < len(texto):
            cor = texto[i + 1].lower()
            resultado += cores.get(cor, "")
            i += 2
        else:
            resultado += texto[i]
            i += 1
    resultado += "\033[0m"
    print(resultado)