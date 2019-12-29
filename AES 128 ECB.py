from Crypto.Cipher import AES
import base64


BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def aesEncrypt(key, data):
    
    key = key.encode('utf8')
    
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    
    result = cipher.encrypt(data.encode())
    encodestrs = base64.b64encode(result)
    enctext = encodestrs.decode('utf8')
    print(enctext)
    return enctext

def aesDecrypt(key, data):
    
    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)

    
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    print(text_decrypted)
    return text_decrypted


data=input("Password:")
ecdata=input("Password to decrypt:")
key=input("Key:")
if len(ecdata)==0:
    ecdata = aesEncrypt(key, data)
    print(ecdata)
if len(data)==0:   
    edata=aesDecrypt(key, ecdata)
    print(edata)