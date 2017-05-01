import time
start_time = time.time()

from random import randint
cache = [[0]*2 for _ in range(50)]
#read_file = open("Short_Hostname.txt","r")
read_file = open("Url_24th_Feb_non_unique.txt","r")
in_cache = 0
counter = 0
Miss = 0

for i in iter(read_file):
	counter = counter + 1
	
	for j in range(0,len(cache)):		
		if i != cache[j][0]:
			in_cache = 0

		else:
			in_cache = 1
			cache[j][1] = counter
			break
	if in_cache==0:
		if cache[len(cache)-1][1]!=0: #Once cahe is initially filled. The if part will implement RR(Random Replacement)
			Miss = Miss + 1
			position=randint(0,len(cache)-1)
			cache[position][0] = i
			cache[position][1] = counter

		else: #At first we have to fill the cache. The else part will thus help in filling up the cache fo the first
			min_value = min(b for (a,b) in cache)
			for k in range(0,len(cache)):
				if min_value == cache[k][1]:
					cache[k][0] = i
					cache[k][1] = counter
					break


#for z in range(0,len(cache)):
#	print cache[z][0],(cache[z][1])

print " RR Miss is ",(Miss)
print("--- %s seconds ---" % (time.time() - start_time))


