import csv
from eth_account import Account

# Enable unaudited HD wallet features (optional)
Account.enable_unaudited_hdwallet_features()

# Number of addresses to generate
NUM_ADDRESSES = 4000

# Lists to store data
k0_data = []
k1_data = []
k2_data = []
k3_data = []

# Generate 4,366 Ethereum accounts
for _ in range(NUM_ADDRESSES):
    # Create a new account
    account = Account.create()
    private_key = account._private_key.hex()[2:]  # Remove '0x' prefix
    address = account.address

    # Split the private key into left and right 128-bit parts (32 hex chars each)
    left_128 = account._private_key.hex()[:32]  # First 32 hex chars (128 bits)
    right_128 = account._private_key.hex()[32:]  # Last 32 hex chars (128 bits)

    # Append to respective data lists
    # k1_data.append([address, left_128])
    # k2_data.append([address, right_128])
    k0_data.append([account._private_key.hex()])
    k1_data.append([left_128])
    k2_data.append([right_128])
    k3_data.append([left_128 + " " + right_128])
    
# Write to k1.csv (address, left 128-bit key)
with open('eth0.csv', mode='w', newline='') as k0_file:
    writer = csv.writer(k0_file)
    # writer.writerow(['Address', 'Left_128bit_Key'])
    writer.writerows(k3_data)


# Write to k1.csv (address, left 128-bit key)
with open('eth1.csv', mode='w', newline='') as k1_file:
    writer = csv.writer(k1_file)
    # writer.writerow(['Address', 'Left_128bit_Key'])
    writer.writerows(k1_data)

# Write to k2.csv (address, right 128-bit key)
with open('eth2.csv', mode='w', newline='') as k2_file:
    writer = csv.writer(k2_file)
    # writer.writerow(['Address', 'Right_128bit_Key'])
    writer.writerows(k2_data)

print(f"Generated {NUM_ADDRESSES} Ethereum addresses.")
print("Exported left 128-bit keys to k1.csv")
print("Exported right 128-bit keys to k2.csv")