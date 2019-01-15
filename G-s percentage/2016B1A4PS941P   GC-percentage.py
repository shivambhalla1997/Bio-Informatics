# program to calculate the number of G in the gene and the percent of G in the whole gene

gene= open("BRCA1_gene.txt","r")

#making the value of G-C to be 0

GC=0
total=0

#skip the first header line
gene.readline()

for line in gene:
    line =line.lower() #converting the gene string to lower case
    for ch in line:
        total+=1
        if ch=='g' or ch=='c':
            GC+=1
        
#printing the total G's in the gene        
print ("number of G+C =",GC)

#calculating and printing the G's percentage
G_percentage=(GC+0.)/(total+0.)
print ("GC percentage =",G_percentage*100,"%")

