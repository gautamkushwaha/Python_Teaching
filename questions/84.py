

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            print(l)
        return i + 1
    
print(file_len("file.txt"))
        