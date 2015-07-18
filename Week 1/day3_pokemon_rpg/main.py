from pokemon import Pokemon
import random
__author__ = 'winnie'

# Just creating random Pokemon
pikachu = Pokemon("Pikachu", "Fire", 6)
charmander = Pokemon("Charmander", "Fire", 3)
wartortle = Pokemon("Wartortle", "Water", 2)

my_pokedex = {pikachu.name: pikachu, charmander.name: charmander,
           wartortle.name: wartortle}
gold = 100

def generate_pokemon():
    possible_names = ["Pigeon", "Caterpie", "Pikachu", "Charmander",
                           "Wartortle", "Psyduck", "Ditto", "Dragonite" ]
    possible_skills = ["Fire", "Water", "Earth"]
    name = random.randint(0, len(possible_names)-1)
    skill = random.randint(0, len(possible_skills)-1)
    return possible_names[name], possible_skills[skill]

def quest():
    return None

def determine_winner(pokemon, enemy):
    skills = ["Fire", "Water", "Earth"]
    if abs(pokemon.level - enemy.level)<5:
        logic = skills.index(pokemon.skill) - skills.index(enemy.skill)%3
        if logic == 2:
            print "You Lost!"
        elif logic == 1:
            print "You Won!"
        else:
            print "You Tied!"
    elif pokemon.level > enemy.level:
        return pokemon.name
    else:
        return enemy.name

def print_pokemon(my_pokedex):
    for x in my_pokedex:
        print "\t{}:  Skill is {} and Level is {}".format(x, my_pokedex[x].skill,
                                                        my_pokedex[x].level)


print "Welcome to the world of Pokemon!"
action = raw_input("Do you want to (v)iew, (t)rain or (f)ight your pokemon? ")

while action!= "q":
    if action == "v":
        print "You have the following pokemon: {}".format(my_pokedex)
        # Option to level up
    elif action == "t":

        pass
    elif action == "f":
        # generate a random enemy Pokemon
        name, skill = generate_pokemon()
        enemy = Pokemon(name=name,skill=skill, level=5)
        print "**You are fighting: {} with {} skill and level {}**\n".format(enemy.name,
                                                                       enemy.skill, enemy.level)
        # Pick a pokemon to fight
        print "\tHere are a list of your pokemon: "
        print_pokemon = print_pokemon(my_pokedex)
        pokemon = raw_input("\nWhich pokemon do you want to choose? ")

        winner = determine_winner(my_pokedex[pokemon], enemy)

        print winner
    action = raw_input("Do you want to (v)iew, (quest) or (f)ight your pokemon?")




