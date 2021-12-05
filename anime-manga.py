import os
import requests


def main():

    url = "https://kitsu.io/api/edge/anime"
    headers = {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json'
    }
    params = {
            'page[limit]':  1,
            'page[offset]': 0,
            'filter[text]': name
            }
    re = requests.get(url, headers=headers, params=params)
    resp = re.json()
    img = resp['data'][0]['attributes']['posterImage']['original']
    title = resp['data'][0]['attributes']['titles']['en']
    types = resp['data'][0]['type']
    save_file = "img/" + types + "/" + title
    with open(save_file, 'bw') as f:
        f.write(requests.get(img).content)


if __name__ == '__main__':
    main()
