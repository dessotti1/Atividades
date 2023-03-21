def is_fibonacci(n):

  fib = [0, 1]
  
  while fib[-1] < n:
      fib.append(fib[-1] + fib[-2])
  
  for elem in fib:
    if elem == n:
      return True
  
  return False

num = int(input("Digite um número: "))

if is_fibonacci(num):
  print("Esse número pertence à sequência de Fibonacci.")
  
else:
  print("Esse número não pertence à sequência de Fibonacci.")
  
