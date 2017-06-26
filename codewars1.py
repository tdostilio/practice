def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
def order(sentence):
  # code here
    my_list = [0] * 100
    array = sentence
    array = array.split(' ')
    i = 0
    while i < len(array):
        for j in array[i]:
            try:
                int(j) == int
                my_list[int(j)] = array[i]
            except:
                pass
        i = i + 1    
    try:
        my_list = remove_values_from_list(my_list, 0)
    except:
        pass
    my_string = " ".join(my_list)
    return my_string

print order("is2 Thi1s T4est 3a") 

Grade = order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
print Grade



print type(order("is2 Thi1s T4est 3a"))