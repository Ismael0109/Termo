# ====== PROGRAMA BASEADO NO TERMO ========

from rich import print
from rich.prompt import Prompt
import random, time

'''
Busca uma palavra aleatória numa Lista de Palavras, reseta os contadores de letras tanto da palavra certa, quanto da palavra comparação.
Retorna a palavra a palavra sem acentos 
list, dict, dict -> str
'''
def buscarPalavra(lista_palavras, dict_contagem_letras_da_palavra, dict_contagem_letras_comparacao):
    num = random.randint(0, (len(lista_palavras)-1))
    palavra_aleatoria = str.lower(lista_palavras[num])
    letras_da_palavra = []
    for letra in palavra_aleatoria:
        letra_sem_acento = verificarAcentos(letra)
        letras_da_palavra.append(letra_sem_acento)
    
    palavra_recebida = "".join(letras_da_palavra)
    
    resetar_contagem(dict_contagem_letras_da_palavra)
    resetar_contagem(dict_contagem_letras_comparacao)
    
    verificarQuantidadeDasLetras(palavra_recebida, dict_contagem_letras_da_palavra)
    return palavra_recebida

'''
Verifica se a letra pertence a palavra e retorna uma mensagem indicando se está na posição errada ou se não há
str, str, dict, dict -> str
'''
def existeLetra(letra_digitada, palavra_certa, contador_letra, contador_letra_comparacao):
    for letra_certa in palavra_certa:
        
        if(letra_certa == letra_digitada and contador_letra[letra_digitada] > contador_letra_comparacao[letra_digitada]):
            return "[bold yellow]Posição Errada[/bold yellow]"
        else:
            continue
    return "[bold red]Não Tem[/bold red]"



'''
Verifica e Atualiza a quantidade de cada letra individualente na palavra, aplicando os valores no dicionário de contagem
str, dict -> None
'''

def verificarQuantidadeDasLetras(palavra, dicionario_contagem_letras):
    for letra in palavra:
        dicionario_contagem_letras.update({
            letra: dicionario_contagem_letras[letra] + 1})

'''
Verifica se a letra tem algum tipo de acento presente na língua portuguesae converte na letra original
str -> str
'''
def verificarAcentos(letra_digitada):
    if letra_digitada in ("á", "à", "â", "ã"):
        return "a"
    elif letra_digitada in ("é", "è", "ê"):
        return "e"
    elif letra_digitada in ("í", "ì", "î"):
        return "i"
    elif letra_digitada in ("ó", "ò", "ô", "õ"):
        return "o"
    elif letra_digitada in ("ú", "ù", "û"):
        return "u"
    elif (letra_digitada == "ç"):
        return "c"
    else:
        return letra_digitada
'''
Atualiza o dicionário da contagem de letras "zerando"
dict -> None
'''

def resetar_contagem(dicionario_contagem):
    dicionario_contagem.update({
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
    "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
    "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0
    })

#Lista de Palavras Possíveis
lista_palavras = []
#Abertura do arquivo externo de palavras e adicioná-las a lista
with open("palavras.txt", "r", encoding="utf-8") as arquivoPalavras:
    for linha in arquivoPalavras:
        linha_Formatada = linha.strip()
        if(len(linha_Formatada) == 5):
            lista_palavras.append(linha_Formatada)

contagemLetras = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
    "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
    "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0
}
contagemLetrasComparacao = contagemLetras.copy()

opcao = "0" #Zerando a Opcção

palavraCerta = buscarPalavra(lista_palavras, contagemLetras, contagemLetrasComparacao) # Define a Palavra antes de Começar o While
listaMensagensLetras = [""] * 5
listaLetras = [""] * 5
while (opcao != "4"):
    
    print("[bold blue]=========== TERMO ===========[/bold blue]")
    time.sleep(0.5)
    print("1 - JOGAR")
    time.sleep(0.2)
    print("2 - DESISTIR")
    time.sleep(0.2)
    print("3 - MUDAR A PALAVRA")
    time.sleep(0.2)
    print("4 - SAIR\n")
    time.sleep(0.5)
    
    opcao = input("Escolha uma Opção: ")
    time.sleep(0.5)
    
    if(opcao not in ("1", "2", "3", "4")):
        print("[bold red]DIGITE UM VALOR VÁLIDO!!![/bold red]")
        continue
    elif(opcao == "1"):
        resetar_contagem(contagemLetrasComparacao)
        palavra = str.lower(Prompt.ask("Digite uma Palavra de [bold blue](5 LETRAS) (NÃO USE ACENTOS)[/bold blue]"))
        
        
        if(len(palavra) == 5):
            if(palavra == palavraCerta):
                time.sleep(0.25)
                print("\n\n[italic green]PARABÉEENS!!! VOCÊ ACERTOU!!![/italic green]\n")
                
                time.sleep(0.25)
                print("[bold blue]Temos Mais uma Rodada Para Você![/bold blue]\n")
                palavraCerta = buscarPalavra(lista_palavras, contagemLetras, contagemLetrasComparacao)
            else:
                
                verificacao_letras_certas = [False] * 5
                for i in range(len(palavra)):
                    l = verificarAcentos(palavra[i])
                    if l == verificarAcentos(palavraCerta[i]):
                        verificacao_letras_certas[i] = True
                        listaMensagensLetras[i] = "[bold green]No Lugar Certo[/bold green]"
                        
                        listaLetras[i] = l
                    
                        contagemLetrasComparacao.update({
                            l: contagemLetrasComparacao[l] + 1
                        })

                for i in range(len(palavra)):
                    if not verificacao_letras_certas[i]:
                        letra_final = verificarAcentos(palavra[i])
                        mensagem_letra = existeLetra(letra_final,palavraCerta, contagemLetras, contagemLetrasComparacao)
                        listaMensagensLetras[i] = mensagem_letra
                        
                        listaLetras[i] = letra_final
                        
                        contagemLetrasComparacao.update({
                            letra_final: contagemLetrasComparacao[letra_final] + 1
                        })
                        
                for x in range(len(listaMensagensLetras)):
                    time.sleep(0.5)
                    print(f"[bold blue]{str.upper(listaLetras[x])}[/bold blue]  -  [bold]{listaMensagensLetras[x]}")
                listaLetras.clear()
                listaMensagensLetras.clear()
                listaLetras = [""]*5
                listaMensagensLetras = [""]*5
                
            continue
        else:
            print("[bold red]Valor Inválido[/bold red]\n")
            continue
    
    elif(opcao == "2"):
        opcaoCerteza = "0"
        while True:
            opcaoCerteza = Prompt.ask("\nVocê Tem Certeza: [bold green]1- Sim[/bold green] | [bold red]2 - Não[/bold red] ")
            if(opcaoCerteza == "1"):
                time.sleep(0.5)
                print(f"\nA Palavra era *[bold blue]{palavraCerta}[/bold blue]*")
                time.sleep(0.25)
                print("\nVocê Saiu!! Obrigado por Tentar!")
                opcao = "4"
                break
            
            elif(opcaoCerteza == "2"):
                
                break
            
            else:
                print("\n[bold red]DIGITE ALGO VÁLIDO!!!![/bold red]")
                continue
        continue

    elif(opcao == "3"):
        # Realizando Novo Jogo
        time.sleep(0.5)
        print(f"A Palavra Certa era *[bold blue]{palavraCerta}[/bold blue]*")
        palavraCerta = buscarPalavra(lista_palavras, contagemLetras, contagemLetrasComparacao)
        
        time.sleep(0.5)

        print("\nNova Palavra Já Disponível\n\n")
        
        continue
    
    elif(opcao == "4"):
        print("\nVOCÊ SAIU DO PROGRAMA!!!! Obrigado pela Jogatina")
        break