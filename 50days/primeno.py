start = 11
end = 27

for p in range(start, end + 1):
   if p > 1:
       for n in range(2, p):
           if (p %n) == 0:
	     break
        else:
            print(p)
	  
