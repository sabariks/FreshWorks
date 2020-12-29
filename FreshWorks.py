from tkinter import *
root = Tk()
def Submit(st1,st2,st3):
    import json
    record={'Name':'','UserName':'','Password':''}
    record['Name']=st1
    record['UserName']=st2
    record['Password']=st3
    j=json.dumps(record)
    s=st1+'.json'
    with open(s,'w') as f:
        f.write(j)
        f.close()
    l=Label(root,text='File is created!')
    l.grid(row=10,column=1)
def create():
    Submit(E1.get(),E2.get(),E3.get())
myLabel = Label(root, text="Name")
E1 = Entry(root,width=50)
myLabel2 = Label(root, text="user name")
E2 = Entry(root, width=50)
myLabel3 = Label(root, text="Password")
E3 = Entry(root, width=50)
myLabel.grid(row=0,column=0)
E1.grid(row=0,column=1)
myLabel2.grid(row=2,column=0)
E2.grid(row=2,column=1)
myLabel3.grid(row=4,column=0)
E3.grid(row=4,column=1)
Mybutton=Button(root,text="Submit",command=create)
Mybutton.grid(row=8,column=1)
print(E1.get())
root.geometry("450x450")
root.title("FreshWorks")
root.mainloop()
