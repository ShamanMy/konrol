n=int(input("Ievadi vecumu: "))
if n<100:
  galvas1=3+3*n
  acis1=galvas1*2
  print(galvas1,acis1)
if n>=100:
  galvas2=3+(3*99)+(n-99)*2
  acis2=galvas2*2
  print(galvas2,acis2)