from math import sqrt 

def primeCount(arr, n): 
	max_val = arr[0]; 
	for i in range(len(arr)): 
		if(arr[i] > max_val): 
			max_val = arr[i] 
    
	prime =[ True for i in range(max_val + 1)] 

	prime[0] = False
	prime[1] = False
	k = int(sqrt(max_val)) + 1
	for p in range(2, k, 1): 
		
		if (prime[p] == True): 
			 
			for i in range(p * 2, max_val + 1, p): 
				prime[i] = False

	count = 0
	for i in range(0, n, 1): 
		if (prime[arr[i]]): 
			count += 1

	return count 

if __name__ == '__main__': 
	arr = [1, 2, 3, 4, 5, 6, 7] 
	n = len(arr) 

	print(primeCount(arr, n)) 