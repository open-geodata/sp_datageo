#!/usr/bin/env python
# coding: utf-8

import os
import re
import shutil
import zipfile
import requests
import geopandas as gpd
from datetime import date
from bs4 import BeautifulSoup


def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def download_datageo_shp(url_meta):
    print('Página com metadados: {}'.format(url_meta))

    # Abre a página dos metadados
    page = requests.get(url_meta)
    print('Resposta da página foi {}'.format(page))

    # Parser HTML
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.find_all('a', href=True)

    # Procura Shapefile
    for i in soup:
        text = i.text.split(' ')
        #print(text)
        for j in text:
            #print(j)
            if j in 'Shapefile':
                print('> Encontrei o shapefile')
                url = i['href']
                print('Link: {}'.format(url))

    # Download do arquivo e paga o nome a partir do content-disposition
    # Arquivo zip (shapefile) vai para a pasta de 'data/brutos'
    r = requests.get(url, allow_redirects=True)
    filename = get_filename_from_cd(r.headers.get('content-disposition'))
    open(os.path.join('data', 'brutos', filename), 'wb').write(r.content)

    # Com o nome do arquivo, é realizado o download da página dos metadados
    file_meta = filename.split('.')[0]
    r = requests.get(url_meta, allow_redirects=True)
    open(os.path.join('data', 'brutos', '{}.html'.format(file_meta)), 'wb').write(r.content)

    # Unzip
    file = os.path.join('data', 'brutos', filename)
    temp = os.path.join(os.path.dirname(file), 'temp')
    os.makedirs(temp, exist_ok=True)
    with zipfile.ZipFile(file, 'r') as zip_ref: zip_ref.extractall(temp)

    # Lista Arquivos
    os.listdir(temp)

    # Pega o nome do shapefile PRECISA HAVER SOMENTE UM!
    shp = [i for i in os.listdir(temp) if i.endswith('.shp')]
    a = len(shp)
    b = shp[0]
    print('Encontrei {} arquivos ".shp", sendo que o primeiro deles é o "{}"'.format(a, b))

    # Read shapefile
    gdf = gpd.read_file(os.path.join(temp, shp[0]))
    print(gdf.head(5))

    # Reprojeta
    print(gdf.crs)
    gdf = gdf.to_crs(epsg=4326)
    print(gdf.crs)
    gdf.plot()

    # Excluí pasta temporária
    shutil.rmtree(temp)
    
    return gdf


try:
    if __name__ == '__main__':
        main()
except:
    pass




