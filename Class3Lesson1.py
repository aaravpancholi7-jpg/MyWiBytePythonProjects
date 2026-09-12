import random

specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screensize', 'Price']

laptop = dict.fromkeys(specs)

print (laptop)

master_dict = {}

master_dict = {}
master_dict['Brands'] =  ['WDell', 'WAsus', 'WAcer', 'WLenovo', 'WHP', 'WMacbook', 'WChromebook']
master_dict['Models'] = ['AAA', 'BBB', 'CCC']
master_dict['CPUs'] = ['WIntel i5', 'WIntel i7', 'WAMD Ryzen']
master_dict['Speeds'] = ['2 GHz', '3 GHz', '3.15 GHz', '3.8 GHz']
master_dict['RAMs'] = [ '2 GB', '4 GB', '8 GB', '16 GB']
master_dict['Storages'] = [ '128 GB', '256 GB', '512 GB', '1024 GB']
master_dict['Screensizes'] = [ '9 in', '12 in', '14.9 in', '17 in']
master_dict['Prices'] = ['$200', '$300', '$400']


n_laptops = 3
laptop_list = []

for _ in range(n_laptops):
    new_laptop = dict.fromkeys(specs)
    for kk in new_laptop:
        new_laptop[kk] = random.choice(master_dict[kk+'s'])
    laptop_list.append(new_laptop)

user_choice = dict.fromkeys(specs)
for kk in specs:
    user_choice[kk] = input('Any preference for ' + kk + "(enter none for no preference)" + '\n')

query = ""

for kk in user_choice:
    if user_choice[kk].lower() == 'none':
        pass
    else:
        query = query + 'laptop[' + '\'' + kk + '\'] == ' + '\'' + user_choice[kk] + '\' and '

query = query[0:-4:1]
if query == '':
    selected = [laptop for laptop in laptop_list if eval(query)]
else:
    selected = [laptop for laptop in laptop_list]
