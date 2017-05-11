import csv
import sys

with open("Url_24th_Feb_non_unique.txt") as xh:
  with open('User_24th_Feb_non_unique.txt') as yh:
    with open("User_Url.txt","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists
      #Write to third file
      for i in range(len(xlines)):
        line = ylines[i].strip() + ' ' + xlines[i]
        zh.write(line)


#Source : http://stackoverflow.com/questions/39717828/python-combine-two-text-files-into-one-line-by-line
