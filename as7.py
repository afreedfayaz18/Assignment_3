test_keys = ["Amal", "Afreed", "Varsha"] 
test_values = [18, 7, 10] 
print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
res = {} 
for key in test_keys: 
    for value in test_values: 
        res[key] = value 
        test_values.remove(value) 
        break    
print ("Resultant dictionary is : " +  str(res)) 