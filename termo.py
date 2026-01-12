from rich import print
from rich.prompt import Prompt, IntPrompt

# ====== PROGRAMA BASEADO NO TERMO ========
import random
import time

#Funcão que busca uma palavra na lista (Por enquanto sem banco de dados)
def buscarPalavra(lista, dicionarioContagemLetras, contagemComp):
    num = random.randint(0, (len(lista)-1))
    palavraAleatoria = lista[num]
    listaLetrasPalavra = []
    for y in range(len(palavraAleatoria)):
        LetraSemAcento = verificarAcentos(palavraAleatoria[y])
        listaLetrasPalavra.append(LetraSemAcento)
    
    palavraRecebida = "".join(listaLetrasPalavra)
    
    dicionarioContagemLetras.update({
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
    "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
    "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0
})
    contagemComp.update({
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
    "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
    "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0
})
    verificarQuantidadeDasLetras(palavraRecebida, dicionarioContagemLetras)
    return palavraRecebida

#Funcão Que analisa se a letra da palavra está presnete na Palavra CERTA
def existeLetra(letraDigitada, palavraCerta, contLetra, contLetraComp):
    for indice in range(0, len(palavraCerta)):
        
        if(palavraCerta[indice].lower() == letraDigitada.lower() and contLetra[letraDigitada] > contLetraComp[letraDigitada]):
            return "[bold yellow]Posição Errada[/bold yellow]"
        else:
            continue
    return "[bold red]Não Tem[/bold red]"

#Faz a Verificação se a Letra está no Lugar Certo ou Não
def letra(palavraCerta, palavraDigitada, indiceLetra, contLetra, contLetraComp):
    
    
    letraCorreta = palavraCerta[indiceLetra].lower()
    letraDigitada = palavraDigitada[indiceLetra].lower()
    
    letraDigitada = verificarAcentos(letraDigitada)
        
    if(letraCorreta == letraDigitada):
        return "[bold green]No Lugar Certo[/bold green]"
    else:
        Mensagem = existeLetra(letraDigitada, palavraCerta, contLetra, contLetraComp)
        return Mensagem

def verificarQuantidadeDasLetras(palavraCerta, dicionarioContagemLetras):
    for indice in range(len(palavraCerta)):
        dicionarioContagemLetras.update({palavraCerta[indice].lower(): dicionarioContagemLetras[palavraCerta[indice].lower()] + 1})

def verificarAcentos(letraDigitada):
    if(letraDigitada == "á" or letraDigitada == "à" or letraDigitada == "â" or letraDigitada == "ã"):
        return "a"
    elif(letraDigitada == "é" or letraDigitada == "è" or letraDigitada == "ê"):
        return "e"
    elif(letraDigitada == "í" or letraDigitada == "ì" or letraDigitada == "î"):
        return "i"
    elif(letraDigitada == "ó" or letraDigitada == "ò" or letraDigitada == "ô" or letraDigitada == "õ"):
        return "o"
    elif(letraDigitada == "ú" or letraDigitada == "ù" or letraDigitada == "û"):
        return "u"
    elif(letraDigitada == "ç"):
        return "c"
    else:
        return letraDigitada
#Lista de Palavras Possíveis
lista = []

with open("palavras.txt", "r", encoding="utf-8") as arquivoPalavras:
    for linha in arquivoPalavras:
        linha_Formatada = linha.strip()
        if(len(linha_Formatada) == 5):
            lista.append(linha_Formatada)

contagemLetras = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
    "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
    "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0
}
contagemLetrasComparacao = contagemLetras.copy()

opcao = 0 #Zerando a Opcção

palavraCerta = buscarPalavra(lista, contagemLetras, contagemLetrasComparacao) # Define a Palavra antes de Começar o While
listaMensagensLetras = []
listaLetras = []
while (opcao != 4):
    
    print("[bold blue]=========== TERMO ===========[/bold blue]")
    time.sleep(1.5)
    print("1 - JOGAR")
    time.sleep(0.5)
    print("2 - DESISTIR")
    time.sleep(0.5)
    print("3 - MUDAR A PALAVRA")
    time.sleep(0.5)
    print("4 - SAIR")
    print()
    time.sleep(1.25)
    
    opcao = int(input("Escolha uma Opção: "))
    time.sleep(2)
    
    if(opcao < 1 or opcao > 4):
        print("[bold red]DIGITE UM VALOR VÁLIDO!!! OU NÃO SABE LER??!![/bold red]")
        continue
    elif(opcao == 1):
        contagemLetrasComparacao = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
            "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
            "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
            "y": 0, "z": 0
        }
        palavra = Prompt.ask("Digite uma Palavra de [bold blue](5 LETRAS) (NÃO USE ACENTOS)[/bold blue]")
        #palavra = input("Digite uma Palavra de *(5 LETRAS)* *(NÃO USE ACENTOS)*: ")
        
        if(len(palavra) == 5):
            if(palavra.lower() == palavraCerta.lower()):
                print()
                print()
                time.sleep(1)
                print("[italic green]PARABÉEENS!!! VOCÊ ACERTOU!!![/italic green]")
                print()
                time.sleep(1)
                print("[bold blue]Temos Mais uma Rodada Para Você![/bold blue]")
                palavraCerta = buscarPalavra(lista, contagemLetras, contagemLetrasComparacao)
                print()
            else:
                for iLetra in range(0, len(palavra)):
                    
                    MensagemLetra = letra(palavraCerta, palavra, iLetra, contagemLetras, contagemLetrasComparacao)
                    listaMensagensLetras.insert(iLetra, MensagemLetra)
                    LetraFinal = verificarAcentos(palavra[iLetra])
                    listaLetras.insert(iLetra, LetraFinal)
                    contagemLetrasComparacao.update({LetraFinal.lower(): contagemLetrasComparacao[LetraFinal.lower()] + 1})
                    
                print()
                for x in range(0, len(listaMensagensLetras)):
                    time.sleep(1)
                    print(f"[bold blue]{listaLetras[x]}[/bold blue]  -  [bold]{listaMensagensLetras[x]}")
                listaLetras.clear()
                listaMensagensLetras.clear()
                
            continue
        else:
            print("[bold red]Valor Inválido[/bold red]")
            print()
            continue
    
    elif(opcao == 2):
        print()
        opcaoCerteza = 0
        while(opcaoCerteza != 1 or opcaoCerteza != 2):
            opcaoCerteza = IntPrompt.ask("Você Tem Certeza: [bold green]1- Sim[/bold green] | [bold red]2 - Não[/bold red]: ")
            if(opcaoCerteza == 1):
                print()
                time.sleep(1)
                print(f"A Palavra era *[bold blue]{palavraCerta}[/bold blue]*")
                print()
                time.sleep(0.5)
                print("VocÊ Saiu!!")
                opcao = 4
                break
            
            elif(opcaoCerteza == 2):
                
                break
            
            else:
                print("[bold red]DIGITE ALGO VÁLIDO!!!![/bold red]")
                continue
        continue

    elif(opcao == 3):
        # Realizando Novo Jogo
        time.sleep(0.5)
        print(f"A Palavra Certa era *[bold blue]{palavraCerta}[/bold blue]*")
        palavraCerta = buscarPalavra(lista, contagemLetras, contagemLetrasComparacao)
        
        print()
        time.sleep(0.5)

        print("Nova Palavra Já Disponível")
        print()
        print()
        continue
    
    elif(opcao == 4):
        print()
        print("VOCÊ SAIU DO PROGRAMA!!!! Obrigado pela Jogatina")
        break