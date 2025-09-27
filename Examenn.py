import random

# Clase Entrenador
class Entrenador:
    def __init__(self, nombre=""):
        self.nombre = nombre

# Clase Pokemon
class Pokemon:
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max

    def recuperar(self):
        self.vida_actual = self.vida_max

    def muestra(self):
        print(f"Pokemon {self.nombre} | Ataque Máximo: {self.max_ataque} | "
              f"Vida Máxma: {self.vida_max} | Vida Actual: {self.vida_actual}")

entrenador1 = None
pokemon1 = None
victorias = 0
derrotas = 0

# Función para crear al entrenador y pokemon
def crearEntrenadorPokemon(num):
    if num == 1:
        nombre_entrenador = input("Ingrese nombre de su entrenador: ")
        nombre_pokemon = input("Ingrese nombre de su Pokémon: ")
    else:
        nombre_entrenador = input("Ingrese nombre del entrenador rival: ")
        nombre_pokemon = input("Ingrese nombre del Pokémon rival: ")

    e = Entrenador(nombre_entrenador)
    p = Pokemon(nombre_pokemon)

    print(f"\nSe creó al entrenador {e.nombre} con el pokemon:")
    p.muestra()
    print("----------------------------------------------------------------")
    return e, p

# Función del valor de ataque
def valorDeAtaque(pokemon):
    return random.randint(0, pokemon.max_ataque)

# Función de defender
def defender(pokemon, ataque):
    dado = random.randint(1, 6)
    if dado == 6:
        ataque = 0
        print("El ataque fue defendido")
    pokemon.vida_actual -= ataque
    if pokemon.vida_actual < 0:
        pokemon.vida_actual = 0
    return pokemon.vida_actual

# Programa principal
print("----- PELEA DE POKEMONES-----")
entrenador1, pokemon1 = crearEntrenadorPokemon(1)

while True:
    print("\n----- MENÚ -----")
    print("P) Pelear")
    print("F) Finalizar")
    opcion = input("Elija opción: ").upper()

    if opcion == "P":
        pokemon1.recuperar()

        entrenador2, pokemon2 = crearEntrenadorPokemon(2)
        turno = 1  

        while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
            if turno == 1:
                ataque = valorDeAtaque(pokemon1)
                print(f"\n{entrenador1.nombre} ataca con su Pokemon {pokemon1.nombre} (hace {ataque} de daño)")
                defender(pokemon2, ataque)
                pokemon2.muestra()
                turno = 2
            else:
                ataque = valorDeAtaque(pokemon2)
                print(f"\n{entrenador2.nombre} ataca con su Pokemon {pokemon2.nombre} (hace {ataque} de daño)")
                defender(pokemon1, ataque)
                pokemon1.muestra()
                turno = 1

        # Resultado
        if pokemon1.vida_actual > 0:
            print(f"\nGanó el entrenador {entrenador1.nombre} con su Pokemon {pokemon1.nombre}")
            victorias += 1
        else:
            print(f"\nGanó el entrenador {entrenador2.nombre} con su Pokemon {pokemon2.nombre}")
            derrotas += 1

    elif opcion == "F":
        print("\n----- JUEGO FINALIZADO -----")
        print("Nombre y Estadisticas del Pokemon Ganador:")
        pokemon1.muestra()
        print(f"Numero de encuentros ganados: {victorias}")
        print(f"Numero de encuentros perdidos: {derrotas}")
        break

    else:
        print("Opción no válida, intente de nuevo.")