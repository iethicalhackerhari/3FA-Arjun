from hashlib import md5
from Crypto.Cipher import DES3

def encryption(key, file_path):
    
        # Encode given key to 16 byte ascii key with md5 operation
        key_hash = md5(key.encode('ascii')).digest()

        # Adjust key parity of generated Hash Key for Final Triple DES Key
        tdes_key = DES3.adjust_key_parity(key_hash)

        cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

        with open(file_path, 'rb') as input_file:
            file_bytes = input_file.read()
            new_file_bytes = cipher.encrypt(file_bytes)

        with open(file_path, 'wb') as output_file:
            output_file.write(new_file_bytes)
            
def decryption(key, file_path):
    
        # Encode given key to 16 byte ascii key with md5 operation
        key_hash = md5(key.encode('ascii')).digest()

        # Adjust key parity of generated Hash Key for Final Triple DES Key
        tdes_key = DES3.adjust_key_parity(key_hash)

        cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

        with open(file_path, 'rb') as input_file:
            file_bytes = input_file.read()
            new_file_bytes = cipher.decrypt(file_bytes)

        with open(file_path, 'wb') as output_file:
            output_file.write(new_file_bytes)
            
decryption('arjun',r"D:\python\arjun\3FA\secretVault\sreehari.txt")