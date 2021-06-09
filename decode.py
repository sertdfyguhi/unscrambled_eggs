from base64 import b64decode
from binascii import unhexlify
import re

# https://www.reddit.com/r/UnscramblingTheEggs/comments/nv0xou/block_2821_decoded/
def decode_BLOCK2821(string):
    hexed = ''
    split = string.split('.')

    while len(split) > 1:
        ascii_code = split[0] + split[1][0]
        hexed += chr(int(ascii_code))
        split.pop(0)
        split[0] = split[0][1:]

    return b64decode(unhexlify(hexed.encode('ascii'))).decode('ascii')

# https://www.reddit.com/r/UnscramblingTheEggs/comments/nv1o7z/information_decoded/
def decode_Info1(enc):
    _enc = re.sub('===|==|=', '==.', enc)
    split = _enc.split('.')
    split.pop(-1)
    res = [chr(int(unhexlify(b64decode(el.encode('ascii'))))) for el in split]
    return b64decode(''.join(res).encode('ascii')).decode('ascii')
  
# https://www.reddit.com/r/UnscramblingTheEggs/comments/nvr0hz/i_decoded_the_new_information_post/
def decode_Info2(string):
    # hexadecimal
    res = unhexlify(string.encode('ascii'))
    # base64
    res = b64decode(res)
    # custom algorithm for other Information. post
    res = decode_Info1(res.decode('ascii'))
    # custom algorithm for BLOCK 2821
    res = decode_BLOCK2821(res)
    # hexadecimal
    res = unhexlify(res.encode('ascii'))
    # custom algorithm for other Information. post
    res = decode_Info1(res.decode('ascii'))
    # base64
    res = b64decode(res.encode('ascii'))
    # custom algorithm for other Information. post
    res = decode_Info1(res.decode('ascii'))
    return res
