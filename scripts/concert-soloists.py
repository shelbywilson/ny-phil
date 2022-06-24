import json

f = open('./../data/complete.json')
w = open('./../data/concerts-soloists.json', 'w')
data = json.load(f)

found = {}
exclude = [
    '',
    ' ',
    '  ',
    'Audience',
    'No Soloist',
]
dateRange = {
    'min': 9999,
    'max': 0
}
for program in data['programs']:
    for work in program['works']:
        for soloist in work['soloists']:
            try:
                if (soloist['soloistName'] not in exclude):
                    name = soloist['soloistName']
                    instrument = soloist['soloistInstrument']

                    if (instrument == "" or instrument == " "):
                        instrument = 'not specified'

                    if (name not in found):
                        found[name] = {
                            'programs': {},
                            'range': {},
                            'instrument': [],
                        }
                    if (instrument not in found[name]['instrument']):
                        found[name]['instrument'].append(instrument)
                    found[name]['programs'][program['id']] = {
                        'range': [
                            program['concerts'][0]['Date'],
                            program['concerts'][len(program['concerts']) - 1]['Date'],
                        ],
                    }
            except:
                continue

for i in found:
    dateRange = {
        'min': 9999,
        'max': 0
    }

    for p in found[i]['programs']:
        d1 = int(found[i]['programs'][p]['range'][0].split('-')[0])
        d2 = int(found[i]['programs'][p]['range'][1].split('-')[0])
        if d1 < dateRange['min']:
            dateRange['min'] = d1
        if d2 > dateRange['max']:
            dateRange['max'] = d2

    found[i]['range'] = dateRange
    found[i]['instrument'].sort()
    found[i]['num_programs'] = len(found[i]['programs'].keys())
    print(i)
    print('\t', found[i]['range'])

json.dump(found, w, ensure_ascii=False)
    
w.close()
f.close()