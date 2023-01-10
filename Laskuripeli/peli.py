'''
Python-ohjelmoinnin perusteet
Kesä/Syksy2022
(C) Hanna Maksimainen
DTNS21
'''

#Importataan kirjastot, joita käytetään
import json #JSON tiedoston käsittelyyn
import random #Numeroiden arpomiseen
import time #Pelin kysymysten ja tietojen tauotus

print() #Tulostettaa tyhjä rivi, jotta ohjeiden lukeminen on selkeämpää

try: # Toteutetaan try-except poikkeusten keräys, antaa virheen, jos jokin ei toimi
    f = open( 'peliohjeet.json', 'r' ) # Avataan json tiedosto, josta löytyy ohjeet pelaamiseen
    data = json.load( f )
    print(data) # Tulostetaan data ulos 
except json.decoder.JSONDecodeError as poikkeustieto:
    print("Meni ihan metsään!") #Tulostus, jos ei toimi
    print(poikkeustieto)
except:
    print("Virhettä pukkaa!") #Tulostus, jos ei toimi
finally: #Yhteyden sulkeminen
    print() #Tulostettaa tyhjä rivi, jotta ohjeiden lukeminen on selkeämpää
    print("ONNEA PELIIN!")
    print() #Tyhjä rivi
    time.sleep(3) #Tauotetaan aloitusta

pelaaja = str(input("Hei! \nAnna nimesi: ")) #Kysytään käyttäjältä nimimerkki, jolla pelaa
time.sleep(1) #Tauotetaan aloitusta
print() #Tyhjä rivi
time.sleep(2) #Tauotetaan aloitusta
print("Hei,", pelaaja,"! \nAloitetaan peli! Pelissä tulee yhteen-, kerto-ja vähennyslaskuja.") #Ilmoitetaan pelin aloittanisesta
print() #Tyhjä rivi
time.sleep(2) #Tauotetaan aloitusta

for i in range(5): #Tehdään for-loop, joka toistaa eri järjestyksessä laskuja

    def plussaLasku(): #Funktio yhteenlaskuille, palauttaa tuloksen.
        luku1 = random.randint(1,10) #Arvotaan luvut randomilla 1-10 välillä
        luku2 = random.randint(1,10) #Arvotaan luvut randomilla 1-10 välillä

        print("Paljonko on ", luku1, "+", luku2,"?") #Käyttäjälle näytettävä laskutoimitus
   
        vastaus = int(input("Vastaus:")) #Input käyttäjän vastaukselle

        if vastaus != luku1+luku2: #If-else rakenne, ilmoittaa onko tulos oikein vai väärin
            print("VÄÄRÄ VASTAUS!\nOikea vastaus on", luku1+luku2,"!") #Ilmoitetaan käyttäjälle, että vastaus on väärin sekä oikea tulos.
            print() #Tyhjä rivi
            return #Palautetaan arvo

        else:
            print("OIKEA VASTAUS!\nHienosti menee!") #Ilmoitetaan käyttäjälle, että vastaus on oikein
            print() #Tyhjä rivi
            return #Palautetaan arvo

    def miinuLasku(): #Funktio vähennyslaskuille, palauttaa tuloksen.
        luku3 = random.randint(5,10) #Arvotaan luvut randomilla 5-10 välillä
        luku4 = random.randint(1,5) #Arvotaan luvut randomilla 1-5 välillä

        print("Paljonko on ", luku3, "-", luku4,"?") #Käyttäjälle näytettävä laskutoimitus

        vastaus = int(input("Vastaus:")) #Input käyttäjän vastaukselle

        if vastaus != luku3-luku4: #If-else rakenne, ilmoittaa onko tulos oikein vai väärin
            print("VÄÄRÄ VASTAUS!\nOikea vasta us on", luku3-luku4,"!") #Ilmoitetaan käyttäjälle, että vastaus on väärin sekä oikea tulos.
            print() #Tyhjä rivi 
            return #Palautetaan arvo

        else:
            print("OIKEA VASTAUS!\nJatka samaan malliin!") #Ilmoitetaan käyttäjälle, että vastaus on oikein
            print() #Tyhjä rivi
            return #Palautetaan arvo

    def kertoLasku(): #Funktio kertolaskulle, palauttaa tuloksen.
        luku5 = random.randint(1,5) #Arvotaan luvut randomilla 1-5 välillä
        luku6 = random.randint(1,10) #Arvotaan luvut randomilla 1-10 välillä

        print("Paljonko on ", luku5, "*", luku6,"?") #Käyttäjälle näytettävä laskutoimitus
   
        vastaus = int(input("Vastaus:")) #Input käyttäjän vastaukselle

        if vastaus != luku5*luku6: #If-else rakenne, ilmoittaa onko tulos oikein vai väärin
            print("VÄÄRÄ VASTAUS!\nOikea vastaus on", luku5*luku6,"!") #Ilmoitetaan käyttäjälle, että vastaus on väärin sekä oikea tulos.
            print() #Tyhjä rivi 
            return #Palautetaan arvo

        else:
            print("OIKEA VASTAUS!\nMahtavaa!") #Ilmoitetaan käyttäjälle, että vastaus on oikein
            print() #Tyhjä rivi 
            return #Palautetaan arvo

    # Tulostetaan funktiot ja käyttäjä pääsee pelaamaan yhteen-, vähennys-ja kertolaskuja
    plussaLasku()
    miinuLasku()
    kertoLasku()
    
def lisaPeli(): #Funktio lisäpelille, kertolaskuja
    for i in range(5): #Tehdään for-loop, joka toistaa eri järjestyksessä laskuja

        luku5 = random.randint(5,10) #Arvotaan luvut randomilla 5-10 välillä
        luku6 = random.randint(1,5) #Arvotaan luvut randomilla 1-5 välillä
 
        print("Paljonko on ", luku5, "*", luku6,"?") #Käyttäjälle näytettävä laskutoimitus
   
        vastaus = int(input("Vastaus:")) #Input käyttäjän vastaukselle

        if vastaus != luku5*luku6: #If-else rakenne, ilmoittaa onko tulos oikein vai väärin
            print("VÄÄRÄ VASTAUS!\nOikea vastaus on", luku5*luku6,"!") #Ilmoitetaan käyttäjälle, että vastaus on väärin sekä oikea tulos.
            print() #Tyhjä rivi 

        else:
            print("OIKEA VASTAUS! Olet hyvä tässä!") #Ilmoitetaan käyttäjälle, että vastaus on oikein
            print() #Tyhjä rivi 

uusiPeli = str(input("PSSSTTT.... Haluatko pelata vielä lisäpelin kertolaskuja? Paina y jos haluat, e jos et halua: ")) # Kysytään käyttäjältä, haluaako vielä jatkaa pelaamista vai lopettaa

def jatko(): #Funktio pelin jatkamiseen
    if uusiPeli == "y": # If-else lause, jos vastaa y, peli jatkuu, jos vastaa e, peli päättyy
        lisaPeli()
        pass
    else:
        pass  
    
jatko() # Tulostetaan funktio

# Json formaatti
k = '''
    "KIITOS PELAAMISESTA!",
    "PELI LOPPUU NYT!"

'''
print(k)