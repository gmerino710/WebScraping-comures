from requests import get
from bs4 import BeautifulSoup
import glob
import sys
from impresion import imprimir
import pandas as pd

nombree="Municipalidades Agremiadas 2015 - 2018"
link= "http://www.comures.org.sv/html/agremiados/listado_2018.html"
page_content =open("COMURES __ Agremiados.html",encoding="utf-8-sig")
soup = BeautifulSoup(page_content, "html.parser")
titulos = soup.find_all(class_="titnegro")
tabla = soup.find("table", class_="paco")
trs = tabla.find_all('tr');

#datos de alcaldes
alcaldes =[]
municipios =[]
departamentos =[]

for item in trs:
    rows = item.find('td',class_="alcalde")
    muni= item.find('td',class_="muni")
    depart = item.find('td',class_="depa")
    alcaldes.append(rows.text.strip())
    municipios.append(muni.text.strip())
    departamentos.append(depart.text.strip())

    

nombre = pd.DataFrame({
       "Nombre":alcaldes, 
       "Municipio":municipios,
       "Departamento":departamentos,
       "Fuente":"Sitio Web Corporación de Municipalidades de la República de El Salvador: ",
       "Enlace":link,
       "Enlace nombre":nombree,
})


imprimir(nombre)       

