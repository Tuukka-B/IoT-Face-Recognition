# IoT Face Recognition

## Tekijät

* Samson Azizyan (M3156), Arttu Häyrynen (M3350), Tuukka Bordi (M2296), Jaber Askari (M2947)
* Versionumero 0.2


## Sisällysluettelo 

* [Vaatimusmäärittely](#vaatimusmäärittely)
    * [Järjestelmän yleiskuvaus](#järjestelmän-yleiskuvaus)
    * [Kohdeyleisö](#kohdeyleisö)
    * [Käyttöympäristö ja käytetyt teknologiat](#käyttöympäristö-ja-käytetyt-teknologiat)
    * [Komponentit](#komponentit)
    * [Käyttäjäroolit](#käyttäjäroolit)
    * [Ominaisuudet](#ominaisuudet)
    * [Käyttötapaukset](#käyttötapaukset)
    * [Hyväksyntätestit](#hyväksyntätestit)
    * [Käsitemalli](#käsitemalli)
    * [Luokkakaavio](#luokkamalli)
    * [Työnjako](#työnjako)
    * [Työaikasuunnitelma](#työaika-suunnitelma)
* [Loppuraportti](#loppuraportti)
    * [Asennus](#asennus)
    * [Tetoa ohjelmasta](#tietoa-ohjelmasta)
    * [Kuvaruutukaappaukset](#kuvaruutukaappaukset)
    * [Mukana tulevat tiedostot](#mukana-tulevat-tiedostot)
    * [Tietokanta](#tietokanta)
    * [Ongelmat, jatkokehitysideat](#ongelmat-jatkokehitysideat)
    * [Työmäärä](#työmäärä)
    * [Yhteenveto](#yhteenveto)


# Vaatimusmäärittely

## Järjestelmän yleiskuvaus

[Linkki projekti-ideaan](https://project.seeedstudio.com/SeeedStudio/face-recognization-smart-lock-with-lte-pi-hat-abcec9)

Suunnitelemamme järjestelmä on Raspberry Pi:n pohjalle kameramoduulin avulla toteutettu kasvojentunnistusjärjestelmä. Tähän järjestelmään on liitettynä ESP32 -moduuli, jonka avulla saamme lisättyä järjestelmään langattomia toiminnallisuuksia. Projekti voi laajentua ja tominnalisuudet lisääntyä, jos näyttää siltä, että tähän on aikaa.


## Kohdeyleisö

## Käyttöympäristö ja käytetyt teknologiat

Projekti vaatii seuraavat Linux-kirjastot: 
* build-essential
* cmake 
* gfortran 
* git 
* wget 
* curl 
* graphicsmagick 
* libgraphicsmagick1-dev 
* libatlas-dev 
* libavcodec-dev 
* libavformat-dev 
* libboost-all-dev 
* libgtk2.0-dev 
* libjpeg-dev 
* liblapack-dev 
* libswscale-dev 
* pkg-config 
* python3-dev 
* python3-numpy 

Python-komponenteista tarvitsemme nämä:

* https://github.com/ageitgey/face_recognition.git - python-kirjasto, jota käytämme kasvojen tunnistamiseen
* GPIO -kirjasto, jota käytetään GPIO-pinnien ohjaukseen
* picamera -kirjasto kameran ohjaukseen
* PIL / Image -kirjastoa kuvan esittämiseen näytöllä tunnistautumisen yhteydessä

Muita valinnaisia kirjastoja, joista saattaa olla hyötyä: time, os, numpy, matplotlib.pyplot

Lisäksi käytämme tunnettuja Python-kirjastoja ESP32:n ohjaukseen

## Komponentit

<img src="files/blueprint.jpg" alt="Face recognition tech">

* Raspberry Pi 3 Model B
* Raspberry Pi Camera Module
* [Grove - Relay](https://project.seeedstudio.com/products/grove-relay)
* ESP32

## Käyttäjäroolit

## Ominaisuudet

## Käyttötapaukset

## Hyväksyntätestit

## Käsitemalli

## Luokkakaavio

## Työnjako

## Työaikasuunnitelma

<br><br>

# Loppuraportti

## Asenus

## Kuvaruutukaapaukset

## Tietokanta

## Ongelmat, jatkokehitysideat

## Työmäärä

## Yhteenveto


* Yleinen selostus
* Koodi
* Komponentit
* Vaiheet
    * Kasvojentunnistus, SMS-kuluvalvonta
* Extravaiheet
    * Smart home   
    * Komponentit: wlan-kytkimiä
    * kaksivaiheinen tunnistautuminen / sms
    * kuva ja lupa sovelluksen avulla