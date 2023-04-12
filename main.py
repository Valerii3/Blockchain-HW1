import argparse
import os
import rsa

def generate(keypair):

    (pubkey, privkey) = rsa.newkeys(2048) # 2048 is the key length

    public_key_file = os.path.join(keypair, 'public_key.pem')
    os.makedirs(os.path.dirname(public_key_file), exist_ok=True)
    with open(public_key_file, 'wb') as f:
        f.write(pubkey.save_pkcs1())

    private_key_file = os.path.join(keypair, 'private_key.pem')
    os.makedirs(os.path.dirname(private_key_file), exist_ok=True)
    with open(private_key_file, 'wb') as f:
        f.write(privkey.save_pkcs1())




def sign(file, keypair):
    with open(keypair, 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    # Read the contents of the file to sign
    with open(file, 'rb') as f:
        file_contents = file.read()

    # Sign the file contents using the private key
    signature = rsa.sign(file_contents, private_key, 'SHA-256')

    # Write the signature to a file
    signature_path = file + '.sig'
    with open(signature_path, 'wb') as signature_file:
        signature_file.write(signature)


def verify(file, keypair, signature):
    with open(keypair, 'rb') as key_file:
        public_key = rsa.PublicKey.load_pkcs1(key_file.read())

    with open(file, 'rb') as file:
        file_contents = file.read()

    with open(signature, 'rb') as signature_file:
        signature = signature_file.read()

    try:
        rsa.verify(file_contents, signature, public_key)
        print('Signature is valid')
    except rsa.pkcs1.VerificationError:
        print('Signature is invalid')

def main():
    print("URA")
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, help='Available commands: generate, sign, verify')
    parser.add_argument('file', nargs='?', default=None, type=str, help='File you want to sign or verify')
    parser.add_argument('keypair', type=str,
                        help='File with keypair (public and private keys)')
    parser.add_argument('signature', nargs='?', default=None, type=str, help='Signature file')
    args = parser.parse_args()
    if args.command == 'generate':
        generate(args.keypair)
    elif args.command == 'sign':
        sign(args.file, args.keypair)
    elif args.command == 'verify':
        verify(args.file, args.keypair, args.signature)


if __name__ == "__main__":
    main()
