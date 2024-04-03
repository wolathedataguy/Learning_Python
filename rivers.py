rivers ={
    'nile':'Egypt',
    'limpopo':'East Africa',
    'zambezi':'South Africa',
    'amazon':'South America',
    'misouri':'USA'
    }

for river in rivers.keys():
    print(river.title() + ' river')
    print(rivers[river] + '\n')