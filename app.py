import sys
import pyhtml as h
from jinja2 import Template

f=open('data.csv','r')
marks_table=f.readlines()[1:]

x=sys.argv

if x[1]=='-c':
    course_id=x[2]
    highest=0
    sum=0
    count=0
    for row in marks_table:
        value=row.split(',')
        if value[1]==course_id:
            count+=1
            sum+=int(value[2])
            if int(value[2])>highest:
                highest=int(value[2])
    if count>0:
        avg=sum/count
    print(sum)
    out=open('output.html','w')
    te=Template("<table><tr><td>Average Marks</td><td>Maximum Marks</td></tr><tr><td>{{avg}}</td><td>{{highest}}</td></tr></table>")
    ter=te.render(avg=50,highest=highest)
    out.write(ter)



elif x[1]=='-s':
    student_id=x[2]
    final_table=[]
    total=0
    for row in marks_table:
        value=row.split(',')
        if value[0]==student_id:
            total+=int(value[2])
            final_table.append(value)
    out=open('output.html','w')
    #make Template using jinja2
    te=Template("<table><tr><td>Student id</td><td>Course id</td><td>Marks</td></tr>{% for my_item in final_table %} <tr><td>{{my_item[0]}}</td><td>{{my_item[1]}}</td><td>{{my_item[2]}}</td></tr> {% endfor %}<tr><td colspan='2'>Total Marks</td><td>{{total}}</td></tr></table>")
    ter=te.render(final_table=final_table,total=total)
    out.write(ter)
else:
    print('Other value not allowed')
