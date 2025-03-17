# server.py

import asyncio
import websockets
import json

# Set of connected clients
connected_clients = set()

async def handler(websocket, path):
    # Register client
    connected_clients.add(websocket)
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            # Echo the message back to the client
            response = json.dumps({"message": f"Echo: {message}"})
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected: {websocket.remote_address}")
    finally:
        # Unregister client
        connected_clients.remove(websocket)

async def send_periodic_messages():
    while True:
        if connected_clients:
            message = json.dumps({"message": "Hello from server!"})
            await asyncio.wait([client.send(message) for client in connected_clients])
            print("Sent periodic message to all clients.")
        await asyncio.sleep(10)  # Send every 10 seconds

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        await send_periodic_messages()  # Run until interrupted

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")