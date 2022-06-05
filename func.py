def addZero(n, z = 2):
  return str(n).zfill(z)

def clockString(ms, v2 = False):
  if v2 == True:
    ss = int(str(ms).split(".")[0])

    if str(ms / 3600).find("-") != -1:
      hh = 0
    else:
      hh = int(str(ms / 3600).split(".")[0])

    if str(ms / 60).find("-") != -1:
      mm = 0
    else:
      mm = int(str(ms / 60).split(".")[0]) % 60

    if str(ms / 60).find("-") != -1:
      ss = 0
    else:
      ss = int(str(ms).split(".")[0]) % 60

    ms = ms % 1000

    hh = addZero(hh)
    mm = addZero(mm)
    ss = addZero(ss)

    return hh + ":" + mm + ":" + ss
  else:
    ms = int(str(ms).split(".")[0])

    if str(ms / 3600000).find("-") != -1:
      hh = 0
    else:
      hh = int(str(ms / 3600000).split(".")[0])

    if str(ms / 60000).find("-") != -1:
      mm = 0
    else:
      mm = int(str(ms / 60000).split(".")[0]) % 60

    if str(ms / 1000).find("-") != -1:
      ss = 0
    else:
      ss = int(str(ms / 1000).split(".")[0]) % 60

    ms = ms % 1000

    hh = addZero(hh)
    mm = addZero(mm)
    ss = addZero(ss)
    ms = addZero(ms, 4)

    return hh + ":" + mm + ":" + ss + " " + ms
