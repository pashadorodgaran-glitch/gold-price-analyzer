prices = [19000, 21000, 18500, 22000, 19500]
kamtarin = prices[0] 
for price in prices :
    if kamtarin > price :
        kamtarin = price 
print(kamtarin,"کمترین")

bishtarin = prices[0]
for price in prices :
    if bishtarin < price :
        bishtarin = price 
print(bishtarin,"بیشترین")

jam = 0 
for price in prices :
      jam += price
    
     
print(jam,"حاصل جمع")
    