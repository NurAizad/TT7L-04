#chemistry
chem_frame=tk.Frame(bg="#212129")
chemf4_frame=tk.Frame(bg="#212129")
chemf4c2_frame=tk.Frame(bg="#212129")
nucleon_frame=tk.Frame(bg="#212129")
chemf4c6_frame=tk.Frame(bg="#212129")
pH_frame=tk.Frame(bg='#212129')

chemf5_frame=tk.Frame(bg="#212129")
chemf5c1_frame=tk.Frame(bg="#212129")
Eocell_frame=tk.Frame(bg="#212129")
chemf5c3_frame=tk.Frame(bg="#212129")
fuelValue_frame=tk.Frame(bg="#212129")


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
                number_of_protons_label=tk.Label(nucleon_frame,text="Number of Protons",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                number_of_neutrons_label=tk.Label(nucleon_frame,text="Number of Neutrons",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                result_label=tk.Label(nucleon_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                number_of_protons_entry=tk.Entry(nucleon_frame, font=("Helvetica", 16))
                number_of_neutrons_entry=tk.Entry(nucleon_frame, font=("Helvetica", 16))

                nucleon_back=tk.Button(nucleon_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(nucleon_frame,chemf4c2_frame,result_label))
                nucleon_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(nucleon_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:nucleon_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                nucleon_label.grid(row=0,column=1,pady=10,padx=20)
                number_of_protons_label.grid(row=1,column=0,pady=10,padx=10)
                number_of_neutrons_label.grid(row=2,column=0,pady=10,padx=10)

                number_of_protons_entry.grid(row=1,column=2,padx=20)
                number_of_neutrons_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,padx=20)

            f4Chapter2_label=tk.Label(chemf4c2_frame, text="Chemistry Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            nucleon_number_button=tk.Button(chemf4c2_frame,text="Nucleon Number",bg="#add8e6", font=("Helvetica",24),command=lambda:nucleon_number())
            

            chem_f4c2_back=tk.Button(chemf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4c2_frame,chemf4_frame))
            chem_f4c2_back.grid(row=9,column=1,pady=10)


            f4Chapter2_label.grid(row=0,column=1,padx=20,pady=10)
            nucleon_number_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
                    
        def chem_f4_chap6():
            backbutton(chemf4_frame,chemf4c6_frame)

            f4Chapter6_label=tk.Label(chemf4c6_frame,text='Chemistry Form 4 Chapter 6' ,bg="#212129",fg="#08edff",font=("Helvetica",34))
            f4Chapter6_label.grid(row=0,column=1,pady=10,padx=20)
            pH_button=tk.Button(chemf4c6_frame,text='pH Value', bg="#add8e6", font=("Helvetica",24),command=lambda:pH())
            pH_button.grid(row=1,column=1,pady=10,padx=20,sticky="ew")
            chem_f4c6_back=tk.Button(chemf4c6_frame, text='Back' , bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:backbutton(chemf4c6_frame,chemf4_frame))
            chem_f4c6_back.grid(row=9,column=1,pady=10)

            def pH():
                backbutton(chemf4c6_frame,pH_frame)
                def pH_calc():
                    pH_value=float(pH_value_entry.get())
                    if pH_value <0:
                        messagebox.showerror(title="Error", message="pH value cannot be negative")
                    else:
                        pH = -math.log10(pH_value)
                    result_label.config(text=f"{pH}")

                pH_label=tk.Label(pH_frame, text='pH Value',bg="#212129",fg="#08edff",font=("Helvetica",34) ) 
                pH_value_label=tk.Label(pH_frame,text='H ions',bg="#212129",fg="#add8e6",font=("Helvetica",34))
                result_label=tk.Label(pH_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                pH_value_entry=tk.Entry(pH_frame, font=("Helvetica", 16))
                pH_back=tk.Button(pH_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(pH_frame,chemf4c6_frame,result_label))
                pH_back.grid(row=9, column=1, pady=10)
                calculate_button=tk.Button(pH_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:pH_calc())
                calculate_button.grid(row=8,column=1,pady=10)
                pH_label.grid(row=0,column=1,pady=10)
                pH_value_label.grid(row=1,column=0,pady=10,padx=70)
                pH_value_entry.grid(row=1,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10,padx=20)


        f4Chapter_label=tk.Label(chemf4_frame, text="Chemistry Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(chemf4_frame,text="Chapter 2",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f4_chap2())
        chap3_button=tk.Button(chemf4_frame,text="Chapter 3",bg="#adb0b4", font=("Helvetica",24))
        chap4_button=tk.Button(chemf4_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(chemf4_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(chemf4_frame,text="Chapter 6",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f4_chap6())
        chap7_button=tk.Button(chemf4_frame,text="Chapter 7",bg="#adb0b4", font=("Helvetica",24))
        chap8_button=tk.Button(chemf4_frame,text="Chapter 8",bg="#adb0b4", font=("Helvetica",24))
        

        chem_f4_back=tk.Button(chemf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4_frame,pack_surface))
        chem_f4_back.grid(row=6,column=2,pady=40)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=20,pady=50)
        chap3_button.grid(row=1,column=2,padx=20)
        chap4_button.grid(row=1,column=4,padx=20)
        chap5_button.grid(row=2,column=0,padx=20,pady=50)
        chap6_button.grid(row=2,column=2,padx=20)
        chap7_button.grid(row=2,column=4,padx=20)
        chap8_button.grid(row=3,column=2,padx=20,pady=50)
    
    def chem_f5():
        backbutton(chem_frame,chemf5_frame)
        def chem_f5_chap1():
            backbutton(chemf5_frame,chemf5c1_frame)

            f5Chapter1_label=tk.Label(chemf5c1_frame, text='Chemistry form 5 chapter 1 ', bg="#212129",fg="#08edff",font=("Helvetica",34))
            f5Chapter1_label.grid(row=0,column=1,pady=10,padx=20)
            Eocell_button=tk.Button(chemf5c1_frame, text='Cell Voltage', bg="#f08080", font=("Helvetica",24), command=lambda:Eocell())
            Eocell_button.grid(row=1,column=1,pady=10,padx=20,sticky="ew")
            chem_f5c1_back=tk.Button(biof4c4_frame, text='Back', bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16) ,command=lambda:backbutton(chemf5c1_frame,chemf4_frame) )
            chem_f5c1_back.grid(row=9,column=1,pady=10)

            def Eocell():
                backbutton(chemf5c1_frame,Eocell_frame)
                def Eocell_calc():
                    Eo_cathode=float(Eo_cathode_entry.get())
                    Eo_anode=float(Eo_anode_entry.get())
                    if Eo_cathode <0:
                        messagebox.showerror(title="Error", message="Eo cathode cannot be negative")
                    else:
                        Eo_cell= Eo_cathode - Eo_anode
                    result_label.config(text=f"{Eo_cell} V")

                Eocell_label=tk.Label(Eocell_frame, text="Cell Voltage",bg="#212129",fg="#08edff",font=("Helvetica",34))
                Eo_cathode_label= tk.Label(Eocell_frame,text="Eo cathode",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                Eo_anode_label = tk.Label(Eocell_frame,text="Eo anode",bg="#212129",fg="#add8e6", font=("Helvetica", 24)) 
                result_label = tk.Label(Eocell_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                Eo_cathode_entry = tk.Entry(Eocell_frame, font=("Helvetica", 16))
                Eo_anode_entry = tk.Entry(Eocell_frame, font=("Helvetica", 16))
                Eocell_back = tk.Button(Eocell_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(Eocell_frame,chemf5c1_frame,result_label))
                Eocell_back.grid(row=9,column=1,pady=10)
                calculate_button = tk.Button(Eocell_frame, text='Calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:Eocell_calc())
                calculate_button.grid(row=8,column=1,pady=10)
                Eocell_label.grid(row=0, column=1,pady=10)
                Eo_cathode_label.grid(row=1,column=0, pady=10,padx=20)
                Eo_anode_label.grid(row=2, column=0,pady=10,padx=20)
                Eo_cathode_entry.grid(row=1,column=2,padx=20)
                Eo_anode_entry.grid(row=2, column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10,padx=20)

            f5Chapter1_label=tk.Label(chemf5c1_frame, text="Chemistry Form 5 Chapter 1", bg="#212129",fg="#08edff",font=("Helvetica",34))
            Eocell_button=tk.Button(chemf5c1_frame,text="Cell Voltage",bg="#add8e6", font=("Helvetica",24),command=lambda:Eocell())
            

            chem_f5c1_back=tk.Button(chemf5c1_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf5c1_frame,chemf5_frame))
            chem_f5c1_back.grid(row=9,column=1,pady=10)


            f5Chapter1_label.grid(row=0,column=1,padx=20,pady=10)
            Eocell_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)   

        chem_f5_back=tk.Button(chemf5_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf5_frame,pack_surface))
        chem_f5_back.grid(row=6,column=2,pady=40)

        f5Chapter_label=tk.Label(chemf5_frame, text="Chemistry Form 5", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap1_button=tk.Button(chemf5_frame,text="Chapter 1",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f5_chap1())

        f5Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap1_button.grid(row=1,column=2,padx=20,pady=50)

        def chem_f5_chap3():
            backbutton(chemf5_frame,chemf5c3_frame)
            def fuelValue():
                backbutton(chemf5c3_frame, fuelValue_frame)
                def fuelValue_calc():
                    heat=float(heat_entry.get())
                    molMass=float(molMass_entry.get())
                    if molMass <0:
                        messagebox.showerror(title="Error", message="Molar Mass cannot be negative")
                    else:
                        fuelValue=heat/molMass
                    result_label.config(text=f"{fuelValue} kJ/g")

                fuelValue_label=tk.Label(fuelValue_frame, text="Fuel Value", bg="#212129",fg="#08edff",font=("Helvetica",34))
                heat_label=tk.Label(fuelValue_frame,text="Heat of Combustion",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                molMass_label=tk.Label(fuelValue_frame,text="Molar Mass",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                result_label=tk.Label(fuelValue_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                heat_entry=tk.Entry(fuelValue_frame, font=("Helvetica", 16))
                molMass_entry=tk.Entry(fuelValue_frame, font=("Helvetica", 16))

                nucleon_back=tk.Button(fuelValue_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(fuelValue_frame,chemf5c3_frame,result_label))
                nucleon_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(fuelValue_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:fuelValue_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                fuelValue_label.grid(row=0,column=1,pady=10,padx=20)
                heat_label.grid(row=1,column=0,pady=10,padx=10)
                molMass_label.grid(row=2,column=0,pady=10,padx=10)

                heat_entry.grid(row=1,column=2,padx=20)
                molMass_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,padx=20)

            f5Chapter3_label=tk.Label(chemf5c3_frame, text="Chemistry Form 5 Chapter 3", bg="#212129",fg="#08edff",font=("Helvetica",34))
            fuelValue_button=tk.Button(chemf5c3_frame,text="Fuel Value",bg="#add8e6", font=("Helvetica",24),command=lambda:fuelValue())
            

            chem_f5c3_back=tk.Button(chemf5c3_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf5c3_frame,chemf5_frame))
            chem_f5c3_back.grid(row=9,column=1,pady=10)


            f5Chapter3_label.grid(row=0,column=1,padx=20,pady=10)
            fuelValue_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
 
        f5Chapter_label=tk.Label(chemf5_frame, text="Chemistry Form 5", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap1_button=tk.Button(chemf5_frame,text="Chapter 1",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f5_chap1())
        chap2_button=tk.Button(chemf5_frame,text="Chapter 2",bg="#adb0b4", font=("Helvetica",24))
        chap3_button=tk.Button(chemf5_frame,text="Chapter 3",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f5_chap3())
        chap4_button=tk.Button(chemf5_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(chemf5_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        
        

        chem_f5_back=tk.Button(chemf5_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf5_frame,pack_surface))
        chem_f5_back.grid(row=6,column=2,pady=40)

        f5Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap1_button.grid(row=1,column=0,padx=20,pady=50)
        chap2_button.grid(row=1,column=2,padx=20)
        chap3_button.grid(row=1,column=4,padx=20)
        chap4_button.grid(row=2,column=0,padx=20,pady=50)
        chap5_button.grid(row=2,column=2,padx=20)
        

    form4_button=tk.Button(chem_frame,text="Form 4", bg="#add8e6", font=("Helvetica",24), command=lambda:chem_f4())
    form5_button=tk.Button(chem_frame,text="Form 5", bg="#add8e6", font=("Helvetica",24), command=lambda:chem_f5())
    chooseForm_label=tk.Label(chem_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))

    chem_back = tk.Button(chem_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(pack_surface,forget_surface))

    form4_button.grid(row=1,column=0,padx=20,pady=100)
    form5_button.grid(row=1,column=2,padx=20)
    chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)
    chem_back.grid(row=6,column=1,pady=40)
