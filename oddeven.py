import time
def get_odds_evens_count(L):
	oddcount=0
	evencount=0
	for x in L:
		if isinstance(x,int):
			if x%2== 0 :
				evencount += 1
			else:
				oddcount+= 1
     
	return evencount, oddcount
  
L = [1,2]
print("sggs")
startTime1 = time.time()
print(get_odds_evens_count(L))
endTime1 = time.time()
Total_time= startTime1 - endTime1
print(Total_time)

def get_odds_evens_count(L):
	oddcount=0
	evencount=0
	for x in L:
		if int == type(x) :
			if x%2== 0 :
				evencount += 1
			else:
				oddcount+= 1
     
	return evencount, oddcount
   
L = [1,2]
print("sggs")
startTime = time.time()
print(get_odds_evens_count(L))
endTime = time.time()
Total_time= startTime - endTime
print(Total_time)
def get_odds_evens_count(L):
	oddcount=0
	evencount=0
	for x in L:
		if isinstance(x,int):
			if x%2 :
				oddcount += 1
			else:
				evencount+= 1
     
	return evencount, oddcount
   
L = [1,2]
print("sggs")
startTime = time.time()
print(get_odds_evens_count(L))
endTime = time.time()
Total_time= startTime - endTime
print(Total_time)
def get_odds_evens_count(L):
	oddcount=0
	evencount=0
	for x in L:
		if isinstance(x,int):
				oddcount += x%2 ==1 
		
				evencount+= x%2==0
     
	return evencount, oddcount
   
L = [1,2]
print("sggs")
startTime = time.time()
print(get_odds_evens_count(L))
endTime = time.time()
Total_time= startTime - endTime
print(Total_time)
