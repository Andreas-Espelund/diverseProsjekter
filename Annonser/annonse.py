
import webbrowser
class Annonse:
    def __init__(self,tittel,opprettaDato,VeilPris,lenke):
        self._tittel = tittel
        self._opprettaDato = opprettaDato
        self._Veilpris = VeilPris
        self._gjeldandePris = VeilPris
        self._lenke = lenke

    def __str__(self):
        streng = '----'+self._tittel+'----'+'\n'
        streng +='Oppretta: '+self._opprettaDato+'\n'
        streng += 'Pris: '+str(self._gjeldandePris)+'   Rabatt: '+str(self._Veilpris-self._gjeldandePris)+'\n'
        return streng
    def open(self):
        webbrowser.open(self._lenke)

    def endrePris(self,nypris):
        self._pris = nypris

    def hentPris(self):
        return self._pris


test= Annonse('Ram','10.11.20',800,'https://www.finn.no/bap/forsale/ad.html?finnkode=197443473')

print(test)

test.open()
