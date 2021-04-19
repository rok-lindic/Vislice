import random
#konstante
stevilo_dovoljenih_napak=10

PRAVILNA_CRKA='+'
PONOVLJENA_CRKA='o'
NAPACNA_CRKA='-'

ZMAGA='W'
PORAZ='L'

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() #pravilno geslo
        #kar je uporabnik do sedaj uganil
        self.crke = crke.upper() #do sedaj ugibane črke
        #samo velike crke


    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]
    
    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > stevilo_dovoljenih_napak
    
    def zmaga(self):
        return all([i in self.crke for i in self.geslo])

    def pravilni_del_gesla(self):
        rezultat=''
        for c in self.geslo:
            if c in self.crke:#smo uganili
                rezultat+=c
            else:#nismo še uganili
                rezultat+='_'
        return rezultat
    def nepravilni_ugibi(self):
        return ''.join(self.napacne_crke())
    
    def ugibaj(self,crka):
        crka=crka.upper()
        if self.poraz():
            return PORAZ
        
        if crka in self.crke:
            return ponovljena_crka
        if crka not in self.crke:
            self.crke += crka

        if self.zmaga():
            return ZMAGA
        if crke in self.geslo:
            return PRAVILNA_CRKA
        if self.poraz():
            return PORAZ
        return NAPACNA_CRKA


    bazen_besed=[]
    
    with open('besede.txt', encoding='utf-8') as input_file:
        bazen_besed = input_file.readlines()
    def nova_igra(bazen_besed):
        beseda = random.choice(bazen_besed)

        return Igra(beseda, '')

