        #taking dates input
date1 = input("Enter start date(dd/mm/yyyy):")
date2 = input("Enter end date(dd/mm/yyyy):")

dd1 = date1[0:2]        #day of first date
dd1 = int(dd1)

dd2 = date2[0:2]        #day of second date
dd2 = int(dd2)


mm1 = date1[3:5]        #month of first date
mm1 = int(mm1)
mm2 = date2[3:5]        #month of second date
mm2 = int(mm2)

yyyy1 = date1[6:10]     #year of first date
yyyy1 = int(yyyy1)
yyyy2 = date2[6:10]     #year of second date
yyyy2 = int(yyyy2)

if(yyyy2<yyyy1):
    print("please enter a valid date")
else:
    if dd2 < dd1:
        dd2 += 30
        day = dd2-dd1
        mm1 += 1
    else:
        day = dd2-dd1

    if mm2<mm1:
        mm2 += 12
        month = mm2-mm1
        yyyy1 += 1
    else:
        month = mm2-mm1
    year = yyyy2 - yyyy1
    print("Difference between dates is:",day,"days",month,"months",year,"year")


