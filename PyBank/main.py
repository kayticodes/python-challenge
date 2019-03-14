#Set variables
    totalmonths = 0 
    nettotal = 0
    netchange = 0
    date = []
    profit = []
    change = []
#designate our delimiter 
    csvreader=csv.reader(csvfile, delimiter=",")
#Tell the program to skip the header when gathering data
    header = next(csvreader)

#Create a for loop that will gather the number of months and the difference in profit/losses
    for row in csvreader : 
#Get the number of months
        totalmonths +=1
        #print(totalmonths)
#Get the number of dates
        date.append(row[0])
#Get the profit/loss
        profit.append(int(row[1]))
#Get the net total
        nettotal+=int(row[1])

#Calculate what the "profit/losses" changes are from the previous row
    for prorow in range(1,totalmonths):
        change.append(profit[prorow]-profit[prorow-1])
        #print(prorow)
#Calculate the "profit/losses" average change
    avechange = round(sum(change)/len(change),2)
    #print(avechange)
#Get the what the greatest increase is
    grChange = round(max(change),2)
#Store the calculated max change
    increaseindex = change.index(grChange)
#Retreive which month had the greatest decrease in profits
    grDecrease = round(min(change),2)
#Store the greatest decrease
    decreaseindex = change.index(grDecrease)

#Print results 
print('Financial Analysis\n------------------------------')
print(f'Total Months: {totalmonths}')
print(f'Total: ${nettotal}')
print(f'Average Change: ${avechange}')
print(f'Greatest Increase in Profits:{date[increaseindex+1]} ${grChange}')
print(f'Greatest Decrease in Profits: {date[decreaseindex+1]} ${grDecrease}')

#to print in terminal run this command: python main.py
#print to a txt file run this command: python main.py >> results.txt 
