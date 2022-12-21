#!/usr/bin/python3
# selection_buttons.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com


from tkinter import *
from tkinter import ttk   
from tkinter import filedialog


#from tkinter import filedialog # use this for browse below 


class Reactions:
    
    def __init__(self, master):
        
        
        #create a frame widget inside the master widget
        self.frame_top = ttk.Frame(master)
        self.frame_top.pack()
        
        #populate the first frame with addtional widgets
        ttk.Label(self.frame_top, text = 'Reaction Table Generator').grid(row = 0,
                 column = 0, columnspan = 2)
        

        self.f_x = ttk.Checkbutton(self.frame_top, text = 'Fx')
        self.f_y = ttk.Checkbutton(self.frame_top, text = 'Fy')
        self.f_z = ttk.Checkbutton(self.frame_top, text = 'Fz')
        self.m_x = ttk.Checkbutton(self.frame_top, text = 'Mx')
        self.m_y = ttk.Checkbutton(self.frame_top, text = 'My')
        self.m_z = ttk.Checkbutton(self.frame_top, text = 'Mz')
        
        self.f_x.grid(row = 1 , column = 0) 
        self.f_y.grid(row = 2 , column = 0)
        self.f_z.grid(row = 3 , column = 0) 
        self.m_x.grid(row = 1 , column = 1) 
        self.m_y.grid(row = 2 , column = 1) 
        self.m_z.grid(row = 3 , column = 1)  
        
        #create variables to store the results of the checkbox
        self.check_box_fx = IntVar()
        self.check_box_fx.set(1)
        self.check_box_fy = IntVar()
        self.check_box_fy.set(1)
        self.check_box_fz = IntVar()
        self.check_box_fz.set(1)
        self.check_box_mx = IntVar()
        self.check_box_mx.set(1)
        self.check_box_my = IntVar()
        self.check_box_my.set(1)
        self.check_box_mz = IntVar()
        self.check_box_mz.set(1)
        
        self.f_x.config(variable = self.check_box_fx, onvalue = 1, offvalue = 0)
        self.f_y.config(variable = self.check_box_fy, onvalue = 1, offvalue = 0)
        self.f_z.config(variable = self.check_box_fz, onvalue = 1, offvalue = 0)
        self.m_x.config(variable = self.check_box_mx, onvalue = 1, offvalue = 0)
        self.m_y.config(variable = self.check_box_my, onvalue = 1, offvalue = 0)
        self.m_z.config(variable = self.check_box_mz, onvalue = 1, offvalue = 0)
        
       
        
        
        #create another frame widget inside the master widget
        self.frame_bottom = ttk.Frame(master)
        self.frame_bottom.pack()
       
        ttk.Label(self.frame_bottom, text = 'Select Required Reactions').grid(row = 2,
                 column = 0, columnspan = 2)

        ttk.Label(self.frame_bottom, text = 'Enter Output File Name Below').grid(row = 3,
                 column = 0, columnspan = 2)

        
        self.output_variable = StringVar()
        self.output_variable.set('Output File Name')
        self.output_entry = ttk.Entry(self.frame_bottom, width = 50, justify= 'center',textvariable = self.output_variable).grid(row = 4, column = 0, columnspan = 2, padx = 10)  
        

        ttk.Label(self.frame_bottom, text = 'Close Window to Select Reaction RC (comma-seperated) File and Output Folder Location').grid(row = 5,
                 column = 0, columnspan = 2)
         
        #populate the second frame with addtional widgets
        # ttk.Button(self.frame_bottom, text = 'Browse for Reaction File',command = self.file_link).grid(row = 0, column = 0, padx = 5, pady = 5)
        # ttk.Button(self.frame_bottom, text = 'Clear File',
        #            command = self.clear).grid(row = 0, column = 1 , padx = 5, pady = 5)
        
        # self.file_name = ttk.Entry(self.frame_bottom, width = 35)
        # self.file_name.grid(row = 1, column = 0, columnspan = 2, padx = 10)
        

        # ttk.Button(self.frame_bottom, text = 'Browse for Design Folder',command = self.folder_link).grid(row = 2, column = 0, padx = 5, pady = 5)
        # ttk.Button(self.frame_bottom, text = 'Clear Folder',
        #            command = self.clear_folder).grid(row = 2, column = 1 , padx = 5, pady = 5)

        # self.folder_name = ttk.Entry(self.frame_bottom, width = 35)
        # self.folder_name.grid(row = 3, column = 0, columnspan = 2, padx = 10)


        # ttk.Button(self.frame_bottom, text = 'Generate Table',
        #            command = self.close_window).grid(row = 5,column = 0, 
        #             columnspan = 2, padx = 5, pady = 5)

        self.chosen_reaction = self.reactions_selected
        self.file = self.file_link
        self.folder = self.folder_link
        self.output_entry = self.output
        
    
    def output(self):
        self.out = self.output_variable.get()
        return (self.out)

   
    def file_link (self):
        
        self.file_path = filedialog.askopenfilename(title='Select Reaction .rc File from Microstran (comma seperated)')
        # self.file_name.insert(0,self.file_path)
        return (self.file_path)

    def folder_link(self):
        self.folder_path = filedialog.askdirectory(title = 'Folder Location to Save Reaction Output')
        # self.folder_name.insert(0,self.folder_path)
        return (self.folder_path)
       
            
    def reactions_selected (self):
        
        self.reaction_results = []
    
        self.reaction_results.append(self.check_box_fx.get())
        self.reaction_results.append(self.check_box_fy.get())
        self.reaction_results.append(self.check_box_fz.get())
        self.reaction_results.append(self.check_box_mx.get())
        self.reaction_results.append(self.check_box_my.get())
        self.reaction_results.append(self.check_box_mz.get())

        return (self.reaction_results)

       
        
    # def clear(self):
    #         self.file_name.delete(0, 'end')

    # def clear_folder(self):
    #         self.folder_name.delete(0, 'end')



def main():

    root = Tk()
    reactions = Reactions(root)
    root.mainloop()

    a = (reactions.chosen_reaction())
    b = (reactions.file())
    c = (reactions.folder())
    d= (reactions.output_entry())

    return a,b,c,d
   
gui_outputs = main()

print (gui_outputs[0])
print (gui_outputs[1])
print (gui_outputs[2])
print (gui_outputs[3])

