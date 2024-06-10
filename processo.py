from lavoratori import convert_employee_data, get_employee
from autogui import ask_days, ask_name, scrivi, down, tab, big_left
import time
from causali import causali

employee_data = convert_employee_data("PRESENZE REWORK.xlsx")

def the_process():

    name = ask_name()
    giorni = ask_days()

    worker = get_employee(employee_data, name=name)
    print(worker["lavorate"])

    giustif = [] #qui si accumulano i nominativi (ex: a_Ordinario)

    for key in worker["lavorate"]:
        giustif.append(key)
    print(giustif)

    time.sleep(2)


    for i in range(giorni): #g è a_ord, i è il numero del giorno
        for g in giustif: 
            x = worker["lavorate"][g][i] #setuppato il loop per row after row
            print(f"{g}: {x}")
            if g == "a_Ordinario": #g è giustificativo, x è il valore
                scrivi(str(x))
                tab()
                tab()
            elif g in causali.keys():
                if x == 0:
                    pass
                else:
                    sigla = causali.get(g) #recupera il valore della causale
                    scrivi(str(sigla))
                    print(str(sigla))
                    tab()
                    scrivi(str(x))
                    print(str(x))
                    tab()
            else:
                pass
        big_left() # dovrebbe riportare alla casella a sx delle ordinarie
        scrivi(str(worker["lavorate"]["a_Ordinario"][i])) # riscrive il valore solo a causa delle ferie etc
        down() 

the_process()