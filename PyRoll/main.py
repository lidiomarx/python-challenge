import csv

fn = 'election_data.csv'
ofn = 'results.txt'
reader = csv.reader(open(fn))
header = next(reader)
out_fhandler = open(ofn,'w')
votes = {}
total = 0
winner = None
for voter,county,candidate in reader:
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    if winner is None or votes[candidate] > votes[winner]:
        winner = candidate
    total += 1

output = f"""Election Results
-------------------------
Total Votes: {total}
-------------------------"""
print(output)
out_fhandler.write(output+'\n')
for candidate in votes:
    output = f"{candidate}: {100*votes[candidate]/total:0.3f}% ({votes[candidate]})"
    print(output)
    out_fhandler.write(output+'\n')

output = f"""-------------------------
Winner: {winner}
-------------------------
"""
print(output)
out_fhandler.write(output+'\n')
