import zipfile as z
import os
from time import time, sleep as s
from func import clockString

def clr():
  linux = "clear"
  windows = "cls"
  os.system([linux, windows][os.name == "nt"])

clr()
with open("banner.txt", "r") as b:
  banner = b.read()
  b.close()

print("\033[32;1m" + banner + "\033[0;0m")
choose = input(" [??] Enter numbers > ")

try:
  choose = int(choose)
except:
  print("\033[31;1mInvalid number!\033[0;0m")
  s(1)
  exit()


if choose == 0:
  print("Sayōnara!")
  s(1)
  exit()
elif choose == 1:
  print()
  file = input(" [??] Enter the zip file name > ")
  if not z.is_zipfile(file):
    print(f"\033[31;1mFile \"{file}\" does not exist or it is not a zip file!\033[0;0m")
    s(1)
    exit()
  else:
    print()
    wordlist = input(" [??] Enter the wordlist file > ")
    zip = z.ZipFile(file)
    i = 0
    fail = 0
    old = time()
    with open(wordlist, "r") as w:
      os.mkdir(file.replace(".zip", ""))
      passwd = w.readlines()
      for x in passwd:
        password = x.split("\n")[0]
        try:
          zip.extractall(pwd = bytes(password, "UTF-8"), path=file.replace(".zip", ""))
          new = clockString(time() - old, True)
          print(time() - old)
          i += 1
          print(f"[*] Password found :)\n[**] Password : {password}\n[***] Takes {new} to complete. Requires {i} tries to complete")
          exit()
        except:
          i += 1
          fail += 1
          pass
      if fail == i: print("[X] Sorry, Password not found :(")
      exit()
