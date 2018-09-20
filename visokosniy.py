for x in range(1555, 1705):
     if x%4 == 0 and x%100!=0 and  x%400!=0:
         print(x, '- высокосный')
     elif x%100==0 and  x%400==0:
         print(x, '- высокосный')
     
