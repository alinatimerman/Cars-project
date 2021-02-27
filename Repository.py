from Plane import *
from Passenger import *
from Recursion import *
class Repository():
    def __init__(self):
        self.__listOfPlane=[]
        
    def addPlane(self,num,company, numSeats,destination,list):
        passengerList=[]
        if len(list)>int(numSeats):
            raise ValueError
        else:
            for i in range(0,len(list)):
                p=Passenger(list[i][0],list[i][1],list[i][2])
                passengerList.append(p)
            p=Plane(num,company,numSeats,destination,passengerList)
            self.__listOfPlane.append(p)
    
    def getAll(self):
        for i in range(0,len(self.__listOfPlane)):
            print(self.__listOfPlane[i])
            
    def updatePlane(self,num,company, numSeats,destination,list):
        passengerList=[]
        for i in range(0,len(self.__listOfPlane)):
            if num==self.__listOfPlane[i].getNumber():   
                self.__listOfPlane[i].setCompany(company)
                self.__listOfPlane[i].setNumberSeats(numSeats)
                self.__listOfPlane[i].setDestination(destination)
                for j in range(0,len(list)):
                    p=Passenger(list[j][0],list[j][1],list[j][2])
                    passengerList.append(p)
                self.__listOfPlane[i].setList(passengerList) 
                
    def updatePassengerList(self,num,list):
        passengerList=[]
        for i in range(0,len(list)):
                    p=Passenger(list[i][0],list[i][1],list[i][2])
                    passengerList.append(p)
        for i in range(0,len(self.__listOfPlane)):
            if num==self.__listOfPlane[i].getNumber():
                self.__listOfPlane[i].setList(passengerList)
                
    def updatePassenger(self,num, index,list):
        for i in range(0,len(self.__listOfPlane)):
            if num==self.__listOfPlane[i].getNumber():
                p=Passenger(list[0],list[1],list[2])
                self.__listOfPlane[i].updateToList(index,p)
    
    def deletePassengerRepo(self,plane,index):
        self.__listOfPlane[plane].deletePassenger(index)
        
    def deletePlane(self,plane):
        del self.__listOfPlane[plane]
    '''
    Sort the passengers in a plane by last name
    '''
    
           
    def sortPassengerByLastNameR(self,index):
        self.__listOfPlane[int(index)].sortPassengerByLastName()
    '''
    Sort planes according to the number of passengers
    '''
    def sortPlanesByNrPassenger(self,l):
        for i in range(0, len(l) - 1):
            min_pos = i
            for j in range(i + 1, len(l)):
                if l[j].getLenList() < l[min_pos].getLenList():
                    min_pos = j
            if (i < min_pos):
                aux = l[i]
                l[i] = l[min_pos]
                l[min_pos] = aux
        return l   
    
    def sortPlaneByNrPassengerR(self):
        self.__listOfPlane=self.sortPlanesByNrPassenger(self.__listOfPlane)
    '''
    Sort planes according to the number of passengers with the first name starting with a given substring
    '''
    def getNrPlanesStartWithAStr(self,str):
        list=[]
        for i in range(0,len(self.__listOfPlane)):
            count=0
            l=self.__listOfPlane[i].getList()
            for j in range(0, len(l)):
                if l[j].getFirstName().startswith(str):
                    count+=1
            list.append(count)
        return list
        
                
    def sortPlanesByNrPassengerStartWithString(self,str):
        list=self.getNrPlanesStartWithAStr(str)
        for i in range(0, len(list)-1):
            for j in range(i+1,len(list)):
                if list[i]>list[j]:
                    list[i],list[j]=list[j],list[i]
                    self.__listOfPlane[i], self.__listOfPlane[j]=self.__listOfPlane[j],self.__listOfPlane[i]
    '''
    Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
    '''
    def getConcatOfNumAndDest(self):
        list=[]
        for i in range(0,len(self.__listOfPlane)):
            concat=self.__listOfPlane[i].getNumber()+self.__listOfPlane[i].getDestination()
            list.append(concat)
        return list
                      
    def sortPlanesByConcat(self):
        list=self.getConcatOfNumAndDest()
        for i in range(0, len(list)-1):
            for j in range(i+1,len(list)):
                if list[i]>list[j]:
                    list[i],list[j]=list[j],list[i]
                    self.__listOfPlane[i], self.__listOfPlane[j]=self.__listOfPlane[j],self.__listOfPlane[i]
    '''
    Identify planes that have passengers with passport numbers starting with the same 3 letters
    '''
    def getPlanesStartPassWithSame3(self):
        l=[]
        for i in range(0,len(self.__listOfPlane)):
            list=self.__listOfPlane[i].getList()
            letters=list[0].getPassport()[0:3]
            #print(letters)
            check=True
            for j in range(1,len(list)):
                if not list[j].getPassport().startswith(letters):
                    check=False
            if check==True:
                #print(self.__listOfPlane[i])
                l.append(self.__listOfPlane[i])
        return l
    '''
    Identify passengers from a given plane for which the first name or last name contain a string given as parameter
    '''                
    def getPassengerWithStringinFirstorLastName(self, index,str):
        l=[]
        for i in range(0 , len(self.__listOfPlane[int(index)].getList())):
            if (str in self.__listOfPlane[int(index)].getList()[i].getFirstName()) or (str in self.__listOfPlane[int(index)].getList()[i].getLastName()):
                #print(self.__listOfPlane[int(index)].getList()[i])
                l.append(self.__listOfPlane[int(index)].getList()[i])
        return l        
    '''
    Identify plane/planes where there is a passenger with given name
    '''    
    def getPlaneWithPassengerWithGivenName(self,fname,lname):
        l=[]
        for i in range(0,len(self.__listOfPlane)):
            list=self.__listOfPlane[i].getList()
            for j in range(0,len(list)):
                if (list[j].getFirstName()==fname) and (list[j].getLastName()==lname):
                    #print(self.__listOfPlane[i])
                    l.append(self.__listOfPlane[i])    
        return l
    def Recursion1R(self,index,k):
        self.__listOfPlane[index].Recursion1(k)
        
    def Recursion2R(self,k):
        printCombination(self.__listOfPlane, len(self.__listOfPlane), k)    
        
        
        
        
        
        
        
        
        
        
        