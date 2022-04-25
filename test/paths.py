import os




data_path = os.path.join('..', 'data')
os.makedirs(data_path, exist_ok=True)

input_path = os.path.join(data_path, 'input')
os.makedirs(input_path, exist_ok=True)

output_path = os.path.join(data_path, 'output')
os.makedirs(output_path, exist_ok=True)

output_path_gjson = os.path.join(output_path, 'geojson')
os.makedirs(output_path_gjson, exist_ok=True)

output_path_gpkg = os.path.join(output_path, 'gpkg')
os.makedirs(output_path_gpkg, exist_ok=True)

bruto_path = os.path.join(data_path, 'brutos')
os.makedirs(bruto_path, exist_ok=True)

src_path = os.path.join('..', 'src')
os.makedirs(src_path, exist_ok=True)
