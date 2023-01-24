import pandas as pd

reaction_summary = pd.read_csv('./reaction_text_file.txt')

#Set index column to Node
reaction_summary = reaction_summary.set_index("Node")

# Sort by Node and Case Values
reaction_summary = reaction_summary.sort_values(by=['Node','Case'])

# loop through all the nodes and get a dataframe for each node
overall_dataframe = pd.DataFrame

for i in range(1,10):
  if(i == 1):
    overall_dataframe = reaction_summary.iloc[lambda x: x.index == i]
    continue
  df = reaction_summary.iloc[lambda x: x.index == i]

  overall_dataframe = overall_dataframe.join(df.reset_index(),rsuffix=f'_{i}')

# print(overall_dataframe)
# Write to excel
# overall_dataframe.to_excel('output.xlsx', sheet_name='Reactions')

data = {
    ('A', 'Fx'): [1, 2, 3],
    ('A', 'Fy'): [4, 5, 6],
    ('A', 'Fz'): [7, 8, 9],
}

df = pd.DataFrame(data,index=[0,45,90])
# print(df.index.name='Load Direction')

# df.to_excel('output.xlsx', sheet_name='Reactions')







# Read in how many nodes are in text files

# Read how many load cases are in the text file

# Generate the ASCII numbers from A -> ? depending on the number of nodes
