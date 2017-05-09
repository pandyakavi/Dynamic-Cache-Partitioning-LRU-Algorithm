cache = [[0]*2 for _ in range(100)]
read_file = open("url_23rd_feb.txt","r")
in_cache = 0
counter = 0
Miss = 0
cnt=0	

for i in iter(read_file):
	counter = counter + 1
	print counter
	for j in range(0,len(cache)):		
		if i != cache[j][0]:
			in_cache = 0
		else:
			in_cache = 1

			rd_file = open("url_23rd_feb_cp.txt","r")
			lines_till_end = rd_file.readlines()[counter:]
			rd_file.close()

			nxt_counter=0
		
			match_found=0
			for line in lines_till_end:
				nxt_counter+=1
				if i==line:
					match_found=1
					break
			if match_found==0:
				 Next_Count=170135*2 #EOF
			else:
				Next_Count=nxt_counter
			cache[j][1]=Next_Count
			break

	if in_cache==0:
			
		if cache[len(cache)-1][1]!=0:
			Miss = Miss + 1
		
		rd_file = open("url_23rd_feb_cp.txt","r")
		line_til_end = rd_file.readlines()[counter:]
		rd_file.close()

		match_found=0
		nxt_counter=0
		for lin in line_til_end:
			nxt_counter+=1
			if i==lin:
				match_found=1
				break

		if match_found==0:			
			Next_Count=170135*2 #EOF
		else:
			Next_Count=nxt_counter

		if cache[len(cache)-1][1]!=0:
			max_value = max(b for (a,b) in cache)
			for k in range(0,len(cache)):
				if max_value == cache[k][1]:
					cache[k][0] = i
					cache[k][1] = Next_Count
					break
		else:
			min_value = min(b for (a,b) in cache)
			for k in range(0,len(cache)):
				if min_value == cache[k][1]:
					cache[k][0] = i
					cache[k][1] = Next_Count
					break
	

print "Miss is ",(Miss)

	#A SNAPSHOT OF WHAT ALGORITHM DOES
	# cache[URL][Next_Count]
	# if new_request in cache
	#     then
	#     update Next_Count
	# else
	#     remove the cached url with highest Next_Count 	

