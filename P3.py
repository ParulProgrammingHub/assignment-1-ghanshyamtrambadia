# enter value in centimetre and convert it to meter and kilometre.
cm=input("Enter the value in centimeter")
m= float (cm/100)
km= float (m/1000)
choice = input("""Enter 1 to convert in meter
and  2 to convert in kilometer""")
if choice ==1:
    print "The distance in meter is %s" % (m)
elif choice ==2:
    print "The distance in kilometer is %s" % (km)
else:
    print "Enter the valid Choice"
    
