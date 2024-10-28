import websocket
import sys
conn_string=sys.argv[1]

websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect(conn_string)
ws.send("Hello, Server")
print(ws.recv())
ws.close()
