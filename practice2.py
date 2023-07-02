#list1 = [1,2,3,4,5,6,7,8,9]
#list2 = [1,2,3,4,5,6,7,8,9]

#count = 0 
#for x in list1:
    #count = count + 1
    #for y in list2:
        #count = count + 1

#print(count)


#for i in range(10):
    #for j in range(1):
        #print(0, end = " ")
    #print()


num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39]

for idx, i in enumerate(num_list):
    if i == 36:
        print(i, "found at position:" , idx)
