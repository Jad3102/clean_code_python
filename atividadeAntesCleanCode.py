x = 1
idades = list()
while x < 40:
 
lista_idades = (input("Digite a idade de um aluno:")
)
 
x = x + 1
 
if lista_idades == 'fim'
:
 
break
 
else:
 
print(
'
.
.
.
'
)
 
idades.append(int(lista_idades)
)
 
media = sum(idades) / len(idades)
 
maior_idade = max(idades)
 
menor_idade = min(idades)
print(45 * "
_
")
print("A média de idades da turma é: {}.\n"
 
"Sendo a maior idade: {}.\n"
 
"E a menor idade: {}.".format(media, maior_idade, menor_idade)
)
print(45 * "
_
")
print("As idades digitadas foram:", idades)
print(45 * "
_
")
if media < 18:
 
print("Sua turma é Jovem!")
elif media > 18 and media < 60:
 
print("Sua turma é Adulta")
elif 60 <= media:
 
print("Sua turma é Idosa!"