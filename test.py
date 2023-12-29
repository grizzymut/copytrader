import requests
import time

def scan_solscan_transaction_hashes(address, seen_hashes=set()):
    base_url = "https://public-api.solscan.io"
    address_url = f"{base_url}/account/history/{address}?limit=10"

    try:
        response = requests.get(address_url)
        response.raise_for_status()

        data = response.json()
        transactions = data.get("result", [])

        new_hashes = []
        if transactions:
            for tx in transactions:
                tx_hash = tx['signature']
                if tx_hash not in seen_hashes:
                    seen_hashes.add(tx_hash)
                    new_hashes.append(tx_hash)

        return new_hashes

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def show_counter():
    for i in range(1, 31):
        print(f"Counter: {i}")
        time.sleep(1)
        # Clear the terminal screen (use 'cls' for Windows)
        print("\033c", end="")

if __name__ == "__main__":
    address_to_scan = "5LVnED8D8za6JcC8pnFocyyTVW5xhicJSupavn6AEaTu"
    seen_transaction_hashes = set()

    while True:
        show_counter()
        new_hashes = scan_solscan_transaction_hashes(address_to_scan, seen_transaction_hashes)

        if new_hashes:
            print("New Transaction Hashes:")
            for tx_hash in new_hashes:
                print(tx_hash)

        # Reset the counter after reaching 30
        print("Counter: Resetting...")
        time.sleep(2)  # Sleep for 2 seconds before the next loop
