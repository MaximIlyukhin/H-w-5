# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

file_1 = open('3_1.txt')
string = file_1.readline()
file_1.close()
a = ''
for i in range(len(string)):
    counter = 0
    if string[i] in a:
        continue
    else:
        for j in range(len(string)):
            if string[i] == string[j]:
                counter+=1                  
        a += str(counter)+str(string[i])
print(a)

file_1 = open('3_2.txt')
string_mix = file_1.readline()
file_1.close()
for i in range(0,len(string_mix),2):
    print(string_mix[i+1]*int(string_mix[i]), end= '')
