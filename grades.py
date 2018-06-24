import compute
'''
Created on May 14, 2018

@author: anush
'''



a1list=[]
with open("class.txt","r") as file_obj:
    datasets=file_obj.readlines()
with open("a1.txt","r") as a1file:
    first_line=a1file.readline()
    rest_lines=a1file.readlines()
with open("a2.txt","r") as a2file:
    first_linea2=a2file.readline()
    a2data=a2file.readlines()
with open("project.txt","r") as projfile:
    first_lineproject=projfile.readline()
    projdata=projfile.readlines()
with open("test1.txt","r") as test1file:
    first_linetest1=test1file.readline()
    test1data=test1file.readlines()
with open("test2.txt","r") as test2file:
    first_linetest2=test2file.readline()
    test2data=test2file.readlines()
options=("a1","A1","a2","A2","pr","PR","t1","T1","t2","T2")

while True:
    print ("1> Display individual component")
    print ("2> Display component average")
    print ("3> Display Standard Report")
    print ("4> Sort by alternate column")
    print ("5> Change Pass/Fail point")
    print ("6> Exit")
    user_choice=input("Select from above options from 1-6-->")
    if user_choice=="1":
        option1=input("select component name (A1,A2,PR,T1,orT2)-->") 
        while option1 not in options:
            option1=input("select valid option either A1,A2,PR,T1,orT2--> ")
        if(option1=="A1" or option1=="a1"):
            compute.a1component("A1 grades",first_line,rest_lines,datasets)
        elif(option1=="A2" or option1=="a2"):
            compute.a1component("A2 grades",first_linea2,a2data,datasets)
        elif(option1=="PR" or option1=="pr"):
            compute.a1component("PR grades",first_lineproject,projdata,datasets)
        elif(option1=="T1" or option1=="t1"):
            compute.a1component("T1 grades",first_linetest1,test1data,datasets)
        elif(option1=="T2" or option1=="t2"):
            compute.a1component("T2 grades",first_linetest2,test2data,datasets)
    elif user_choice=="2":
        option2=input("select component name (A1,A2,PR,T1,orT2)-->")
        while option2 not in options:
            option2=input("select valid option either (A1,A2,PR,T1,orT2) ")
        if(option2=="a1" or option2=="A1"):
            compute.a1average("A1 average",first_line,rest_lines,datasets)
        elif(option2=="a2" or option2=="A2"):
            compute.a1average("A2 average",first_linea2,a2data,datasets)
        elif(option2=="PR" or option2=="pr"):
            compute.a1average("Project average",first_lineproject,projdata,datasets)
        elif(option2=="T1" or option2=="t1"):
            compute.a1average("T1 average",first_linetest1,test1data,datasets)
        elif(option2=="T2" or option2=="t2"):
            compute.a1average("T2 average",first_linetest2,test2data,datasets)
    elif user_choice=="3":
        compute.standardreport(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2,"50")    
    elif user_choice=="4":
        opt=["0","1",0,1]
        option3=input(" select by 0.LastName or 1.GR(Numeric Grade)")
        while(option3 not in opt):
            option3=input("please choose correct option, select 0 for lastname and 1 for grade ")
        if option3=="0":
            compute.sort_by_lastname(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2)
        elif option3=="1":
            compute.sort_by_gr(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2)
    elif user_choice=="5":
        option4=input("select new P/F point")
        compute.standardreport(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2,option4)
    elif user_choice=="6":
        print("GOOD BYEE")
        break;
    else:
        print("Please select a valid option between 1-6  ")