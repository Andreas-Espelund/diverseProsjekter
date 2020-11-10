
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
        streng += 'Pris: '+self._gjeldandePris+'   Rabatt: '+self._Veilpris-self._gjeldandePris+'\n'

    def open(self):
        webbrowser.open(self._lenke)



webbrowser.open('https://www.finn.no/bap/forsale/ad.html?finnkode=197443473')
    
