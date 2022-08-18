i = [1,[1,2],1]
for j in i:
    if isinstance(j,int):
        print(j)
        print('int')
    elif isinstance(j,list):
        print(j)
        print('list')