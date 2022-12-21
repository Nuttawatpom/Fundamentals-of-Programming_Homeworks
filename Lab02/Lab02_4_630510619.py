#630510619
#nuttawat khamwangsawat
#section003
#Lab02_04
milliseconds = int(input("Input number of milliseconds: "))#set milleseconds
day = (milliseconds/(10**3)/3600/24)#find day for milliseconds
hour = (day-int(day))*24#find hour
minute = (hour-int(hour))*60#minute
second = (minute-int(minute))*60#find second
millisec = ((second-int(second))*(10**3))#find millisec
print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %.0f millisec(s)"%(day,hour,minute,second,millisec))#answer