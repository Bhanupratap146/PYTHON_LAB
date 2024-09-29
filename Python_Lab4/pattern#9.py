n = 4
start = 1

for i in range(1, n + 1):
   
    end = start + i - 1
   
    for j in range(end, start - 1, -1):
      print(j, end=" ")
    
   
    start = end+1
    print()