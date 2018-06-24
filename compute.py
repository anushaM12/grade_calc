'''
Created on May 14, 2018

@author: anush
'''
from _collections import OrderedDict
class stu_data:
    def __init__(self,stu_id,firstname,lastname):
        self.stu_id=stu_id
        self.firstname=firstname
        self.lastname=lastname
def a1component(x,first_line,alist,datasets):
    print(x," ",'({})'.format(first_line.strip()))
    for each_line in datasets:
        stu_id,first_name,last_name=each_line.split("|")
        stu_data_obj= stu_data(stu_id,first_name,last_name)
        for single_line in alist:
            #single_line.replace('\n','')
            stu1_id,a1marks=single_line.split("|")
            if stu1_id in stu_data_obj.stu_id:
            
                print(stu1_id," "*5,stu_data_obj.lastname.replace("\n",""),",",stu_data_obj.firstname.replace("\n","")," "*(6-len(stu_data_obj.firstname)),a1marks.replace("\n",""))
def a1average(x,first_line,rest_lines,datasets):
    total_students=0
    summation=0.0
    for line in datasets:
        total_students+=1
    for each_line in rest_lines:
        stu1_id,a1marks=each_line.split("|")
        summation+=float(a1marks)
    avg=summation/total_students
    print(x,":",round(avg,2),"/",first_line)
def checkgrade(passpoint,grandfinal):
    passpoint=int(passpoint)
    gradecal=(100-passpoint)/7
    if(grandfinal<passpoint):
        return "F"
    if(grandfinal>gradecal and grandfinal<=gradecal+passpoint):
        return "c"
    if(grandfinal>gradecal+passpoint and grandfinal<=2*gradecal+passpoint):
        return "B-"
    if(grandfinal>2*gradecal+passpoint and grandfinal<=3*gradecal+passpoint):
        return "B"
    if(grandfinal>3*gradecal+passpoint and grandfinal<=4*gradecal+passpoint):
        return "B+"
    if(grandfinal>4*gradecal+passpoint and grandfinal<=5*gradecal+passpoint):
        return "A-"
    if(grandfinal>5*gradecal+passpoint and grandfinal<=6*gradecal+passpoint):
        return "A"
    if(grandfinal>6*gradecal+passpoint and grandfinal<=7*gradecal+passpoint):
        return "A+"
        
def standardcalculation(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,a2total,projecttotal,test1total,test2total,passpoint):
    classdata={}
    #classdt={}
    count=0
    Grand_Total=0.0
    FinalGrade=""
    student_data={'lastname','firstname','a1mark','a2mark','projmark','test1mark','test2mark','gr','fl'}
    total_students=0
    for line in datasets:
        total_students+=1
    for i in range(0,total_students):
        for line in datasets:
            stu_id,firstname,lastname=line.split("|")
            classdata[stu_id]={}
            classdata[stu_id]['lastname']=lastname.replace("\n","")
            classdata[stu_id]['firstname']=firstname
            for entry in student_data:
                for single_line in rest_lines:
                    studentid,a1marks=single_line.split("|")
                    if studentid in stu_id:
                        count+=1
                        classdata[stu_id]['a1mark']=float(a1marks.replace("\n","")) 
                if count==0:
                    classdata[stu_id]['a1mark']=0.0
            count=0
            for entry in student_data:
                for single_line in a2data:
                    studentid,a2marks=single_line.split("|")
                    if studentid in stu_id:
                        count+=1
                        classdata[stu_id]['a2mark']=float(a2marks.replace("\n",""))
                if count==0:
                    classdata[stu_id]['a2mark']=0.0
            count=0
            for entry in student_data:
                for single_line in projdata:
                    studentid,projmarks=single_line.split("|")
                    if studentid in stu_id:
                        count+=1
                        classdata[stu_id]['projmark']=float(projmarks.replace("\n",""))
                if count==0:
                    classdata[stu_id]['projmark']=0.0
            count=0
                        
            for entry in student_data:
                for single_line in test1data:
                    studentid,test1marks=single_line.split("|")
                    if studentid in stu_id:
                        count+=1
                        classdata[stu_id]['test1mark']=float(test1marks.replace("\n",""))
                if count==0:
                    classdata[stu_id]['test1mark']=0.0
            count=0
            for entry in student_data:
                for single_line in test2data:
                    studentid,test2marks=single_line.split("|")
                    if studentid in stu_id:
                        count+=1
                        classdata[stu_id]['test2mark']=float(test2marks.replace("\n",""))
                if count==0:
                    classdata[stu_id]['test2mark']=0.0
                #test2fl=float(classdata[stu_id]['test2mark'])
                #Grand_Total+=30*test2fl/float(test2total)
                #print(Grand_Total)
                #print(type(classdata[stu_id]['test2mark']))
                Grand_Total+=(30*(classdata[stu_id]['test2mark']))/float(test2total)+(30*(classdata[stu_id]['test1mark']))/float(test1total)+(25*(classdata[stu_id]['projmark']))/float(projecttotal)+(7.5*(classdata[stu_id]['a1mark']))/float(first_line)+(7.5*(classdata[stu_id]['a2mark']))/float(a2total)
                classdata[stu_id]['gr']=Grand_Total
                FinalGrade=checkgrade(passpoint,Grand_Total)
                classdata[stu_id]['fl']=FinalGrade
                Grand_Total=0
                count=0
    return classdata
def standardreport(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2,passpoint):
    classdata=standardcalculation(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2,passpoint)
    
    #print("ID:"," "*3,"  LN:"," "*3,"FN:"," "*4, "A1:","A2:","PR:","T1:","T2:","GR:"," "*3,"FL: ")
    print('{:<8s}{:>6s}{:>6s}{:>8s}{:>4s}{:>4s}{:>4s}{:>4s}{:>6s}{:>4s}'.format("ID","LN","FN","A1","A2","PR","T1","T2","GR","FL"))
    for key,value in sorted(classdata.items()):
        print(key," "*3,value['lastname']," "*(6-len(value['lastname'])),value['firstname'],
              " "*(6-len(value['firstname']))," " if int(value['a1mark'])==0 else int(value['a1mark']) ," "*(4-len(str(value['a1mark']))),
              " " if int(value['a2mark'])==0 else int(value['a2mark'])," "*(4-len(str(value['a2mark']))),
              " " if int(value['projmark'])==0 else int(value['projmark'])," "*(4-len(str(value['projmark']))),
              " " if int(value['test1mark'])==0 else int(value['test1mark']) ," "*(4-len(str(value['test1mark']))),
              " " if int(value['test2mark'])==0 else int(value['test2mark']),
              " "*(4-len(str(value['test2mark']))),'{:.2f}'.format(round(value['gr'],2))," "*(2-len(str(value['gr']))),value['fl'])
def sort_by_lastname(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2):
    lastnamesort=standardcalculation(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2,50)
    ordered=OrderedDict(sorted(lastnamesort.items(),key=lambda i:i[1]['lastname']))
    print('{:<8s}{:>6s}{:>6s}{:>8s}{:>4s}{:>4s}{:>4s}{:>4s}{:>6s}{:>4s}'.format("ID","LN","FN","A1","A2","PR","T1","T2","GR","FL"))
    for key,value in ordered.items():
        print(key," "*3,value['lastname']," "*(6-len(value['lastname'])),value['firstname'],
              " "*(6-len(value['firstname']))," " if int(value['a1mark'])==0 else int(value['a1mark']) ," "*(4-len(str(value['a1mark']))),
              " " if int(value['a2mark'])==0 else int(value['a2mark'])," "*(4-len(str(value['a2mark']))),
              " " if int(value['projmark'])==0 else int(value['projmark'])," "*(4-len(str(value['projmark']))),
              " " if int(value['test1mark'])==0 else int(value['test1mark']) ," "*(4-len(str(value['test1mark']))),
              " " if int(value['test2mark'])==0 else int(value['test2mark']),
              " "*(4-len(str(value['test2mark']))),'{:.2f}'.format(round(value['gr'],2))," "*(2-len(str(value['gr']))),value['fl'])
def sort_by_gr(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2):
    grsort=standardcalculation(first_line,datasets,rest_lines,a2data,projdata,test1data,test2data,first_linea2,first_lineproject,first_linetest1,first_linetest2,50)
    ordered=OrderedDict(sorted(grsort.items(),key=lambda i:i[1]['gr'],reverse=True))
    print('{:<8s}{:>6s}{:>6s}{:>8s}{:>4s}{:>4s}{:>4s}{:>4s}{:>6s}{:>4s}'.format("ID","LN","FN","A1","A2","PR","T1","T2","GR","FL"))
    for key,value in ordered.items():
        print(key," "*3,value['lastname']," "*(6-len(value['lastname'])),value['firstname'],
              " "*(6-len(value['firstname']))," " if int(value['a1mark'])==0 else int(value['a1mark']) ," "*(4-len(str(value['a1mark']))),
              " " if int(value['a2mark'])==0 else int(value['a2mark'])," "*(4-len(str(value['a2mark']))),
              " " if int(value['projmark'])==0 else int(value['projmark'])," "*(4-len(str(value['projmark']))),
              " " if int(value['test1mark'])==0 else int(value['test1mark']) ," "*(4-len(str(value['test1mark']))),
              " " if int(value['test2mark'])==0 else int(value['test2mark']),
              " "*(4-len(str(value['test2mark']))),'{:.2f}'.format(round(value['gr'],2))," "*(2-len(str(value['gr']))),value['fl'])
    
   
            
    
