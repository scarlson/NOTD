s = "Stone"
t = "Tree"
g = "Grass"
e = "Entrance"

maps = {}

maps['a'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s],
[s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s ],
[ s,g,g,g,g,g,g,g,g,g,t,t,t,g,g,g,g,g,g,g,g,g,g,g,s],
[s,g,g,g,g,g,g,g,g,g,t,t,t,t,g,g,g,t,t,t,t,t,g,g,s ],
[ s,g,g,g,s,s,g,g,g,g,g,g,g,g,g,g,g,t,t,s,t,t,g,g,s],
[s,g,g,g,g,t,s,g,g,g,s,s,s,s,g,g,g,t,t,s,s,t,g,g,s ],
[ s,g,g,s,t,t,s,g,g,s,g,g,g,s,g,g,g,t,s,s,s,t,g,g,s],
[s,g,g,g,s,t,s,g,g,g,s,g,g,s,g,g,g,g,g,g,g,g,g,g,s ],
[ s,g,g,g,s,s,g,g,g,g,s,g,s,g,g,g,g,t,s,s,s,t,g,g,s],
[s,g,g,g,g,g,g,g,g,s,g,g,g,g,s,g,g,t,t,s,s,t,g,g,s ],
[ s,g,g,g,g,g,g,g,s,s,g,t,g,s,s,g,g,t,t,s,t,t,g,g,s],
[e,g,g,g,g,g,g,g,g,g,g,t,t,g,g,g,g,g,g,g,g,g,g,g,e ],
[ s,g,g,g,g,g,g,g,s,s,g,t,g,s,s,g,g,t,s,g,g,g,g,g,s],
[s,g,g,g,g,g,g,g,g,s,g,g,g,g,s,g,g,t,t,s,g,g,g,g,s ],
[ s,g,g,t,s,t,g,g,g,g,s,g,s,g,g,g,t,t,t,s,g,g,g,g,s],
[s,g,g,g,t,s,t,g,g,g,s,g,g,s,g,g,t,g,g,t,g,g,g,g,s ],
[ s,g,g,t,t,t,g,g,g,s,g,g,g,s,g,g,g,g,g,g,g,g,g,g,s],
[s,g,g,g,t,s,t,g,g,g,s,s,s,s,g,g,t,g,g,t,g,g,g,g,s ],
[ s,g,g,t,s,t,g,g,g,g,t,t,t,g,g,g,t,t,t,s,g,g,g,g,s],
[s,g,g,g,g,g,g,g,g,g,g,t,t,g,g,g,g,t,t,s,g,g,g,g,s ],
[ s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,s,g,g,g,g,g,s],
[s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s ],
[ s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
'''
maps['b'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['c'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['d'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['e'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['f'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['g'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['h'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['i'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['j'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['k'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['l'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['m'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['n'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['o'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['p'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['q'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['r'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['s'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['t'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['u'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['v'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['w'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['x'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
maps['y'] = [
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[e, , , , , , , , , , , , , , , , , , , , , , , ,e ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s, , , , , , , , , , , , , , , , , , , , , , , ,s ],
[ s, , , , , , , , , , , , , , , , , , , , , , , ,s],
[s,s,s,s,s,s,s,s,s,s,s,s,e,s,s,s,s,s,s,s,s,s,s,s,s ]
]
'''
