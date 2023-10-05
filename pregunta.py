"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    def evaluar(lista):
        plantilla = ''
        for i in lista:
            if len(i)>0:
                i = i.replace('.', '')
                plantilla = plantilla + i + ' '
        return plantilla.strip()
    file = "clusters_report.txt"
    content = []
    string = ''
    with open(file, 'r') as f:
        for i, linea in enumerate(f):
            if i < 4 : continue
            try:
                int(linea[:6].replace(' ', ''))
                if len(string) != 0:
                    c1 = int(string[:5].replace(' ', ''))
                    c2 = int(string[6:14].replace(' ', ''))
                    c3 = float(string[22:29].replace(' ', '').replace(',', '.'))
                    # c4 = string[36:].replace('  ', '').strip()
                    c4 = evaluar(string[36:].split(' '))
                    content.append([c1, c2, c3, c4])
                linea = linea.replace('\n', ' ')
                linea = linea.replace('\t', ' ')
                string = linea
            except:
                linea = linea.replace('  ', ' ')
                linea = linea.replace('\n', ' ')
                linea = linea.replace('\t', ' ')
                string += linea
    c1 = int(string[:5].replace(' ', ''))
    c2 = int(string[6:14].replace(' ', ''))
    c3 = float(string[22:29].replace(' ', '').replace(',', '.'))
    # c4 = string[36:].replace('  ', '').strip()
    c4 = evaluar(string[36:].split(' '))
    content.append([c1, c2, c3, c4])
    df = pd.DataFrame(data=content, columns=['cluster', 
                                             'cantidad_de_palabras_clave', 
                                             'porcentaje_de_palabras_clave', 
                                             'principales_palabras_clave'])
    return df


if __name__ == '__main__':
    df = ingest_data()
    
    
    