import os
from playsound import playsound

PRESIDENTE = []
GOVERNADOR = []
GOV = {}

def apuracaoGovernador():

    # Variaveis Governadores
    soma13Gov = []
    soma44 = []
    SomaNuloGov = []

    for votoGov in GOVERNADOR:
        if votoGov == 13:
            soma13Gov.append(votoGov)
        elif votoGov == 44:
            soma44.append(votoGov)
        else:
            SomaNuloGov.append(votoGov)

    print(f"""
            +----------------------------------------+
            |Apuração das Eleições 2022 - Governador |
            +----------------------------------------+
            Total de votos: {len(GOVERNADOR)}

            Agnelo: {len(soma13Gov)} votos
            Ibanes {len(soma44)} votos

            Total des votos nulos {len(SomaNuloGov)} votos

        """)
    if soma13Gov < soma44:
        print(f"""
            Governador eleito, Agnelo Silva com {len(soma13Gov)} votos válidos!
            """)
    if soma13Gov > soma44:
        print(f"""
            Governador eleito, Ibanes Rocha com {len(soma44)} votos válidos!
            """)
    exit()


def apuracaoPresidente():
    # Variaveis Presidenciais
    soma13Pres = []
    soma22 = []
    SomaNuloPres = []
    print("\n" * os.get_terminal_size().lines)

    for votoPre in PRESIDENTE:
        if votoPre == numPres:
            soma13Pres.append(votoPre)
        elif votoPre == numPres1:
            soma22.append(votoPre)
        else:
            SomaNuloPres.append(votoPre)

    print(f"""
            +----------------------------------------+
            |Apuração das Eleições 2022 - Presidente |
            +----------------------------------------+
            Total de votos: {len(PRESIDENTE)}

            {pres}: {len(soma13Pres)} votos
            {pres1} {len(soma22)} votos

            Total des votos nulos {len(SomaNuloPres)} votos
            """)
    if soma13Pres < soma22:
        print(f"""
            Presidente eleito, {pres} com {len(soma13Pres)} votos válidos!
            """)
    if soma13Pres > soma22:
        print(f"""
            Presidente eleito, {pres1} com {len(soma22)} votos válidos!
            """)


def votoGovernante():
    confirmaGov = True
    while confirmaGov:
        try:
            votoGovernador = int(input("Governador: "))
            if votoGovernador == 13:
                print("Agnelo Silva")
                confirmaGov = input(
                    "Confirma o voto [(S/s) - Sim | (N/n) - Não]? ")
                if confirmaGov.isnumeric():
                    print(
                        "Por favor entre com o valor s[S] para confirmar ou n[N] para não confirmar")
                    continue
                if confirmaGov == "s" or confirmaGov == "S":
                    governo = governador(votoGovernador)
                    print(governo)
                    confirmaGov = False
                    break

            if votoGovernador == 44:
                print("Ibaneis Rocha")
                confirmaGov = input(
                    "Confirma o voto [(S/s) - Sim | (N/n) - Não]? ")
                if confirmaGov.isnumeric():
                    print(
                        "Por favor entre com o valor s[S] para confirmar ou n[N] para não confirmar")
                    continue
                if confirmaGov == "s" or confirmaGov == "S":
                    governo = governador(votoGovernador)
                    print(governo)
                    confirmaGov = False
                    break

            if votoGovernador != 13 or votoGovernador != 22:
                print("Voto Nulo!")
                confirmaGov = input(
                    "Confirma o voto [(S/s) - Sim | (N/n) - Não]? ")
                if confirmaGov.isnumeric():
                    print(
                        "Por favor entre com o valor s[S] para confirmar ou n[N] para não confirmar")
                    continue
                if confirmaGov == "s" or confirmaGov == "S":
                    governo = governador(governador)
                    print(governo)
                    confirmaGov = False
                    break

            elif confirmaGov != "s" or confirmaGov != "S":
                print("Voce precisa confirmar seu voto!!!")
                continue
        except ValueError:
            print("Entre com um valor válido!")
            continue    

def votoPresidenciavel():
    confirmaPre = True
    while confirmaPre:
        try:
            votoPresidente = int(input("PRESIDENTE: "))
            if votoPresidente == numPres:
                print(pres)
                confirmaPre = input(
                    "Confirma o voto [(S/s) - Sim | (N/n) - Não]? ")
            # if confirmaPre.isnumeric():
            #         print(
            #             "Por favor entre com o valor s[S] para confirmar ou n[N] para não confirmar")
            #         continue
            if confirmaPre == "s" or confirmaPre == "S":
                presidenciavel = presidente(votoPresidente)
                print(presidenciavel)
                confirmaPre = False
                break

            if votoPresidente == numPres1:
                print(pres1)
                confirmaPre = input(
                    "Confirma o voto [(S/s) - Sim | (N/n) - Não]? ")
                if confirmaPre.isnumeric():
                    print(
                        "Por favor entre com o valor s[S] para confirmar ou n[N] para não confirmar")
                    continue
     
            if confirmaPre == "s" or confirmaPre == "S":
                presidenciavel = presidente(votoPresidente)
                print(presidenciavel)
                confirmaPre = False
                break

            if votoPresidente == 3333:
                PresidenteEleito = apuracaoPresidente()
                print(PresidenteEleito)
                print()
                GovernadorEleito = apuracaoGovernador()
                print(GovernadorEleito)
                break
          

            if votoPresidente != numPres1 or votoPresidente != numPres:
                print("Voto Nulo!")
                confirmaPre = input(
                    "Confirma o voto [(S/s) - Sim | (N/n) - Não]? ")
                if confirmaPre.isnumeric():
                    print(
                        "Por favor entre com o valor s[S] para confirmar ou n[N] para não confirmar")
                    continue
                if confirmaPre == "s" or confirmaPre == "S":
                    presidenciavel = presidente(votoPresidente)
                    print(presidenciavel)
                    confirmaPre = False
                    break

            elif confirmaPre != "s" or confirmaPre != "S":
                print("Voce precisa confirmar seu voto!")
                continue
        except ValueError:
            print("Entre com um valor válido!")
            continue

def presidente(voto):
    if voto == numPres or voto == numPres1:
        PRESIDENTE.append(voto)
        playsound('confirm.mp3')
        return ("""

        Voto confirmado...
        OBRIGADO!!!

            """)
    else:
        PRESIDENTE.append(voto)
        playsound('confirm.mp3')
        return "Voto Nulo Confirmado"


def governador(voto):
    if voto == 13 or voto == 44:
        GOVERNADOR.append(voto)
        playsound('confirm.mp3')
        return ("""

        Voto confirmado...
        OBRIGADO!!!

            """)

    else:
        GOVERNADOR.append(voto)
        playsound('confirm.mp3')
        return "Voto Nulo Confirmado"

if __name__ == "__main__":
    print("\n" * os.get_terminal_size().lines)
    print(f"""
                                    Eleiçoes 2022
                          Cadastro de Estados e Canditatos

    """)

    UF = input("Qual o seu estado: ")
    print()
    # Configuração Presidente
    pres = input("Nome do PRIMEIRO candidato a Presidência da República: ")
    numPres = int(input(f"Qual o numero do partido do canditato {pres}: "))
    print("\n" * os.get_terminal_size().lines)
    pres1 = input("Nome do SEGUNDO candidato a Presidência da República: ")
    numPres1 = int(input(f"Qual o numero do partido do canditato {pres1}: "))
    
    while numPres == numPres1:
            print("\n" * os.get_terminal_size().lines)    
            print("ATENÇÃO: Corrija os campos...")
            print()
            pres1 = input("Nome do SEGUNDO candidato a Presidência da República: ")
            numPres1 = int(input(f"Qual o numero do partido do canditato {pres1}: "))
    
    # Configuração Governador

    cadGov = True
    while cadGov:
        print("\n" * os.get_terminal_size().lines)  
        nome = input("Entre com o nome do governador: ")
        numero = int(input(f"Entre com o numero do governador: "))
        GOV[numero] = nome
        cad = input("Cadastra o proximo? [s/N]")
        if cad == "s" or cad == "S":
            cadGov = True
        else:
            cadGov = False
        
    while True:
        
        print("\n" * os.get_terminal_size().lines)
        print(f"""
                                        Eleiçoes 2022
            TRE - Brasil - Votos Presidente e Governador do Estado do {UF}

            """)

        votoPresidenciavel()
        votoGovernante()
