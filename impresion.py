import glob
import sys

import pandas as pd




def imprimir(table):
    archivocsv = 'export_dataframe.csv'

    exist_archivo = glob.glob(archivocsv)

    if not exist_archivo:
       export_csv = table.to_csv (archivocsv)
       print('archivo creado')
    else:
        print('archivo ya existe')

        print('---------------------------')
        print('SI')
        print('NO')
        print('---------------------------')

        respiesta = input('¿desea crear nuevo archivo?: ').upper()
     
        if respiesta == 'SI':
            nuevo = input('nuevo nombre del archivo: ')
            export_csv = table.to_csv ('{}.csv'.format(nuevo))
            print('creado con nuevo nombre')
        elif respiesta=='NO':
            export_csv = table.to_csv (archivocsv)
            print('archivo sobreescrito')  
        else:
            print('Seleccion invalida')      