#!/usr/bin/env python
# coding: utf-8

import os

data_path = os.path.join('..', 'data')
os.makedirs(data_path, exist_ok=True)

input_path = os.path.join(data_path, 'input')
os.makedirs(input_path, exist_ok=True)



src_path = os.path.join('..', 'src')
os.makedirs(src_path, exist_ok=True)



# bruto_path = os.path.join(data_path, 'brutos')
# os.makedirs(bruto_path, exist_ok=True)



output_path = os.path.join(data_path, 'output')
os.makedirs(output_path, exist_ok=True)

output_path_geo = os.path.join(output_path, 'geo')
os.makedirs(output_path_geo, exist_ok=True)

output_path_datageo = os.path.join(output_path, 'datageo')
os.makedirs(output_path_datageo, exist_ok=True)

output_path_map = os.path.join(output_path, 'map')
os.makedirs(output_path_map, exist_ok=True)

output_path_tab = os.path.join(output_path, 'tab')
os.makedirs(output_path_tab, exist_ok=True)

