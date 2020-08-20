# <!-- * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote. -->

import os 
import csv

poll_data = os.path.join("election_data.csv")

def poll_analysis(poll_data):
#set variables 
  total_votes = 0
  unique_candidates = [] 
  khan_votes = 0
  correy_votes = 0
  li_votes = 0
  otooley_votes = 0
  khan_percent = 0 
  correy_percent = 0 
  li_percent = 0 
  otooley_percent = 0 
#for each row in poll_data do the following
  for row in poll_data:
    total_votes += 1
    candidate = row[2]
    # if candidate == "Khan":
    #   khan_votes = khan_votes + 1 
#this if statement will append the string in row[2] to unique_candidates[] if the value is unique
    if candidate not in unique_candidates:
        unique_candidates.append(candidate)
    if candidate == unique_candidates[0]:
      khan_votes = khan_votes + 1 
    elif candidate == unique_candidates[1]:
      correy_votes = correy_votes + 1 
    elif candidate == unique_candidates[2]:
      li_votes = li_votes + 1 
    else:
      otooley_votes = otooley_votes + 1
  khan_percent = (khan_votes/total_votes)*100 
  correy_percent = (correy_votes/total_votes)*100
  li_percent = (li_votes/total_votes)*100
  otooley_percent = (otooley_votes/total_votes)*100 
    
  if total_votes == khan_votes + correy_votes + li_votes + otooley_votes:
    success = True
  cand_dict = {"Khan": khan_percent, "Correy": correy_percent, "Li": li_percent}
  winner = max(cand_dict, key=cand_dict.get)


    # if str(row[2]) == "Khan":
    #   khan_votes = khan_votes + 1 
#write countif statement that will sum numbers if they are equal to one of the values in the list 
  # khan_votes = sum(1 for row in poll_data if candidate == unique_candidates[0])
  # correy_votes = sum(1 for row in poll_data if candidate == unique_candidates[1])
  # li_votes = sum(1 for row in poll_data if candidate == unique_candidates[2])
  # otooley_votes = sum(1 for row in poll_data if candidate == unique_candidates[3])
  return [total_votes, unique_candidates, khan_votes, correy_votes, li_votes, otooley_votes, success, khan_percent, correy_percent, li_percent, otooley_percent, winner]

with open(poll_data, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ',')
  next(csvfile)
  analysis = poll_analysis(csvreader)
output_summary = print(
f"""Poll Results:\n
Total votes: {analysis[0]}\n
Unique Candidates: {analysis[1]}\n
Khan total votes: {analysis[2]}, {analysis[7]}%\n
Correy total votes: {analysis[3]}, {analysis[8]}%\n
Li total votes: {analysis[4]}, {analysis[9]}%\n
O'Tooley total votes: {analysis[5]}, {analysis[10]}%\n
All votes accounted for: {analysis[6]}\n
winner: {analysis[11]}"""
)

output_path = os.path.join("..", "output", "PollResults.txt")

with open(output_path, "a") as f:
  print(
f"""Poll Results:\n
Total votes: {analysis[0]}\n
Unique Candidates: {analysis[1]}\n
Khan total votes: {analysis[2]}, {analysis[7]}%\n
Correy total votes: {analysis[3]}, {analysis[8]}%\n
Li total votes: {analysis[4]}, {analysis[9]}%\n
O'Tooley total votes: {analysis[5]}, {analysis[10]}%\n
All votes accounted for: {analysis[6]}\n
winner: {analysis[11]}""", file = f
)
