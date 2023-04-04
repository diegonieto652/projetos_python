

lista = {}

while True:
    nome_candidato = input('nome do candidato: ')
    if nome_candidato == '00':
        break
    nota = input(f'nota candidato(a) {nome_candidato}: ')
    lista.update({f'{nome_candidato}': f'{nota}'})


listadict_ordenado = dict(sorted(lista.items(), key=lambda item: float(item[1]), reverse=True))

print(listadict_ordenado)

a = 0
for chave, valores in listadict_ordenado.items():
    a = a + 1
    print(f'{a} - {chave} --> {listadict_ordenado[chave]}')