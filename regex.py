################################## REGULAR EXPRESSION #######################################
#  ################################ find lower case ###########################################
# import re
# xyz=r'[a-z]'
# text="The Trustees Hello have approved the following updated policy document"
# match=re.findall(xyz,text)
# print(match)

# ############################### find upper case ###########################################
# import re
# xyz=r'[A-Z]'
# text="The Trustees Hello have approved the following updated policy document"
# match=re.findall(xyz,text)
# print(match)

# ###################################### find number ###########################################
# import re
# xyz=r'[0-9]'
# text="There are 20 Student in AI Batch 2024"
# match=re.findall(xyz,text)
# print(match)

# ################################### print space(use small s) ###############################
# import re
# xyz=r'\s'
# text="There are 20 Student in AI Batch 2024"
# match=re.findall(xyz,text)
# print(match)

# ################################### print letter(use capital S) ##############################
# import re
# xyz=r'\S'
# text="There are 20 Student in AI Batch 2024"
# match=re.findall(xyz,text)
# print(match)

# ################################# print all number and alphabet ###########################
# import re
# xyz=r'\w'
# text="There are 20 Student in AI Batch 2024"
# match=re.findall(xyz,text)
# print(match)

# ################################### find character of word ################################
# import re
# xyz=r'\w{5}'
# text="There are 20 Student in AI Batch 2024"
# match=re.findall(xyz,text)
# print(match)

#################################### find word ############################################
# import re
# xyz=r'name'
# text="Hello what is your name? my name is sakshi singh rajput"
# match=re.findall(xyz,text)
# print(match)

#################################### use quantifiers #######################################################
# import re
# xyz=r'qwert?'
# text="qwe qwert qwertyu  qwsern qwserd qwert"
# match=re.findall(xyz,text)
# print(match)

#(*)for many
# import re
# xyz=r'qwert*'
# text="qwe qwert qwertyu  qwsern qwserd qwert"
# match=re.findall(xyz,text)
# print(match)

############################################### MATCH WORD ##################################################
# import re
# xyz= r'Sakshi'
# x='Sakshi Singh Rajput'
# match=re.match(xyz,x)
# if match:
#     print("Match Found :",match.group())
# else:
#     print("No Match")

############################################### TASK ##############################################################
#Task - 1:
#  Write a regex pattern to find all occurrences of 2 to 4 digit numbers in the string "123 4567 89 01234". 
# Use re.findall to extract the matches.

# import re
# xyz=r'\b\d{2,4}\b'
# digit_numbers="123 4567 89 01234"
# match=re.findall(xyz,digit_numbers)
# print(match)

# # Task - 2: 
# # Write a regex pattern to find all words with exactly 4 characters in the string "This is a test of the regex function.
# # " Use re.findall to get the matches.

# import re
# xyz=r'\b\w{4}\b'
# string="This is a test of the regex function."
# match=re.findall(xyz,string)
# print(match)

# # Task - 3:
# #  Write a regex pattern to find all occurrences of the word "pen" in the string "I have an pen, and you have an pen too.
# # " Use re.findall to get the matches

# import re
# xyz=r'pen'
# string="I have an pen, and you have an pen too."
# match=re.findall(xyz,string)
# print(match) 

######################################## sub patter for replacement ##############################################

# import re
# xyz=r'Srija'
# rep='Shailesh'
# x='Srija is  the trainer in NSTI'
# z=re.sub(xyz,rep,x)
# print(z)

######################################### split number and string ###################################################

# import re
# xyz=r'\d+'
# string="fdsdsabdjk34352hghsdakj3y7436374"
# z=re.split(xyz,string)
# match=re.findall(xyz,string)
# print('numbers :',match)
# print('string:',z)

####################################### VALIDATION NUMBER ##########################################

# import re
# mob="+91-9685948467"
# xyz=r'^\+?\d{1,2}[-\s]?\d{10}$'
# if re.match(xyz,mob):
#     print("valid no.")
# else:
#     print("InValid")

###################################### mail pattern #########################################

import re
mail="sakshisingh@#$123@gmail.com"
xyz=r'^[A-Za-z0-9#$%@\-]+@[a-z]+\.[a-z]{1,3}$'
if re.match(xyz,mail):
    print("valid Email")
else:
    print("InValid Email")

####################################### PASSWORD VALIDATION #################################

# import re
# password="Sakshi18@"
# xyz=r'(?=.*[A-Z])(?=.*[a-z](?=.*\d)(?=.*[@$!%&])[A-Za-z\d@$!%]{10,}'
# # xyz= r'(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[@$!%&])[A-Za-z\d@$!%]{10,}'
# if re.match(xyz,password):
#     print("Strong password")
# else:
#     print("Weak Password")

############################################ LAB #############################################

# import re
# sample_text="""The quick brown fox jumps over the lazy foxes and wild animal.
# The dog quickly ran away. My email is example@example.com and my number is(123)456-7890"""
# dog_pattern=r"The.quick"
# print(f"Dot(.)pattern '{{dot_pattern}}:",re.findall(dog_pattern,sample_text))