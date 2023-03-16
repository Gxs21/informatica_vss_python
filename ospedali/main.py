from classe_ospedale import ospedale
from classe_paziente import paziente
def main():

    paziente1= paziente(1, "sogno", "morfeo", "narcolessia", "rosso")

    ospedale1=ospedale("sognatori", "casarano", 300)

    ospedale1.aggiungiPazienti(paziente1)

    ospedale1.modificaCodicePaziente("sogno")
main()