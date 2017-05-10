#----- TYPE - 1 -----

counter=0
liner=0

for i in $(cat 'User_Freq_23_Feb.txt'); do
   counter=$((counter+i))
   liner=$((liner+1))
   
   if [ "$counter" -gt 85068 ] #50% of 170135
   then 
	break
   fi
	
done

echo $counter
echo $liner
linerr=$((liner+1))

user_id=`cat 'User_Freq_descending_23_Feb.txt' | head -n $liner | cut -d ' ' -f 2`
#echo $user_id

for k in $user_id; do  
   echo "$k" "TYPE_1" >> User_Types.txt
done

#---- TYPE - 2  -----

counter_1=0
liner_1=0
mid_file=`sed -n $linerr,66p User_Freq_23_Feb.txt`

for j in $mid_file; do  
   counter_1=$((counter_1+j))
   liner_1=$((liner_1+1))

   if [ "$counter_1" -gt 51040 ] #30% of 170135
   then
   	break
   fi
      
done

echo $counter_1
echo $liner_1
linerr_1=$((liner+liner_1))

user_id_1=`sed -n $linerr,"$linerr_1"p User_Freq_descending_23_Feb.txt | cut -d ' ' -f 2`
#echo $user_id_1
for m in $user_id_1; do  
   echo "$m" "TYPE_2" >> User_Types.txt
done

#------- TYPE - 3  --------

linerr_2=$((linerr_1+1))
user_id_2=`sed -n $linerr_2,66p User_Freq_descending_23_Feb.txt | cut -d ' ' -f 2`
#echo $user_id_2
for n in $user_id_2; do  
   echo "$n" "TYPE_3" >> User_Types.txt
done

