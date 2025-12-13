from NPC import *
from Castle import *
from Hero import *
from Army import *
from game_help import help


cas = Castle('dima')
hero = Hero('lol')
hero2 = Hero('im')
cas2 = Castle("vasaya")
cas.army_creation(Human, 100)
cas2.army_creation(Canon, 100)
hero.army_attack_player(cas, cas2)
hero.army_attack_npc(dragon, 1000, cas)
