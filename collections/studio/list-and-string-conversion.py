proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

print(',' in proto_list1)
print(';' in proto_list2)
print(' ' in proto_list3)
print(' ' in proto_list4)

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

if ',' in proto_list1:
    word_list = proto_list1.split(',')
    word_list.reverse()
    new_string = ','.join(word_list)
    print(new_string)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

if ';' in proto_list2:
    word_list2 = proto_list2.split(';')
    word_list2.sort()
    new_string2 = ','.join(word_list2)
    print(new_string2)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

if ' ' in proto_list3:
    word_list3 = proto_list3.split(' ')
    word_list3.sort(reverse=True)
    new_string3 = ','.join(word_list3)
    print(new_string3)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.

if ', ' in proto_list4:
    word_list = proto_list4.split(',')
    word_list = [word.strip() for word in word_list]
    word_list.reverse()
    new_string = ','.join(word_list)
    print(new_string)