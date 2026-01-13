#!/usr/bin/env python
# coding: utf-8

# In[1]:



import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
import joblib
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


final_RF_PMS = joblib.load(resource_path('RF_PMS.joblib'))
final_RF_PDS = joblib.load(resource_path('RF_PDS.joblib'))
norm_scaler_PMS = joblib.load(resource_path('scaler_PMS.joblib'))
norm_scaler_PDS = joblib.load(resource_path('scaler_PDS.joblib'))


a1 = tk.Tk()
a1.title("Prediction of unit time reaction conversion rate for biochar-activated persulfate systems")
a1.geometry("800x635+245+5")
a1.iconbitmap(resource_path("Icon.ico"))
canvas = tk.Canvas(a1,width=800,height=635)
canvas.pack()

canvas.create_rectangle(35,40,765,69,fill="#1E90FF",outline="") 
canvas.create_rectangle(35,68,765,450,fill="#E2EAF4",outline="") 
canvas.create_rectangle(35,450,400,630,fill="#EBE6F8",outline="") 
canvas.create_rectangle(400,450,765,630,fill="#DCECED",outline="") 
canvas.create_rectangle(35,535,765,564,fill="#1E90FF",outline="") 

tk.Label(a1,text="Prediction of unit time reaction conversion rate for biochar-activated persulfate systems",
         font=("Microsoft Yahei",13),fg="#060270").place(x=40,y=5)
tk.Label(a1,text="Input",font=("Microsoft Yahei",13),fg="#67B9FA").place(x=375,y=40)
tk.Label(a1,text="Preparation conditions",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="black").place(x=45,y=70)
tk.Label(a1,text="source of biochar",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=45,y=95)



source_value = tk.IntVar()

source_mapping = {
    "Forestry residues": 1,
    "Agricultural residues": 2,
    "Animal residues": 3,
    "Algae residues": 4,
    "Other": 5
}
s0 = ttk.Combobox(a1, values=["Forestry residues", "Agricultural residues", "Animal residues","Algae residues","Other"],width=45   )
s0.place(x=45,y=120)
def update_source_value(event):
    global source_value

    selected = s0.get()

    source_value.set(source_mapping[selected])
s0.bind("<<ComboboxSelected>>", update_source_value)


tk.Label(a1,text="pyrolysis temperature (℃)",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=410,y=95)
tk.Label(a1,text="Physico-porous structural properties of biochar",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="black").place(x=45,y=150)
tk.Label(a1,text="specific surface area (m²/g)",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=45,y=175)
tk.Label(a1,text="average pore diameter (nm)",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=297.5,y=175)
tk.Label(a1,text="ID/IG",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=550,y=175)
tk.Label(a1,text="Surface element composition of biochar",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="black").place(x=45,y=230)
tk.Label(a1,text="C content",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=45,y=255)
tk.Label(a1,text="N content",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=297.5,y=255)
tk.Label(a1,text="O/C",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=550,y=255)
tk.Label(a1,text="Experimental conditions",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="black").place(x=45,y=310)
tk.Label(a1,text="ionization potential of pollutants (eV)",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=45,y=335)
tk.Label(a1,text="contaminant concentration (mg/L)",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=410,y=335)
tk.Label(a1,text="initial pH",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=45,y=390)
tk.Label(a1,text="reaction temperature (℃)",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=297.5,y=390)
tk.Label(a1,text="biochar dosage (g/L)",font=("Microsoft Yahei",13),bg="#E2EAF4",fg="gray").place(x=550,y=390)
tk.Label(a1,text="PMS",font=("Microsoft Yahei",13),bg="#EBE6F8",fg="#3F0366").place(x=203,y=450)
tk.Label(a1,text="PDS",font=("Microsoft Yahei",13),bg="#DCECED",fg="#3F0366").place(x=568,y=450)
tk.Label(a1,text="peroxymonosulfate concentration (mM)",font=("Microsoft Yahei",13),bg="#EBE6F8",fg="gray").place(x=45,y=475)
tk.Label(a1,text="peroxydisulfate concentration (mM)",font=("Microsoft Yahei",13),bg="#DCECED",fg="gray").place(x=410,y=475)
tk.Label(a1,text="Output",font=("Microsoft Yahei",13),fg="#67B9FA").place(x=373,y=535)
tk.Label(a1,text="URR×10⁴ (mg·mg⁻¹·mM⁻¹·min⁻¹)",font=("Microsoft Yahei",13),bg="#FFFF33",fg="black").place(x=45,y=570)
tk.Label(a1,text="URR×10⁴ (mg·mg⁻¹·mM⁻¹·min⁻¹)",font=("Microsoft Yahei",13),bg="#FFFF33",fg="black").place(x=410,y=570)

s1 = tk. StringVar()
s1.set("")
s2 = tk. StringVar()
s2.set("")
s3 = tk. StringVar()
s3.set("")
s4 = tk. StringVar()
s4.set("")
s5 = tk. StringVar()
s5.set("")
s6 = tk. StringVar()
s6.set("")
s7 = tk. StringVar()
s7.set("")
s8 = tk. StringVar()
s8.set("")
s9 = tk. StringVar()
s9.set("")
s10 = tk. StringVar()
s10.set("")
s11= tk. StringVar()
s11.set("")
s12= tk. StringVar()
s12.set("")
s13= tk. StringVar()
s13.set("")
s14= tk. StringVar()
s14.set("")
s15= tk. StringVar()
s15.set("")

tk.Entry(a1,width=34,textvariable=s2,fg="black",font=("Microsoft Yahei",13)).place(x=410,y=120)

tk.Entry(a1,width=20,textvariable=s3,fg="black",font=("Microsoft Yahei",13)).place(x=45,y=200)
tk.Entry(a1,width=20,textvariable=s4,fg="black",font=("Microsoft Yahei",13)).place(x=297.5,y=200)
tk.Entry(a1,width=20,textvariable=s5,fg="black",font=("Microsoft Yahei",13)).place(x=550,y=200)

tk.Entry(a1,width=20,textvariable=s6,fg="black",font=("Microsoft Yahei",13)).place(x=45,y=280)
tk.Entry(a1,width=20,textvariable=s7,fg="black",font=("Microsoft Yahei",13)).place(x=297.5,y=280)
tk.Entry(a1,width=20,textvariable=s8,fg="black",font=("Microsoft Yahei",13)).place(x=550,y=280)

tk.Entry(a1,width=28,textvariable=s9,fg="black",font=("Microsoft Yahei",13)).place(x=45,y=360)
def jieshi():
    a2 = tk.Toplevel()
    a2.title("Ionization potential of pollutants (eV)")
    a2.geometry("400x625+535+5")
    canvas = tk.Canvas(a2,width=400,height=625)
    canvas.pack()
    canvas.create_line(200, 0, 200, 625, fill="black", width=2)
    tk.Label(a2,text="Malachite Green",font=("Microsoft Yahei",10),fg="black").place(x=5,y=0)
    tk.Label(a2,text="5.593",font=("Microsoft Yahei",10),fg="black").place(x=135,y=0)
    tk.Label(a2,text="Rhodamine B",font=("Microsoft Yahei",10),fg="black").place(x=5,y=25)
    tk.Label(a2,text="5.851",font=("Microsoft Yahei",10),fg="black").place(x=135,y=25)
    tk.Label(a2,text="Tartrazine",font=("Microsoft Yahei",10),fg="black").place(x=5,y=50)
    tk.Label(a2,text="6.326",font=("Microsoft Yahei",10),fg="black").place(x=135,y=50)
    tk.Label(a2,text="Methyl orange",font=("Microsoft Yahei",10),fg="black").place(x=5,y=75)
    tk.Label(a2,text="6.395",font=("Microsoft Yahei",10),fg="black").place(x=135,y=75)
    tk.Label(a2,text="Methylene blue",font=("Microsoft Yahei",10),fg="black").place(x=5,y=100)
    tk.Label(a2,text="6.416",font=("Microsoft Yahei",10),fg="black").place(x=135,y=100)
    tk.Label(a2,text="Diclofenac sodium",font=("Microsoft Yahei",10),fg="black").place(x=5,y=125)
    tk.Label(a2,text="6.729",font=("Microsoft Yahei",10),fg="black").place(x=135,y=125)
    tk.Label(a2,text="Gatifloxacin",font=("Microsoft Yahei",10),fg="black").place(x=5,y=150)
    tk.Label(a2,text="6.739",font=("Microsoft Yahei",10),fg="black").place(x=135,y=150)
    tk.Label(a2,text="Acid orange Ⅱ",font=("Microsoft Yahei",10),fg="black").place(x=5,y=175)
    tk.Label(a2,text="6.747",font=("Microsoft Yahei",10),fg="black").place(x=135,y=175)
    tk.Label(a2,text="Levofloxacin",font=("Microsoft Yahei",10),fg="black").place(x=5,y=200)
    tk.Label(a2,text="6.753",font=("Microsoft Yahei",10),fg="black").place(x=135,y=200)
    tk.Label(a2,text="Ofloxacin",font=("Microsoft Yahei",10),fg="black").place(x=5,y=225)
    tk.Label(a2,text="6.753",font=("Microsoft Yahei",10),fg="black").place(x=135,y=225)
    tk.Label(a2,text="Enrofloxacin",font=("Microsoft Yahei",10),fg="black").place(x=5,y=250)
    tk.Label(a2,text="6.783",font=("Microsoft Yahei",10),fg="black").place(x=135,y=250)
    tk.Label(a2,text="Benzo[a]pyrene",font=("Microsoft Yahei",10),fg="black").place(x=5,y=275)
    tk.Label(a2,text="6.803",font=("Microsoft Yahei",10),fg="black").place(x=135,y=275)
    tk.Label(a2,text="Dimethomorph",font=("Microsoft Yahei",10),fg="black").place(x=5,y=300)
    tk.Label(a2,text="6.845",font=("Microsoft Yahei",10),fg="black").place(x=135,y=300)
    tk.Label(a2,text="Ciprofloxacin",font=("Microsoft Yahei",10),fg="black").place(x=5,y=325)
    tk.Label(a2,text="6.859",font=("Microsoft Yahei",10),fg="black").place(x=135,y=325)
    tk.Label(a2,text="Tetracycline hydrochloride",font=("Microsoft Yahei",10),fg="black").place(x=5,y=350)
    tk.Label(a2,text="6.893",font=("Microsoft Yahei",10),fg="black").place(x=135,y=350)
    tk.Label(a2,text="Trimethoprim",font=("Microsoft Yahei",10),fg="black").place(x=5,y=375)
    tk.Label(a2,text="6.893",font=("Microsoft Yahei",10),fg="black").place(x=135,y=375)
    tk.Label(a2,text="Acid Orange 7",font=("Microsoft Yahei",10),fg="black").place(x=5,y=400)
    tk.Label(a2,text="6.954",font=("Microsoft Yahei",10),fg="black").place(x=135,y=400)
    tk.Label(a2,text="Losartan",font=("Microsoft Yahei",10),fg="black").place(x=5,y=425)
    tk.Label(a2,text="6.955",font=("Microsoft Yahei",10),fg="black").place(x=135,y=425)
    tk.Label(a2,text="Norfloxacin",font=("Microsoft Yahei",10),fg="black").place(x=5,y=450)
    tk.Label(a2,text="7.048",font=("Microsoft Yahei",10),fg="black").place(x=135,y=450)
    tk.Label(a2,text="Oxytetracycline",font=("Microsoft Yahei",10),fg="black").place(x=5,y=475)
    tk.Label(a2,text="7.107",font=("Microsoft Yahei",10),fg="black").place(x=135,y=475)
    tk.Label(a2,text="Bisphenol A",font=("Microsoft Yahei",10),fg="black").place(x=5,y=500)
    tk.Label(a2,text="7.160",font=("Microsoft Yahei",10),fg="black").place(x=135,y=500)
    tk.Label(a2,text="Tetracycline",font=("Microsoft Yahei",10),fg="black").place(x=205,y=0)
    tk.Label(a2,text="7.200",font=("Microsoft Yahei",10),fg="black").place(x=335,y=0)
    tk.Label(a2,text="Acyclovir",font=("Microsoft Yahei",10),fg="black").place(x=205,y=25)
    tk.Label(a2,text="7.408",font=("Microsoft Yahei",10),fg="black").place(x=335,y=25)
    tk.Label(a2,text="Sulfamethazine",font=("Microsoft Yahei",10),fg="black").place(x=205,y=50)
    tk.Label(a2,text="7.432",font=("Microsoft Yahei",10),fg="black").place(x=335,y=50)
    tk.Label(a2,text="Cephalexin",font=("Microsoft Yahei",10),fg="black").place(x=205,y=75)
    tk.Label(a2,text="7.527",font=("Microsoft Yahei",10),fg="black").place(x=335,y=75)
    tk.Label(a2,text="Bensulfuron methyl",font=("Microsoft Yahei",10),fg="black").place(x=205,y=100)
    tk.Label(a2,text="7.535",font=("Microsoft Yahei",10),fg="black").place(x=335,y=100)
    tk.Label(a2,text="Sulfa-pyridine",font=("Microsoft Yahei",10),fg="black").place(x=205,y=125)
    tk.Label(a2,text="7.537",font=("Microsoft Yahei",10),fg="black").place(x=335,y=125)
    tk.Label(a2,text="Sulfamethoxazole",font=("Microsoft Yahei",10),fg="black").place(x=205,y=150)
    tk.Label(a2,text="7.541",font=("Microsoft Yahei",10),fg="black").place(x=335,y=150)
    tk.Label(a2,text="Ampicillin",font=("Microsoft Yahei",10),fg="black").place(x=205,y=175)
    tk.Label(a2,text="7.601",font=("Microsoft Yahei",10),fg="black").place(x=335,y=175)
    tk.Label(a2,text="Acetaminophen",font=("Microsoft Yahei",10),fg="black").place(x=205,y=200)
    tk.Label(a2,text="7.612",font=("Microsoft Yahei",10),fg="black").place(x=335,y=200)
    tk.Label(a2,text="Diclofenac",font=("Microsoft Yahei",10),fg="black").place(x=205,y=225)
    tk.Label(a2,text="7.614",font=("Microsoft Yahei",10),fg="black").place(x=335,y=225)
    tk.Label(a2,text="Sulfadiazine",font=("Microsoft Yahei",10),fg="black").place(x=205,y=250)
    tk.Label(a2,text="7.628",font=("Microsoft Yahei",10),fg="black").place(x=335,y=250)
    tk.Label(a2,text="Valsartan",font=("Microsoft Yahei",10),fg="black").place(x=205,y=275)
    tk.Label(a2,text="7.651",font=("Microsoft Yahei",10),fg="black").place(x=335,y=275)
    tk.Label(a2,text="Naphthalene",font=("Microsoft Yahei",10),fg="black").place(x=205,y=300)
    tk.Label(a2,text="7.968",font=("Microsoft Yahei",10),fg="black").place(x=335,y=300)
    tk.Label(a2,text="Atrazine",font=("Microsoft Yahei",10),fg="black").place(x=205,y=325)
    tk.Label(a2,text="7.998",font=("Microsoft Yahei",10),fg="black").place(x=335,y=325)
    tk.Label(a2,text="1,4-Dioxane",font=("Microsoft Yahei",10),fg="black").place(x=205,y=350)
    tk.Label(a2,text="8.266",font=("Microsoft Yahei",10),fg="black").place(x=335,y=350)
    tk.Label(a2,text="p-Chlorophenol",font=("Microsoft Yahei",10),fg="black").place(x=205,y=375)
    tk.Label(a2,text="8.322",font=("Microsoft Yahei",10),fg="black").place(x=335,y=375)
    tk.Label(a2,text="2,4-Dichlorophenol",font=("Microsoft Yahei",10),fg="black").place(x=205,y=400)
    tk.Label(a2,text="8.408",font=("Microsoft Yahei",10),fg="black").place(x=335,y=400)
    tk.Label(a2,text="Clofibric acid",font=("Microsoft Yahei",10),fg="black").place(x=205,y=425)
    tk.Label(a2,text="8.475",font=("Microsoft Yahei",10),fg="black").place(x=335,y=425)
    tk.Label(a2,text="Phenol",font=("Microsoft Yahei",10),fg="black").place(x=205,y=450)
    tk.Label(a2,text="8.534",font=("Microsoft Yahei",10),fg="black").place(x=335,y=450)
    tk.Label(a2,text="Methylparaben",font=("Microsoft Yahei",10),fg="black").place(x=205,y=475)
    tk.Label(a2,text="8.590",font=("Microsoft Yahei",10),fg="black").place(x=335,y=475)
    tk.Label(a2,text="p-Hydroxybenzoic acid",font=("Microsoft Yahei",10),fg="black").place(x=205,y=500)
    tk.Label(a2,text="8.688",font=("Microsoft Yahei",10),fg="black").place(x=335,y=500)
    tk.Label(a2,text="Salicylic acid",font=("Microsoft Yahei",10),fg="black").place(x=205,y=525)
    tk.Label(a2,text="8.927",font=("Microsoft Yahei",10),fg="black").place(x=335,y=525)
    tk.Label(a2,text="p-Nitrophenol",font=("Microsoft Yahei",10),fg="black").place(x=205,y=550)
    tk.Label(a2,text="9.103",font=("Microsoft Yahei",10),fg="black").place(x=335,y=550)
    tk.Label(a2,text="Benzoic acid",font=("Microsoft Yahei",10),fg="black").place(x=205,y=575)
    tk.Label(a2,text="9.215",font=("Microsoft Yahei",10),fg="black").place(x=335,y=575)
    tk.Label(a2,text="Urea",font=("Microsoft Yahei",10),fg="black").place(x=205,y=600)
    tk.Label(a2,text="9.713",font=("Microsoft Yahei",10),fg="black").place(x=335,y=600)

tk.Button(a1,command=jieshi,text="Tip",font=("Microsoft Yahei",8),fg="black",bg="#E8E8E8",width=5).place(x=340,y=360)
tk.Entry(a1,width=34,textvariable=s10,fg="black",font=("Microsoft Yahei",13)).place(x=410,y=360)
tk.Entry(a1,width=20,textvariable=s11,fg="black",font=("Microsoft Yahei",13)).place(x=45,y=415)
tk.Entry(a1,width=20,textvariable=s12,fg="black",font=("Microsoft Yahei",13)).place(x=297.5,y=415)
tk.Entry(a1,width=20,textvariable=s13,fg="black",font=("Microsoft Yahei",13)).place(x=550,y=415)

tk.Entry(a1,width=34,textvariable=s14,fg="black",font=("Microsoft Yahei",13)).place(x=45,y=500)
tk.Entry(a1,width=34,textvariable=s15,fg="black",font=("Microsoft Yahei",13)).place(x=410,y=500)

def yuce1():
    try:
        X_new_PMS=[float(source_value.get()),float(s3.get()),float(s4.get()),float(s2.get()),float(s6.get()),float(s8.get()),float(s7.get()),
                   float(s5.get()),float(s14.get()),float(s12.get()),float(s13.get()),float(s11.get()),float(s9.get()),float(s10.get())]

        X_new_normalized_PMS = norm_scaler_PMS.transform(np.array(X_new_PMS).reshape(1, -1))
        y_new_PMS = final_RF_PMS.predict(X_new_normalized_PMS)
        y_new_PMS_var.set(f"{y_new_PMS[0]:.4f}")  
    except ValueError:
        y_new_PMS_var.set("Invalid input")

def yuce2():
    try:
        X_new_PDS=[float(source_value.get()),float(s3.get()),float(s4.get()),float(s2.get()),float(s6.get()),float(s8.get()),float(s7.get()),
                   float(s5.get()),float(s15.get()),float(s12.get()),float(s13.get()),float(s11.get()),float(s9.get()),float(s10.get())]

        X_new_normalized_PDS = norm_scaler_PDS.transform(np.array(X_new_PDS).reshape(1, -1))
        y_new_PDS = final_RF_PDS.predict(X_new_normalized_PDS)
        y_new_PDS_var.set(f"{y_new_PDS[0]:.4f}") 
    except ValueError:
        y_new_PDS_var.set("Invalid input")

y_new_PMS_var = tk.StringVar()  
y_new_PDS_var = tk.StringVar() 

tk.Entry(a1,width=13,textvariable=y_new_PMS_var,fg="black",font=("Microsoft Yahei",13)).place(x=45,y=600)
tk.Entry(a1,width=13,textvariable=y_new_PDS_var,fg="black",font=("Microsoft Yahei",13)).place(x=410,y=600)

tk.Button(a1,command=yuce1,text="Prediction",font=("Microsoft Yahei",10),fg="white",bg="#FF1493",width=7).place(x=320,y=580)
tk.Button(a1,command=yuce2,text="Prediction",font=("Microsoft Yahei",10),fg="white",bg="#FF1493",width=7).place(x=685,y=580)

a1.mainloop()


# In[ ]:




