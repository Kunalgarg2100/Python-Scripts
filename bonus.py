
import matplotlib.pyplot as plt
import csv
assign_1 = []
assign_1g = []
assign_2 = []
assign_2g = []
assign_3g = []
assign_4g = []
assign_3 = []
assign_4 = []
labs = []
labsg =[]
lab_exam = []
lab_examg =[]
midsem_1 = []
midsem_1g = []
midsem_2g = []
midsem_2 = []
end_sem = []
end_semg = []
grand =[]
grandg = []


with open('grades.csv','r') as csvfile:
    plots = csv.reader(csvfile,delimiter = ',')

    for row in plots:
        if row[0] != 'rollno':
             
             assign_1.append(float(row[1]))
             assign_2.append(float(row[2]))
             assign_3.append(float(row[3]))
             assign_4.append(float(row[4]))
             labs.append(float(row[5]))
             lab_exam.append(float(row[6]))
             midsem_1.append(float(row[7]))
             midsem_2.append(float(row[8]))
             end_sem.append(float(row[9]))

length = len(assign_1)
for i in range (0,length):
    grand.append(assign_1[i] + assign_2[i] + assign_3[i] + assign_4[i] + lab_exam[i] + labs[i] + midsem_2[i] + midsem_1[i] + end_sem[i])
    assign_1g.append(assign_1[i])
    assign_2g.append(assign_2[i])
    assign_3g.append(assign_3[i])
    assign_4g.append(assign_4[i])
    labsg.append(labs[i])
    lab_examg.append(lab_exam[i]*2)
    midsem_1g.append(midsem_1[i]/9)
    midsem_2g.append(midsem_2[i]/9)
    end_semg.append(end_sem[i]/18)
    grandg.append(grand[i]/41.5)

filename = ['assignment_1','assignment_2','assignment_3','assignment_4','labs','lab_exam','midsem_1','midsem_2','end_sem','grand_total']
titlename = ['Assignment 1','Assignment 2','Assignment 3','Assignment 4','Lab','Lab exam','Midsem 1','Midsem 2','End Sem','Grand Total']
grades_display = [assign_1g,assign_2g,assign_3g,assign_4g,labsg,lab_examg,midsem_1g,midsem_2g,end_semg,grandg]
grades = ['A','A-','B','B-','C','C-','D','F']
x = [0,1.25, 2.5, 3.75, 5,6.25, 7.5, 8.75, 10]
def fun3(ass,m):
    plt.xlabel('Grade')
    plt.ylabel('No of students')
    plt.title(titlename[m] + '\n' + 'Analysis')
    plt.xticks(x, grades)
    plt.hist(ass, x,edgecolor ='black',linewidth='1.2', align='left')
    print('Saving ' + filename[m] + '.png')
    plt.savefig(filename[m] + '.png')
    plt.clf()

for q in range(0,len(grades_display)):
    fun3(grades_display[q],q)
