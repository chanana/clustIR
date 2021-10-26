# functions.py contains functions that don't return html
from brukeropusreader.opus_parser import parse_data, parse_meta

def read_opus_data(opus_bytes):
    meta_data = parse_meta(opus_bytes)
    opus_data = parse_data(opus_bytes, meta_data)
    x = [round(i) for i in opus_data.get_range("AB")[:-1]]
    y = [round(i, 4) for i in opus_data["AB"][0 : len(x)]]

    return x, y