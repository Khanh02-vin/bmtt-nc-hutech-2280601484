from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, NoEncryption
import os

class ECCCipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.key_file = "ecc_keys.bin"

    def generate_keys(self):
        self.private_key = ec.generate_private_key(ec.SECP256K1())
        self.public_key = self.private_key.public_key()
        
        with open(self.key_file, 'wb') as f:
            private_bytes = self.private_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.PKCS8,
                encryption_algorithm=NoEncryption()
            )
            public_bytes = self.public_key.public_bytes(
                encoding=Encoding.PEM,
                format=PublicFormat.SubjectPublicKeyInfo
            )
            f.write(private_bytes + public_bytes)

    def load_keys(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                content = f.read()
                private_key = content[:800]  
                public_key = content[800:]  
                return private_key, public_key
        return None, None

    def sign(self, message, private_key):
        if isinstance(message, str):
            message = message.encode()
        signature = self.private_key.sign(
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return signature

    def verify(self, message, signature, public_key):
        try:
            if isinstance(message, str):
                message = message.encode()
            self.public_key.verify(
                signature,
                message,
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False

if __name__ == "__main__":
    ecc = ECCCipher()
    
    ecc.generate_keys()
    
    message = "Hello, World!"
    private_key, public_key = ecc.load_keys()
    
    signature = ecc.sign(message, private_key)
    print(f"Signature: {signature.hex()}")
    
    is_valid = ecc.verify(message, signature, public_key)
    print(f"Signature valid: {is_valid}")