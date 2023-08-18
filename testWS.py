import websocket
import json
import threading

class WebSocketClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.ws = None

    def on_message(self, ws, message):
        data = json.loads(message)
        print(f"Received message from {data['username']}: {data['message']}")

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")

    def on_open(self, ws):
        def run(*args):
            while True:
                message = input("Enter a message (type 'exit' to quit): ")
                if message == "exit":
                    break
                self.ws.send(json.dumps({
                    'message': message,
                    'username': 'console',
                }))
            self.ws.close()
            print("WebSocket connection closed")

        threading.Thread(target=run).start()

    def start(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.server_url,on_message=self.on_message,
            on_error=self.on_error,on_close=self.on_close)

        self.ws.on_open = self.on_open
        self.ws.run_forever()

if __name__ == "__main__":
    server_url = "ws://127.0.0.1:8000/ws/chat/1/" 
    client = WebSocketClient(server_url)
    client.start()
