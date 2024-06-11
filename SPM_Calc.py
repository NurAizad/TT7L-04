'''
---IMPORTANT!!!!---
1. Create branch guna nama korg
2. After save always :-
    a) git add .
    b) git commit -m "comment"
3. Make sure edit dkt branch bukan dkt main code
4. Kalau nak merge dgn main code, buat branch baru sbb takut tk jadi . so apa apa boleh pergi balik branch asal
'''
#chemistry
chem_frame=tk.Frame(bg="#212129")
chemf4_frame=tk.Frame(bg="#212129")
chemf4c2_frame=tk.Frame(bg="#212129")
nucleon_frame=tk.Frame(bg="#212129")


def ChemistryPage(forget_surface, pack_surface):
    backbutton(forget_surface, pack_surface)
    def chem_f4():
        backbutton(chem_frame,chemf4_frame)
        def chem_f4_chap2():
            backbutton(chemf4_frame,chemf4c2_frame)
            def nucleon_number():
                backbutton(chemf4c2_frame, nucleon_frame)
                def nucleon_calc():
                    number_of_protons=int(number_of_protons_entry.get())
                    number_of_neutrons=int(number_of_neutrons_entry.get())
                    if number_of_protons <0 or number_of_neutrons <0:
                        messagebox.showerror(title="Error", message="Number of protons and number of neutrons cannot be negative")
                    else:
                        nucleon=number_of_protons + number_of_neutrons
                    result_label.config(text=f"{nucleon}")


                nucleon_label=tk.Label(nucleon_frame, text="Nucleon Number", bg="#212129",fg="#08edff",font=("Helvetica",34))
                number_of_protons_label=tk.Label(nucleon_frame,text="Number of Protons",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                number_of_neutrons_label=tk.Label(nucleon_frame,text="Number of Neutrons",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(nucleon_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                number_of_protons_entry=tk.Entry(nucleon_frame, font=("Helvetica", 16))
                number_of_neutrons_entry=tk.Entry(nucleon_frame, font=("Helvetica", 16))

                nucleon_back=tk.Button(nucleon_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(nucleon_frame,chemf4c2_frame,result_label))
                nucleon_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(nucleon_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:nucleon_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                nucleon_label.grid(row=0,column=1,pady=10,padx=20)
                number_of_protons_label.grid(row=1,column=0,pady=10,padx=20)
                number_of_neutrons_label.grid(row=2,column=0,pady=10,padx=50)

                number_of_protons_entry.grid(row=1,column=2,padx=20)
                number_of_neutrons_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=2,padx=20)

            f4Chapter2_label=tk.Label(chemf4c2_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            nucleon_number_button=tk.Button(chemf4c2_frame,text="Speed",bg="#90ee90", font=("Helvetica",24),command=lambda:nucleon_number())
            

            chem_f4c2_back=tk.Button(chemf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4c2_frame,chemf4_frame))
            chem_f4c2_back.grid(row=9,column=1,pady=10)


            f4Chapter2_label.grid(row=0,column=1,padx=20,pady=10)
            nucleon_number_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
                    

        f4Chapter_label=tk.Label(chemf4_frame, text="Physics Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(chemf4_frame,text="Chapter 2",bg="#90ee90", font=("Helvetica",24),command=lambda:chem_f4_chap2())
        chap3_button=tk.Button(chemf4_frame,text="Chapter 3",bg="#adb0b4", font=("Helvetica",24))
        chap4_button=tk.Button(chemf4_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(chemf4_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(chemf4_frame,text="Chapter 6",bg="#adb0b4", font=("Helvetica",24))

        chem_f4_back=tk.Button(chemf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4_frame,pack_surface))
        chem_f4_back.grid(row=6,column=2,pady=40)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=20,pady=50)
        chap3_button.grid(row=1,column=2,padx=20)
        chap4_button.grid(row=1,column=4,padx=20)
        chap5_button.grid(row=2,column=1,padx=20,pady=50)
        chap6_button.grid(row=2,column=3,padx=20)
    
    
    form4_button=tk.Button(chem_frame,text="Form 4", bg="#90ee90", font=("Helvetica",24), command=lambda:chem_f4())
    form5_button=tk.Button(chem_frame,text="Form 5", bg="#adb0b4", font=("Helvetica",24))
    chooseForm_label=tk.Label(chem_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))

    chem_back = tk.Button(chem_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(pack_surface,forget_surface))

    form4_button.grid(row=1,column=0,padx=20,pady=100)
    form5_button.grid(row=1,column=2,padx=20)
    chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)
    chem_back.grid(row=6,column=1,pady=40)


