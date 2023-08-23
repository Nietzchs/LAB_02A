from flask import Flask
app = Flask(__name__)
@app.route("/hola/<a>/<b>",methods=['GET'])
def hola(a,b):
    return str(int(a)*int(b))
@app.route('/primo/<n>')
def primo(n):
    n=int(n)
    for i in range(2,int(n**(1/2))):
        if n%i ==0:
            return "no es primo"
    return "es primo"

if __name__=='__main__':
    app.run()