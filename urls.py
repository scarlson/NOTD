from handlers.StaticPages import IndexHandler
from handlers.GameHandlers import NotdHandler
from handlers.WebSocket import WSHandler

data = {}
data['rooms'] = {}
data['ips'] = {}
WS = []

url_patterns = [
    (r"/", IndexHandler, dict(data=data)),
    (r"/ws/", WSHandler, dict(data=data)),
    (r"/([a-zA-Z0-9]+)", NotdHandler, dict(data=data)),
]
