import asyncio
import websockets

async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = "Client message"
        await websocket.send(message)
        print(f"Sent message: {message}")

        response = await websocket.recv()
        print(f"Received response: {response}")

asyncio.get_event_loop().run_until_complete(main()
