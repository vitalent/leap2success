import csv
from eth_account import Account

# Enable unaudited HD wallet features (optional)
Account.enable_unaudited_hdwallet_features()

# Number of addresses per file
NUM_ADDRESSES = 4000

# Number of files to generate (eth01.csv to eth20.csv)
NUM_FILES = 20

# Generate files eth01.csv to eth20.csv
for file_num in range(1, NUM_FILES + 1):
    # List to store data for the current file
    key_data = []
    
    # Generate 4,000 Ethereum accounts
    for _ in range(NUM_ADDRESSES):
        # Create a new account
        account = Account.create()
        private_key = account._private_key.hex()  # Get private key with '0x' prefix
        
        # Split the private key into left and right 128-bit parts (32 hex chars each)
        left_128 = private_key[:34]  # First 32 hex chars + '0x'
        right_128 = private_key[34:]  # Last 32 hex chars
        
        # Append to key_data as a single row with space-separated values
        key_data.append([left_128 + " " + right_128])
    
    # Write to file ethXX.csv (e.g., eth01.csv, eth02.csv, ..., eth20.csv)
    filename = f'eth{file_num:02d}.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(key_data)