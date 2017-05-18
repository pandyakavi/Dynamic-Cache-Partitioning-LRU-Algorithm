for i in $(cat 'User23.txt'); do

counter=0

#File-2
if grep -Fxq "$i" User24.txt 
then
    counter=$((counter+1))
fi


if [ $counter -ne 1 ]
then
    echo "$i" >> User_23_24_common_files.txt
fi

done
