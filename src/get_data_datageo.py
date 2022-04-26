#!/usr/bin/env python
# coding: utf-8

import os
import re
import sys
import shutil
import zipfile
import requests
import geopandas as gpd
from bs4 import BeautifulSoup


sys.path.append(os.path.join(os.getcwd(), '..', 'src'))
from paths import *


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


def get_url_shapefile(id_lyr):
    '''
    Pega a URL do shapefile
    
    '''
    
    # Input dos caminhos para os metadados
    url_api = 'http://datageo.ambiente.sp.gov.br/geoportal/catalog/search/resource/details.page?uuid='
    url_meta = '{}{}'.format(url_api, '%7B{}%7D'.format(id_lyr))

    # Abre a página dos metadados
    r = requests.get(url_meta, allow_redirects=True)

    # Parser HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find_all('a', href=True)

    # Procura Shapefile
    for i in soup:
        text = i.text.split(' ')
        #print(text)
        for j in text:
            #print(j)
            if j in 'Shapefile':                
                url = i['href']
                print('Encontrei o shapefile:\n{}\n'.format(url))
                return url


def get_metadata_file(id_lyr, output_path, filename=None):
    '''
    Salva arquivo de metadados
    
    '''
    
    # Input dos caminhos para os metadados
    url_api = 'http://datageo.ambiente.sp.gov.br/geoportal/catalog/search/resource/details.page?uuid='
    
    # URL
    url_meta = '{}{}'.format(url_api, '%7B{}%7D'.format(id_lyr))
    print('Página com metadados:\n{}'.format(url_meta))

    # Set Filename
    if filename is None:
        url = get_url_shapefile(id_lyr)
        r = requests.get(url, allow_redirects=True)
        filename_cd = get_filename_from_cd(r.headers.get('content-disposition'))
        filename_metadata = filename_cd.split('.')[0]
    
    else:
        filename_metadata = filename
    
    # Get Metadata File
    r = requests.get(url_meta, allow_redirects=True)
    open(os.path.join(output_path, '{}.html'.format(filename_metadata)), 'wb').write(r.content)
    print('Página HTML dos metadados salva!\n')


def download_shapefile(id_lyr, output_path, filename=None):
    # Get Shapefile
    url = get_url_shapefile(id_lyr)
    r = requests.get(url, allow_redirects=True)
    
    # Set Filename
    if filename is None:
        # Get Zip filename from CD
        zip_filename = get_filename_from_cd(r.headers.get('content-disposition'))
    
    else:
        zip_filename = f'{filename}.zip'
        
    # Get Zipfile
    open(os.path.join(output_path, zip_filename), 'wb').write(r.content)

    # Unzip
    zipfile_file = os.path.join(output_path, zip_filename)
    zipfile_temp = os.path.join(os.path.dirname(zipfile_file), 'temp')
    os.makedirs(zipfile_temp, exist_ok=True)
    with zipfile.ZipFile(zipfile_file, 'r') as zip_obj:
        zip_obj.extractall(zipfile_temp)

    # Pega o nome do shapefile PRECISA HAVER SOMENTE UM!
    list_shps = [i for i in os.listdir(zipfile_temp) if i.endswith('.shp')]
    print(f'Encontrei {len(list_shps)} arquivos "shapefile", sendo que o primeiro deles é o "{list_shps[0]}"')

    # Read shapefile
    gdf = gpd.read_file(os.path.join(zipfile_temp, list_shps[0]))
    print(gdf.head())

    # Reprojeta
    print(gdf.crs)
    gdf = gdf.to_crs(epsg=4326)
    print(gdf.crs)
    gdf.plot()

    # Excluí pasta temporária
    shutil.rmtree(zipfile_temp)
    return gdf


try:
    if __name__ == '__main__':
        pass
except:
    pass







