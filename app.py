from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST']) #if page needs to be redirected to /predict 
def predict(): #and what will done is define in the function...we will use it to send prediction to html
  #  values=[int(x) for x in request.form.values]
  ram=int(request.form.get("ram"))
  rom=int(request.form.get("rom"))
  ss=int(request.form.get("mobile_size"))
  pc=int(request.form.get("primary_cam"))
  bc=int(request.form.get("selfi_cam"))
  battery=int(request.form.get("battery_power"))
  values=[ram,rom,ss,pc,bc,battery]
  final=np.array(values)
  prediction=model.predict(final.reshape(1,-1))
  output=prediction[0]
  return render_template('index.html',sent_value= f"Expected price is: {output}")
    


if __name__=="__main__":
    app.run(debug=True)

    #here  first we need to activate environment using env_folder\Scripts\activate.bat
    # change to directory that contains app file
    #run python file app.py