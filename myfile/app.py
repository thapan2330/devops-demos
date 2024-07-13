from flask import flask

app=flask(__name__)
@app.rout('/')
def index():
    return"st.mary's engeering college" !


if __name__=='__main__':
    app.run(debug=true)
