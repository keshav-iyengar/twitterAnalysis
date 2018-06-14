import tweepy
import time
import io
from collections import Counter
from datetime import datetime
import numpy as np



#Keshav Iyengar


#f = io.open('./trump.txt', 'r', encoding='utf-8')
fileName = input("File name: ")
filePath = './' + fileName
#filePath = "./trump.txt"
n = int(input("N = "))
#n = 3

f = open(filePath, "r")

listOfUsers = []
for line in f:
    listOfUsers.append(line.split(' ', 1)[0])

sorted_list = Counter(listOfUsers)

print("The top " + str(n) + " users who have tweeted the most are:")
print(sorted_list.most_common()[:n])
print('\n')

f.close()

f = open(filePath, "r")

w = 2
h = len(listOfUsers)
usersAndFollowers = [ [' ' for x in range(w)] for y in range(h) ] 
usersAndRetweets = [ [' ' for x in range(w)] for y in range(h) ] 
usersAndDatetime = [ [' ' for x in range(w)] for y in range(h) ] 
theLine = []
row = 0

for line in f:
	theLine = line.split() #store each line in an array split by words
	length = len(theLine) #to access the last and second to last elements (followers and retweets)
	
	usersAndFollowers[row][0] = theLine[0] #store the username
	usersAndFollowers[row][1] = theLine[length-2] #store his/her follower count
	
	usersAndRetweets[row][0] = theLine[0]
	usersAndRetweets[row][1] = theLine[length-1]

	#usersAndDatetime[row][0] = theLine[0]
	#s = theLine[1] #store the date/time stamp
	#t = datetime.strptime(s[1:-6], '%d/%b/%Y:%H')
	#usersAndDatetime[row][1] = t #strip the brackets, minutes and seconds and convert to date/time object

	row+=1

#convert the string follower/retweet counts to ints
for i in range(h):
	usersAndFollowers[i][1] = int(usersAndFollowers[i][1])
	usersAndRetweets[i][1] = int(usersAndRetweets[i][1])

#sort the two dimensional array in decreasing order by follower/retweet count
usersAndFollowers = sorted(usersAndFollowers, key=lambda x: x[1], reverse=True) 
usersAndRetweets = sorted(usersAndRetweets, key=lambda x: x[1], reverse=True) 

print("The top " + str(n) + " users with the most followers are:")
#print the top n entries in the array
for i in range(n):
	print(usersAndFollowers[i])

print('\n')

print("The top " + str(n) + " users with the most retweets are:")
#print the top n entries in the array
for i in range(n):
	print(usersAndRetweets[i])

f.close()

f = open(filePath, "r")

#store all the dates (without time) 
dateList = []
for line in f:
	theLine = line.split()
	date = theLine[1].split(':')
	dateList.append(date[0][1:])

f.close()

f = open(filePath, "r")

hoursList = []
for line in f:
	theLine = line.split()
	hour = theLine[1].split(':')
	hoursList.append(hour[1])

f.close()

f = open(filePath, "r")

usersAndHrsList = []
index = 0
for line in f:
	theLine = line.split()
	usersAndHrsList.append(theLine[0] + " " + hoursList[index])
	index+=1

f.close()

prevDayIndex = 0
previousDay = dateList[prevDayIndex]

curDayIndex = 0
currentDay = dateList[curDayIndex]

prevHrIndex = 0
previousHour = hoursList[prevHrIndex]

curHrIndex = 0
currentHour = hoursList[curHrIndex]

usersAndHrsList_2 = []
index = 0

f = open(filePath, "r")

for line in f:

	if previousDay == currentDay: #comparing previous line's day to the current line's day

		if previousHour == currentHour: #same for hours
			
			usersAndHrsList_2.append(usersAndHrsList[index]) #if in same day/hour, append to list
			index+=1
			previousHour = hoursList[curHrIndex] #the new 'previousHour' is equal to the one we just examined
			curHrIndex+=1 #to look at the next line's hour
			currentHour = hoursList[curHrIndex] #next line's hour

		else: #if different hours, print the list and continue
			
			sortedList = Counter(usersAndHrsList_2)
			print("Users that tweeted the most per hour for " + previousDay + ": " + str(sortedList.most_common()[:n])) #add [:n] here
			usersAndHrsList_2 = []
			previousHour = hoursList[curHrIndex]
			currentHour = hoursList[curHrIndex]
			
		previousDay = dateList[curDayIndex] #see comments on hours
		curDayIndex+=1 
		currentDay = dateList[curDayIndex]
		
	else: #if different days, print the list and continue

		sortedList = Counter(usersAndHrsList_2)
		print("Users that tweeted the most per hour for " + previousDay + ": " + str(sortedList.most_common()[:n])) #add [:n] here
		usersAndHrsList_2 = []
		previousDay = dateList[curDayIndex]
		currentDay = dateList[curDayIndex]
		
f.close()


