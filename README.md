# Image Copies Finder

To use this program you should have Pillow module for Python.

Console program in Russian. 

This program takes the path of folder with pictures and looks for similar. The comparison works like this: takes first picture, resizes in ks^2 (ks = 32 by default) times smaller, takes small variant of next picture and calculates their difference. If difference is none name of second picture is writen in copies.txt. In the end of process it prints list of copies' names.

If the process has been interrupted, you should not worry about lost time. Current position is writen in count.txt. After interruption program begins in position in the file.



# Поиск копий картинок

Консольное приложение на русском.

Программа принимает путь папки с картинками и ищет похожие. Сравнение работает следующим образом: берётся первая картинка, уменьшается в ks^2 (ks =32 по умолчанию) раз
берётся следующая картинка, также уменьшается, считается разность между ними. Если разность не найдена, название второго файла записывается в copies.txt. В конце выводится список имён файлов-копий

Если процесс был прерван, не стоит жалеть о потраченном времени. Текущая позиция записывается в count.txt. После прерывания программа начнёт с позиции, записанной в файле.
