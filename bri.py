# exercise 1 _ my name cipher
# i'm using my full name: okechukwu knowledge 
# first name is knowledge, length = 9
full_name = "okechukwu knowledge"
full_name = input("okechukwu knowledge")
# the shift  amount = number of characters in first name
first_name = full_name.split()[0] #.split function will group each word sepertly by spaces in the string above into single as long a they are. then[0] is index, 
shift =len(first_name)
print(f"okechukwu knowledge: {okechukw_knowledge}")
print(f"knowledge: {knowledge}")
print(f"nine: {shift}")
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
          # determine if the upper or lower 
          base =ord ("A") if char.isupper() else ord('a')
          #shift the letter, wraping around using modulo 26
          new_char = chr((ord(char) - base + shift) % 26 + base)
          resuit += new_char 
    else:
          # leave space, puncatuation, number unchangeed
          result += char 
    return result 

def decrypt(text, shift):
    # decryption is just encryption with th opposite shift 
    return encrypt(text, _shift)
# Encrypt the full name 
encrypted = encrypt(full_name, shift)
print(f"okechukwu: {encrypted}")
# decrypt it back to confirm it works
decrypted = decrypt(encrypted, shift)
print(f"decryted: {decrypted}")
      

''''''
#exercises 7 
#createva set of all students in the class (10)
all_students = {"amaka", "chibuike","gift", "favour", "mike","ike","prosper","godstime","ike","gift"}
# create seperate set for attendance on monday,tuesday,and wednesday_attendance
monday_attendance = {"amaka", "chibuike","gift", "mike","ike","favour", "prosper"}
tuesday_attendance = {"chibuike", "gift", "mike", "ike", "ike", "favour","godstime"}
wednesday_attendance = {"gift","ike", "mike","chibuike","ike"}
# find who attended all 3 days (intrsection of allthree sets)
attended_all three = monday.instersection(tuesday, wednesday)
# set poerations: who missed at least one day? missed (Dfference)
 at least one = all student.difference(attended_all_three)
set operation; who never attended at aii?(difference)
missed at list one = full class. difference(monday_attended-all_three)
all all_students 