from NPC import *
from Castle import *
from Hero import *
from Army import *

#объекты классов NPC и Army уже готовые
#в замке создается армия за деньги (уничтожение армии приводит к уничтожение замка => проигрыш)
#Герой может: сам атаковать npc(метод attack_npc), атаковать npc с армией из замка(army_attack_npc) и атаковать армию другого игрока(army_attack_player)
#в методе unit_type класса Castle есть 3 варианта: Human, Giant, Canon
#NPC: skeleton, dragon, goblin
cas = Castle('dima')
hero = Hero('lol')
hero2 = Hero('im')
cas2 = Castle("vasaya")
cas.army_creation()