from datetime import datetime

lines = []
tdate = ''
td, tt, th = 0, 0, 0
d, t, h = 0, 0, 0
with open('data_partial.csv') as data:
    for dline in data:
        l = dline.strip()
        date = l.split(',')[0].replace('.', '-')
        if date != 'Date':
            if tdate != date:
                tfate = date
                td, tt, th = 0, 0, 0
            d = float(l[-1])
            #print(l, l.split(',')[1])
            pt = datetime.strptime(l.split(',')[1],'%H:%M:%S')
            t = pt.second + pt.minute*60 + pt.hour*3600
            try:
                h = float(l.split(',')[-2])
            except:
                pass
            
            time = l.split(',')[1]
            
            with open('narvik_weather.csv') as weather:
                for wline in weather:
                    if wline.split(',')[0] != 'date_time':
                        wdate, wtime = wline.split(',')[0].split(' ')
                        #print(date, wdate, time[:2], wtime[:2])
                        if date == wdate and time[:2] == wtime[:2]:
                            #print(date, wdate, time[3], wtime[3])
                            with open('narvik_uv_radiation.csv') as uv:
                                for uline in uv:
                                    if date == uline[:10]:
                                        lines.append(l+','+wline.strip()+','+uline)
                                        #print(l+','+wline.strip()+','+uline)
                                        #print(td-d, tt-t)
                                        #try:
                                        #    print(th-h)
                                        #except:
                                        #    pass
                                        #input()
                                        break
                            break
            td = float(l.split(',')[-1])
            pt = datetime.strptime(l.split(',')[1],'%H:%M:%S')
            tt = pt.second + pt.minute*60 + pt.hour*3600
            try:
                th = float(l.split(',')[-2])
            except:
                pass
                            
                            

with open('data.csv', 'a') as f:
    for line in lines:
        f.write(line)
    
