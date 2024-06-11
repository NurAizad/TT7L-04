     def bio_f4_chap4():
            backbutton(biof4_frame,biof4c4_frame)
        
            form_4_chapter_4_label=tk.Label(biof4c4_frame, text='percentage diff in mass', bg="#212129",fg="#08edff",font=("Helvetica",34))
            form_4_chapter_4_label.grid(row=0, column=0)
            percentage_diff_in_mass_button=tk.Button(biof4c4_frame, text='percentage diff in mass', bg="#212129",fg="#08edff",font=("Helvetica",34), command=lambda:percentage_diff_in_mass())
            percentage_diff_in_mass_button.grid(row=1,column=4,padx=10)
            backbutton_f4c4=tk.Button(biof4c4_frame, text='back', bg="#212129",fg="#08edff",font=("Helvetica",34) ,command=lambda:backbutton(biof4c4_frame,biof4_frame) )
            backbutton_f4c4.grid(row=1,column=1)


            def percentage_diff_in_mass():
                backbutton(biof4c4_frame, percentage_diff_in_mass_frame)
                def percentage_difference_in_mass_calc():
                    final_mass = int(final_mass_entry.get())
                    initial_mass = int(initial_mass_entry.get())
                    if final_mass<0 or initial_mass<0:
                        messagebox.showerror(title="Error", message="final or initial mass cannot be negative")
                    else:
                            percentage_difference_in_mass = ((final_mass-initial_mass)/initial_mass)*0.01
                    result_label.config(text=f"{percentage_difference_in_mass}")
                


                percentage_diff_in_mass_label = tk.Label(percentage_diff_in_mass_frame, text="percentage difference in mass",bg="#212129",fg="#08edff",font=("Helvetica",34))
                final_mass_label= tk.Label(percentage_diff_in_mass_frame,text="final mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                initial_mass_label = tk.Label(percentage_diff_in_mass_frame,text="initial mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24)) 
                result_label = tk.Label(percentage_diff_in_mass_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                final_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))
                initial_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))

                percentage_diff_in_mass_back = tk.Button(percentage_diff_in_mass_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(percentage_diff_in_mass_frame,biof4c4_frame,result_label))
                percentage_diff_in_mass_back.grid(row=9,column=1,pady=10)
                calculate_button = tk.Button(percentage_diff_in_mass_frame, text='calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:percentage_difference_in_mass_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                percentage_diff_in_mass_label.grid(row=0, column=1,pady=10)
                final_mass_label.grid(row=1,column=0, pady=10)
                initial_mass_label.grid(row=2, column=0,pady=10)
                final_mass_entry.grid(row=1,column=2)
                initial_mass_entry.grid(row=2, column=2)
                result_label.grid(row=3,column=1,pady=10)

    
