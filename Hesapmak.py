def Add(a,b):
  print(a+b)
def sub(a,b):
  print(a-b)
def mul(a,b):
  print(a*b)
def div(a,b):
  print(a/b)
a=int(input("Birinci sayıyı giriniz:"))
b=int(input("ikinci sayıyı giriniz:"))
operator=input("operation:")
if operator=="+":
  Add(a,b)
elif operator=="-":
  sub(a,b)
elif operator=="*":
   mul(a,b)
elif operator=="/":
   div(a,b)
else:
   print("Fehler")
