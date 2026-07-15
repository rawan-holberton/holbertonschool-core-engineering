#!/usr/bin/env python3

import asyncio
import websockets


async def connection_handler(websocket):
    """
    Handle a WebSocket connection.

    Receives messages from a client and sends back the exact same message.
    """
    async for message in websocket:
        await websocket.send(message)


async def main():
    """
    Start the WebSocket echo server.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
