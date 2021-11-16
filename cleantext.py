import re
import sys

no_of_sets =4
qno=0
l = len(sys.argv)
if l>2:
    qno=int(sys.argv[2])-1
if l>3:
    no_of_sets = int(sys.argv[3])

filename = sys.argv[1]
file = open(filename)
file2 = open("questions.txt",'w')
text = file.readlines()
text2 =[]

for line in text:
    line = line.encode("ascii","ignore").decode()
    line = re.sub('\W+', ' ', line)
    file2.write(line+"\n")
file.close()
file2.close()

filename = "questions.txt"
file = open(filename,'r')
text = file.readlines()
file.close()

questions = []

for line in text:
    line = line.strip()
    if line in ['\n', '\r\n']:
        continue
    # line = ''.join(char for char in line if char.isalnum())
    if len(line)>10 and line[0].isdigit():
        nqno = [int(i) for i in line.split() if i.isdigit()]
        if len(nqno)>0 and nqno[0] == qno+1 :
            # print(line)
            line=line.split(' ',1)[1]
            if(line.endswith(("Point","point","Points"))):
                questions.append(line.rsplit(' ',2)[0])
            qno = qno + 1

i=0
batch=len(questions)//no_of_sets
for i in range(no_of_sets):
    filename = "set"+str(i+1)+".txt"
    file = open(filename,'w')
    j = i+1
    for ques in questions[i*batch:j*batch]:
        # print("------------",ques)
        file.write(ques+'\n')
    file.close()
