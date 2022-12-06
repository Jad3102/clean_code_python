lista_idades = []
idades = 0

def verificar():
    if media < 18:
        print("Sua turma é Jovem!")

    elif 18 < media < 60:
        print("Sua turma é Adulta")

    else:
        print("Sua turma é Idosa!")


def mostrar_mostar_resultados():
    print(45 * "_")
    print(f"A média de idades da turma é: {media}.\n"
        f"Sendo a maior idade: {maior_idade}.\n"
        f"E a menor idade: {menor_idade}.")
    print(f"As idades digitadas foram: {lista_idades}")
    print(45 * "_")

for x in range(4):
        lista_idades.append(int(input("Digite a idade de um aluno:")))
        media = sum(lista_idades) / len(lista_idades)
        maior_idade = max(lista_idades)
        menor_idade = min(lista_idades)
        
verificar()
mostrar_mostar_resultados()


