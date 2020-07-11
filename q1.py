import random
import plotgraph
import time
import math

population=int(input("Enter Population size : "))
chromosomelength=int(input("Enter length of Chromosome : "))
maxfitness=(pow(2,chromosomelength))-1

def calculatefitness(temp):
    count=chromosomelength
    fitness=0
    for j in range(len(temp)):
        count-=1
        if temp[j]==1:
            fitness+=pow(2,count)
    return fitness
    
    
def printfunc(l):
    for i in range(len(l[0])):
        print ("individual : ",l[0][i] ," , fitness : ",l[1][i])
        
def createindiviuals(population,chromosomelength):
    list=[]
    temp=[]
    fitnesslist=[]
    for i in range(population):
        fitness=0
        for j in reversed(range(chromosomelength)):
            x=random.randint(0,100)
            if x<=50:
                temp.append(0)
            elif x>50 and x<=100:
                fitness+=pow(2,j)
                temp.append(1)
        list.append(temp.copy())
        fitnesslist.append(fitness)
        temp.clear()
    return list,fitnesslist

def crossoverfirst(c1,c2,l1,l2):
    temp1=[]
    for x in range(c1):
        temp1.append(l1[x])
    for y in range(c1,c2):
        temp1.append(l2[y])
    for x in range(c2,chromosomelength):
        temp1.append(l1[x])
    
    if temp1[c2]==0:
        temp1[c2]=1
    # elif temp1[c2]==1:
    #     temp1[c2]=0
    
    return temp1

def crossoversecond(c1,c2,l1,l2):
    temp2=[]
    for x in range(c1):
        temp2.append(l2[x])
    for y in range(c1,c2):
        temp2.append(l1[y])
    for x in range(c2,chromosomelength):
        temp2.append(l2[x])
    
    if temp2[c2]==0:
        temp2[c2]=1
    # elif temp2[c2]==1:
    #     temp2[c2]=0
    
    return temp2
    

def creategenes(ll):
    list=[]
    temp1=[]
    temp2=[]
    fitnesslist=[]
    l=ll[0].copy()
    flag=False
    if (population%2)!=0:
        flag=True
        
    for i in range(math.floor(population/2)):
        crossoverpoint1=random.randint(0,round(chromosomelength/2)-1)
        crossoverpoint2=random.randint(round(chromosomelength/2),chromosomelength-1)
        
        temp1=crossoverfirst(crossoverpoint1,crossoverpoint2,l[i],l[i+1])
        
        fitness=calculatefitness(temp1)
        fitnesslist.append(fitness)
        list.append(temp1.copy())
        
        temp2=crossoversecond(crossoverpoint1,crossoverpoint2,l[i],l[i+1])
            
        fitness2=calculatefitness(temp2)
        fitnesslist.append(fitness2)
        list.append(temp2.copy())
        
        temp1.clear()
        temp2.clear()
    
    if flag==True:
        temp1.clear()
        temp2.clear()
        crossoverpoint1=random.randint(0,round(chromosomelength/2)-1)
        crossoverpoint2=random.randint(round(chromosomelength/2),chromosomelength-1)
        
        temp1=crossoverfirst(crossoverpoint1,crossoverpoint2,l[i+1],l[i+2])
        fitness=calculatefitness(temp1)
        
        temp2=crossoversecond(crossoverpoint1,crossoverpoint2,l[i],l[i+1])
            
        fitness2=calculatefitness(temp2)
        
        if fitness>=fitness2:
            fitnesslist.append(fitness)
            list.append(temp1.copy())
        elif fitness2>fitness:
            fitnesslist.append(fitness2)
            list.append(temp2.copy())
        
    return list,fitnesslist

result=createindiviuals(population,chromosomelength)
jj=0
p=math.ceil(population/2)+1
remainder=population-p

while maxfitness not in result[1]:
    print("\n************* Generation ",jj, " ********************")
    jj+=1
    printfunc(result)
    temp=list(result)
    t1=[]
    t2=[]
    for i in range (remainder):
        t1.clear()
        t2.clear()
        t1=temp[0].copy()
        t2=temp[1].copy()
        index1=temp[1].index(min(temp[1]))
        t1.pop(index1)
        t2.pop(index1)
        temp[0]=t1.copy()
        temp[1]=t2.copy()
    # if jj==100:
    #     break
    result=creategenes(temp)

print("\n*****************  Generation ",jj," *********************")
printfunc(result)
f=open("population.txt","a")
f.write(str(population)+",")
f.close()

f=open("generation.txt","a")
f.write(str(jj)+",")
f.close()

f=open("chromosome.txt","a")
f.write(str(chromosomelength)+",")
f.close()
# plotgraph.plottingchromosome()
# plotgraph.plottingpopulation()
        