import os, time
from PIL import Image, ImageChops


dr = input('Путь к папке: ')
if dr[len(dr)-1]!='\\': dr+='\\'
c = 0
copis = []
pics = os.listdir(dr)
print('Всего картинок: '+str(len(pics))+'\n')
ks = 32
cp=0

if os.path.exists('count.txt'):
    with open('count.txt', 'r') as ctrlpnt:
        cp = int(ctrlpnt.read())
        if cp>=len(pics)-2:
            cp=0

if cp==0:
    print('Сравнение с начала')
    with open('copies.txt', 'w') as copys:
        copys.write('')
else:
    print('Остановка на '+str(cp+1)+' картинке')

for i in range(cp, len(pics)-1):
    with open('count.txt', 'w') as ctrlpnt:
        ctrlpnt.write(str(i))
    a=time.time()
    image_1=Image.open(dr+pics[i])
    w, h = image_1.size
    image_1 = image_1.resize([int(w/ks), int(h/ks)])
    print('\nСравнивается '+str(i+1)+' картинка')
    for j in range(i+1, len(pics)):
        image_2=Image.open(dr+pics[j])
        w, h = image_2.size
        w=int(w/ks)
        h=int(h/ks)
        image_2 = image_2.resize([w, h])
        result=ImageChops.difference(image_1, image_2)
        if result.getbbox()==None:
            with open('copies.txt', 'a') as copys:
                copys.write(pics[j]+'\n')
            print('Картинка '+pics[j]+' является копией '+pics[i])
    print('Прошло '+str(time.time()-a)+' секунд')
        
print()
print()
 
with open('copies.txt', 'r') as copys:
    rdr=copys.read()
    for i in range(0, rdr.count('\n')):
        copis = rdr.split()
    
if copis==[]:
    print('Похожих картинок не было')
else:
    print('Удалить:')
    for i in copis:
        print(i)