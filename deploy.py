from flask import Flask , render_template , request
import pickle

app = Flask(__name__ )
#load the model 

model = pickle.load(open('saved_model.sav' , 'rb'))


@app.route('/')
def home():
    

    return render_template('Home.html', **locals())

if __name__ == '__main__':
    
    app.run(debug=True)

