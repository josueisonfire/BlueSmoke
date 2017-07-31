
from websocket import create_connection
ws = create_connection("ws://localhost:1010")
print "Sending 'Hello, World'..."
ws.send("Hello, World")
print "Sent"
ws.close()