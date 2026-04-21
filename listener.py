import os
import csv
import json
import webbrowser

output_csv = "upcoming_multipliers.csv"
seen_hashes = set()

# === Your game URL ===
url_to_open = (
    "https://games-interface.bitville-api.com/spribe?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50IjoicHJvZC1scyIsImFjY291bnRfaWQiOjQsImN1c3RvbWVyX2lkIjo1OTI1ODcsInBhcnRuZXJfY3VzdG9tZXJfaWQiOiI2MDM3NyIsImN1cnJlbmN5IjoiTFNMIn0.ZF5LZW9eqydbVwin-TpgwWSoe76Z0zvIyH-goh07w2k&account=prod-ls&popup=true&lang=en&id=aviator&parentUrl=/games/go/spribe?id=aviator"
)

# === Launch the game in browser ===
def start():
    print(f"[INFO] Opening game URL: {url_to_open}")
    webbrowser.open(url_to_open)

# === Hash to Multiplier decoding logic ===
def spribe_hash_to_multiplier(hash_str):
    try:
        h = int(hash_str[:13], 16)
        multiplier = (100 * (2**52)) // (2**52 - h)
        return round(multiplier / 100, 2)
    except:
        return None

# === Save hash and predicted multiplier ===
def save_to_csv(game_hash, multiplier):
    file_exists = os.path.exists(output_csv)
    with open(output_csv, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["hash", "multiplier"])
        writer.writerow([game_hash, multiplier])

# === Recursive hash scanner ===
def extract_and_decode(data):
    try:
        json_data = json.loads(data)
    except:
        return

    def scan(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, (dict, list)):
                    scan(value)
                elif isinstance(value, str) and len(value) >= 13 and value[:13].isalnum():
                    if value not in seen_hashes:
                        multiplier = spribe_hash_to_multiplier(value)
                        if multiplier and 1 <= multiplier <= 1000:
                            print(f"[UPCOMING] Multiplier will be: {multiplier}x (hash: {value})")
                            save_to_csv(value, multiplier)
                            seen_hashes.add(value)
        elif isinstance(obj, list):
            for item in obj:
                scan(item)

    scan(json_data)

# === WebSocket listener for mitmproxy ===
def websocket_message(flow):
    if flow.messages:
        for msg in flow.messages:
            if msg.from_server:
                try:
                    content = msg.content
                    if not content:
                        continue
                    if isinstance(content, bytes):
                        content = content.decode("utf-8", errors="ignore")
                    extract_and_decode(content)
                except Exception as e: 
                    print(f"[ERROR] {e}")

# === Start the browser when script is run ===
start()
