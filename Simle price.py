import asyncio
import base64
import hashlib
import hmac
import time
import websockets

global answer
answer = ""

print("Введите пару в формате 'BTC_USD': ")

def start_exmo_client(url, init_messages):
    async def ws_loop():
        async with websockets.connect(url) as websocket:
            for init_message in init_messages:
                await websocket.send(init_message)
                print("Request on: ", init_message[init_message.find("[") + 1: init_message.find("]")])
            count = 0
            while count < 3:
                answer = await websocket.recv()
                count += 1
            else:
                print("Last price:", answer[answer.find("price") + 8: answer.find("quantity") - 3])

    try:
        asyncio.new_event_loop().run_until_complete(ws_loop())
    except websockets.exceptions.ConnectionClosed as ex:
        print("connection closed", ex)
    except KeyboardInterrupt:
        pass


def public_api_usage_example(pare=input()):

    start_exmo_client(
        "wss://ws-api.exmo.com:443/v1/public",
        [f"""{{
        "id":1,
        "method":"subscribe",
        "topics":["spot/trades:{pare}"]
        }}"""]
    )


if __name__ == "__main__":
    public_api_usage_example()
