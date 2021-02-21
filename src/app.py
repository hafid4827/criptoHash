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
#'../dict/dictPassword.txt'
def _CRIV1(_Encripting, HashSelect, rutDict = ''):
    if rutDict != '': rutDict = '../dict/dictPassword.txt'
    openDict = open(path.abspath(rutDict),'r').readlines()
    return openDict[list(map(lambda iterDict : funcDicstCall(iterDict.replace('\n', '').encode('utf-8'),HashSelect),openDict)).index(_Encripting)].replace('\n', '')

def _CRIV2(_Encripting, HashSelect, rutDict = ''):
    if rutDict != '': rutDict = '../dict/dictPassword.txt'
    openDict = open(path.abspath(rutDict),'r').readlines()
    for i in openDict:
        if _Encripting == funcDicstCall(i.replace('\n', '').encode('utf-8'), HashSelect):
            return i.replace('\n', '')
        
def _CRIV3(_Encripting, HashSelect, rutDict = ''):
    if rutDict != '': rutDict = '../dict/dictPassword.txt'
    return [i.replace('\n', '') for i in open(path.abspath(rutDict),'r').readlines() if _Encripting == funcDicstCall(i.replace('\n', '').encode('utf-8'), HashSelect)]

def argumentLinePy(Def, Sha, Option, Redirect):
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


# 7ca973a353c97334ee3f51c3cd7d116ac2dfe7579d6a2a62c6d3cb2aabd8042c61f0aa4177cde0c94a3102d27033f5f7156169f97422adc31c9cb3160da7a823
# dc517d7ed2c7e9ec2870aabefbd9985f395ebbca1a0a100807cbdd489796ce91dce58500c79e20c18ffe322b339465999c5cf37e5937db6b42a08ac48b9a74e6
# ce7aaac2b65b110c2c52d2636441037f64468ebec5f741df29e7a7876fd3c2e2389a7fdfd9df866e9ce697718e4bea33d10c5f22d02134e9a2c62628c949088f

if __name__ == '__main__':
    parser = ArgumentParser(description = ' -D CRYV1 -S dc517d7ed2c7e9ec2870a... -O sha512 -R ../dict/dictPassword.txt')
    parser.add_argument('-D', '--DEF',)
    parser.add_argument('-S', '--SHA',)
    parser.add_argument('-L', '--LEN',)
    parser.add_argument('-T', '--TEXT',)
    parser.add_argument('-O', '--OPTION',)
    parser.add_argument('-R', '--REDIRECT',)
    args = parser.parse_args()
    print('\n\t'+'-'*30)
    initTime = time()
    print(f'\tContraseña decifrada:', argumentLinePy(
        Def = args.DEF,
        Sha= args.SHA,
        Option= args.OPTION,
        Redirect= args.REDIRECT,
        ))
    print(f'\tTiempo de ejecucion: {time() - initTime}')
    print('\t'+'-'*30)
# PENDIENTES
# ayuda para usuarios 
# ejemplos para usuarios 
# cantidad de caracteres para intentar identificar el tipo de criptografia yu no recorrerlos todo de un solo tiro
# convertir de caracteres a criptografia



