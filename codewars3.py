# def openOrSenior(data):
#     membership = []
#     for i in range(len(data)):
#         if data[i][0] >= 55 and data[i][1] > 7:
#             membership.append('Senior')
#         else:
#             membership.append('Open')
#     return membership
# openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])



# # UNIQUE IN ORDER CODE WARS

# def unique_in_order(iterable):
#     uchars = []
#     for i in range(len(iterable)):
#         if iterable[i] in uchars:
#                 if iterable[i] != iterable[i-1]:
#                     uchars.append(iterable[i])
#                 else:
#                     pass
                    
#         else:
#             uchars.append(iterable[i])
#     return uchars       
            


# unique_in_order('AAAABBBCCDAABBB')


# # Take a walk codewars
# def isValidWalk(walk):
#     #determine if walk is valid
#     distance = 0
#     coordinates = {'n':1, 's':-1, 'e':2, 'w': -2}
#     for s in walk:
#         distance +=coordinates[s]
#     if distance != 0:
#         return False
#     else:
#         return True

# isValidWalk(['n','s','e','e'])

# def findSmallestInt(arr):
#     low = arr[0]
#     for i in range(len(arr)):
#         if arr[i] < low:
#             low = arr[i]
#     return low


# #DNA Codewars
# def DNA_strand(dna):
#     dna_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
#     new_strand = []
#     for x in dna:
#         new_strand.append(dna_dict[x])
#     new_strand = ''.join(new_strand)
#     return new_strand


# #DISEMVOWEL CODEWARS
# def disemvowel(string):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     new_string = []
#     for x in string:
#         if x not in vowels:
#             new_string.append(x)
#         else:
#             pass
#     new_string = ''.join(new_string)
#     return new_string

# print disemvowel("hello")

# #ATM PIN CODES:
# def validate_pin(pin): 
#     if pin.isdigit():
#          if len(str(pin)) == 4 or len(str(pin)) == 6:
#             return True
#     return False


## Count Vowels
# def getCount(inputStr):
#     num_vowels = 0
#     vowels = 'aeiou'
#     for x in inputStr:
#         if x.lower() in vowels:
#             num_vowels = num_vowels + 1
#     return num_vowels

# print getCount('fire')

# def spin_words(sentence):
#     words = sentence.split()
#     spun_sentence = ''
#     for word in words:
#         if len(word) >= 5:
#             spun_sentence += word[::-1]
#             spun_sentence += " "
#         else:
#             spun_sentence += word
#             spun_sentence += " "
#     spun_sentence = spun_sentence.strip(' ')
#     return spun_sentence

# print spin_words("fire burner")

#NEW CHALLENGE

def namelist(names):
    #your code here
    new_list = []
    for i in  range(len(names)):
        new_list.append(names[i]['name'])
    new_list = ', '.join(new_list)
    return new_list


print namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])