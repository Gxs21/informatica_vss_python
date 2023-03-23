from classe_supporto import supporto
from classe_lettore_CD_DVD import lettore

def main():
    supporto1= supporto(34, "davide", "gemitaiz", 13, "CD", 95, 2018)
    supporto2= supporto(31, "scatola nera", "gemitaiz", 14, "cd", 89, 2020)
    supporto1.toString()
    print (supporto1.confronta(supporto2))
    lettore1= lettore("Re di Roma", 300)
    lettore1.add_supporto(supporto1)
    print(lettore1.get_nr_CD_DVD())
    print(lettore1.add_to_pos(supporto2, 1))
    lettore1.kill_supporto(34)
    lettore1.add_supporto(supporto2)
    lettore1.cerca_supporto("scatola nera")
main()