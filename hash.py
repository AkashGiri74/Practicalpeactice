import hashlib
def hash(str):
    h=hashlib.sha256(str.encode())
    return h.hexdigest()
a=hash("hello")
print("hash value",a)
