# DataGeo

O [**DataGeo**](http://datageo.ambiente.sp.gov.br/) é o sistema da [**Secretaria de Infraestrutura e Meio Ambiente (SIMA)**](https://www.infraestruturameioambiente.sp.gov.br) que disponibiliza diversas informações relevantes. Entendo que trata-se do pilar do que é chamado de _Infraestrutura de Dados Espaciais Ambientais do Estado de São Paulo_. No evento MundoGEO Connect, edição de 2014, foi feita [uma apresentação](https://mundogeoconnect.com/2014/arquivos/palestras/9_mai-a-arlete-ohata.pdf) que explica melhor a concepção do DataGeo.

O DataGeo é a interface de um Geoserver:

- http://datageo.ambiente.sp.gov.br/geoserver/web/

<br>

As informações são disponibilizadas, majoritariamente, em formato WMS (_Web Map Service_), que impossibilita análises espaciais, possibilitando apenas visualizações :poop:. Alguns _layers_ estão acessíveis nos formatos editáveis mais usuais, sendo que os dados armazenados nesse repositório são derivados destes formatos.

<br>

---

### Objetivo do repositório

Este repositório tem a finalidade de disponibilizar as rotinas empregadas para fazer o _download_ e tratamento dos dados, bem como disponibilizar os dados espaciais de maneira remota, sendo facilmente utilizado em outras aplicações.

- **_Download_**: tentativa de busca dos dados por meio do _link_ dos metadados;
- **_Tratamento dos Atributos_**: deletar colunas desnecessárias, renomear colunas etc;
- **_Transformação de Projeção_**: buscar padronizar a base de dados em EPSG: 4326, tento em vista ser o mais empregado em _webmaps_;
- **_Excluir Lixos_**: deletar arquivos intermediários, mantendo apenas o arquivo bruto e a versão que utilizo em outros códigos.

<br>

---

### Obtendo ID dos layers

A forma de se referenciar aos _layers_ se dá através dos IDs, que são códigos similares a este: _B9A45FE3D-C444-4E8D-AE3B-8037D38EF4B3_.
Para obter esse código basta inspecionar elemento "Metadata".

<br>

---

### Consumindo dados do repositório

O _link_ para um determinado arquivo _geojson_ no repositório é apresentado abaixo

```bash
https://github.com/michelmetran/geo_SP_DataGeo/blob/master/data/LimiteMunicipal.geojson
```

<br>

A partir disso faz-se necessário alterar `github.com` por `raw.githubusercontent.com` e remover o `blob/`. Com isso é possível ler o arquivo _geojson_ diretamente nos códigos do python usando, por exemplo, a biblioteca _geopandas_.

```python
import geopandas as gpd

url = 'https://raw.githubusercontent.com/open-geodata/sp_datageo/master/data/LimiteMunicipal.geojson'
gdf_mun = gpd.read_file(url)
```

# Monitoramento Água Subterrânea Poço Tubular

http://datageo.ambiente.sp.gov.br/serviceTranslator/rest/getXml/Geoserver_Publico/MonitoramentoAguaSubterraneaPocoTubular/1435155782463/wms
http://datageo.ambiente.sp.gov.br/geoserver/datageo/MonitoramentoAguaSubterraneaPocoTubular/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=MonitoramentoAguaSubterraneaPocoTubular

# Monitoramento Água Subterrânea Aquífero Freático

http://datageo.ambiente.sp.gov.br/serviceTranslator/rest/getXml/Geoserver_Publico/MonitoramentoAguaSubterraneaAquiferoFreatico/1435155782478/wms
http://datageo.ambiente.sp.gov.br/geoserver/datageo/MonitoramentoAguaSubterraneaAquiferoFreatico/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=MonitoramentoAguaSubterraneaAquiferoFreatico
