from math import floor
from msilib.schema import SelfReg
from random import random
import random

class pocketMonster :
    def __init__(self, name, life, strenght, defense, type) :
        self.__monsterName = name
        self.__monsterPV = life
        self.__monsterPVMAX = life
        self.__monsterStr = strenght
        self.__monsterDef = defense
        self.__monsterType = type

    def getName(self):
        return self.__monsterName

    def getPv(self):
        return self.__monsterPV

    def getAtk(self):
        return self.__monsterStr

    def getDef(self):
        return self.__monsterDef

    def getType(self):
        return self.__monsterType
        
    def regen(self):
        rand = random.randint(1, 6)
        if(self.__monsterPVMAX < self.__monsterPV + rand * (self.__monsterPV)/10):
            self.__monsterPV = self.__monsterPVMAX
        else :
            self.__monsterPV = self.__monsterPV + rand * (self.__monsterPV)/10
        
        return print(self.__monsterName,"se repose et récupère de la vie. Il retourne à",self.__monsterPV,"PV")

    def compareTypes(self, ennemiType):
        if((ennemiType == "Feu" and self.__monsterType == "Plante") or (ennemiType == "Eau" and self.__monsterType == "Feu") or (ennemiType == "Plante" and self.__monsterType == "Eau")):
            return 1
        else :
            return 2
    
    def pvLost(self, ennemiAtk, type):
        if(0 > ennemiAtk - self.__monsterDef) :
            if(type == 1) :
                self.__monsterPV = self.__monsterPV-2
                return print("C'est super efficace !")
            else :
                self.__monsterPV = self.__monsterPV-1
                
        else :
            if(type == 1):
                self.__monsterPV = (self.__monsterPV - ennemiAtk)*2
                return print("C'est super efficace !")
            else :
                self.__monsterPV = self.__monsterPV - ennemiAtk
                

class moveSet :
    def __init__(self,name,power,type,txt):
        self.__atkName = name
        self.__atkPower = power
        self.__atkType = type
        self.__atkTxt = txt
    
    def getAtkName(self):
        return self.__atkName

    def getAtkPower(self):
        return self.__atkPower

    def getAtkType(self):
        return self.__atkType

    def getAtkTxt(self):
        return self.__atkTxt
    

Tyty = pocketMonster("Tyty", 25,10,36,"Feu")
TytyMoveSet = {
    "1-" : moveSet("Briquet",50,"Feu","Votre monstre utilise son fidèle briquet pour brûler son adversaire."),
    "2-" : moveSet("Bec",40,"Normal","Votre monstre possède un bec solide, son adversaire s'apprête à le découvrir."),
    "3-" : moveSet("Plume enflammée",70,"Feu","Votre monstre s'attaque à son adversaire avec des plumes aussi tranchantes que brûlante."),
    "4-" : moveSet("Serre acérées",80,"Normal","Votre monstre possède des serres plutôt dangereuse.")
}
Grominet = pocketMonster("Silvestre",50,25,12,"Plante")
GrominetMoveSet = {
    "1-" : moveSet("Briquet",50,"Feu","Votre monstre utilise son fidèle briquet pour brûler son adversaire."),
    "2-" : moveSet("Bec",40,"Normal","Votre monstre possède un bec solide, son adversaire s'apprête à le découvrir."),
    "3-" : moveSet("Plume enflammée",70,"Feu","Votre monstre s'attaque à son adversaire avec des plumes aussi tranchantes que brûlante."),
    "4-" : moveSet("Serre acérées",80,"Normal","Votre monstre possède des serres plutôt dangereuse.")
}

print("Un monstre apparaît ! C'est un" , Grominet.getName() , "sauvage, vite" , Tyty.getName() , "en avant !")
while(Tyty.getPv()>0 and Grominet.getPv()>0):
    
    choixE = random.randint(1, 2)
    if(choixE == 1):
        Grominet.regen()
    else :
        print("Le", Grominet.getName(), "attaque !")
        Tyty.pvLost(Grominet.getAtk(),Tyty.compareTypes(Grominet.getType()))
        print(Tyty.getName(), "subit des dégâts, il reste" , Tyty.getPv() , "PV à votre monstre.") 

    print("C'est au tour de votre monstre.")
    choixJ = input("Que voulez-vous faire ? 1-Vous soigner 2-Attaquer : ")
    if(choixJ == '1'):
        Tyty.regen()
    else :
        print(Tyty.getName(),"attaque !")
        Grominet.pvLost(Tyty.getAtk(),Grominet.compareTypes(Tyty.getType()))
        print("Le" ,Grominet.getName(), "sauvage subit des dégâts, il lui reste" , Grominet.getPv() , "PV.") 
