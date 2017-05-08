import time
start_time = time.time()

cache = [[0]*2 for _ in range(1000)]
#read_file = open("Short_Hostname.txt","r")
read_file = open("Url_24th_Feb_non_unique.txt","r")
in_cache = 0
Miss = 0
init = 1

for i in iter(read_file):
	
	for j in range(0,len(cache)):		
		if i != cache[j][0]:
			in_cache = 0

		else:
			in_cache = 1
			cache[j][1] = cache[j][1] + 1
			break
	if in_cache==0:
		if cache[len(cache)-1][1]!=0: #Once cahe is initially filled. The if part will implement MRU
			Miss = Miss + 1
			max_value = max(y for (x,y) in cache)
			for z in range(0,len(cache)):
				if max_value == cache[z][1]:
					cache[z][0] = i
					cache[z][1] = init
					break
		else: #At first we have to fill the cache. The else part will thus help in filling up the cache fo the first
			min_value = min(b for (a,b) in cache)
			for k in range(0,len(cache)):
				if min_value == cache[k][1]:
					cache[k][0] = i
					cache[k][1] = init
					break


#for z in range(0,len(cache)):
#	print cache[z][0],(cache[z][1])

print "MFU Miss is ",(Miss)

	#Read the webaddress from the host file
	#Check if that webaddress is in our cache
	# IF the webaddress in cache 
	#	THEN just update the counter value
	# ELSE
	#	Delete the row which has low counter value
	#       And add the current web address and the counter value in the deleted row place

print("--- %s seconds ---" % (time.time() - start_time))
