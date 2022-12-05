import tkinter as tk
from tkinter import *

# tkinter GUI
root= tk.Tk()

#Make a Canvas (i.e, a screen for your project
canvas = tk.Canvas(root, width = 500, height = 400)
canvas.pack()
canvas.configure(bg="black")

label10= tk.Label(root,text= 'Diabetes Prediction app', font=('Arial Bold',20))
canvas.create_window(280,30, window=label10)
        

label1 = tk.Label(root, text=' Patient Name : ')
canvas.create_window(120, 70, window=label1)
entry1 = tk.Entry (root) 
canvas.create_window(290, 70, window=entry1)

label2 = tk.Label(root, text=' Glucose conc. : ')
canvas.create_window(120, 100, window=label2)
entry2 = tk.Entry (root)
canvas.create_window(290, 100, window=entry2)

label3 = tk.Label(root, text=' Blood Pressure : ')
canvas.create_window(120, 160, window=label3)
entry3 = tk.Entry (root)
canvas.create_window(290, 160, window=entry3)

label4 = tk.Label(root, text=' Skin Thickness : ')
canvas.create_window(120, 190, window=label4)
entry4 = tk.Entry (root)
canvas.create_window(290, 190, window=entry4)

label5 = tk.Label(root, text=' Insulin : ')
canvas.create_window(120, 220, window=label5)
entry5 = tk.Entry (root)
canvas.create_window(290, 220, window=entry5)

label6 = tk.Label(root, text=' BMI : ')
canvas.create_window(120, 250, window=label6)
entry6 = tk.Entry (root) 
canvas.create_window(290, 250, window=entry6)

label7 = tk.Label(root, text=' Age : ')
canvas.create_window(120, 280, window=label7)
entry7 = tk.Entry (root) 
canvas.create_window(290, 280, window=entry7)

label8 = tk.Label(root, text=' Diabetes Pedigree : ')
canvas.create_window(120, 310, window=label8)
entry8 = tk.Entry (root) 
canvas.create_window(290, 310, window=entry8)

label9 = tk.Label(root, text=' Pregnancies : ')
canvas.create_window(120, 130, window=label9)
entry9 = tk.Entry (root)
canvas.create_window(290, 130, window=entry9)

import joblib
filename = "Completed_model.joblib"
loaded_model = joblib.load(filename)


def values():
    glucose = int(entry2.get())
    blood_pressure = int(entry3.get())
    skin_thickness = int(entry4.get())
    insulin = int(entry5.get())
    BMI = float(entry6.get())
    age= int(entry7.get())
    diabetes_pedigree= float(entry8.get())
    pregnancies = int(entry9.get())
    
    Prediction_result = loaded_model.predict([[pregnancies, glucose ,blood_pressure, skin_thickness, insulin, BMI, age, diabetes_pedigree]])

    if list(Prediction_result) == [0]:
        output= entry1.get()+ ' has not got diabetes. No need to worry :)'
        print(output)

    else:
        output= entry1.get()+ ' has got diabetes. Please consult a doctor '
        print(output)
        
    label_Prediction = tk.Label(root, text=  output, bg='orange')
    canvas.create_window(290, 370, window=label_Prediction)
    print(Prediction_result)


button = tk.Button (root, text='Submit',command=values, bg='orange')
canvas.create_window(250, 350, window=button)


root.mainloop()

