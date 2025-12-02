#write a program to check if 2 lists share no common elements
def share_no_common_elements(list1, list2):
    for n in list1:
        if n in list2:
            return False
    return True
# list1 =[1,2,3,4] 
# list2 =[5,6,7,8]

list1 =[1,2,3] 
list2 =[3,4]

print(share_no_common_elements(list1, list2))