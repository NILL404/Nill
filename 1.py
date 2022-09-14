import os, platform
os.system('xdg-open https://facebook.com/nkd202>
bit = platform.architecture()[0]
if bit == '64bit':
    import bxi
else:
    exit('\33[1;31msorry not support 32bit')