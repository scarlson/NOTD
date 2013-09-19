import time
import random
from models.Notd import Board

print 'board setup:',
t = time.time()
b = Board(width=10,height=10)
print "%.3f" % (time.time()-t)

players = [
"Adrian",
"Adriana",
"Alejandra",
"Alejandro",
"Alex",
"Alma",
"Ana",
"Andrea",
"Andres",
"Angel",
"Brenda",
"Carlos",
"Cesar",
"Christian",
"Cynthia",
"Daniel",
"Daniela",
"David",
"Diana",
"Eduardo",
"Elizabeth",
"Erika",
"Fernanda",
"Fernando",
"Francisco",
"Gabriela",
"Ivan",
"Javier",
"Jesus",
"Jonathan",
"Jorge",
"Jose",
"Juan Carlos",
"Karla",
"Laura",
"Liliana",
"Luis",
"Maria",
"Mariana",
"Melissa",
"Miguel",
"Natalia",
"Oscar",
"Paola",
"Paulina",
"Roberto",
"Rodrigo",
"Samantha",
"Sandra",
"Sofia"]

print 'adding players',
t = time.time()
while len(b.players) < 4:
    player = random.choice(players)
    b.add_player(player)
print "%.3f" % (time.time()-t)

print 'adding zombies',
t = time.time()
while len(b.npcs) < 20:
    b.add_zombie()
print "%.3f" % (time.time()-t)

def valid_f():
    z = []
    for i in range(500):
        t = time.time()
        x = b.astar_fields
        z.append(time.time()-t)
    print "%.3f" % (sum(z)/len(z))

def astar():
    z = []
    ast = b.aStar
    ast2 = b.aStar2
    p = b.players[0]
    for x in b.npcs:
        t = time.time()
        ast(p,x)
        z.append(time.time()-t)
    print 'ast', "%.3f" % (sum(z)/len(z))
    z = []
    for x in b.npcs:
        t = time.time()
        ast2(p,x)
        z.append(time.time()-t)
    print 'ast2', "%.3f" % (sum(z)/len(z))

def ai_time():
    for i in range(5):
        print i
        t = time.time()
        for p in b.players:
            while p.cur_energy > 0:
                key = random.choice(['w','a','d','s','space'])
                b.action(p.name, key)
        print "%.3f" % (time.time()-t)


def distance_assert():
    f1 = b.getField((2,1))
    f2 = b.getField((9,3))
    print 'dist1', f1.coords, 'to', f2.coords, '=', b.distance(f1,f2)
    print 'dist2', f1.coords, 'to', f2.coords, '=', b.distance2(f1,f2)
    f1 = b.getField((6,8))
    f2 = b.getField((8,6))
    print 'dist1', f1.coords, 'to', f2.coords, '=', b.distance(f1,f2)
    print 'dist2', f1.coords, 'to', f2.coords, '=', b.distance2(f1,f2)

distance_assert()
