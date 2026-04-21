import hashlib

def hash_record(data, prev=""):
    return hashlib.sha256((str(data) + prev).encode()).hexdigest()