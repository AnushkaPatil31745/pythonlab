def get_SL_SS(L):
    num=[x for x in L if isinstance(x, (int,float))] 
    if len(set(num)) < 2:
     return None
          
    sort_num = sorted(set(num))
    second_smallest = sort_num[1]
    second_largest = sort_num[-2]
         
    return second_smallest, second_largest

L = [1, 2.5, 3, 4+5j, "sggs"]
SS,SL = get_SL_SS(L)
print("Second Smallest:", SS)
print("Second Largest:", SL)
	
