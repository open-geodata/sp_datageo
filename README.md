# DataGeo

<br>

O [**DataGeo**](http://datageo.ambiente.sp.gov.br/) é o sistema da ~~Secretaria Estadual de Meio Ambiente do Estado de São Paulo (SMA)~~ [**Secretaria de Infraestrutura e Meio Ambiente (SIMA)**](https://www.infraestruturameioambiente.sp.gov.br) que disponibiliza diversas informações relevantes. Entendo que trata-se do pilar do que é chamado de *Infraestrutura de Dados Espaciais Ambientais do Estado de São Paulo*. No evento MundoGEO Connect, edição de 2014, foi feita [uma apresentação](https://mundogeoconnect.com/2014/arquivos/palestras/9_mai-a-arlete-ohata.pdf) que explica melhor a concepção do DataGeo.

<br>

As informações são disponibilizadas, majoritariamente, em formato WMS (*Web Map Service*), que impossibilita análises espaciais, possibilitando apenas visualizações :poop:. Alguns *layers* estão acessíveis nos formatos editáveis mais usuais, sendo que os dados armazenados nesse repositório são derivados destes formatos.

<br>

----

### Objetivo do repositório

Este repositório tem a finalidade de disponibilizar as rotinas empregadas para fazer o *download* e tratamento dos dados, bem como disponibilizar os dados espaciais de maneira remota, sendo facilmente utilizado em outras aplicações.

- ***Download***: tentativa de busca dos dados por meio do *link* dos metadados;
- ***Tratamento dos Atributos***: deletar colunas desnecessárias, renomear colunas etc;
- ***Transformação de Projeção***: buscar padronizar a base de dados em EPSG: 4326, tento em vista ser o mais empregado em *webmaps*;
- ***Excluir Lixos***: deletar arquivos intermediários, mantendo apenas o arquivo bruto e a versão que utilizo em outros códigos.

<br>

----

### Obtendo ID dos layers

A forma de se referenciar aos *layers* se dá através dos IDs, que são códigos similares a este: *B9A45FE3D-C444-4E8D-AE3B-8037D38EF4B3*.
Para obter esse código basta inspecionar elemento "Metadata".

<br>

----

### Consumindo dados do repositório

O *link* para um determinado arquivo *geojson* no repositório é apresentado abaixo

```bash
https://github.com/michelmetran/geo_SP_DataGeo/blob/master/data/LimiteMunicipal.geojson
```

<br>

A partir disso faz-se necessário alterar `github.com` por `raw.githubusercontent.com` e remover o `blob/`. Com isso é possível ler o arquivo *geojson* diretamente nos códigos do python usando, por exemplo, a biblioteca *geopandas*.

```python
import geopandas as gpd

url = 'https://raw.githubusercontent.com/open-geodata/sp_datageo/master/data/LimiteMunicipal.geojson'
gdf_mun = gpd.read_file(url)
```
