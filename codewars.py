def reverso(string:str):
    reversed = string[::-1]
    return reversed

print(reverso('hola'))

#%% cant días

def rental_car_cost(d:int):
    if 1<=d<3:
        total_value = 40*d 
    elif 3<=d<7:
        value_perday = 40*d
        total_value = value_perday - 20
    elif d >=7:
        value_perday = 40*d
        total_value = value_perday - 50
    return total_value

print(rental_car_cost(4))

#%%  remove char

s = 'cucaracha'

print(s[1:-1])

#%% Game Banjo

def are_you_playing_banjo(name):
    if name[0].upper() == 'R':
        cond = name + ' plays banjo'
        return cond
    else:
        cond = name + ' does not play banjo'
        return cond

are_you_playing_banjo('royce')

#%% 