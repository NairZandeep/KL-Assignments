import asyncio
import websockets

async def handle_connection(websocket, path):
    message = await websocket.recv()
    print(f"Received message: {message}")

    response = "Server response"
    await websocket.send(response)
    print(f"Sent response: {response}")

start_server = websockets.serve(handle_connection, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()