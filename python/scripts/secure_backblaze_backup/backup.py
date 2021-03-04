import argparse
import sys

from keys import create_key, load_key
from actions import encrypt_file, decrypt_file


parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument(
    "-k",
    "--key",
    help="Path to encryption key, if one already exists. If argument is not provided, then a new encryption key will be created.",
    type=str,
)
parser.add_argument(
    "-a",
    "--action",
    help="The action for the script to perform. ENCRYPT or DECRYPT.",
    type=str,
    required=True,
)
parser.add_argument(
    "-f", "--file", help="The file to ENCRYPT or DECRYPT.", type=str, required=True
)

args = parser.parse_args()


if __name__ == "__main__":

    if args.action.lower() == "encrypt":
        if args.key:  # If an encryption key was provided
            encryption_key = load_key(args.key)
            encrypt_file(args.file, encryption_key)
            print(f"{args.file} has been encrypted")
        else:  # If an encryption key was NOT provided
            new_key = create_key()
            encrypt_file(args.file, new_key)
            print(f"{args.file} has been encrypted")

    elif args.action.lower() == "decrypt":
        if args.key is None:  # If an encryption key was NOT provided
            print(
                "Cannot DECRYPT a file without the key that encrypted it. Please pass the '-k' option."
            )
            sys.exit(1)
        else:  # If an encryption key was provided
            encryption_key = load_key(args.key)
            decrypted_file = decrypt_file(args.file, encryption_key)
            print(f"{args.file} has been decrypted!")

    else:
        print(f"Invalid option: {args.action}")
        sys.exit(1)
