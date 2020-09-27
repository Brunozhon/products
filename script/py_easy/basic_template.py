def prompt(q):
  que = q + ": "
  ans = input(que)
  return ans;

def count(num):
  return range(num + 1)

def printForrmated(text, format):
  if format = "curly brackets":
    print("(" + text + ")")
  elif format = "square brakets":
    print("[" + text + "]")
  elif format = "object brakets":
    print("{" + text + "}")
  elif format = "double quotes":
    print('"' + text + '"')
  elif format = "single quotes":
    print("'" + text + "'")
  else:
    print(text)
