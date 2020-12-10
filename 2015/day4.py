import hashlib

inpoute = "yzbqklnj"

if __name__ == '__main__':

    for i in range(10000000):
        result = (hashlib.md5((inpoute + str(i)).encode())).hexdigest()
        if result[:6] == '000000':
            print(result)
            print(i)
            exit()