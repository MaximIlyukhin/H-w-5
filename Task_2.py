# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

data = [k for k in range(1,10)]
size = 3
for i in range(1,len(data)+1,size):
    for j in range(size):
        print(i+j, end=' | ')
    print()
    print('- '*size*2, sep='')




    
    

