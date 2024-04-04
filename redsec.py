import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search


def clear_screen():
    # Limpa a tela no Windows ou sistemas Unix
    os.system("cls" if os.name == "nt" else "clear")


def pesquisar_sites(wordlist_file, palavra_chave):
    palavra_chave_encontrada = False
    clear_screen()
    with open(wordlist_file, "r") as file:
        sites = file.readlines()
        for site in sites:
            site = site.strip()  # Remove espaços em branco e quebras de linha
            url = site  # Não é necessário adicionar "http://www." automaticamente
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    # Aqui você pode adicionar lógica para pesquisar algo específico na página
                    # Procurar pela palavra-chave
                    if palavra_chave.lower() in soup.get_text().lower():
                        palavra_chave_encontrada = True
                        print(
                            f"A palavra-chave '{palavra_chave}' foi encontrada em {site}"
                        )
                else:
                    print(f"Não foi possível acessar {site}")
            except Exception as e:
                print(f"Ocorreu um erro ao acessar {site}: {str(e)}")
    if not palavra_chave_encontrada:
        print(
            f"A pesquisa sobre '\033[31m{palavra_chave}\033[0m' não foi encontrada nos sites da lista. Procurando no Google..."
        )
        # Realizar uma pesquisa no Google
        for j in search(palavra_chave, num=1, stop=1, pause=2):  # Apenas 1 resultado
            print(
                f"\n\033[1mInformações sobre '\033[31m{palavra_chave}\033[0m\033[1m' baseadas na pesquisa do Google:\033[0m"
            )
            print(j)  # Imprime o primeiro resultado da pesquisa do Google


# Nome do arquivo com a lista de sites
wordlist_file = "sites.txt"

# Loop do menu
while True:
    clear_screen()
    print("\033[1m=== MENU REDSEC SUPORTE ===\033[0m")
    print("\033[94m[1] Usar suporte IA\033[0m")
    print("\033[94m[2] Sair\033[0m")
    escolha = input("\033[94m[+]:\033[0m ")

    if escolha == "1":
        clear_screen()
        palavra_chave = input("Digite oque vc esteja procurando: ")
        pesquisar_sites(wordlist_file, palavra_chave)
        input("\nPressione Enter para continuar...")
    elif escolha == "2":
        clear_screen()
        print("Obrigado por usar o programa! Até logo!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
        input("\nPressione Enter para continuar...")
