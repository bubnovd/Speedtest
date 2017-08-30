#!/usr/bin/env python3

import datetime, os

dir="/var/www/html/"
index="index.html"

findex = open(dir+index, 'w')
findex.write("<html><head><title>Bandwidth. Powered by bubnovd.net</title></head>\n<body>")
#перебираем файлы в директории и для каждого строим график
for filename in os.listdir(dir+"in"):
        fin = dir+"in/"+filename
        fout = dir+"out/"+filename
        imgpath = "out/"+filename+".png"

        st = open(fin, 'r')
        res = open(fout, 'w')

        #убираем лишнее из файла
        for line in st:
            w = line.split(',')
            ti = datetime.time(int(w[0][-6:][0:2]), int(w[0][-6:][2:4]), int(w[0][-6:][4:6]))
            da = datetime.date(int(w[0][0:8][0:4]), int(w[0][0:8][4:6]), int(w[0][0:8][6:9]))
            print("{0} {1} {2}".format(da, ti, int(w[8])/(1024**2)), file=res)

        res.close()

        from os import system, remove
        system('gnuplot -e "filename=\''+fout+'\'; outf=\''+fout+'.png\'\" plot.gp')    #строим график

        remove(fout)
        findex.write("<img src="+imgpath+">\n") #пишем картинку в веб
findex.write("</body></html>")
findex.close()
