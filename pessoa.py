import random


from pokemon import *

NOMES = [
    "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
    "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"
]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp"),
]



class Pessoa:
    
    def __init__(self, nome=None, pokemons=[], dinheiro = 100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

        
    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("pokemon de ", self)
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
            
        else:
            print("{} nao tem pokemon".format(self))


    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("inimigo tem nenhum pokemon")     


    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print("um pokemon selvagem apareceu: {}".format(pokemon))
            
            escolha = input("deseja explorar pokemon? (s/n): ")

            if escolha == "s":
                if random.random() >= 0.65:
                    self.capturar(pokemon)
                    print("pokemon capturado")
                else:
                    print("{} fugiu".format(pokemon))

            else:
                print("pokemon fugiu")


        else:
            print("essa exploração deu em nada")

    
    def mostrar_dinheiro(self):
        print("voce possui ${} em sua conta".format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("voce ganhou ${}".format(quantidade))
        self.mostrar_dinheiro()
            
     
    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        meu_pokemon = self.escolher_pokemon()

        
        if meu_pokemon and pokemon_inimigo:
            while True:
                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    print("{} ganhou a batalha".format(self))
                    break
                
                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break
        else:
            print("Essa batalha não pôde ocorrer")
        

        


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemons):
        self.pokemons.append(pokemons)
        print("{} capturou {}".format(self, pokemons))

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = input("escolha seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("jogador escolheu {}".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("escolha invalida")
        else:
            print("Esse jogador não possui pokemon")        

        



class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1,6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))
                
            super().__init__(nome = nome, pokemons = pokemons_aleatorios)
    
        else:
            super().__init__(nome = nome, pokemons = pokemons)
    