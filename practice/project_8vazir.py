import numpy as np
import random
class Gentic():
    def __init__(self,parentnumber,crossoverpercent,mutationpercent):
        self.parentnumber = parentnumber
        self.crossoverpercent=crossoverpercent
        self.mutationpercent=mutationpercent
    

    def generation(self):
        parentlist= list()
        for i in range(self.parentnumber):
           parent = list(range(1,9))
           np.random.shuffle(parent)
           parentlist.append(parent)
        return parentlist
    
    def crossover(self,parentlist):
        listnumber=list(range(0,9))
        crossover=list()
        for i in range(int(self.parentnumber*self.crossoverpercent/2)):
            crossoverlist=random.choices(parentlist, k=2)
            randomnumber= random.choice(listnumber)
            child1=crossoverlist[0][:randomnumber] + crossoverlist[1][randomnumber:]
            child2=crossoverlist[1][:randomnumber] + crossoverlist[0][randomnumber:]
            crossover.append(child1)
            crossover.append(child2)
        return crossover
    
    def mutation(self,crossover):
        listnumber=list(range(0,8))
        select_for_mutation= random.choices(crossover, k = int(self.crossoverpercent*len(crossover)))
        mutationlist=list()
        for i in select_for_mutation:
            randomnumber_index= random.choice(listnumber)
            randomnumber_value= random.choice(listnumber)
            i[randomnumber_index]=randomnumber_value
            mutationlist.append(i)
        return mutationlist
    
    def cost(self,parent,crossover,mutation):
        data = parent+crossover+mutation
        cost = list()
        #print('++++++++++++++++++','len data : ',len(data))
        for i in data:
            for j in range(1,9):
                if j in i:
                    counter = i.count(j)
                    if counter >1:
                       data.remove(i)
                       cost.append(i)
                       break
            #print('++++++++++++++++++','len data : ',len(data))

        for answer in data:
            for i in range(9):
                for j in range(2,9):
                    if i+j<8:
                        if answer[i] - answer[i+j] == j:
                            cost.append(answer)
                            data.remove(answer)
                        break
                if answer not in data:
                    break
        data_uni=list()
        for answer in data:
            if answer not in data_uni:
                data_uni.append(answer)

                        
  
                        
        return cost,data_uni
                    
    
#    def gentic():
    


a=Gentic(6,0.8,0.3)
parent=a.generation()
print(parent)
print("***************************************")
print("***************************************")
print("***************************************")
while True:
    crossover=a.crossover(parent)
#    print(crossover)
#    print("*    **************************************")
#    print("***************************************")
    mutation = a.mutation(crossover)
#    print(mutation)

#    print("***************************************")
#   print("***************************************")
    cost,parent=a.cost(parent,crossover,mutation)
    if len(cost) == 0 :
        break
    else:
        continue
result =parent
#uni = set(parent)
print("***************************************")
print("***************************************")
#uni_asnswer = print(uni)
uni = list()
for answer in result:
    if answer not in uni:
        uni.append(answer)
print('answer:',len(parent),'\n',result)
print('uni:',len(uni),'\n',uni)


