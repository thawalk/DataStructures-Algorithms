def total(n, target,value = 0):
    if n == target + 1:
        print(value)
    value += n
    total(n+1, target, value)

total(1,5)
  
