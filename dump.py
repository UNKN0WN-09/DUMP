import os,time,platform
os.system('clear')
print('[•] Checking Updates')
os.system('git pull')
os.system('xdg-opne https://github.com/UNKN0WN-09')
bit = platform.architecture()[0]
if bit=='64bit':
    import sxs
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')