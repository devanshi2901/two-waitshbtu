ini_dict = {'a':{'b':1, 'c':2}, 'b':{'b':1, 'c':2},  

            'c':{'a':2, 'b':3}, 'd':{'a':2, 'b':7}} 

print ("initial dictionary", str(ini_dict)) 

  


result = {} 

  

for key, value in ini_dict.items(): 

    if value not in result.values(): 

        result[key] = value 

          

print ("result", str(result)) 
