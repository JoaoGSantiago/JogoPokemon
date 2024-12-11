import pickle

from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print("ola {}, voce podera esocolher o seu primeiro pokemon".format(player))

    pokemon1 = PokemonEletrico("Pikachu", level =1)
    pokemon2 = PokemonFogo("Charmander", level = 1)
    pokemon3 = PokemonAgua("Squirtle", level = 1)


    print("escolha apenas 1:")
    print("1 - ", pokemon1)
    print("2 - ", pokemon2)
    print("3 - ", pokemon3)

    while True:
        escolha = input("escolha seu pokemon: ")

        if escolha == "1":
            player.capturar(pokemon1)
            break
        
        elif escolha == "2":
            player.capturar(pokemon2)
            break

        elif escolha == "3":
            player.capturar(pokemon3)
            break
        
        else:
            print("escolha invalida")


def salvar(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("jogo salvo com sucesso")
    except Exception as error:
        print("erro ao salvar o jogo")
        print(error)

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("jogo carregado com sucesso")
            return player
    except Exception as error:
        print("save nao encontrado")
        


if __name__ == "__main__":
    print("-------------------------------")
    print("bem vindo ao game pokemon RPG")
    print("-------------------------------")
    
    player = carregar_jogo()

    if not player:

        nome = input("qual é o seu nome?: ")
        
        player = Player(nome)

        print("ola {}, esse é um mundo habitado por pokemons, a partir de agora sua missão é capturar pokemons e derrotar seus inimigos".format(player))
        
        if player.pokemons:
            print("voce atualmente tem esses pokemons: ")
            player.mostrar_pokemons
        else:
            print("voce nao tem nenhum pokemon, voce tera que escolher um")
            escolher_pokemon_inicial(player)

        print("Pronto, agora enfrente seu primeiro inimigo")

        inimigo1 = Inimigo(nome = "Gary", pokemons = [PokemonAgua("Squirtle", level = 1)])

        player.batalhar(inimigo1)

        salvar(player)

    while True:
        print("----------------------------")
        print("1 - explorar o mundo")
        print("2 - batalhar com um inimgo")
        print("3 - mostrar dinheiro")
        print("4 - mostrar pokemon")
        print("5 - salvar jogo")
        print("0 - sair do jogo")
        escolha = input("escolha o que quer fazer agora: ")
        print("----------------------------")

        if escolha == "0":
            print("fechando o jogo")
            break
        elif escolha == "1":
            player.explorar()

        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)

        elif escolha == "3":
            player.mostrar_dinheiro()

        elif escolha == "4":
            player.mostrar_pokemons()
            
        elif escolha == "5":
            salvar(player)
            

        else:
            print("escolha invalida")
