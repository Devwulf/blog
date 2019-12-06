import PySimpleGUI as sg # pip install PySimpleGUI
import datetime
import os

layout = [ [sg.Text('Post title')],
           [sg.InputText()],
           [sg.OK(), sg.Cancel()] ]

event, post_title = sg.Window('Insert your post title', layout).Read()
if post_title != "" and event != "Cancel":
    d = datetime.datetime.today()
    d_text = d.strftime('%Y-%m-%d')
    post_title[0] = post_title[0].replace(" ", "-")
    f_name = "_posts/"+d_text+"-"+post_title[0]+".md"
    mode = 'a' if os.path.exists(f_name) else 'w'
    if not os.path.exists(f_name):
        with open(f_name, mode) as f:
            f.write("---\ntitle: \"Title\"\ncategories:\n - Blog\ntags:\n - PLEASE CHANGE ME!\n---")
        f.close()
    else:
        sg.Popup('Blog already exists, choose a different name')
