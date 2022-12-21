
# from reaction_generator import Reactions
# from tkinter import*


# def main():
#     root = Tk()
#     reactions = Reactions(root)
#     root.mainloop()

#     a = (reactions.chosen_reaction())
#     b = (reactions.file())
#     c = (reactions.folder())
#     d = (reactions.output_entry())

#     return a,b,c,d
   

# gui_outputs = main()

# print (gui_outputs[0])
# print (gui_outputs[1])
# print (gui_outputs[2])
# print (gui_outputs[3])


# values = [1,1,1,1,1,1]

# def selected_reactions(binary_list):
#     """Input a list of 6 values 0 or 1. (0 - exclude , 1 include reaction)"""
    
#     react = ['Fx','Fy','Fz','Mx','My','Mz']
#     selected = []

#     for b,r in zip(binary_list,react):
#         if b == 1:
#             selected.append(r)

#     return selected

# print (selected_reactions(values))


a = "hello"

b = 'there'

c = f'{a}/{b}.rc' 

print(c[:-2])












