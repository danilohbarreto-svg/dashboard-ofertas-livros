"""Leitura dos arquivos CSV do projeto.
"""
import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros_v2():
    
    try:
        with open(CAMINHO_LIVROS,"r", encoding="utf-8") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteeu na leitura do arquivo", error)


def ler_livros():
    livros = []
    try:
        with open(CAMINHO_LIVROS,"r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteeu na leitura do arquivo", error)
    return livros 

def ler_livros_v1():
    arquivo = None
    try:

        arquivo = open("livros.csv","r", encoding="utf-8")
        print(arquivo.read())
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteeu na leitura do arquivo", error)
    finally:
        if arquivo is not None:
            arquivo.close()


def calculo_preco_medio(livros):
    soma : float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        soma += preco_num

    preco_medio: float = soma / len(livros)
    return preco_medio

def contar_cinco_estrelas(livros):
    contador: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if nota_limpa == "five":
            contador += 1

    return contador
    

def preco_mais_caro(livros):
    preco_mais_caro: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        if preco_num > preco_mais_caro:
            preco_mais_caro = preco_num

    return preco_mais_caro


def livro_mais_caro(livros):
    
    livro_mais_caro = None
    maior_preco: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "").strip()
        preco_num: float = float(preco_original_limpo)

        if preco_num > maior_preco:
            maior_preco = preco_num
            livro_mais_caro = livro

    return livro_mais_caro






if __name__ == "__main__":
    livros = ler_livros()
    print(f"A quantidade de livros da coleção é de {len(livros)}")

    preco_medio: float = calculo_preco_medio(livros)
    print(f"O preço médio dos livros é de £{preco_medio:.2f}")

    cinco_estrelas = contar_cinco_estrelas(livros)
    print(f"A quantidade de livros com 5 estrelas é : {cinco_estrelas}")

    preco_caro: float = preco_mais_caro(livros)
    print(f"O preço do livro mais caro é: £{preco_caro:.2f}")

    livro_caro = livro_mais_caro(livros)
    print(f"O livro mais caro é: {livro_caro['titulo']} com preço de £{livro_caro['preco']}")