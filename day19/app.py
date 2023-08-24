from nltk.chat.util import Chat
q1=r'what is your name'
a1=['my name is harshit pratap','I am a harshit']
q2=r'kya aaj kuch accha hoga'
a2=['kya pata']
qa_pair=[
    [q1,a1],[q2,a2]]
cb=Chat(qa_pair)
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    text='Hi '
    global cb
    if request.args.get('q') !=None:
        que=request.args.get('q')
        text=cb.respond(que)
        if text==None:
            text='Unknown'
    return render_template('indexcb.html',resp=text)

@app.route('/new')
def new():
    return "<html><h1>harshit</h1></html>"


app.run(debug=True)