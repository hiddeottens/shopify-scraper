path = './stores.csv'
import pandas as pd
from shopify import extract_products_json

result = ''

with open(path) as csvfile:
    df = pd.read_csv(csvfile)
    url = df['url']
    products = extract_products_json(url)

    print(products)