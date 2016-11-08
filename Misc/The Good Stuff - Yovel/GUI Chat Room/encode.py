import sys
import os

def encodec(c, key='c', ops='^'):
    c = ord(c)
    k = ord(key)
    a = eval('hex(c'+ops[0]+'k)')[2:]
    for op in ops[1:]:
        a = eval('a'+op+'k')
    while len(a) <= 1:
        a = '0'+a
    return a.upper()

def encode(inp, key='c', ops='^'):
    e = []
    for i in inp:
        e.append(encodec(i, key, ops))
    return (''.join(e))

def decode(inp, key='c', ops='^'):
    e = []
    chars = []
    i = 0
    for k in range(int(len(inp)/2)):
        chars.append(inp[i]+inp[i+1])
        i += 2
    for k in chars:
        r = ''
        r = eval('int(\'0x\'+k, 16)'+ops[0]+'ord(key)')
        for op in ops[1:]:
            r = eval('r'+op+'ord(key)')
        e.append(chr(r))
    return (''.join(e))


def decode_file(filename, key='c', operations='^'):
    f = open(filename, 'r')
    c = f.read()
    f.close()
    f = open('decoded.txt', 'w+')
    f.write(decode(c, key, operations))
    f.close()
    os.remove(filename)
def encode_file(filename, key='c', operations='^'):
    f = open(filename, 'r')
    c = f.read()
    f.close()
    f = open('encoded.txt', 'w+')
    f.write(encode(c, key, operations))
    f.close()
    os.remove(filename)
