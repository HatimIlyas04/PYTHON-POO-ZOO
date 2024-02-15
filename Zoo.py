class Animal:
    __Code = 0
    __NomS = ""
    __Espece = ""
    __Age = 0
    __PaysOr = ""
    
    def __init__(self , Code , NomS , Espece , Age , PaysOr):
        self.__Code = Code
        self.__NomS = NomS
        self.__Espece = Espece
        self.__Age = Age
        self.__PaysOr = PaysOr
    
    
    def getCode(self):
        return self.__Code
    def setCode(self , Value):
        self.__Code = Value
        
    def getNomS(self):
        return self.__NomS
    def setNomS(self , Value):
        self.__NomS = Value
        
    def getEspece(self):
        return self.__Espece
    def setEspece(self , Value):
        self.__Espece = Value
    
    def getAge(self):
        return self.__Age
    def setAge(self , Value):
        if Value > 0:
            return self.__Age
        else:
            raise Exception("age invalid")
        
    def getPaysOr(self):
        return self.__PaysOr
    def setPaysOr(self , Value):
        self.__PaysOr = Value
        
    def AfficherInfo(self):
        print(f"Le code : {self.__Code}")
        print(f"Le nom scientifique : {self.__NomS}")
        print(f"L espece : {self.__Espece}")
        print(f"L'age  : {self.__Age}")
        print(f"Le pays d'origine:{self.__PaysOr}")
        
class Zoo:
    __ListAnm = []        
    __Nom = ""
    __Superficie = ""
    
    def __init__(self , ListAnm , Nom , Superficie):
        self.__ListAnm = ListAnm
        self.__Nom = Nom
        self.__Superficie = Superficie
        
    def AjoueterAnm(self , NvAnimal):
        self.__ListAnm.append(NvAnimal)
        
    def SupprimerAnm(self , Animal):
        self.__ListAnm.remove(Animal)
        
    def AfficherM(self):
        print(f"La liste des animaux:" , {self.__ListAnm})
        print(f"Le Nom :" , {self.__Nom})
        print(f"Le superficie:" , {self.__Superficie})
        
# A1 = Animal(123 , "lien" , "jrada" , 12 , "Maldive")
# A1.AfficherInfo()

Z1 = Zoo(["Dyen , Azer ,Qsdf , HTR" ] , "Zagoura" , "HAHA")
Z1.AjoueterAnm("KSIDA")
Z1.AfficherM()
