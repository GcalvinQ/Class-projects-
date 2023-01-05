###########################################################################
#
# Calvin Grant
# Zombie Tracing
# 12/15/22
#
############################################################################

# function to print patient zeros
def print_contact_records(my_words2):
    print("Contact Record: ")
    for names in my_words2:
        # splitting each name at each space 
        names2 = names.split(" ", 5)
        # will also hold the info on the patient zeros 
        names3 = names2[0]
        names4 = names2[1:]
        # calling the merge sort function
        merge_sort(names4)
        names5 = ', '.join(names4)
        print(f"\t{names3} was in contact with {names5}")


# used the merge sort due to its average performace of o(nlog2n) for sorting performance
# using the merge sort implimented from class
def merge_sort(lst):
  if (len(lst) > 1):
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)

    l, r, i = 0, 0, 0
    while (l < len(left) and r < len(right)):
      if (left[l] <= right[r]):
        lst[i] = left[l]
        l += 1
      else:
        lst[i] = right[r]
        r += 1
      i += 1
    while (l < len(left)):
      lst[i] = left[l]
      l += 1
      i += 1
    while (r < len(right)):
      lst[i] = right[r]
      r += 1
      i += 1
  
# going to use a binary search tree
# or hashing 
def print_patient_zeros(names):
    patient_zero_list = []
    # used to see if the patient truely is patient zero 
    comparitive_list = []
    for names in my_words2:
        # splitting each name at each space 
        names = names.split(" ", 5)
        # will also hold the info on the patient zeros 
        names3 = names[0]
        names4 = names[1:]
        # appending to the appropriate lists 
        patient_zero_list.append(names3)
        comparitive_list.append(names4)
        
    # reslicing to create single list using list comprehension 
    names5 = [name for l in comparitive_list for name in l]
    # calling the merge_sort function to make the values predictable
    # i. e. in alphabetical order ( O(nlog2n) not bad )
    merge_sort(names5)
    # for each name in the list of names hash the name and put into hash table 
    for name in names5:
        s = H(name)
        while (ht[s] != None):
            s = (s + 3) % m
        ht[s] = name
        
    # getting the correct 'patient zeros' by searching in both the hash table and the list of potential patient zeros 
    for name in ht:
        for patient in patient_zero_list:
            if (name == patient):
                patient_zero_list.remove(name)
    
    # printed the desired output 
    patient_zeros_formatted = ', '.join(patient_zero_list)
    print(f"\nPatient Zeros: {patient_zeros_formatted}")


# to print out the potential zombies 
def print_potential_zombies(names):
    patient_zero_list = []
    # used to see if the patient truely is patient zero 
    comparitive_list = []
    for names in my_words2:
        # splitting each name at each space 
        names = names.split(" ", 5)
        # will also hold the info on the patient zeros 
        names3 = names[0]
        names4 = names[1:]
        # appending to the appropriate lists 
        patient_zero_list.append(names3)
        comparitive_list.append(names4)
        
    # reslicing to create single list using list comprehension 
    names7 = [name for l in comparitive_list for name in l]
    merge_sort(names7)
    # for each name in the list of names hash the name and put into hash table 
    for name in names7:
        s = H(name)
        while (ht2[s] != None):
            s = (s + 3) % m
        ht2[s] = name
    
    # instance of a list 
    res = []
    # store the contents of the hash table into this list if the value is a name 
    for val in ht2:
        if val != None :
            res.append(val)
     
    res = [*set(res)]
    
    # making sure the names are only presented if desired 
    for name in patient_zero_list:
        for patient in res:
            if (patient == name):
                res.remove(patient)
    
    # making sure the output is alphabetcial
    merge_sort(res)
    potential_zombies_formatted = ', '.join(res)          
#     print(f"\nPotential Zombies: {potential_zombies_formatted}")
    return potential_zombies_formatted
    
        
# using hashing to be able to seach in the future for the names of potential patient zeros
# I decided to use hashing because the data is kind of large and I wanted to be able to search quickly through the list
# if you place print statements into the print_potential_zombies function you can see the hash table fill up
# I do not really know if the hash table was even nessesary or really used but, it has also allowed me to get access to data from different functions
def H(n):
    return sum(I(c) for c in n) % m

def I(c):
    return ord(c) - ord("A")

def print_neither_option_names(names): 
    patient_zero_list = []
    # used to see if the patient truely is patient zero 
    comparitive_list = []
    for names in my_words2:
        # splitting each name at each space 
        names = names.split(" ", 5)
        # will also hold the info on the patient zeros 
        names3 = names[0]
        names4 = names[1:]
        # appending to the appropriate lists 
        patient_zero_list.append(names3)
        comparitive_list.append(names4)

    # this will contain a list of names that contain the "neither" condition, but are not yet excluding the 
    res = []
    # store the contents of the hash table into this list if the value is a name 
    for val in ht2:
        if val != None :
            res.append(val)
    
    # this will contain a list of names that contain the "neither" condition, but are not yet excluding the 
    res2 = []
    # making sure the names are only presented if desired 
    for name in patient_zero_list:
        for patient in res:
            if (patient == name):
                res2.append(patient)
    
    # removing repeated words from the list 
    res = [*set(res)]
    res2 = [*set(res2)]
    print(res)
    print(res2)
    merge_sort(res)
    merge_sort(res2)
    neither_condition_formatted = ', '.join(res2)
    return neither_condition_formatted
    
def print_most_viral_people(names):
    most_viral = ""
    # had to initialize as None so I could get an initial index 
    viral_list = [" "]
    tep_list = []
    for name in names:
        # splitting each name at each space 
        name = name.split(" ", 5)
        tep_list.append(name)
    
    i = 0
    for name_list in tep_list:
        if viral_list == None:
            print("yes")
        if len(name_list) > len(viral_list[i]):
            viral_list.append(name_list)
            i += 1

#
    viral_restripped = [name for l in viral_list for name in l]
    viral_without_placeholder = viral_restripped[1:]
    return viral_without_placeholder
    

def print_most_contact(names):
    # instance of a list 
    res = []
    # store the contents of the hash table into this list if the value is a name 
    for val in ht2:
        if val != None :
            res.append(val)
            
    # I tried to impliment a recursive call function
    # It by adding to a dictionary counter but, I do not think it is recurrsive 
    if not res:
        return None
    counts = {}
    for el in res:
        if el in counts:
            counts[el] += 1
        else:
            counts[el] = 1
    most_repeated = []
    highest_count = 0
    # I was only able to get one name as an output so I added this section of code to allow for maximum counts to be displayed when the values are equal with the max 
    for el, count in counts.items():
        if count > highest_count:
            most_repeated = [el]
            highest_count = count
        elif count == highest_count:
            most_repeated.append(el)
    
    # merge sorting the elements
    merge_sort(most_repeated)
    most_repeated_formatted = ', '.join(most_repeated)
    return most_repeated_formatted

def print_max_distance(names):
    pass
    
    # base case 1 potential zombie
    # if a potential zombie distance is 0
    
    # base case 2 only in contact with potential zombies:
    # if the individual has had contact with only individuals in the dictionary that are patient zeros 
    
    # recursive part
    # maximum distance of me is + 1 of the max distance of the name's distance in the iteration before me 
    
            
    
# opening file and reading as input 
with open('DataSet1.txt', 'r') as input_file:
    words = input_file.read().splitlines()

# this section was meant to be for creating a dictonary to use for the recursive function to find the distance
# I just could not get it to work properly 
# # opening file and reading as input 
# with open('DataSet1.txt', 'r') as input_file:
#     words5 = input_file.read().splitlines()
#     # create an empty dictionary
#     connections = {}
#     
#     for_distance = []
#     for line in words5:
#         new_words = line.replace("," , " ")
#         for_distance.append(new_words)
#     # iterate over the lines
#     for line in for_distance:
#         # add an entry to the dictionary using the first word as the key and the rest of the words as the value
#         connections[line[0]] = line[1:]
        
# creating list
my_words2 = []
# replacing each , with a spece and appending it to the list that was just made 
for line in words:
    my_words = line.replace("," , " ")
    my_words2.append(my_words)
    
# # initializing dictionary to house connections between the individuals in the input file
# connections = {}
# for line in my_words2:
#     my_word = line.split()
#     connections[my_word[0]] = my_word[1:]
# print(connections)
    
# main for part 1 
print_contact_records(my_words2)

# main for part 2
m = 23
# invisible hash table 
ht = [ None ] * m
ht2 = [ None ] * m

print_patient_zeros(my_words2)

# main part 3
printing_potentials = print_potential_zombies(my_words2)
print(f"\nPotential Zombies: {printing_potentials}")

# main for part 4 
printing_neither = print_neither_option_names(my_words2)
print(f"\nNeither patient zero nor potential zombie: {printing_neither}")

# main for part 5
printing_viral = print_most_viral_people(my_words2)
print(f"\nMost viral people: {printing_viral[0]}")


# main for part 6
printing_contacted = print_most_contact(my_words2)
print(f"\nThe most contacted people: {printing_contacted}")

# main for part 7
# max_distance = print_max_distance(my_words2)
# print(max_distance)




    
