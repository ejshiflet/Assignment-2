import numpy as np

player_stats = np.loadtxt('NBA_Player_Stats.tsv', delimiter='\t',dtype=str)

#===========================================================================================================================================================
#field goal accuracy column creation
FGM_index = 7
FGA_index = 8

FGACP = []# list to hold accuracy
FGACP.append("FGACC")#column heading for later

for row in player_stats[1:]:#iterates through list skipping first row with headers
    if(int(row[FGA_index]) == 0):
        FGACP_value = 0
        FGACP.append(str(int((round(FGACP_value,2))*100)))
    else:  
        FGACP_value = int(row[FGM_index]) / int(row[FGA_index])#calculate field goal accuracy
        FGACP.append(str(int((round(FGACP_value,2))*100)))
    

#===========================================================================================================================================================
#3 point accuracy column creation
I3PM_index = 9
I3PA_index = 10

I3PACP = []# list to hold accuracy
I3PACP.append("3PACP")

for row in player_stats[1:]:#iterates through list skipping first row with headers
    if(int(row[I3PA_index]) == 0):# if 0
        I3PACP_value = 0
        I3PACP.append(str(int((round(I3PACP_value,2))*100)))
    else:  
        I3PACP_value = int(row[I3PM_index]) / int(row[I3PA_index]) # calculate 3 point accuracy for every player
        I3PACP.append(str(int((round(I3PACP_value,2))*100)))


#===========================================================================================================================================================
#free throw accuracy column creation

FTM_index = 11
FTA_index = 12

FTACP = []# list to hold free throw accuracy
FTACP.append("FTACP")

for row in player_stats[1:]:#iterates through list skipping first row with headers
    if(int(row[FTA_index]) == 0):
        FTACP_value = 0
        FTACP.append(str(int((round(FTACP_value,2))*100)))
    else:  
        FTACP_value = int(row[FTM_index]) / int(row[FTA_index])#return free throw accuracy as percent
        FTACP.append(str(int((round(FTACP_value,2))*100)))


#===========================================================================================================================================================
#points per minute column creation

PTS_index = 21
MIN_index = 6

points_per_minute = []
points_per_minute.append("PPM")

for row in player_stats[1:]:#iterates through list skipping first row with headers
    if(float(row[MIN_index]) == 0):# if 0
        PPM_value = 0
        points_per_minute.append(str(int((round(PPM_value,2)))))
    else:  
        PPM_value = float(row[PTS_index]) / float(row[MIN_index])#calculate points per minute
        points_per_minute.append(str(round(PPM_value,2)))

#===========================================================================================================================================================

#overall shooting accuracy column creation

overall_accuracy = []
overall_accuracy.append("OA")
i = 1

while(i<len(FTACP)):# will go for the amount of players
    OA_value = int((int(FGACP[i]) + int(I3PACP[i]) + int(FTACP[i])) / 3)#calculate average between the 3 as a percent
    i = i + 1
    overall_accuracy.append(str(OA_value))

#===========================================================================================================================================================

#average blocks column creation

GP_index = 5
BLK_index = 20

average_blocks = []
average_blocks.append("AB")

for row in player_stats[1:]:#iterates through list skipping first row with headers
    if(float(row[GP_index]) == 0):
        AB_value = 0
        average_blocks.append(str((round(AB_value,2))))
    else:  
        AB_value = float(row[BLK_index]) / float(row[GP_index])#calculate average
        average_blocks.append(str(round(AB_value,2)))


#===========================================================================================================================================================

#average number of steals column creation

GP_index = 5
STL_index = 19

average_steals = []
average_steals.append("AS")

for row in player_stats[1:]:#iterates through list skipping first row with headers
    if(float(row[GP_index]) == 0):#if 0
        AS_value = 0
        average_steals.append(str((round(AS_value,2))))
    else:  
        AS_value = float(row[STL_index]) / float(row[GP_index])#calculate average
        average_steals.append(str(round(AS_value,2)))


#===========================================================================================================================================================

#appends all list to end of numpy array as a column

#convert all list to numpy array column
FGACP_array = np.array(FGACP)
I3PACP_array = np.array(I3PACP)
FTACP_array = np.array(FTACP)
points_per_minute_array = np.array(points_per_minute)
overall_accuracy_array = np.array(overall_accuracy)
average_blocks_array = np.array(average_blocks)
average_steals_array = np.array(average_steals)

#make them columns
FGACP_array = FGACP_array.reshape(-1, 1)
I3PACP_array = I3PACP_array.reshape(-1, 1)
FTACP_array = FTACP_array.reshape(-1,1)
points_per_minute_array = points_per_minute_array.reshape(-1, 1)
overall_accuracy_array = overall_accuracy_array.reshape(-1,1)
average_blocks_array = average_blocks_array.reshape(-1, 1)
average_steals_array = average_steals_array.reshape(-1, 1)

#adds them to player stats
player_stats = np.concatenate((player_stats, FGACP_array), axis=1)
player_stats = np.concatenate((player_stats, I3PACP_array), axis=1)
player_stats = np.concatenate((player_stats, FTACP_array), axis=1)
player_stats = np.concatenate((player_stats, points_per_minute_array), axis=1)
player_stats = np.concatenate((player_stats, overall_accuracy_array), axis=1)
player_stats = np.concatenate((player_stats, average_blocks_array), axis=1)
player_stats = np.concatenate((player_stats, average_steals_array), axis=1)


#===========================================================================================================================================================

#A function for appending the top 100 players of any category and return a list

def make_top_100_player_list(index):
    player_stats_no_headers = player_stats[1:, :]

    top_indices = np.argpartition(player_stats_no_headers[:, index].astype(float), -100)[-100:]# get top player indices

    top_names = player_stats[top_indices, 3] #get names from column

    names_list = top_names.tolist()# convert to list and return
    return names_list

#the code below creates the list of the players in each category

top_field_goal_accuracy_players = make_top_100_player_list(34)
top_3point_accuracy_players = make_top_100_player_list(35)
top_free_throw_accuracy_players = make_top_100_player_list(36)
top_points_per_minute_players = make_top_100_player_list(37)
top_overall_shooting_accuracy = make_top_100_player_list(38)
top_average_blocks = make_top_100_player_list(39)
top_average_steals = make_top_100_player_list(40)



