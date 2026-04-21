import websocket
import json
import threading
import time

def spribe_hash_to_multiplier(hash_str):
    """
    Convert Spribe hash to multiplier using known formula.
    """
    h = int(hash_str[:13], 16)
    multiplier = (100 * (2**52)) // (2**52 - h)
    return round(multiplier / 100, 2)

def on_message(ws, message):
    # Incoming message is usually JSON text
    try:
        data = json.loads(message)
    except Exception:
        # Sometimes binary or non-json - ignore
        return

    # Look for pre-round start message with hash & round id
    if isinstance(data, dict):
        # You may need to adapt these keys depending on actual messages you capture
        if data.get("type") == "start" and "data" in data:
            game_hash = data["data"].get("game_hash") or data["data"].get("hash")
            round_id = data["data"].get("round_id") or data["data"].get("uid")
            if game_hash:
                multiplier = spribe_hash_to_multiplier(game_hash)
                print(f"[Round {round_id}] Next multiplier: {multiplier}x (decoded from hash: {game_hash})")

def on_error(ws, error):
    print(f"[ERROR] {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"[WS CLOSED] Code: {close_status_code}, Reason: {close_msg}")

def on_open(ws):
    print("[WS OPENED] Connected to Spribe Aviator WebSocket")

def run():
    ws_url = "wss://af-south-1-game3.spribegaming.com/BlueBox/websocket"

    # These headers simulate browser request (some are optional)
    headers = [
        "Origin: https://aviator-next.spribegaming.com",
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits",
        "Pragma: no-cache",
        "Cache-Control: no-cache"
    ]

    ws = websocket.WebSocketApp(
        ws_url,
        header=headers,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

if __name__ == "__main__":
    run()
