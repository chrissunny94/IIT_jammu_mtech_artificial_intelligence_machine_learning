dictionary={"vin":35,"chris":29}
print( dictionary.keys())

#find the number of repetition of each value 

InputString = 'We are learning Python'
freq_counter = {}

for term in InputString:
    if term in freq_counter:
        freq_counter[term] = freq_counter[term] + 1 
    else:
        freq_counter[term] = 1 
        
print(freq_counter)



#
run ={'vin':35,'rahul':50}
ball_faced={'vin':250,'rahul':60}

max_strike_rate =0
man_of_the_match = ""
for player in run.keys():
    print(player)
    print(run[player])
    strike_rate = run[player]/ball_faced[player]
    if (strike_rate > max_strike_rate):
        max_strike_rate = strike_rate
        man_of_the_match = player

print("player:", man_of_the_match , "max_strike_rate:", max_strike_rate)



run ={'vin':35,'rahul':50}

player_name=""
man_of_the_match = 50
for key,value in run.items():
    print(key)
    if (value == man_of_the_match):
        player_name= key
print("player:", man_of_the_match )


