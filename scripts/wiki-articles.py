import json
import wikipedia
import sys

composer = ''
for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
    if(i == 1):
        composer = sys.argv[i]

f = open('./../data/works-by-composer.json')
w = open('./../data/wiki-articles/works/' + composer + '.json', 'w')
w2= open('./../data/wiki-articles/works/not-found/' + composer + '.json', 'w')
data = json.load(f)

found = {}
not_found = {}
i = 0

for work in data[composer]:
    try:
        composer_last_name = composer.split(',')[0]
        query = work.partition(' (ARR.')[0] + ' ' + composer_last_name
        key = work + '___' + composer_last_name

        print('\n', i, query)
        # if (i < 2):
        if (key not in found):
            i += 1
            try:
                res = wikipedia.search(query, results = 1)
                print(query, res[0])
                summary = wikipedia.summary(res[0])
                print(summary)
                found[key] = {
                    'page_title': res[0],
                    'composerName': composer,
                    'workTitle': work,
                    'summary': summary,
                }
            except:
                print(query, 'not found')
                not_found[key] = {
                    'page_title': '',
                    'composerName': composer,
                    'workTitle': work,
                    'summary': '',
                }
                continue
    except:
        continue

# for i in found:
#     print(i)

json.dump(found, w, indent=4, ensure_ascii=False)
json.dump(not_found, w2, indent=4, ensure_ascii=False)
    
w.close()
w2.close()
f.close()