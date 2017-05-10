counter=0
for i in $(cat 'dstip_unique.txt'); do
   dstip=$i
   freq=`cat 'dstip.txt' | grep -w $dstip | wc -l`
   counter=$((counter+freq))
   echo "$freq" "$dstip" >> dstip_freq.txt
done

echo $counter

sort -n -r dstip_freq.txt >> dstip_freq_descending.txt
