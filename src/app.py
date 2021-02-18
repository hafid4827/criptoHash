import hashlib as hs
import os
from time import time

def funcDicstCall(paramSha, callDictId):
    dictShaFunc = {
        '--md5': hs.md5(paramSha),
        '--sha1': hs.sha1(paramSha),
        '--sha224': hs.sha224(paramSha),
        '--sha256': hs.sha256(paramSha),
        '--sha384': hs.sha384(paramSha),
        '--sha512': hs.sha512(paramSha),
        '--blake2b': hs.blake2b(paramSha),
        '--blake2s': hs.blake2s(paramSha),
        '--sha3_224': hs.sha3_224(paramSha),
        '--sha3_256': hs.sha3_256(paramSha),
        '--sha3_384': hs.sha3_384(paramSha),
        '--sha3_512': hs.sha3_512(paramSha),
        #'--shake_128': hs.shake_128(x.encode('utf-8')).hexdigest(),
        #'--shake_256': hs.shake_256(x.encode('utf-8')).hexdigest(),
    }
    return dictShaFunc[callDictId].hexdigest()

def _CRI(_Encripting, HashSelect, rutDict):
    openDict = open(os.path.abspath(rutDict),'r').readlines()
    return openDict[list(map(lambda iterDict : funcDicstCall(iterDict.replace('\n', '').encode('utf-8'),HashSelect),openDict)).index(_Encripting)].replace('\n', '')

def _CRIV2(rutDict, na):
    openDict = open(os.path.abspath(rutDict),'r').readlines()
    for i in openDict:
        if na == funcDicstCall(i.replace('\n', '').encode('utf-8'), '--sha512'):
            return i
        
if __name__ == '__main__':
    
    print('''
          
          ''')
    #OP_Encripting = input('Introduce tu hash: ')
    #OP_HashSelect = input('introduce tipo de criptografia: ')
    start_time = time()
    prueba = _CRI(_Encripting='dc517d7ed2c7e9ec2870aabefbd9985f395ebbca1a0a100807cbdd489796ce91dce58500c79e20c18ffe322b339465999c5cf37e5937db6b42a08ac48b9a74e6',
               HashSelect='--sha512', 
               rutDict='../dict/dictPassword.txt'
               )
    print(prueba)
    print(time() - start_time)
    
    start_time = time()
    ss = _CRIV2('../dict/dictPassword.txt','dc517d7ed2c7e9ec2870aabefbd9985f395ebbca1a0a100807cbdd489796ce91dce58500c79e20c18ffe322b339465999c5cf37e5937db6b42a08ac48b9a74e6')
    print(ss)
    print(time() - start_time)
    