num = int(input("Enter a number"))
cpy = num
s=0
n=len(str(num))
while num != 0:
  k = num%10
  s = s+(k**n)
  num = num//10
if cpy == s:
  print("Armstrong")
else:
  print("Not an Armstrong")
