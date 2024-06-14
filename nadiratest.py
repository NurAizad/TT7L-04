def PhysicsPage(forget_surface,pack_surface):
    #backbutton(subject_frame,phy_frame)
    backbutton(forget_surface,pack_surface)
    def phy_f4():
        backbutton(phy_frame,phyf4_frame)
        def phy_f4_chap2():
            backbutton(phyf4_frame,phyf4c2_frame)
            def speed():
                backbutton(phyf4c2_frame,speed_frame)
                def speed_calc():
                    distance=float(distance_entry.get())
                    time = float(time_entry.get())
                    if distance<0 or time<0:
                        messagebox.showerror(title="Error", message="Distance or time cannot be negative")
                    else:
                        speed=abs(distance/time)
                    result_label.config(text=f"{speed}")


                speed_label=tk.Label(speed_frame, text="Speed", bg="#212129",fg="#08edff",font=("Helvetica",34))
                distance_label=tk.Label(speed_frame,text="Distance",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(speed_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(speed_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                

                distance_entry=tk.Entry(speed_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(speed_frame, font=("Helvetica", 16))

                speed_back=tk.Button(speed_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(speed_frame,phyf4c2_frame,result_label))
                speed_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(speed_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:speed_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                speed_label.grid(row=0,column=1,pady=10)
                distance_label.grid(row=1,column=0,pady=10)
                time_label.grid(row=2,column=0,pady=10)
                distance_entry.grid(row=1,column=2)
                time_entry.grid(row=2,column=2)
                result_label.grid(row=3,column=1,pady=10)

            def velocity():
                backbutton(phyf4c2_frame,velocity_frame)
                def velocity_calc():
                    displacement=float(displacement_entry.get())
                    time = float(time_entry.get())
                    if time<0:
                        messagebox.showerror(title="Error", message="Time cannot be negative")
                    if time>0:
                        velocity=displacement/time
                    result_label.config(text=f"{velocity}")


                velocity_label=tk.Label(velocity_frame, text="Velocity", bg="#212129",fg="#08edff",font=("Helvetica",34))
                displacement_label=tk.Label(velocity_frame,text="Displacement",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(velocity_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(velocity_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                displacement_entry=tk.Entry(velocity_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(velocity_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(velocity_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(velocity_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(velocity_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:velocity_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                velocity_label.grid(row=0,column=1,pady=10)
                displacement_label.grid(row=1,column=0,pady=10)
                time_label.grid(row=2,column=0,pady=10)
                displacement_entry.grid(row=1,column=2)
                time_entry.grid(row=2,column=2)
                result_label.grid(row=3,column=1,pady=10)
            
            def acceleration():
                backbutton(phyf4c2_frame,acceleration_frame)
                def acceleration_calc():
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    t = float(time_entry.get())
                    if t<0:
                        messagebox.showerror(title="Error", message="Time cannot be negative")
                    if t>0:
                        acceleration=(v-u)/t
                    result_label.config(text=f"{acceleration}")


                acceleration_label=tk.Label(acceleration_frame, text="Acceleration", bg="#212129",fg="#08edff",font=("Helvetica",34))
                ini_vel_label=tk.Label(acceleration_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                fin_vel_label=tk.Label(acceleration_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(acceleration_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(acceleration_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                ini_vel_entry=tk.Entry(acceleration_frame, font=("Helvetica", 16))
                fin_vel_entry=tk.Entry(acceleration_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(acceleration_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(acceleration_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(acceleration_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(acceleration_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:acceleration_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                acceleration_label.grid(row=0,column=1,pady=10)
                ini_vel_label.grid(row=1,column=0,pady=10)
                fin_vel_label.grid(row=2,column=0,pady=10)
                time_label.grid(row=3,column=0,pady=10)

                ini_vel_entry.grid(row=1,column=2)
                fin_vel_entry.grid(row=2,column=2)
                time_entry.grid(row=3,column=2)
                result_label.grid(row=4,column=1,pady=10)

            def momentum():
                backbutton(phyf4c2_frame,momentum_frame)
                def momentum_calc():
                    v=float(vel_entry.get())
                    m=float(mass_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        momentum=m*v
                    result_label.config(text=f"{momentum}")


                momentum_label=tk.Label(momentum_frame, text="Momentum", bg="#212129",fg="#08edff",font=("Helvetica",34))
                vel_label=tk.Label(momentum_frame,text="Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(momentum_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(momentum_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                vel_entry=tk.Entry(momentum_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(momentum_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(momentum_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(momentum_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(momentum_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:momentum_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                momentum_label.grid(row=0,column=1,pady=10)
                vel_label.grid(row=1,column=0,pady=10)
                mass_label.grid(row=2,column=0,pady=10)

                vel_entry.grid(row=1,column=2)
                mass_entry.grid(row=2,column=2)
                result_label.grid(row=3,column=1,pady=10)

            def force():
                backbutton(phyf4c2_frame,force_frame)
                def force_calc():
                    m=float(mass_entry.get())
                    a=float(acc_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        force=m*a
                    result_label.config(text=f"{force}")


                force_label=tk.Label(force_frame, text="Force", bg="#212129",fg="#08edff",font=("Helvetica",34))
                mass_label=tk.Label(force_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                acc_label=tk.Label(force_frame,text="Acceleration",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(force_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                mass_entry=tk.Entry(force_frame, font=("Helvetica", 16))
                acc_entry=tk.Entry(force_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(force_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(force_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(force_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:force_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                force_label.grid(row=0,column=1,pady=10)
                mass_label.grid(row=1,column=0,pady=10)
                acc_label.grid(row=2,column=0,pady=10)

                mass_entry.grid(row=1,column=2)
                acc_entry.grid(row=2,column=2)
                result_label.grid(row=3,column=1,pady=10)

            def impulse():
                backbutton(phyf4c2_frame,impulse_frame)
                def impulse_calc():
                    m=float(mass_entry.get())
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        impulse=m*v-m*u
                    result_label.config(text=f"{impulse}")


                impulse_label=tk.Label(impulse_frame, text="Impulse", bg="#212129",fg="#08edff",font=("Helvetica",34))
                fin_vel_label=tk.Label(impulse_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                ini_vel_label=tk.Label(impulse_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(impulse_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(impulse_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                fin_vel_entry=tk.Entry(impulse_frame, font=("Helvetica", 16))
                ini_vel_entry=tk.Entry(impulse_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(impulse_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(impulse_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(impulse_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(impulse_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:impulse_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                impulse_label.grid(row=0,column=1,pady=10)
                fin_vel_label.grid(row=1,column=0,pady=10)
                ini_vel_label.grid(row=2,column=0,pady=10)
                mass_label.grid(row=3,column=0,pady=10)

                fin_vel_entry.grid(row=1,column=2)
                ini_vel_entry.grid(row=2,column=2)
                mass_entry.grid(row=3,column=2)
                result_label.grid(row=4,column=1,pady=10)

            def impulsiveForce():
                backbutton(phyf4c2_frame,impulsiveForce_frame)
                def impulsiveForce_calc():
                    m=float(mass_entry.get())
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    t=float(time_entry.get())
                    if m<0 or t<0:
                        messagebox.showerror(title="Error", message="Mass or time cannot be negative")
                    else:
                        impulsiveForce=(m*v-m*u)/t
                    result_label.config(text=f"{impulsiveForce}")


                impulsiveForce_label=tk.Label(impulsiveForce_frame, text="Impulsive Force", bg="#212129",fg="#08edff",font=("Helvetica",34))
                fin_vel_label=tk.Label(impulsiveForce_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                ini_vel_label=tk.Label(impulsiveForce_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(impulsiveForce_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(impulsiveForce_frame,text="Time",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(impulsiveForce_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                fin_vel_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))
                ini_vel_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(impulsiveForce_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(impulsiveForce_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(impulsiveForce_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:impulsiveForce_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                impulsiveForce_label.grid(row=0,column=1,pady=10)
                fin_vel_label.grid(row=1,column=0,pady=10)
                ini_vel_label.grid(row=2,column=0,pady=10)
                mass_label.grid(row=3,column=0,pady=10)
                time_label.grid(row=4,column=0,pady=10)

                fin_vel_entry.grid(row=1,column=2)
                ini_vel_entry.grid(row=2,column=2)
                mass_entry.grid(row=3,column=2)
                time_entry.grid(row=4,column=2)
                result_label.grid(row=5,column=1,pady=10)

            def weight():
                backbutton(phyf4c2_frame,weight_frame)
                def weight_calc():
                    m=float(mass_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        weight=m*9.81
                    result_label.config(text=f"{weight}")


                weight_label=tk.Label(weight_frame, text="Weight", bg="#212129",fg="#08edff",font=("Helvetica",34))
                mass_label=tk.Label(weight_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(weight_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                mass_entry=tk.Entry(weight_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(weight_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(weight_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(weight_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:weight_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                weight_label.grid(row=0,column=1,pady=10)
                mass_label.grid(row=1,column=0,pady=10)

                mass_entry.grid(row=1,column=2)
                result_label.grid(row=2,column=1,pady=10)
            
            f4Chapter2_label=tk.Label(phyf4c2_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            speed_button=tk.Button(phyf4c2_frame,text="Speed",bg="#90ee90", font=("Helvetica",24),command=lambda:speed())
            velocity_button=tk.Button(phyf4c2_frame,text="Velocity",bg="#90ee90", font=("Helvetica",24),command=lambda:velocity())
            acceleration_button=tk.Button(phyf4c2_frame,text="Acceleration",bg="#90ee90", font=("Helvetica",24),command=lambda:acceleration())
            momentum_button=tk.Button(phyf4c2_frame,text="Momentum",bg="#90ee90", font=("Helvetica",24),command=lambda:momentum())
            force_button=tk.Button(phyf4c2_frame,text="Force",bg="#90ee90", font=("Helvetica",24),command=lambda:force())
            impulse_button=tk.Button(phyf4c2_frame,text="Impulse",bg="#90ee90", font=("Helvetica",24),command=lambda:impulse())
            impulsive_force_button=tk.Button(phyf4c2_frame,text="Impulsive Force",bg="#90ee90", font=("Helvetica",24),command=lambda:impulsiveForce())
            weight_button=tk.Button(phyf4c2_frame,text="Weight",bg="#90ee90", font=("Helvetica",24),command=lambda:weight())

            phy_f4c2_back=tk.Button(phyf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf4c2_frame,phyf4_frame))
            phy_f4c2_back.grid(row=9,column=1,pady=10)


            f4Chapter2_label.grid(row=0,column=1,pady=10)
            speed_button.grid(row=1,column=1,pady=10,sticky="ew")          
            velocity_button.grid(row=2,column=1,pady=10,sticky="ew")          
            acceleration_button.grid(row=3,column=1,pady=10,sticky="ew")       
            momentum_button.grid(row=4,column=1,pady=10,sticky="ew")      
            force_button.grid(row=5,column=1,pady=10,sticky="ew")        
            impulse_button.grid(row=6,column=1,pady=10,sticky="ew")       
            impulsive_force_button.grid(row=7,column=1,pady=10,sticky="ew")    
            weight_button.grid(row=8,column=1,pady=10,sticky="ew")              
            


        f4Chapter_label=tk.Label(phyf4_frame, text="Physics Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(phyf4_frame,text="Chapter 2",bg="#90ee90", font=("Helvetica",24),command=lambda:phy_f4_chap2())
        chap3_button=tk.Button(phyf4_frame,text="Chapter 3",bg="#90ee90", font=("Helvetica",24))
        chap4_button=tk.Button(phyf4_frame,text="Chapter 4",bg="#90ee90", font=("Helvetica",24))
        chap5_button=tk.Button(phyf4_frame,text="Chapter 5",bg="#90ee90", font=("Helvetica",24))
        chap6_button=tk.Button(phyf4_frame,text="Chapter 6",bg="#90ee90", font=("Helvetica",24))

        phy_f4_back=tk.Button(phyf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf4_frame,pack_surface))
        phy_f4_back.grid(row=6,column=2,pady=10)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=10,pady=50)
        chap3_button.grid(row=1,column=2,padx=10)
        chap4_button.grid(row=1,column=4,padx=10)
        chap5_button.grid(row=2,column=1,padx=10,pady=50)
        chap6_button.grid(row=2,column=3,padx=10)

    form4_button=tk.Button(phy_frame,text="Form 4", bg="#90ee90", font=("Helvetica",24), command=lambda:phy_f4())
    form5_button=tk.Button(phy_frame,text="Form 5", bg="#90ee90", font=("Helvetica",24),)
    chooseForm_label=tk.Label(phy_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))

    phy_back = tk.Button(phy_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(pack_surface,forget_surface))

    form4_button.grid(row=1,column=0,padx=5,pady=200)
    form5_button.grid(row=1,column=2,padx=5)
    chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)
    phy_back.grid(row=6,column=1)
    

    def transpiration_rate():
                backbutton(biof5c9_frame,transpiration_rate_frame)
                def transpiration_rate_calc():
                    distance_moved_by_air_bubble_from_x_to_y = int(distance_moved_by_air_bubble_from_x_to_y_entry.get())
                    time=int(time_entry.get())
                    if time<0 or distance_moved_by_air_bubble_from_x_to_y <0:
                        messagebox.showerror(title="Error", message="input cannot be negative")
                    else:
                        transpiration_rate = distance_moved_by_air_bubble_from_x_to_y/time 
                    result_label.config(text=f"{transpiration_rate}")

                transpiration_rate_label = tk.Label(transpiration_rate_frame,text="transpiration rate",bg="#212129",fg="#08edff",font=("Helvetica",34))
                distance_moved_by_air_bubble_from_x_to_y_label=tk.Label(transpiration_rate_frame,text="distance moved by air bubble from x to y",bg="#212129",fg="#08edff",font=("Helvetica",24))
                time_label=tk.Label(transpiration_rate_frame,text="time",bg="#212129",fg="#08edff",font=("Helvetica",24))     
                result_label=tk.Label(transpiration_rate_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                distance_moved_by_air_bubble_from_x_to_y_entry=tk.Entry(transpiration_rate_frame,font=("Helvetica",16))
                time_entry=tk.Entry(transpiration_rate_frame,font=("Helvetica",16))

                transpiration_rate_back=tk.Button(transpiration_rate_frame,text='Back',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(transpiration_rate_frame,biof5c9_frame,result_label))
                transpiration_rate_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(transpiration_rate_frame,text='calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:transpiration_rate_calc())      
                calculate_button.grid(row=8,column=1,pady=10)

                transpiration_rate_label.grid(row=0,column=1,pady=10)
                distance_moved_by_air_bubble_from_x_to_y_label.grid(row=1,column=0,pady=10)
                time_label.grid(row=2,column=0,pady=10)
                distance_moved_by_air_bubble_from_x_to_y_entry.grid(row=1,column=2)
                time_entry.grid(row=2,column=2)
                result_label.grid(row=3,column=1,pady=10)