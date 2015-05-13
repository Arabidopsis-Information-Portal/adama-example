import json
import requests


def search(args):
    gene = args['gene']
    model = args.get('model', '1')

    url = 'https://mpss.udel.edu/web/php/pages/abundances.php'
    response = requests.get(url,
                            verify=False,
                            params={'SITE': 'at_sRNA',
                                    'format': 'json',
                                    'featureName': gene,
                                    'model': model})
    response.raise_for_status()

    data = response.json()['abundance_data']
    for row in data:
        print json.dumps(row)
        print '---'


def list(args):
    raise Exception('not implemented yet')
