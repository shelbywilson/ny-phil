import json

f = open('./../data/complete.json')
data = json.load(f)['programs']

index = {}
i = 0
for p in data:
    # entry = {}
    for c in p['concerts']:
        date = c['Date'].split('T')[0]
        # entry['date'] = date
        split = date.split('-')
        # entry['program'] = p

        key = split[1] + '-' + split[2]
        if key not in index:
            index[key] = []
        index[key].append({'program': p, 'year': split[0] })

        i += 1
        print(i)

for date in index:
  d = date.split('-')
  w = open('./../data/date-indices/' + str(d[0]) + '-' + str(d[1]) + '.json', 'w')
  print(str(d[0]) + '-' + str(d[1]))
  json.dump(index[date], w, indent=4, ensure_ascii=False)
  w.close()

f.close()
