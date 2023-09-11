import csv
att=[['Sunny','Rainy'],['Warm','Cold'],['Normal','High'],['Strong','Weak'],['Warm','Cool'],['Same','Change']]
a=[]
with open('/content/data.csv','r') as csvFile:
  reader=csv.reader(csvFile)
  for row in reader:
    a.append(row)
n=len(att)
hyp=[0]*n
print(hyp)
for i in range(0,n):
    hyp[i]=a[1][i]
for i in range(1,len(a)):
    if a[i][n]=="Yes":
      for j in range(0,n):
        if(a[i][j]!=hyp[j]):
          hyp[j]='?'
        else:
          hyp[j]=a[i][j]
print(hyp)
