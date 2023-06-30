people = 40
teams = 4

for i in teams:
  team[i] = []
  
team_four =[]
team_three =[]
team_two=[]
team_one=[]

while counter > 0:
  team_number = counter % teams
  if team_number == 0: team_number = 4 and team_four.append(counter)
  elif team_number == 3: team_number = 3 and team_three.append(counter)
  elif team_number == 2: team_number = 2 and team_two.append(counter)
  elif team_number == 1: team_number =1 and team_one.append(counter)
  print("Team 4",team_four)
  print("Team 3",team_three)
  print("Team 2",team_two)
  print("Team 1",team_one)
  print ("Team member", counter, "has been assigned")
  counter = counter - 1
  

  def assign_teams(people, teams):
    teamnumber = [[] for _ in range(teams)]
    
    for i in range(people):
        person = "Person {}".format(i + 1)
        team = i % teams
        teamnumber[team].append(person)
    
    return teamnumber

# Example usage
num_people = 40
num_teams = 4

teams_assigned = assign_teams(num_people, num_teams)

# Print which person is in which team
for i, team in enumerate(teams_assigned):
    print("Team {}: {}".format(i + 1, ", ".join(team)))
