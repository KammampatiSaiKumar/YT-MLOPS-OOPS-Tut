lst=[1,2,3]
my_str='mlops playlist'
my_int=155
# print(type(my_str))
# print(type(my_int))
# print(type(lst))
# print(type(lst))
# print(type(lst))

from oops_proj import chatbook
user1=chatbook()
print(user1.id)

chatbook.set_id(100)

user2=chatbook()
print(user2.id)

# user3=chatbook()
# print(user3.id)




# print(user1._chatbook__name)-->ENCAPSULATION

# getter and setter
# print(user1.get_name())
# user1.set_name('sai_agent')
# print(user1.get_name())