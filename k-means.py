#k-means algorithm
#dataset=[[[]..],[[],..],[class[individu],...],..]
#initilize the dataset with the first elements
#listOfCenters=[,,,]
#calcul distance between each individu and all the center
#add this individu in the nearst class in the cluster
#continue this process (calcul of distance between the individus and the centers) until there is no more changes in the list of centers
#k : number of classes we want :

import csv
from math import sqrt

#this function get all the data 'exept the name of the flour' convert them to float and put them into dataSetPrim
def prepareDataSet(dataSet, dataSetPrim) :
    for individu in dataSet :
        tmpList=list()
        for j in range(len(individu) - 1) :
            tmpList.append(float(individu[j]))
        dataSetPrim.append(tmpList)
            

#initialize the cluster
def initCluster(cluster, listOfCenters, dataSet, k) :
    for i in range(k) :
        #add class with one individu
        cluster.append([dataSet[i]])
        #initilize the list of centers
        listOfCenters.append(dataSet[i])
        

def getDistanceOf(individu1, individu2) :
    nbrOfAttr = len(individu1)
    som=0
    for i in range(nbrOfAttr) :
        som += (individu1[i] - individu2[i])**2
    return sqrt(som)

#this function return the center of a given classe
def getCenterOf(classe) :
    if len(classe) == 1 :
        return classe[0]
    if len(classe) == 0 :
        return [0]
    
    nbrAttr = len(classe[0])
    print("nbrAttr =",nbrAttr)
    som=0
    nbrOfIndividus = len(classe)
    center = list()
    
    for individu in classe :
        for i in range(nbrAttr) :
            som += individu[i]
    center.append(som / nbrOfIndividus)
    return center
 
#get all centers of the classes in the cluster
def getAllCentersOf(cluster) :
    allCenters=list()
    
    for classe in cluster :
        allCenters.append(getCenterOf(classe))
        
    return allCenters

def areEquals(individu1, individu2) :
    if len(individu1) != len(individu2) :
        return False
    
    nbrAttr = len(individu1)
    
    for i in range(nbrAttr) :
        if individu1[i] != individu2[i] :
            return False
    
    return True


#this function return true if the two lists are equqls
#if True we will stop the algorithm
def centersAreBalanced(allCentersList1, allCentersList2) :
    if len(allCentersList1) != len(allCentersList2) :
        return False
    
    nbrOfCenters = len(allCentersList1)
    
    for i in range(nbrOfCenters) :
        if not areEquals(allCentersList1[i], allCentersList2[i]) :
                return False
    
    return True


#test if two individuals are in the same classe :
def inTheSameClasse(cluster, individu1, individu2) :
    print (getClasseIndexOf(cluster, individu1) == getClasseIndexOf(cluster, individu2))
    return getClasseIndexOf(cluster, individu1) == getClasseIndexOf(cluster, individu2)


#get the closest individual to a center
def getClosestIndividuTo(cluster, center, dataSetPrim) :
    minDistance = float("inf")
    
    for individu in dataSetPrim :
        if areEquals(center, individu) or inTheSameClasse(cluster, center, individu) :
            continue
        else :
            distance = getDistanceOf(center, individu)
            if distance < minDistance :
                minDistance = distance
                closestIndividu = individu
    
    return closestIndividu

#return True if the individual exist in the classe X
def isExistIn(classe, individu) :
    return individu in classe


#this function return the classe of an individual in the cluster
def getClasseIndexOf(cluster, individu) :
    for classe in cluster :
        if isExistIn(classe, individu) :
            return cluster.index(classe)
    
    return -1 #if the individual doesn't exist in any classe in the cluster

#remove individu
def removeIndividuFrom(cluster, individu) :
    classeIndex = getClasseIndexOf(cluster, individu)
    #if the individu exist in the cluster some where !
    if classeIndex != -1 :
        #getClasseIndfexOf return the index not the classe
        classe = cluster[classeIndex].remove(individu) #remove the individu from the classe by reference


def addIndividuTo(cluster, individu, actualClasseNum) :
    #if the individu doen't exist before, we add it
    if not isExistIn(cluster[actualClasseNum], individu) :
        cluster[actualClasseNum].append(individu) #add the individu in the classe number [actualClasseNum] in the cluster


def foo(cluster, listOfCenters, dataSetPrim) :
    minDistance = float("inf")
    closestInidividu = list()
    actualClasseNum = 0 #we start from the first classe in the cluster
    oldListOfCenters = list() #empty list in the begining ####not centersAreBalanced(oldListOfCenters, listOfCenters)
    #n=0
    
    while not centersAreBalanced(oldListOfCenters, listOfCenters) :
        actualClasseNum = 0
        for center in listOfCenters :
            closestIndividu = getClosestIndividuTo(cluster, center, dataSetPrim) #get the closest individual to this center
            print(closestIndividu, " is the closes to ", center, "\n")
            #if the induvidual doesn't exist before in the actualClasse we remove it from the old one and add it in the actual one
            if getClasseIndexOf(cluster, closestIndividu) != actualClasseNum :
                removeIndividuFrom(cluster, closestIndividu) #remove the individual from the cluster if exist in it
                addIndividuTo(cluster, closestIndividu, actualClasseNum) #add this indivdual to the cluster in the new classe
            
            print("cluster = ",cluster)
            actualClasseNum += 1 #pass to the next classe in the cluster
        
        oldListOfCenters = listOfCenters #remember the old list of centers
        listOfCenters = getAllCentersOf(cluster) #get the new centers
        #n += 1
        
    #print("***", oldListOfCenters, " *** \n")
    #print("***", listOfCenters, " ***")
    #print(listOfCenters, " new")
    #print(actualClasseNum, " num classe")



#main
file = open("iris.csv", "r")
lines = csv.reader(file)
dataSet=list(lines)

dataSetPrim=list()
cluster=list()
listOfCenters=list()
k=3

prepareDataSet(dataSet, dataSetPrim)
print("dataPrim = ", dataSetPrim)
initCluster(cluster, listOfCenters, dataSetPrim, k)
#print(cluster)
print("init cluster = ", cluster, "\n")


foo(cluster, listOfCenters, dataSetPrim)

#print("After a will : \n", cluster)



