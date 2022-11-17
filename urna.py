import os
from playsound import playsound

PRESIDENTE = []
GOVERNADOR = []


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
        if votoPre == 13:
            soma13Pres.append(votoPre)
        elif votoPre == 22:
            soma22.append(votoPre)
        else:
            SomaNuloPres.append(votoPre)

    print(f"""
            +----------------------------------------+
            |Apuração das Eleições 2022 - Presidente |
            +----------------------------------------+
            Total de votos: {len(PRESIDENTE)}

            Lula: {len(soma13Pres)} votos
            Bolsonaro {len(soma22)} votos

            Total des votos nulos {len(SomaNuloPres)} votos
            """)
    if soma13Pres < soma22:
        print(f"""
            Presidente eleito, Luiz Inacio Lula da Silva com {len(soma13Pres)} votos válidos!
            """)
    if soma13Pres > soma22:
        print(f"""
            Presidente eleito, Jair Messias Bolsonaro com {len(soma22)} votos válidos!
            """)


def votoGovernante():
    confirmaGov = True
    while confirmaGov:
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


def votoPresidenciavel():
    confirmaPre = True
    while confirmaPre:
        votoPresidente = int(input("PRESIDENTE: "))
        if votoPresidente == 13:
            print("Luiz Inácio Lula da Silva")
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

        if votoPresidente == 22:
            print("Jair Messias Bolsonaro")
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

        if votoPresidente != 13 or votoPresidente != 22:
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


def presidente(voto):
    if voto == 13 or voto == 22:
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
    while True:
        print("\n" * os.get_terminal_size().lines)
        print("""
                                        Eleiçoes 2022
            TRE - Brasil - Votos Presidente e Governador do Estado do Distrito Federal

            """)

        votoPresidenciavel()
        votoGovernante()
