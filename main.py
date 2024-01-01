from tkinter import *
import responses as rp

def bot_reply():
    question = questionField.get()
    question = question.capitalize()
    botResponse = rp.get_response(question)
    textArea.insert(END, 'YOU: ' + question+'\n\n')
    textArea.insert(END, 'BOT: '+ str(botResponse)+'\n\n')
    textArea.yview(END)
    questionField.delete(0, END)

root = Tk()

root.geometry('500x570+100+30')
root.title('Test Chatbot')
root.config(bg='seashell3')

# logopic=PhotoImage(file='xyz.png')

# logoPicLabel = Label(root, image=logopic)
# logoPicLabel.pack()
centreFrame=Frame(root)
centreFrame.pack()

scrollBar = Scrollbar(centreFrame)
scrollBar.pack(side=RIGHT)

textArea = Text(centreFrame,font=('times new roman',20), height=10, yscrollcommand=scrollBar.set
                ,wrap='word')
textArea.pack(side=LEFT)
scrollBar.config(command=textArea.yview)


questionField = Entry(root, font=('verdana',20))
questionField.pack(pady=15,fill=X)

submitButton=Button(root, text='Ask Globot', command=bot_reply)
submitButton.pack()

def click(event):
    submitButton.invoke()

root.bind('<Return>', click)

root.mainloop()