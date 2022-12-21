# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 06:39:32 2020

@author: alexander.nicolaidis
"""

#reaction file - text file from microstran in comma seperated format

import csv
import string

#create a list of characters to use for the reaction headings


def alpha_list (list_of_chosen_reactions,nodes_list):
    '''creates the header row for the reactions fx,fy...etc'''
    
    reaction_letters = list(string.ascii_uppercase)
    header_row_list = ['']
    
    blanks = []
    for i in range(0,len(list_of_chosen_reactions)-1):
        blanks.append('')
    
    for i in range(0,len(nodes_list)):
        header_row_list.append(reaction_letters[i])
        header_row_list.extend(blanks)
        
    return header_row_list
    
    

file_name = 'ZZ-XX-M2-CE-TC3_Grillage_Model-220621_AN.rc'

#open and read the text file
with open (file_name, mode = 'r') as file:
    #skip the header row, store as variable
    header_row = next(file)
    #store the rest of the data in a variable
    contents = file.read()
    
    #break the file up into a list in which each item
    #in the list is a string of the row
    lines = contents.splitlines()
    
    #create a list of list in which each item of the list is a list
    #of each parameter in a line of the file
    data_list_of_lists = []
    
    for line in lines:
        data_list_of_lists.append(line.split(','))
        
    
    #get a list of the nodes and load cases
    unique_load_cases = []
    unique_nodes = []
    
    for i in data_list_of_lists:
        if i[0] not in unique_nodes:
            unique_nodes.append(i[0])
        if i[1] not in unique_load_cases:
            unique_load_cases.append(i[1])

    #create an emty dictionary to store all the data in
    
    empty_dict = {}
    
    for load_case in unique_load_cases:
        empty_dict[load_case] = {}
        for node in unique_nodes:
            empty_dict[load_case][node] = {}
            
    for row in data_list_of_lists:
        empty_dict[row[1]][row[0]]['fx'] = f'{float(row[2]):.0f}'
        empty_dict[row[1]][row[0]]['fy'] = f'{float(row[3]):.0f}'
        empty_dict[row[1]][row[0]]['fz'] = f'{float(row[4]):.0f}'
        empty_dict[row[1]][row[0]]['mx'] = float(row[5])
        empty_dict[row[1]][row[0]]['my'] = float(row[6])
        empty_dict[row[1]][row[0]]['mz'] = float(row[7])

#    print (empty_dict['104']['9'])    
    

#write output to a csv file
filename = 'reactions.csv'       

directions = [0,45,90,135,180,225,270,315]

#by leaving any of these out they will be left out of the results file
#reactions = ['Fx','Fy','Fz','Mx','My','Mz']
reactions = ['Fx','Fy','Fz']



#headings for each reaction block 
in_op_sc = ['In Operation Slew C']
in_op_scc = ['In Operation Slew CC']
out_op = ['Out of Operation']

direction = ['Load Direction']

#loop through and give reaction headings for each node
for node in unique_nodes:
        #loop through and give a reaction heading for the wanted reactions
        for reaction in reactions:
            direction.append(reaction)

#create a list of lists to write to csv file            
in_op_sc_writeable = []
in_op_scc_writeable = []
out_of_op_writable = []



#may be able to covert the below to a function

for index, case in enumerate(unique_load_cases[0:8]):
    list_case = [directions[index]]
    
    for node in unique_nodes:
        if 'Fx' in reactions:
            list_case.append(empty_dict[case][node]['fx'])
        if 'Fy' in reactions:
            list_case.append(empty_dict[case][node]['fy'])
        if 'Fz' in reactions:
            list_case.append(empty_dict[case][node]['fz'])
        if 'Mx' in reactions:
            list_case.append(empty_dict[case][node]['mx'])
        if 'My' in reactions:
            list_case.append(empty_dict[case][node]['my'])
        if 'Mz' in reactions:
            list_case.append(empty_dict[case][node]['mz'])
    
    in_op_sc_writeable.append(list_case)
    
    
for index, case in enumerate(unique_load_cases[8:16]):
    list_case = [directions[index]]
    
    for node in unique_nodes:
        if 'Fx' in reactions:
            list_case.append(empty_dict[case][node]['fx'])
        if 'Fy' in reactions:
            list_case.append(empty_dict[case][node]['fy'])
        if 'Fz' in reactions:
            list_case.append(empty_dict[case][node]['fz'])
        if 'Mx' in reactions:
            list_case.append(empty_dict[case][node]['mx'])
        if 'My' in reactions:
            list_case.append(empty_dict[case][node]['my'])
        if 'Mz' in reactions:
            list_case.append(empty_dict[case][node]['mz'])
    
    in_op_scc_writeable.append(list_case)
    

for index, case in enumerate(unique_load_cases[16:]):
    list_case = [directions[index]]
    
    for node in unique_nodes:
        if 'Fx' in reactions:
            list_case.append(empty_dict[case][node]['fx'])
        if 'Fy' in reactions:
            list_case.append(empty_dict[case][node]['fy'])
        if 'Fz' in reactions:
            list_case.append(empty_dict[case][node]['fz'])
        if 'Mx' in reactions:
            list_case.append(empty_dict[case][node]['mx'])
        if 'My' in reactions:
            list_case.append(empty_dict[case][node]['my'])
        if 'Mz' in reactions:
            list_case.append(empty_dict[case][node]['mz'])
    
    out_of_op_writable.append(list_case)    
    
  

filename = 'ZZ-XX-M3-CE-TC1_Grillage_Model-220608_AN_out_Stab.csv'                      

with open(filename, 'w', newline='') as f:                
    writer = csv.writer(f)
    writer.writerow(in_op_sc)
    writer.writerow(alpha_list(reactions,unique_nodes))
    writer.writerow(direction)
    writer.writerows(in_op_sc_writeable)
    writer.writerow('')
    
    writer.writerow(in_op_scc)
    writer.writerow(alpha_list(reactions,unique_nodes))
    writer.writerow(direction)
    writer.writerows(in_op_scc_writeable)
    writer.writerow('')
    
    writer.writerow(out_op)
    writer.writerow(alpha_list(reactions,unique_nodes))
    writer.writerow(direction)
    writer.writerows(out_of_op_writable)
    
    
    
    
    
    
    
    
    
    
    