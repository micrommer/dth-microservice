from flask import Flask
import random
app = Flask(__name__)


@app.route('/dth')
def hello_world():
    with open("temp.txt", "r+") as file:
        temp = ""
        for line in file.readlines():
            temp = line
            break
        print(temp)
    with open("temp.txt", "w") as file:
        file.write(f"${random.randrange(0,100)} , ${random.randrange(0,100)}")
    temp = temp.replace("$", "")
    return temp
