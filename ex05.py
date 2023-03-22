string = input("Insira uma string: ")

string_invertida = ""
tam = len(string)

for i in range(tam - 1, -1, -1):
  string_invertida += string[i]

print("Sua string invertida: {}".format(string_invertida))
