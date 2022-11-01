"""Aluno: Marcus Vinicius Alves Nogueira

 - Para entender o que faz o algorítmo, leia o arquivo README.md no GitHub.
"""


def medir_tempo(tempo):

    print("\n")  # espaçamento

    ampulheta1 = 3  # Minutos
    ampulheta2 = 5  # Minutos

    # Caso 1: Multiplo de 3 (A)
    if tempo % ampulheta1 == 0:
        print("Utilize a Ampulheta A (3min)")
        if tempo != 3:
            print(f"Faça esse Processo {int(tempo / ampulheta1)} vezes")
    # Caso 2: Multiplo de 5 (B)
    elif tempo % ampulheta2 == 0:
        print("Utilize a Ampulheta B (5min)")
        if tempo != 5:
            print(f"Faça esse Processo {int(tempo / ampulheta2)} vezes")
    # Caso 3: Multiplo de 8 (A+B)
    elif tempo % (ampulheta1 + ampulheta2) == 0:
        print("Utilize a Ampulheta A (3min)")
        print("Ao acabar, Utilize a Ampulheta B (5min)")
        if tempo != 8:
            print(
                f"Faça esse processo {int(tempo/(ampulheta1 + ampulheta2))} vezes")

    # Caso 4: k.3 + 1 = x
    elif (tempo - 1) % 3 == 0:
        print("Utilize as duas ampulhetas ao mesmo tempo")
        print("Quando a Ampulheta A (3min) terminar, faltará 2 minutos em B (5min)")
        print("Inicie A (3min) novamente, quando os 2 minutos de B restante terminar, A terá 1 minuto restante ")
        if tempo != 1:
            print(
                f"Utilize o resto de A mais {int((tempo - 1) / 3)} vezes a ampulheta A para medir o tempo")
        else:
            print("Utilize o resto de A")

    # Caso 5: k.3 + 2 = x
    elif (tempo - 2) % 3 == 0:
        print("Utilize as duas ampulhetas ao mesmo tempo")
        print("Quando a ampulheta A (3min) terminar, faltará 2 minutos em B (5min)")
        if tempo != 2:
            print(
                f"Utilize o resto de B mais {int((tempo - 2) / 3)} vezes a ampulheta B para medir o tempo")
        else:
            print("Utilize o resto de B")


while True:
    print("""
  - Utilizando as seguintes ampulhetas, qual tempo você deseja medir?
  [A] Ampulheta de 3 Minutos
  [B] Ampulheta de 5 Minutos

  [!] Informe o número 0 para sair do programa.
  """)

    time_requested = int(input("Informe o Tempo em minutos: "))

    if time_requested < 1:
        print("- Você não precisa desse algorítimo para medir isso, até mais!")
        break

    medir_tempo(time_requested)
