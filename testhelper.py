from pyethereum import tester as t
import logging
logger = logging.getLogger()
#logger.setLevel(logging.INFO)
s = t.state(fond=long(10**75))

bet = 1000000000
def ls():
    global c
    c = s.contract("lotte.se")


def send(c, data, p=0):
        return s.send(t.k0, c, p, data)


def get(c, n):     
        return s.block.get_storage_data(c, n)

def test():
    ls()
    send(c, [0], bet)
    send(c, [0], bet)
    send(c, [0], bet)
    s.mine()
    s.mine()
    send(c, [0])
    
    
    
def sha3(s1): 
        h = hashlib.new("sha3_512")
        h.update(s1)
        print  h.hexdigest()
        print int(h.hexdigest(), 16)
        return h
def ppath(h):
    p = 0
    i = 0
    while i < 8:
        r = h % 2
        h = h /2
        p = p + r* 2**i
        i +=1
        print r,
    print "\n"+str(p)
    
def ls():
    global c
    c = s.contract("solve.se")

def ld():
    global c3
    c3 = s.contract("dropbox.se")
    s.mine()

def lh():
    global c2
    c2 = s.contract("sha3.se")



def build():
    global data
    data = []
    for i in range(10000, 10010):
        data.append(get(c, i))
