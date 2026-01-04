from NPC import NPC, npc_stats, skeleton, dragon, goblin
from Player import Player
from Castle import castle_start_stats, Castle
from Hero import Hero, start_hero_stats
from Army import Army, Human, Giant, Canon
from game_help import help
import time

#чтобы посмотреть документацию, вызовите функцию help()
help()
npc_stats()
castle_start_stats()

pl1 = Player('p1')
cas1 = Castle('cas1')
hero1 = Hero('hero1')

pl2 = Player('p2')
cas2 = Castle('cas2')
hero2 = Hero('hero2')

help()
cas1.army_creation(Giant, 450)
cas2.army_creation(Canon, 500)
hero1.army_attack_player(cas1, cas2)
# hero1.army_attack_npc(goblin, 20, cas1)