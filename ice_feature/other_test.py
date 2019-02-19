
import os


def random_string(n):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(n))))[0:32]


print(random_string(32))
