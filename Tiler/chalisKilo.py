weights = [1,3,10,26]
data=set()

class datas:
    def fillData(self,weight,num=0):
        cutNum=num
        if (len(weight) == 1): return#last leaf 
        if num != 0: 
            weight.remove(num) #provided number should be removed to create new weights list
            data.add(num)
            
        maxWeight = max(weight)
        s=maxWeight
        d=maxWeight
        for x in weight:
            self.fillData(weight[:],x)  #recursive call with new list and new number to strip 
            if x != maxWeight: 
                s+=x
                d-=x
            data.add(s)
            data.add(d)
        if (s+cutNum) <= 40:
            data.add(s+cutNum) 
        if(d+cutNum) <= 40:
            data.add(d+cutNum)
        if (s-cutNum) >=0:
            data.add(s-cutNum)
        if(d-cutNum) >=0:
            data.add(d-cutNum) 
dosier = datas()
dosier.fillData(weights[:],0)
print(data)

            

