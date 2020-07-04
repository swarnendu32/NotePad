import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,filedialog,font,colorchooser
import os

root=tk.Tk()
root.geometry('1200x800')
root.title('Notebook Text Editor')

################################################__MAIN_MENU__#################################
main_menu=tk.Menu()

new_icon=tk.PhotoImage(file='Icons/new.png')
save_icon=tk.PhotoImage(file='Icons/save.png')
save_as_icon=tk.PhotoImage(file='Icons/save_as.png')
open_icon=tk.PhotoImage(file='Icons/open.png')
exit_icon=tk.PhotoImage(file='Icons/exit.png')
file=tk.Menu(main_menu,tearoff=False)

copy_icon=tk.PhotoImage(file='Icons/copy.png')
cut_icon=tk.PhotoImage(file='Icons/cut.png')
paste_icon=tk.PhotoImage(file='Icons/paste.png')
clear_all_icon=tk.PhotoImage(file='Icons/clear_all.png')
find_icon=tk.PhotoImage(file='Icons/find.png')
edit=tk.Menu(main_menu,tearoff=False)

toolbar_icon=tk.PhotoImage(file='Icons/tool_bar.png')
statusbar_icon=tk.PhotoImage(file='Icons/status_bar.png')
view=tk.Menu(main_menu,tearoff=False)

light_default_icon=tk.PhotoImage(file='Icons/light_default.png')
light_plus_icon=tk.PhotoImage(file='Icons/light_plus.png')
dark_icon=tk.PhotoImage(file='Icons/dark.png')
red_icon=tk.PhotoImage(file='Icons/red.png')
monokai_icon=tk.PhotoImage(file='Icons/monokai.png')
night_blue_icon=tk.PhotoImage(file='Icons/night_blue.png')
colortheme=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='ColorTheme',menu=colortheme)
#----------------------------------------------__END__MAIN_MENU--------------------------------

################################################__TOOLBAR__#################################
tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

size_box=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_box,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

bold_icon=tk.PhotoImage(file='Icons/bold.png')
bold_bttn=ttk.Button(tool_bar,image=bold_icon)
bold_bttn.grid(row=0,column=3,padx=5)

italic_icon=tk.PhotoImage(file='Icons/italic.png')
italic_bttn=ttk.Button(tool_bar,image=italic_icon)
italic_bttn.grid(row=0,column=4,padx=5)

underline_icon=tk.PhotoImage(file='Icons/underline.png')
underline_bttn=ttk.Button(tool_bar,image=underline_icon)
underline_bttn.grid(row=0,column=5,padx=5)

font_color=tk.PhotoImage(file='Icons/font_color.png')
font_color_btn=tk.Button(tool_bar,image=font_color)
font_color_btn.grid(row=0,column=6,padx=5)

left_align=tk.PhotoImage(file='Icons/align_left.png')
left_align_btn=tk.Button(tool_bar,image=left_align)
left_align_btn.grid(row=0,column=7,padx=5)

center_align=tk.PhotoImage(file='Icons/align_center.png')
center_align_btn=tk.Button(tool_bar,image=center_align)
center_align_btn.grid(row=0,column=8,padx=5)

right_align=tk.PhotoImage(file='Icons/align_right.png')
right_align_btn=tk.Button(tool_bar,image=right_align)
right_align_btn.grid(row=0,column=9,padx=5)
#----------------------------------------------__END__TOOLBAR--------------------------------

################################################__TEXT_EDITOR__#################################
text_editor=tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

current_font_family='arial'
current_font_size=16

def change_font(root):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(root):
    global current_font_size
    current_font_size=size_box.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)

def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        if text_property.actual()['underline']==1:
            text_editor.configure(font=(current_font_family,current_font_size,'bold',text_property.actual()['slant'],'underline'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'bold',text_property.actual()['slant'],'normal'))
    if text_property.actual()['weight'] == 'bold':
        if text_property.actual()['underline']==1:
            text_editor.configure(font=(current_font_family,current_font_size,'normal',text_property.actual()['slant'],'underline'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,'normal',text_property.actual()['slant'],'normal'))

bold_bttn.configure(command=change_bold)

def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        if text_property.actual()['underline']==0:
            text_editor.configure(font=(current_font_family,current_font_size,text_property.actual()['weight'],'italic','normal'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,text_property.actual()['weight'],'italic','underline'))
    if text_property.actual()['slant'] == 'italic':
        if text_property.actual()['underline']==1:
            text_editor.configure(font=(current_font_family,current_font_size,text_property.actual()['weight'],'roman','underline'))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,text_property.actual()['weight'],'roman','normal'))

italic_bttn.configure(command=change_italic)

def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,text_property.actual()['weight'],text_property.actual()['slant'],'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,text_property.actual()['weight'],text_property.actual()['slant'],'normal'))

underline_bttn.configure(command=change_underline)

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

left_align_btn.configure(command=align_left)

def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

right_align_btn.configure(command=align_right)

def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

center_align_btn.configure(command=align_center)
#----------------------------------------------__END__TEXT_EDITOR_--------------------------------

################################################__STATUSBAR__#################################
status_bar=ttk.Label(root,text='StatusBar')
status_bar.pack(side=tk.BOTTOM)
text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters : {characters}    Words : {words}')
    text_editor.edit_modified(False)
    
text_editor.bind('<<Modified>>',changed)
#----------------------------------------------__END__STATUSBAR--------------------------------

################################################__MAIN_MENU_FUNCTIONALITY_#################################
######FILE Functionality
#New File
url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

#Open File
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text file','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))

#Save File
def save_file(event=None):
    global url
    try:
        if url:
            content=text_editor.get(1.0,tk.END)
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File',"*.txt"),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

#Save As File
def save_as(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return

#Exit Functionality
def exit_func(event=None):
    global  url,text_changed
    try:
        if text_changed:
            msgbox=messagebox.askyesnocancel('Warning','Do you want to save this file')
            if msgbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        root.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif msgbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return
        
##FILE_Functions
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+S',command=save_as)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)
#----------------------------------------------------------------------------------------------------------------------
#####EDIT Functionality
def find_func(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='white',background='blue')

    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('400x200+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    find_frame=ttk.Labelframe(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)

    text_find_label=ttk.Label(find_frame,text='Find : ')
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label=ttk.Label(find_frame,text='Replace : ')
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    find_input=ttk.Entry(find_frame,width=30)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input=ttk.Entry(find_frame,width=30)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    find_button=ttk.Button(find_frame,text='Find',command=find)
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()

##EDIT_Functions
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)
#-----------------------------------------------------------------------------------------------------------------------
##VIEW_Functioms
show_toolbar_var=tk.BooleanVar()
show_toolbar_var.set(True)
show_statusbar_var=tk.BooleanVar()
show_statusbar_var.set(True)

def hide_toolbar():
    global show_toolbar_var
    if show_toolbar_var:
        tool_bar.pack_forget()
        show_toolbar_var=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar_var=True

def hide_statusbar():
    global show_statusbar_var
    if show_statusbar_var:
        status_bar.pack_forget()
        show_statusbar_var=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar_var=True

view.add_checkbutton(label='ToolBar',onvalue=True,offvalue=False,variable=show_toolbar_var,image=toolbar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='StatusBar',onvalue=True,offvalue=False,variable=show_statusbar_var,image=statusbar_icon,compound=tk.LEFT,command=hide_statusbar)

##COLOR_THEME_Functions
theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}
def change_theme():
    chosen_theme=theme_choice.get()
    colour_tuple=color_dict.get(chosen_theme)
    text_editor.config(background=colour_tuple[1],foreground=colour_tuple[0])
count=0
for i in color_dict:
    colortheme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1
#----------------------------------------------__END__MAIN_MENU_FUNCTIONALITY_--------------------------------
###############################################-------BIND ShortCut Key---------#################################
root.bind('<Control-n>',new_file)
root.bind('<Control-o>',open_file)
root.bind('<Control-s>',save_file)
root.bind('<Control-Alt-s>',save_as)
root.bind('<Control-q>',exit_func)
root.bind('<Control-f>',find_func)
root.bind('<Control-c>',
)
#----------------------------------------------------------------------------------------------------------------
root.config(menu=main_menu)
root.mainloop()