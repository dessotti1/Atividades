import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

valores = []
for dado in dados:
    dia = dado['dia']
    valor = dado['valor']
    
    valores.append(valor)

maior_faturamento = max(valores)

faturamento_dias_trabalhados = []
soma = 0
dias_trabalhados = 0

for elem in valores:
  if elem != 0:
    faturamento_dias_trabalhados.append(elem)
    soma = soma + elem
    dias_trabalhados = dias_trabalhados + 1

menor_faturamento = min(faturamento_dias_trabalhados)
media = soma / dias_trabalhados

dias_acima_da_media = 0
for elem in valores:
  if elem > media:
    dias_acima_da_media = dias_acima_da_media + 1

print("Dentre os dias trabalhados:\n Maior faturamento diário: {}\n Menor faturamento diário: {}\n Total de dias que o faturamento diário superou a média mensal: {}".format(maior_faturamento, menor_faturamento, dias_acima_da_media))
