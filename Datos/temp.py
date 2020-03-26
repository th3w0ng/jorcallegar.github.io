# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


import pandas as pd
import matplotlib as mp
import sklearn as sk
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import date
import re
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
import math as m
import numpy

dfAndalucia=pd.read_excel('datoscovid24.xlsx')
dfAragon=pd.read_excel('datoscovid24.xlsx')
dfAsturias=pd.read_excel('datoscovid24.xlsx')
dfCantabria=pd.read_excel('datoscovid24.xlsx')
dfCeuta=pd.read_excel('datoscovid24.xlsx')
dfCastillaYLeon=pd.read_excel('datoscovid24.xlsx')
dfCastillaLaMancha=pd.read_excel('datoscovid24.xlsx')
dfCanarias=pd.read_excel('datoscovid24.xlsx')
dfCataluña=pd.read_excel('datoscovid24.xlsx')
dfExtremadura=pd.read_excel('datoscovid24.xlsx')
dfGalicia=pd.read_excel('datoscovid24.xlsx')
dfBaleares=pd.read_excel('datoscovid24.xlsx')
dfMurcia=pd.read_excel('datoscovid24.xlsx')
dfMadrid=pd.read_excel('datoscovid24.xlsx')
dfMelilla=pd.read_excel('datoscovid24.xlsx')
dfNavarra=pd.read_excel('datoscovid24.xlsx')
dfPaisVasco=pd.read_excel('datoscovid24.xlsx')
dfLaRioja=pd.read_excel('datoscovid24.xlsx')
dfComunidadValenciana=pd.read_excel('datoscovid24.xlsx')



###Datos Andalucia### 1
j=0
for i in dfAndalucia['ISO']:
    if(i!="AN"):
        dfAndalucia.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Aragon### 2
j=0
for i in dfAragon['ISO']:
    if(i!="AR"):
        dfAragon.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Asturias### 3
j=0
for i in dfAsturias['ISO']:
    if(i!="AS"):
        dfAsturias.drop([j], inplace=True)
        
    
    j=j+1;

###Datos Cantabria### 4
j=0
for i in dfCantabria['ISO']:
    if(i!="CB"):
        dfCantabria.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Ceuta### 5
j=0
for i in dfCeuta['ISO']:
    if(i!="CE"):
        dfCeuta.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos CastillaYLeon### 6
j=0
for i in dfCastillaYLeon['ISO']:
    if(i!="CL"):
        dfCastillaYLeon.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos CastillaLaMancha### 7
j=0
for i in dfCastillaLaMancha['ISO']:
    if(i!="CM"):
        dfCastillaLaMancha.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Canarias### 8
j=0
for i in dfCanarias['ISO']:
    if(i!="CN"):
        dfCanarias.drop([j], inplace=True)
        
    
    j=j+1;
    
    
###Datos Cataluña### 9
j=0
for i in dfCataluña['ISO']:
    if(i!="CT"):
        dfCataluña.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Extremadura### 10
j=0
for i in dfExtremadura['ISO']:
    if(i!="EX"):
        dfExtremadura.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos IslasBaleares### 11
j=0
for i in dfBaleares['ISO']:
    if(i!="IB"):
        dfBaleares.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Galicia### 12
j=0
for i in dfGalicia['ISO']:
    if(i!="GA"):
        dfGalicia.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos ComunidadValenciana###13
j=0
for i in dfComunidadValenciana['ISO']:
    if(i!="VC"):
        dfComunidadValenciana.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Melilla###14
j=0
for i in dfMelilla['ISO']:
    if(i!="ME"):
        dfMelilla.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Murcia###15
j=0
for i in dfMurcia['ISO']:
    if(i!="MC"):
        dfMurcia.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Madrid###16
j=0
for i in dfMadrid['ISO']:
    if(i!="MD"):
        dfMadrid.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Navarra##17#
j=0
for i in dfNavarra['ISO']:
    if(i!="NC"):
        dfNavarra.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Pais vasco###18
j=0
for i in dfPaisVasco['ISO']:
    if(i!="PV"):
        dfPaisVasco.drop([j], inplace=True)
        
    
    j=j+1;
    
###Datos Riojaa###
j=0
for i in dfLaRioja['ISO']:
    if(i!="RI"):
        dfLaRioja.drop([j], inplace=True)
        
    j=j+1;
    
############################################################################
#Vamos a comenzar  a dibujar
    
plt.figure()
plt.scatter(dfAndalucia.index,dfAndalucia['Casos'])
plt.show()

