from arrays.py

algo = Array(10)
print(algo.get_item(333))
algo.set_item(555,3)
print(algo.get_item(3))
print(f"El arreglo tiene {algo.get_length()}elementos")
algo.clear(777)
print(algo.get_item(3))
print("-----------------------------------")
for x in algo:
  print(x)
print("____Prueba de iterador___")
for x in range(algo.get_length()):
  print(x "->" algo.set_item(555,3))
