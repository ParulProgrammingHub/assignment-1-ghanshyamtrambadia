#enter marks of 5 subjects and find the mean of 5 subjects, calculate percentage. If percentage is less than 35 print fail else print pass.
maths=input("marks obtained in maths")
mi=input("marks obtained in mi")
py=input("marks obtained in python")
dbms=input("marks obtained in dbms")
co=input("marks obtained in co")
total = maths + mi + py + dbms + co
avg= total/5.0
print "The mean is %s" % (avg)
per=(total*100)/250
if per<=35 :
    print "YOU HAVE FAILED THE EXAM AND YOU HAVE SCORED %s " % (per)

else :
    print "YOU HAVE PASSED THE EXAM AND YOU HAVE SCORED %s " % (per)
