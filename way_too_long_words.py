# undertanding
# if less than 10 letter print same word
# if more than 10 word then first and last with total letter number between them

# plan
# count total letter of word by length less than 10 letter
# if length is more than 10 word then store first and last word and minus 2 from that

# code 3:35
# def find_firstandlast_with_letter_number_between_them():
#     given_value=given_value.split()
#     word_number=given_value[0]
#     list_of_output=[]
#     for i in range(1,len(word_number)):
#         new_given_value=given_value[i]
#         if len(new_given_value)<=10:
#             list_of_output+=[new_given_value]
#         if len(new_given_value)>10:
#             output=''
#             output+=new_given_value[0]
#             output+=str((len(new_given_value))-2)
#             output+=new_given_value[-1]
#             list_of_output+=[output]
#     return list_of_output

# given_value=[*open(0)]
# output=find_firstandlast_with_letter_number_between_them(given_value)
# for i in output:
#     print(i)



n=int(input())

for i in range(n):
    val=input()
    if len(val)>10:
        output=val[0] + str(len(val)-2) + val[-1]
        print(output)
    else:
        print(val)