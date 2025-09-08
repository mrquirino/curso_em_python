# Cirando uma tupla
carros = ("Fusca", "Civic", "Corolla")

# Acessadno elementos
print(carros[0]) # Fusca

# Tentar modificar uma tupla gera erro
# carros[0] = "Ferrari" # Isso causará um erro!

carros = carros + ("Ferrari",)
print(carros) 

# slicing (possível em listas, tuplas e strings)
print(carros[2:]) #('Corolla', 'Ferrari')