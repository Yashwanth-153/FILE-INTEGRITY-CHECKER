import os
import hashlib

def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)  # Read file in chunks of 64KB
                if not data:
                    break
                sha256_hash.update(data)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

def check_integrity(directory_path):
    """Check the integrity of files in a directory by calculating their SHA-256 hashes."""
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist or is not a directory.")
        return

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            if calculated_hash:
                print(f"File: {file_path}\nSHA-256 Hash: {calculated_hash}\n")

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check integrity: ").strip()
    check_integrity(directory_to_check)