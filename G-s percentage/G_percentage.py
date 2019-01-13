# program to calculate the number of G in the gene and the percent of G in the whole gene

gene= open("BRCA1_gene.txt","r")

#making the value of G to be 0

G=0
total=0

#skip the first header line
gene.readline()

for line in gene:
    line =line.lower() #converting the gene string to lower case
    for ch in line:
        total+=1
        if ch=='g':
            G+=1
        
#printing the total G's in the gene        
print ("number of G's =",G)

#calculating and printing the G's percentage
G_percentage=(G+0.)/(total+0.)
print ("G's percentage =",G_percentage)

