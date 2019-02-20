#python3

"""
Algorithm
Good job! (Max time used: 0.04/5.00, max memory used: 9748480/671088640.)
sack params <= input
loot dict< = input

unit_val = weight/value

sortedUnitVal <= all unit_val sorted

sack_wt = from params
value = 0
while sack has space and loot not empty
    highestValueItem = sortedUnitVal[-1]
    remove highestValueItem from loot
    sack_wt = sack_wt - highestValueItem_weight
    if sack_wt >=0
        value += highestValueItem.value

return value
"""
knapsack_params = list(map(int,input().split()))
loot = []
for x in range(knapsack_params[0]):
    item_params = list(map(int,input().split()))
    value =  item_params[0]
    weight =  item_params[1]
    item = {
        'value': value,
        'weight': weight,
        'unit_value': value/weight
    }
    loot.append(item)

#sorting list of dicts by key 'unit_value'
loot = sorted(loot, key=lambda x: x['unit_value'])

sack_space = knapsack_params[1]
max_sack_val = 0

while sack_space != 0 and len(loot) != 0:
    highest_value_item = loot[-1]
    if sack_space<highest_value_item['weight']:
        unit_value = highest_value_item['unit_value']
        max_sack_val += unit_value*sack_space
        break
    else:
        sack_space = sack_space-highest_value_item['weight']
        loot.remove(highest_value_item)
    if sack_space >=0:
        max_sack_val += highest_value_item['value']

print('%0.4f' % max_sack_val)