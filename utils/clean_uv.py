res = []
with open('uv_narvik.csv', 'r') as f:
    for line in f:
        res.append(line.replace('<pyowm.uvindexapi30.uvindex.UVIndex - reference time=', '').replace(' 12:00:00+00:00', '').replace('value=','').replace('>',''))


with open('uv_narvik_clean.csv', 'a') as f:
    # f.write('date;value\n')
    for uvi in res:
        f.write(str(uvi))
