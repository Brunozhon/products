def prompt(q):
  que = q + ": "
  ans = input(que)
  return ans;

def count(num):
  return range(num + 1)

def printForrmated(text, format):
  if format.lower() == "curved brackets":
    print("(" + text + ")")
  elif format.lower() == "square brakets":
    print("[" + text + "]")
  elif format.lower() == "curly brakets":
    print("{" + text + "}")
  elif format.lower() == "double quotes":
    print('"' + text + '"')
  elif format.lower() == "single quotes":
    print("'" + text + "'")
  else:
    print(text)
