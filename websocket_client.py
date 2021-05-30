from websocket import create_connection
ws = create_connection("ws://localhost:8000/ws")
ws.send("Hello, World")
result = ws.recv()
print("Received '%s'" % result)
ws.close()
