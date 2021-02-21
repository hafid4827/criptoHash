import hashlib as hs
from time import time
from os import path
from argparse import ArgumentParser

def funcDicstCall(paramSha, callDictId):
    dictShaFunc = {
        'md5': hs.md5(paramSha),
        'sha1': hs.sha1(paramSha),
        'sha224': hs.sha224(paramSha),
        'sha256': hs.sha256(paramSha),
        'sha384': hs.sha384(paramSha),
        'sha512': hs.sha512(paramSha),
        'blake2b': hs.blake2b(paramSha),
        'blake2s': hs.blake2s(paramSha),
        'sha3_224': hs.sha3_224(paramSha),
        'sha3_256': hs.sha3_256(paramSha),
        'sha3_384': hs.sha3_384(paramSha),
        'sha3_512': hs.sha3_512(paramSha),
        #'shake_128': hs.shake_128(x.encode('utf-8')).hexdigest(),
        #'shake_256': hs.shake_256(x.encode('utf-8')).hexdigest(),
    }
    return dictShaFunc[callDictId].hexdigest()

def _CRIV1(_Encripting, HashSelect, rutDict):
    openDict = open(path.abspath(rutDict),'r').readlines()
    return openDict[list(map(lambda iterDict : funcDicstCall(iterDict.replace('\n', '').encode('utf-8'),HashSelect),openDict)).index(_Encripting)].replace('\n', '')

def _CRIV2(_Encripting, rutDict, HashSelect):
    openDict = open(path.abspath(rutDict),'r').readlines()
    for i in openDict:
        if _Encripting == funcDicstCall(i.replace('\n', '').encode('utf-8'), HashSelect):
            return i
        
def _CRIV3(_Encripting, rutDict, HashSelect):
    return [i.replace('\n', '') for i in open(path.abspath(rutDict),'r').readlines() if _Encripting == funcDicstCall(i.replace('\n', '').encode('utf-8'), HashSelect)]

def pruebados(Def, Sha, Option, Redirect):
        if Def == 'CRIV1':
            return _CRIV1(
                _Encripting=Sha,
                HashSelect=Option, 
                rutDict=Redirect,)
        elif Def == 'CRIV2':
            return _CRIV2(
                _Encripting=Sha,
                HashSelect=Option, 
                rutDict=Redirect)
        elif Def == 'CRIV3':
            return _CRIV3(
                _Encripting=Sha,
                HashSelect=Option, 
                rutDict=Redirect)


if __name__ == '__main__':
    parser = ArgumentParser(description = ' -D CRYV1 -S dc517d7ed2c7e9ec2870a... -O sha512 -R ../dict/dictPassword.txt')
    parser.add_argument('-D', '--DEF',) # opcion de cualquier funcion que exite 
    parser.add_argument('-S', '--SHA',)# criptografia encriptada
    parser.add_argument('-O', '--OPTION',) # funcion seletivo hash
    parser.add_argument('-R', '--REDIRECT',) # direccion opcional del diccionario
    args = parser.parse_args()
    #OP_Encripting = input('Introduce tu hash: ')
    #OP_HashSelect = input('introduce tipo de criptografia: ')
    initTime = time()
    print(*pruebados(
        Def = args.DEF,
        Sha= args.SHA,
        Option= args.OPTION,
        Redirect= args.REDIRECT,))
    print(time() - initTime)