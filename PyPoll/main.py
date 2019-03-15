#import modules
import os 
import csv 

#create a path for the csv file
election_data= os.path.join("election_data.csv")

#Set our variables
total_votes = 0
stored_candidates = []
unique_candidates = []
votes_candidates = []
votes_percentage = []

#read the CSV 
with open(election_data,newline="") as csvfile: 
    #Set the delimiter as a comma
    csvreader = csv.reader(csvfile,delimiter=",")
    #Tell the program to skip the header row when counting 
    header = next(csvreader)

    #create a loop that will go through each csv row
    for row in csvreader:
        #count the number of votes cast and then total them
        total_votes +=1
        #store the candidates while we're at it 
        stored_candidates.append(row[2])
    
    #create a set for each unique candidate
    for candidates in set(stored_candidates):
        #make a list of all the unique candidates
        unique_candidates.append(candidates)
        #count up the votes for each 
        count_candidates= stored_candidates.count(candidates)
        #create a list tallying the votes 
        votes_candidates.append(count_candidates)
        #Calculate the percentage of votes for each candidate
        votes_calculated = round((count_candidates/total_votes)*100,2)
        #generate a list of the voting percentage
        votes_percentage.append(str(votes_calculated)+"%")
    #using the zip function, create a list putting the candidates together with their corresponding metrics
    poll_results = list(zip(unique_candidates,votes_percentage,votes_candidates))

    #get the candidate with the most votes 
    for x in poll_results:
        if max(votes_candidates)== x[2]:
            winner = x[0]

#print the results 
print("Election Results \n-----------------------")
print(f'Total Votes:  {total_votes}\n------------------------')
print(f'{poll_results[0][0]}: {poll_results[0][1]}({poll_results[0][2]})')   
print(f'{poll_results[1][0]}: {poll_results[1][1]}({poll_results[1][2]})')  
print(f'{poll_results[2][0]}: {poll_results[2][1]}({poll_results[2][2]})') 
print(f'{poll_results[3][0]}: {poll_results[3][1]}({poll_results[3][2]})') 
print('----------------------------')
#instead of using 'Winner', I decided to go with a more politically correct way of disclosing the results  
print(f'Candidate with the most votes: {winner}')


#print to a txt file run this command: python main.py >> results.txt 
#to print in terminal run this command: python main.py

