# SP > DataGeo



O [DataGeo](http://datageo.ambiente.sp.gov.br/) é o sistema da ~~Secretaria Estadual de Meio Ambiente do Estado de São Paulo (SMA)~~ [**Secretaria de Infraestrutura e Meio Ambiente (SIMA)**](https://www.infraestruturameioambiente.sp.gov.br) que disponibiliza diversas informações relevantes. Entendo trata-se do pilar do que é chamado de <u>Infraestrutura de Dados Espaciais Ambientais do Estado de São Paulo</u>. No evento MundoGEO Connect, edição de 2014, foi feita [uma apresentação](https://mundogeoconnect.com/2014/arquivos/palestras/9_mai-a-arlete-ohata.pdf) que explica melhor a concepção do DataGeo.

As informações são disponibilizadas, majoritariamente, em formato WMS (*Web Map Service*), que impossibilita análises espaciais, possibilitando apenas visualizações. Alguns *layers* porém estão acessíveis em formatos editáveis mais usualmente conhecidos, sendo que os dados armazenados nesse repositório são derivados destes formatos.



## Objetivo do repositório

Este repositório tem a finalidade de disponibilizar as rotinas empregadas para fazer o *download e tratamento dos dados, bem como disponibilizar os dados de maneira remota, sendo facilmente utilizado em outras aplicações.


- ***Download***: tentativa de busca dos dados por meio do *link* dos metadados;

- ***Tratamento dos Atributos***: deletar colunas desnecessárias, renomear colunas etc;

- ***Transformação de Projeção***: buscar padronizar a base de dados em EPSG: 4326, tento em vista ser o mais empregado em *webmaps*;

- ***Excluir Lixos***: deletar arquivos intermediários, mantendo apenas o arquivo bruto e a versão que utilizo em outros códigos.