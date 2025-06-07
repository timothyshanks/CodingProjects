# Space exploration crew members' data, containing their names, missions, and roles
crew_data = "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"
crew_list = crew_data.split(';')

for crew in crew_list:
    crew_attr = crew.split(',')
    astronaut_first = crew_attr[0]
    astronaut_last = crew_attr[1]
    mission = crew_attr[2]
    role = crew_attr[3]
    #print(f'{astronaut_first} {astronaut_last} is serving on the {mission} mission and is a {role} class astronaut.')
    print(' '.join(crew_attr))
