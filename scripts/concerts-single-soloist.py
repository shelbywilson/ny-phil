import json

f = open('./../data/complete.json')
w = open('./../data/concerts-single-soloist.json', 'w')
data = json.load(f)

found = {}
exclude = [
    'Audience',
    'No Soloist',
]
for program in data['programs']:
    soloists = []
    instrument = ''
    for work in program['works']:
        for soloist in work['soloists']:
            try:
                if (soloist['soloistName'] not in exclude):
                    if (soloist['soloistName'] not in soloists):
                        soloists.append(soloist['soloistName'])
                        instrument = soloist['soloistInstrument']
                        print(soloist['soloistName'])
            except:
                continue
    if (len(soloists) == 1):
        # found[program['id']] = {
        #     'concerts': program['concerts'],
        #     'range': [
        #         program['concerts'][0]['Date'],
        #         program['concerts'][len(program['concerts']) - 1]['Date'],
        #     ],
        #     'soloist': soloists[0],
        #     'instrument': instrument,
        #     # 'artifact': 'https://archives.nyphil.org/index.php/artifact/' + program['id'] + '/fullview'
        # }
        if (soloists[0] not in found):
            found[soloists[0]] = {
                'programs': [],
                'instrument': [],
            }
        if (instrument not in found[soloists[0]]['instrument']):
            found[soloists[0]]['instrument'].append(instrument)
        found[soloists[0]]['programs'].append({
            'id': program['id'],
            'range': [
                program['concerts'][0]['Date'],
                program['concerts'][len(program['concerts']) - 1]['Date'],
            ],
        })
for i in found:
    print(i)

json.dump(found, w, ensure_ascii=False)
    
w.close()
f.close()