import os
import csv
#Import os and csv and create a variable to store your csv file
csv_path = os.path.join('Resources','election_data.csv')
#Create 4 variables to hold total votes and each candidates vote share
total_votes = 0
CCS_votes = 0
DG_votes = 0
RAD_votes = 0
#Read the csv file into python so we can work on it
with open(csv_path, 'r') as vote_file:
    
    vote_reader = csv.reader(vote_file, delimiter=',')
    
    header = next(vote_reader)
    # Use a for loop to loop through each row
    for row in vote_reader:
        #Add one each row for total votes
        total_votes += 1
        #Use an if statement to see if the candidates name matches then row for votes and if so add one to each corresponding vote variable
        if row[2] == 'Charles Casper Stockham':
           CCS_votes += 1
        elif row[2] == 'Diana DeGette':
            DG_votes += 1
        elif row[2] == 'Raymon Anthony Doane':
            RAD_votes += 1
        
    #Create a list of all the candidates and a list of all the votes for each candidate    
    candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    votes = [CCS_votes, DG_votes, RAD_votes]
    #Create a dictionairy that will hold the zip function of the last two lists as tuples
    candidates_votes = dict(zip(candidates, votes))
    #Store the candidate who got the most in the winner variable using the key function to make sure the one with the most votes is the winner
    winner = max(candidates_votes, key=candidates_votes.get)
    #Find the percentage of the vote gained for each of the 3 candidates
    CCS_percent = round(CCS_votes/total_votes * 100, 3)
    DG_percent = round(DG_votes/total_votes * 100, 3)
    RAD_percent = round(RAD_votes/total_votes * 100, 3)
        
    print("Election Results")
    print("--------------------------------------------------")
    print(f'Total Votes: {total_votes}')
    print(f'Charles Casper Stockham: {CCS_percent}% {CCS_votes}')
    print(f'Diana DeGette: {DG_percent}% {DG_votes}')
    print(f'Raymon Anthony Doane: {RAD_percent}% {RAD_votes}')
    print("--------------------------------------------------")
    print(f'Winner: {winner}')
    print("--------------------------------------------------")
    
    csv_path = os.path.join('Analysis','Voter_Analysis.txt')
    # Use the write application to write our findings into the txt file we created
    #The \n are used to move down a row after each row has been written
    with open(csv_path, "w") as writing_file:
        
        writing_file.write("Election Results")
        writing_file.write("\n")
        writing_file.write("--------------------------------------------------")
        writing_file.write("\n")
        writing_file.write(f'Total Votes: {total_votes}')
        writing_file.write("\n")
        writing_file.write(f'Charles Casper Stockham: {CCS_percent}% {CCS_votes}')
        writing_file.write("\n")
        writing_file.write(f'Diana DeGette: {DG_percent}% {DG_votes}')
        writing_file.write("\n")
        writing_file.write(f'Raymon Anthony Doane: {RAD_percent}% {RAD_votes}')
        writing_file.write("\n")
        writing_file.write("--------------------------------------------------")
        writing_file.write("\n")
        writing_file.write(f'Winner: {winner}')
        writing_file.write("\n")
        writing_file.write("--------------------------------------------------")