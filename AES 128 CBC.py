from Crypto.Cipher  import AES
import base64



BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]



def AES_Encrypt(key, data):
    data = pad(data)
    
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    
    encodestrs = base64.b64encode(encryptedbytes)
    
    enctext = encodestrs.decode('utf8')
    return enctext


def AES_Decrypt(key, data):
    data = data.encode('utf8')
    encodebytes = base64.decodebytes(data)
    
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    
    text_decrypted = unpad(text_decrypted)
    text_decrypted = text_decrypted.decode('utf8')
    print(text_decrypted)
    return text_decrypted

data=input("Password:")
ecdata=input("Password to decrypt:")
key=input("Key:")
vi=input("Vi:")
if len(ecdata)==0:
    enctext = AES_Encrypt(key, data)
    print(enctext)
if len(data)==0:   
    edata=AES_Decrypt(key, ecdata)
    print(edata)