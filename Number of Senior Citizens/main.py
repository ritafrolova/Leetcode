def countSeniors(details):
    count=0
    for i in details:
        list_age= i[11],i[12]
        age="".join(list_age)
        if int(age)>60:
            count+=1
    return count
print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))