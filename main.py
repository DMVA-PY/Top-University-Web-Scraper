import httpx
from rich import print
import pandas as pd
import json

def download_json(url):
    resp = httpx.get(url)
    for node in resp.json()['score_nodes']:
        yield node

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('results.csv', index=False)

def save_to_json(data):
    with open('results.json', 'w') as f:
        json.dump(data, f)

def main():
    results = []
    for i in range(0,35):
        print('page', i)
        url = f'https://www.topuniversities.com/rankings/endpoint?nid=3897789&page={i}&items_per_page=15&tab=indicators'
        for item in download_json(url):
            results.append(item)
    print(len(results))
    
    save_to_csv(results)
    save_to_json(results)

if __name__ == "__main__":
    main()
