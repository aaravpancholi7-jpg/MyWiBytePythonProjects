import random

#laptop = {'Brand' : 'WDell', 'Model': 'ABC111', 'CPU' : 'WIntel i5'}

#laptop['RAM'] = '8 GB'

specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screensize', 'Price']

#laptop = dict.fromkeys(specs)

#laptop = dict(Brand = 'WDell', Model = 'ABC111', CPU = 'WIntel i5')

master_dict = {}
master_dict['Brands'] = ['WDell', 'WLenovo', 'WAcer' , 'WAsus', 'WHP']
master_dict['Models'] = ['AAA', 'BBB', 'CCC']
master_dict['CPUs'] = ['WIntel i5', 'WIntel i7', 'WAMD Ryzen']
master_dict['Speeds'] = ['2 GHz', '3 GHz', '3.5 GHz']
master_dict['RAMs'] = ['2 GB', '4 GB', '8 GB']
master_dict['Storages'] = ['128 GB', '256 GB', '512 GB', '1 TB']
master_dict['Screensizes'] = ['9 in', '12 in', '14.9 in', '17 in']
master_dict['Prices'] = ['$200', '$300', '$400']


models = dict.fromkeys(master_dict['Brands'])

models['WDell'] = ['Inspire', 'Altitude', 'Adam']
models['WAsus'] = ['Vivo', 'TUF', 'Zen']
models['WAcer'] = ['Lite', 'Aspire', 'Nitro']
models['WHP'] = ['Mini', 'Maxima', 'Pro']
models['WLenovo'] = ['Think', 'Idea', 'Yoga']

base_price = {'WDell': 200, 'WAsus' : 190, 'WAcer' : 200, 'WHP' : 220, 'WLenovo' : 230}
feature_price = {'Speed': 10, 'RAM': 20, 'Storage': 5, 'Screensize': 30}


laptops_list = []
n_laptops = 30

for _ in range(n_laptops):
    new_laptop = dict.fromkeys(specs)
    for kk in new_laptop:
        if kk != 'Model':
            new_laptop[kk] = random.choice(master_dict[kk + 's'])
    new_laptop['Model'] = random.choice(models[new_laptop['Brand']])
    new_laptop['Price'] = base_price[new_laptop['Brand']]
    incr_price = 0
    for feature in feature_price:
        incr_price += master_dict[feature+ 's'].index(new_laptop[feature])*feature_price[feature]

    new_price = new_laptop['Price'] + incr_price
    new_laptop['Price'] = '$' + str(new_price)
    laptops_list.append(new_laptop)

#User's Choice

user_choice= dict.fromkeys(specs)


pref = input('Please indicate the specifications where you have a preference for (comma seperated): ')
pref_list = pref.split(',')
pref_list = list(map(str.strip, pref_list))



for kk in specs:
    if kk in pref_list:
        if kk!= 'Model':
            pref_str = '/'.join(master_dict[kk+'s'])
        else:
            pref_str = '/'.join(models[user_choice['Brand']])
        user_choice[kk] = input('Any preference for ' + kk + ': ' + pref_str + ' (Eneter none for no preference)\n')
    else:
        user_choice[kk] = 'none'

#Querry Making

query = ''

for kk in user_choice:
    if user_choice[kk].lower() == 'none':
        pass
    else:
        query = query + 'laptop[' + '\'' + kk + '\'' + '] == ' + '\'' + user_choice[kk] + '\'' + ' and '

query = query[0:-4:1]

selected_laptops = []


#for laptop in laptops_list:
#    selected_laptops.append(laptop)


if query == '':
    selected_laptops = [laptop for laptop in laptops_list]
else:
    #User preference
    #for laptop in laptops_list:
    #    if eval(query):
    #        selected_laptops.append(laptop)
    selected_laptops = [laptop for laptop in laptops_list if eval(query)]

#Displaying Selected Laptops:

print()
print(len(selected_laptops), ' laptops met you preferences.')

print()

#Print Heading
characters = 0

for kk in specs:
    print(kk, end = '')
    characters = len(kk)
    print((12-characters)*' ', end = '')

print()

for laptop in selected_laptops:
    for kk in laptop:
        print(laptop[kk], end = '')
        characters = len(laptop[kk])
        print((12-characters)*' ', end = '')
    print()
