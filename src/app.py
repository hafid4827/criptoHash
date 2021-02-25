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
    }
    return dictShaFunc[callDictId].hexdigest()
#'../dict/dictPassword.txt'
def _CRIV1(_Encripting, HashSelect, rutDict = None):
    if rutDict == None: rutDict = '../dict/dictPassword.txt'
    openDict = open(path.abspath(rutDict),'r').readlines() # variable temporar
    return openDict[list(map(lambda iterDict : funcDicstCall(iterDict.replace('\n', '').encode('utf-8'),HashSelect),openDict)).index(_Encripting)].replace('\n', '')

def _CRIV2(_Encripting, HashSelect, rutDict = None):
    if rutDict == None: rutDict = '../dict/dictPassword.txt'
    openDict = open(path.abspath(rutDict),'r').readlines()
    for i in openDict:
        if _Encripting == funcDicstCall(i.replace('\n', '').encode('utf-8'), HashSelect):
            return i.replace('\n', '')
        
def _CRIV3(_Encripting, HashSelect, rutDict = None):
    if rutDict == None: rutDict = '../dict/dictPassword.txt'
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

if __name__ == '__main__':

    orsep = '\n\t'+'-'*30

    parser = ArgumentParser(
        description='''
        DESCRIPCION:
            criptoHash es un pequeño proyecto de prueba para decifrar contraseñas
            con las criptografias mas populares que se manejan hoy dia.
        ''')
    parser.add_argument(
        '-D', '--DEF', 
        help='# Selector de algoritmo CRIV1, CRIV2, CRIV3')
    parser.add_argument(
        '-S', '--SHA', 
        help='# Criptografia a decifrar ce7aaac2b65b110c2c52d2...')
    parser.add_argument(
        '-T', '--TEXT', 
        help='# Convertidor caracteres -T hola --> ce7aaac2b65b110c2c52d2...')
    parser.add_argument(
        '-O', '--OPTION',
        help='# -O [opcion] --> md5, sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512')
    parser.add_argument(
        '-R', '--REDIRECT',
        help='# Default: ../dict/dictPassword.txt, -R [ruta]')
    args = parser.parse_args()
    
    print(orsep)

    initTime = time()

    try:
        print('\tContraseña decifrada:', argumentLinePy(
        Def = args.DEF,
        Sha= args.SHA,
        Option= args.OPTION,
        Redirect= args.REDIRECT,
        ))
    except:
        print('\tError no se pudo desencriptar')

    if args.TEXT != None:
        print(funcDicstCall(args.TEXT.encode('utf-8'), args.OPTION))

    print('\tTiempo: ',time() - initTime )
    print(orsep)