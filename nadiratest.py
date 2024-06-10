import tkinter as tk
from tkinter import messagebox

def backbutton(current_frame, previous_frame):
    current_frame.pack_forget()
    previous_frame.pack()

def backbutton_delresult(current_frame, previous_frame, result_label):
    result_label.config(text="")
    current_frame.pack_forget()
    previous_frame.pack()

def BiologyPage(forget_surface, pack_surface):
    def bio_f4():
        def bio_f4_chap4():
            def percentage_diff_in_mass():
                def percentage_difference_in_mass_calc():
                    try:
                        final_mass = int(final_mass_entry.get())
                        initial_mass = int(initial_mass_entry.get())
                        if final_mass < 0 or initial_mass < 0:
                            messagebox.showerror(title="Error", message="Final or initial mass cannot be negative")
                        else:
                            percentage_difference_in_mass = ((final_mass - initial_mass) / initial_mass) * 100
                            result_label.config(text=f"{percentage_difference_in_mass:.2f}%")
                    except ValueError:
                        messagebox.showerror(title="Error", message="Please enter valid numbers")

                percentage_diff_in_mass_label = tk.Label(percentage_diff_in_mass_frame, text="Percentage Difference in Mass", bg="#212129", fg="#08edff", font=("Helvetica", 34))
                final_mass_label = tk.Label(percentage_diff_in_mass_frame, text="Final Mass", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                initial_mass_label = tk.Label(percentage_diff_in_mass_frame, text="Initial Mass", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                result_label = tk.Label(percentage_diff_in_mass_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                final_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))
                initial_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))

                percentage_diff_in_mass_back = tk.Button(percentage_diff_in_mass_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(percentage_diff_in_mass_frame, biof4c4_frame, result_label))
                calculate_button = tk.Button(percentage_diff_in_mass_frame, text='Calculate', bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=percentage_difference_in_mass_calc)

                percentage_diff_in_mass_label.grid(row=0, column=1, pady=10)
                final_mass_label.grid(row=1, column=0, pady=10)
                initial_mass_label.grid(row=2, column=0, pady=10)
                final_mass_entry.grid(row=1, column=2)
                initial_mass_entry.grid(row=2, column=2)
                result_label.grid(row=3, column=1, pady=10)
                calculate_button.grid(row=8, column=1, pady=10)
                percentage_diff_in_mass_back.grid(row=9, column=1, pady=10)

                percentage_diff_in_mass_frame.pack()

            biof4c4_frame = tk.Frame(root, bg="#212129")
            percentage_diff_in_mass_frame = tk.Frame(root, bg="#212129")

            percentage_diff_in_mass()

        def bio_f4_chap5():
            def enzyme_reaction_rate():
                def enzyme_reaction_rate_calc():
                    try:
                        time_taken = int(time_entry.get())
                        if time_taken < 0:
                            messagebox.showerror(title="Error", message="Time cannot be negative")
                        else:
                            enzyme_reaction_rate = 1 / time_taken
                            result_label.config(text=f"{enzyme_reaction_rate:.4f}")
                    except ValueError:
                        messagebox.showerror(title="Error", message="Please enter a valid number")

                enzyme_reaction_rate_label = tk.Label(enzyme_reaction_rate_frame, text='Enzyme Reaction Rate', bg="#212129", fg="#08edff", font=("Helvetica", 34))
                time_label = tk.Label(enzyme_reaction_rate_frame, text='Time', bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                result_label = tk.Label(enzyme_reaction_rate_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                time_entry = tk.Entry(enzyme_reaction_rate_frame, font=("Helvetica", 16))

                enzyme_reaction_rate_back = tk.Button(enzyme_reaction_rate_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(enzyme_reaction_rate_frame, biof4c5_frame, result_label))
                calculate_button = tk.Button(enzyme_reaction_rate_frame, text='Calculate', bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=enzyme_reaction_rate_calc)

                enzyme_reaction_rate_label.grid(row=0, column=1, pady=10)
                time_label.grid(row=1, column=0, pady=10)
                time_entry.grid(row=1, column=2)
                result_label.grid(row=3, column=1, pady=10)
                calculate_button.grid(row=8, column=1, pady=10)
                enzyme_reaction_rate_back.grid(row=9, column=1, pady=10)

                enzyme_reaction_rate_frame.pack()

            biof4c5_frame = tk.Frame(root, bg="#212129")
            enzyme_reaction_rate_frame = tk.Frame(root, bg="#212129")

            enzyme_reaction_rate()

        def bio_f4_chap7():
            def energy_value_food_sample():
                def energy_value_food_sample_calc():
                    try:
                        mass_water = int(mass_water_entry.get())
                        temperature_rise = int(temperature_rise_entry.get())
                        mass_food = int(mass_food_entry.get())
                        if mass_food < 0 or mass_water < 0 or temperature_rise < 0:
                            messagebox.showerror(title='Error', message="Mass of water, food, and temperature rise cannot be negative")
                        else:
                            energy_value_food_sample = ((4.2 * mass_water * temperature_rise) / mass_food) * 1000
                            result_label.config(text=f"{energy_value_food_sample:.2f} J")
                    except ValueError:
                        messagebox.showerror(title="Error", message="Please enter valid numbers")

                energy_value_food_sample_label = tk.Label(energy_value_food_sample_frame, text='Energy Value of Food Sample', bg="#212129", fg="#08edff", font=("Helvetica", 34))
                mass_water_label = tk.Label(energy_value_food_sample_frame, text='Mass of Water (g)', bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                temperature_rise_label = tk.Label(energy_value_food_sample_frame, text='Temperature Rise (°C)', bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                mass_food_label = tk.Label(energy_value_food_sample_frame, text='Mass of Food (g)', bg="#212129", fg="#90ee90", font=("Helvetica", 24))

                mass_water_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))
                temperature_rise_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))
                mass_food_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))

                result_label = tk.Label(energy_value_food_sample_frame, text='', bg="#212129", fg="#ff4500", font=("Helvetica", 24))

                energy_value_food_sample_back = tk.Button(energy_value_food_sample_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(energy_value_food_sample_frame, biof4c7_frame, result_label))
                calculate_button = tk.Button(energy_value_food_sample_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=energy_value_food_sample_calc)

                energy_value_food_sample_label.grid(row=0, column=1, pady=10)
                mass_water_label.grid(row=1, column=0, pady=10)
                temperature_rise_label.grid(row=2, column=0, pady=10)
                mass_food_label.grid(row=3, column=0, pady=10)
                mass_water_entry.grid(row=1, column=2)
                temperature_rise_entry.grid(row=2, column=2)
                mass_food_entry.grid(row=3, column=2)
                result_label.grid(row=4, column=1, pady=10)
                calculate_button.grid(row=8, column=1, pady=10)
                energy_value_food_sample_back.grid(row=9, column=1, pady=10)

                energy_value_food_sample_frame.pack()

            biof4c7_frame = tk.Frame(root, bg="#212129")
            energy_value_food_sample_frame = tk.Frame(root, bg="#212129")

            energy_value_food_sample()

        biof4_frame = tk.Frame(root, bg="#212129")

        f4Chapter_label = tk.Label(biof4_frame, text="Biology Form 4", bg="#212129", fg="#08edff", font=("Helvetica", 34))
        f4Chapter4_button = tk.Button(biof4_frame, text="Chapter 4", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=bio_f4_chap4)
        f4Chapter5_button = tk.Button(biof4_frame, text="Chapter 5", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=bio_f4_chap5)
        f4Chapter7_button = tk.Button(biof4_frame, text="Chapter 7", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=bio_f4_chap7)
        biof4_back = tk.Button(biof4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton(biof4_frame, BiologyPage))

        f4Chapter_label.grid(row=0, column=1, pady=10)
        f4Chapter4_button.grid(row=1, column=1, pady=10)
        f4Chapter5_button.grid(row=2, column=1, pady=10)
        f4Chapter7_button.grid(row=3, column=1, pady=10)
        biof4_back.grid(row=4, column=1, pady=10)

        biof4_frame.pack()

    def bio_f5():
        pass  # Add functionality for Form 5 if needed

    biology_frame = tk.Frame(root, bg="#212129")

    f4_button = tk.Button(biology_frame, text="Biology Form 4", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=bio_f4)
    f5_button = tk.Button(biology_frame, text="Biology Form 5", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=bio_f5)
    back_button = tk.Button(biology_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton(biology_frame, forget_surface))

    f4_button.pack(pady=10)
    f5_button.pack(pady=10)
    back_button.pack(pady=10)

    pack_surface.pack_forget()
    biology_frame.pack()

root = tk.Tk()
root.title("Science Calculator")
root.geometry("800x600")
root.configure(bg="#212129")

main_frame = tk.Frame(root, bg="#212129")

biology_button = tk.Button(main_frame, text="Biology", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: BiologyPage(main_frame, main_frame))

biology_button.pack(pady=10)
main_frame.pack()

root.mainloop()
