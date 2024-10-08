from Flast import flask,request
from socketio import SocketIO,emit
import random
import qrcode
app = Flask(__name__)
socketio = SocketIO(app)
current_question = None
players = {}
questions[{

    "question-1" : "what is capital city of France?"
    "options":"A)Paris","B)Brezil","C)Ireland","D)Delhi"

}
]

def generate_qr_code(data):
    qr = qrcode.make(data)
    qr.save("status/qr_code.png")
def index():
    global current_question current_question = random.choice(questions)
    socketio.emit("index.html")
def sumbit_ans():
    if current_question and answer.lower() == current_question["answer"].lower():
        socketio.emit("currect_answer",{"name":player})
        return render_request("congradulations")
    else:
        return render_request("incorrect answer")
       

def next_qns():
    global current_question current_question = random.choice(questions)



