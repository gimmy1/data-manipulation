from us_data import us_state_abbrev, states_list

# print out the 10th item in the list and dictionary
list10 = states_list[9]

# For a dictionary you must retrieve the items, turn into a list, and access nth element
dict10 = list(us_state_abbrev.items())[9]


# Print out 45th key in dictionary
dict45 = list(us_state_abbrev.keys())[45]

# Print out 44th value in dictionary
dict44 = list(us_state_abbrev.values())[43]



# Replace the 15th key in the dictionary with the 28th item in the list
# Step1. Retrieve name of 15th key / old_key
old_key = list(us_state_abbrev.keys())[14]
# Step2. Retrieve new_key
new_key = states_list[28]
# Replace and Pop
us_state_abbrev[new_key] = us_state_abbrev.pop(old_key)
