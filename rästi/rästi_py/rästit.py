from ast import Load
from json import load
import pickle
 
class save_load():
    def __init__(self, param):
        self.param = param
 
def save_rastit(obj):
    try:
        with open("rastit.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        pass

def save_opettaja(obj):
    try:
        with open("opettaja.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        pass

def load_rastit(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        pass

def load_opettaja(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        pass

def append_load_to_list():
    load_rastit_tiedosto = load_rastit("rastit.pickle")
    load_opettaja_tiedosto = load_opettaja("opettaja.pickle")

    if(load_rastit_tiedosto == None):
        print("\tSinulla ei ollut mitään tallennuksia.\n")
        pass

    elif not load_rastit_tiedosto.param:
        print("\tSinulla ei ollut mitään tallennuksia.\n")
        pass

    else:
        for i in load_rastit_tiedosto.param:
            rastit.append(i)

        for i in load_opettaja_tiedosto.param:
            opettaja.append(i)

    print("\tNyt kaikki sinun edeliset tiedot on saatavilla ;)\n")
 

rastit = []
opettaja = []
run_once = 0

while True:

    Mita_tehdaan = str(input("Mitä tehdään?!\n\t1.Näyttää rästit.\n\t2.Lisää rästi.\n\t3.Poistaa rästit.\n\t4.Suljee ohjelma\n\t5.Lataa edelliset tiedot.\n\t------------------\n\t\t"))
    print("")

    if(Mita_tehdaan == "1"):
        if not rastit:
            print("\tHyvää olet tehnyt kaikki rästit! :D\n")
        
        else:
            listnum = 0
            while(listnum < len(rastit)):
                print(f"\tRästi: {rastit[listnum]}\n\topettaja: {opettaja[listnum]}")
                print("\t-------------------\n")
                listnum += 1
    
    elif(Mita_tehdaan == "2"):
        rastit.append(input("\tKirjoittaa rästin nimi: "))
        
        opettaja.append(input("\tKirjoittaa opettajan nimi: "))
        
        print(f"\n\tRästi ja opettaja on lisätty!\n")

    elif(Mita_tehdaan == "3"):
        if not rastit:
            print("\tRästi ei ole saatavilla! Lisää rästi.\n")
        
        else:
            listnum = 0
            while(listnum < len(rastit)):
                print(f"{listnum + 1}-\tRästi: {rastit[listnum]}\n\topettaja: {opettaja[listnum]}\n")
                listnum += 1
            
            try:
                poistaa_nro = int(input("\tMikä rästi haluaisit poistaa?(Kirjoittaa rästin numero): ")) - 1
                rastit.pop(poistaa_nro)
                opettaja.pop(poistaa_nro)

                print("\n\tRästi poistettu!\n")
            
            except ValueError:
                print("\n\tOho! Jotain meni pieleen :(\n\tValitsee yhden rästin numero.\n")

    elif(Mita_tehdaan == "4"):
        rastitSaveList = save_load(rastit)
        opettajaSaveList = save_load(opettaja)

        save_rastit(rastitSaveList)
        save_opettaja(opettajaSaveList)

        print("Kiitos että valitsisitte meidän ohjelma! See u soon =)♡")
        break

    elif(Mita_tehdaan == "5"):
        if run_once == 1:
            print("\tOlet jo ladannut kaikki tiedot, ei tarvitsee kaksi kertaa lataa.\n")
            
        elif run_once == 0:
            append_load_to_list()
            run_once = 1
        else:
            print("\tOho! Jotain meni pieleen :(\n")
            
        

    else:
        print("\tOho! Jotain meni pieleen :(\n\tValitsee yhden numeroista mitä ylhällä näytettiin.\n")
