import tkinter as tk
from tkinter import ttk,font,filedialog,messagebox as m_box
import os , shutil
from PIL import Image, ImageTk

main = tk.Tk()
url_s=""
url_d=""
dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac',".aif",".ogg",".wma",".acc",".ra"),
    'video_extensions' : ('.mp4', '.mkv', '.flv',".webm",".flv",".vob",".gif",".gifv",".avi",".wmv",".yuv",".rm",".amv",".3gp","."),
    'document_extensions' : ('.doc','.docx', '.pdf', '.txt',".tex",".log",".html",".htm",".odt",".xls",".xksx",".ods",".ppt",".pptx"),
    'image_extensions' : ('.png', '.jpg',".jpeg",".jpe",".jif",".jfif",".jfi",".webp",".tif",".tiff",".raw",".jpx"),
    'archive_extensions' : (".zip",".rar",".rar3",".7z",".bz7",".gz",".tar",".gz2")
    }

main.title('File Sorter')


nb=ttk.Notebook(main)
p1=ttk.Frame(nb)
p2=ttk.Frame(nb)
nb.add(p1, text='GUI')
nb.add(p2, text='Details')
nb.pack(expand=True, fill='both')

IMAGE_PATHp1 = r"C:\Users\91735\Downloads\image.png"
WIDTHp1, HEIGTHp1 = 1550, 800
canvasp1 = tk.Canvas(p1, width=WIDTHp1, height=HEIGTHp1)
canvasp1.grid(row=0,column=0)
imgp1 = ImageTk.PhotoImage(Image.open(IMAGE_PATHp1).resize((WIDTHp1, HEIGTHp1), Image.ANTIALIAS))
canvasp1.background = imgp1  
bgp1 = canvasp1.create_image(0, 0, anchor=tk.NW, image=imgp1)


win = ttk.LabelFrame(p1)#.grid(row=50, column = 10,)
win.place(relx = 0.5,rely = 0.5,anchor = 'center') 

IMAGE_PATHwin = r"C:\Users\91735\Downloads\441387-gorgerous-dark-blue-background-images-1920x1080-for-android-50.jpg"
WIDTHwin, HEIGTHwin = 1000, 500
canvaswin = tk.Canvas(win, width=WIDTHwin, height=HEIGTHwin)
canvaswin.place(relx = 0.5,rely = 0.5,anchor = 'center')
imgwin = ImageTk.PhotoImage(Image.open(IMAGE_PATHwin).resize((WIDTHwin, HEIGTHwin), Image.ANTIALIAS))
canvaswin.background = imgwin  # Keep a reference in case this code is put in a function.
bgwin = canvaswin.create_image(0, 0, anchor=tk.NW, image=imgwin)


title = ttk.LabelFrame(p1)
title.place(relx = 0.5,rely = 0.25,anchor = 'n') 
IMAGE_PATHtitle = r"C:\Users\91735\Downloads\441387-gorgerous-dark-blue-background-images-1920x1080-for-android-50.jpg"
WIDTHtitle, HEIGTHtitle = 1000, 500
canvastitle = tk.Canvas(title, width=WIDTHtitle, height=HEIGTHtitle)
canvastitle.place(relx = 0.5,rely = 0.5,anchor = 'center')
imgtitle = ImageTk.PhotoImage(Image.open(IMAGE_PATHtitle).resize((WIDTHtitle, HEIGTHtitle), Image.ANTIALIAS))
canvastitle.background = imgtitle  # Keep a reference in case this code is put in a function.
bgtitle = canvastitle.create_image(0, 0, anchor=tk.NW, image=imgtitle)
title1 = ttk.Label(title, text = 'File Sorter', font=('Arial', 15,'bold')).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)


#labels
imode = ttk.Label(win, text = 'What you want Enter the Path of Folder or Browse the Folder : ', font=('Helvetica', 12,'bold')).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
sourcepath = ttk.Label(win, text = 'Source Folder Path : ', font=('Helvetica', 12,'bold')).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
destinationpath = ttk.Label(win, text = 'Destintion Folder Path : ', font=('Helvetica', 12,'bold')).grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
fileviseextraction = ttk.Label(win, text = 'Do you want to creat Saperate Folder for Each Extension : ', font=('Helvetica', 12,'bold')).grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
copymove = ttk.Label(win, text = 'What do you want copy the files or move  : ', font=('Helvetica', 12,"bold")).grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

# entry box variables # entry boxes 
s1 = tk.StringVar()
d1 = tk.StringVar()
spath = ttk.Entry(win, width=36, textvariable = s1)
spath.grid(row=1, column=1, padx=5, pady=5)
dpath = ttk.Entry(win, width=36, textvariable = d1)
dpath.grid(row=2, column=1, padx=5, pady=5)
l1=""
l2=""
a=0
b=0
def Selects():
    global url_s,l1,a
    url_s = filedialog.askdirectory(initialdir=os.getcwd(), title='Select Folder')
    l1=ttk.Label(win ,text=url_s)
    l1.grid(row=1,column=1,sticky=tk.W,padx=10, pady=5)
    a=1
def Selectd():
    global url_d,l2,b
    url_d = filedialog.askdirectory(initialdir=os.getcwd(), title='Select Folder')
    l2=ttk.Label(win ,text=url_d)
    l2.grid(row=2,column=1,sticky=tk.W,padx=10, pady=5)
    b=1
    # l1=tkk.Label(win ,text="url_d",font=('Helvetica', 12,'bold')).grid(row=2,column=5)
spath_select = tk.Button(win, text = 'Browse',command=Selects).grid(row=1, column=2,padx=0)
dpath_select = tk.Button(win, text = 'Browse',command=Selectd).grid(row=2, column=2)

ans=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='Yes',value='yes', variable=ans).grid(row=3,column=1)
radiobtn2=ttk.Radiobutton(win,text='No',value='no', variable=ans,).grid(row=3,column=2)

cp_var=tk.StringVar()
radiobtn3=ttk.Radiobutton(win,text='Copy',value='copy', variable=cp_var).grid(row=4,column=1)
radiobtn4=ttk.Radiobutton(win,text='Move',value='move', variable=cp_var,).grid(row=4,column=2)

ipmode_var=tk.StringVar()
radiobtn5=ttk.Radiobutton(win,text='Enter',value='enter', variable=ipmode_var).grid(row=0,column=1)
radiobtn6=ttk.Radiobutton(win,text='Select',value='browse', variable=ipmode_var).grid(row=0,column=2)

def submit():

    global url_s
    global url_d
    global ans
    inmode=ipmode_var.get()
    mode=ans.get() 
    cp=cp_var.get() 

    if inmode== "enter":  
        url_s = s1.get()
        url_d = d1.get()
    # url_d=r"C:\Users\91735\Desktop\d"
    # url_s=r"C:\Users\91735\Desktop\s - Copy - Copy"

    if url_s == '' or url_d == '':
        m_box.showerror('Error', 'Please fill both')
        
    else:
        if url_s[1]!=":" or url_d[1]!=":":
            m_box.showerror('Error', 'Invalid Input')
        elif mode=="" or cp=="":
            m_box.showwarning('Warning','You are not Selected all Options')
        
        else:
            sfolderpath = url_s
            dfolderpath = url_d
            def file_finder(folder_path, file_extensions):
                files = []
                for file in os.listdir(folder_path):
                    for extension in file_extensions:
                        if file.endswith(extension):
                            files.append(file)
                return files

            def file_finder1(folder_path, file_extensions):
                files = []
                for file in os.listdir(folder_path):
                    if file.endswith(file_extensions):
                        files.append(file)
                return files
            f=[]
            f1=[]
            for extension_type, extension_tuple in dict_extensions.items():     
                for ex in extension_tuple:
                    for i in file_finder(sfolderpath,extension_tuple):
                        if i not in f1:
                            f1.append(i)
                            if ex not in f:
                                f.append(ex)
                                folder_name = extension_type.split('_')[0] + '_' + 'Files'
                                folder_path = os.path.join(dfolderpath, folder_name)               
                                try:
                                    os.mkdir(folder_path.title())
                                except FileExistsError:
                                    for i in range(1,10):
                                        ans1=m_box.askquestion('Error', f'{folder_name.title()} Folder is alredy Exist\nDo you want to Creat new {folder_name.title()}')
                                        if ans1=="yes":
                                            folder_name = extension_type.split('_')[0] + '_' + 'Files'+"("+str(i)+")"
                                            folder_path = os.path.join(dfolderpath, folder_name,)
                                            try:
                                                os.mkdir(folder_path.title())
                                                break
                                            except:
                                                pass
                                        elif ans1 == "no":
                                            break                        
                if mode=="no":                        
                    for item in file_finder(sfolderpath, extension_tuple):
                        item_path = os.path.join(sfolderpath,item)
                        item_new_path = os.path.join(folder_path,item)
                        if cp=="copy":
                            shutil.copy(item_path,item_new_path)
                            
                        elif co=="move":
                            shutil.move(item_path,item_new_path)
                            
                elif mode=="yes":                   
                    l=[]
                    for ex in extension_tuple:
                        for i in file_finder1(sfolderpath,ex):
                            if ex not in l:
                                l.append(ex)
                                fname=ex[1:4]+"_"+"file"
                                fpath=os.path.join(folder_path,fname)
                                os.mkdir(fpath)
                        for item in file_finder1(sfolderpath, ex):
                            item_path = os.path.join(sfolderpath,item)
                            item_new_path = os.path.join(fpath,item)
                            if cp=="copy":
                                shutil.copy(item_path,item_new_path)
                                
                            elif cp=="move":
                                shutil.move(item_path,item_new_path)
            m_box.showinfo('Done', 'Done')
    


def reset():
    global l1,l2
    spath.delete(0,tk.END)
    dpath.delete(0,tk.END)
    if a!=0:
        l1.destroy()
    if b!=0:
        l2.destroy()
 
submit_btn = tk.Button(win, text = 'Submit', command=submit,height=1,width=20,font=('calibri',15,'bold', 'underline'),).grid(row=8, column=0, pady=30)
rst_btn = tk.Button(win, text = 'Reset', command=reset,height=1,width=20,font=('calibri',15,'bold', 'underline'),).grid(row=8, column=1, pady=30)

detail = ttk.LabelFrame(p2)
detail.grid(row=50, column = 10,)
# title.place(relx = 0.5,rely = 0.25,anchor = 'n') 
detail1 = ttk.Label(detail, text = 'File Sorter', font=('Arial', 10)).grid(row=0, column=0)

main.mainloop()

