import tkinter as tk
from tkinter import messagebox

def BiologyPage(forget_surface, pack_surface):
    def backbutton(current_frame, previous_frame):
        current_frame.grid_forget()
        previous_frame.grid()

    def backbutton_delresult(current_frame, previous_frame, result_label):
        result_label.config(text="")
        current_frame.grid_forget()
        previous_frame.grid()

    bio_frame = tk.Frame(root, bg="#212129")
    biof4_frame = tk.Frame(root, bg="#212129")
    biof4c4_frame = tk.Frame(root, bg="#212129")
    percentage_diff_in_mass_frame = tk.Frame(root, bg="#212129")
    biof4c5_frame = tk.Frame(root, bg="#212129")
    enzyme_reaction_rate_frame = tk.Frame(root, bg="#212129")
    biof4c7_frame = tk.Frame(root, bg="#212129")
    energy_value_food_sample_frame = tk.Frame(root, bg="#212129")
    biof5_frame = tk.Frame(root, bg="#212129")
    biof5c9_frame = tk.Frame(root, bg="#212129")
    percentage_cover_frame = tk.Frame(root, bg="#212129")
    population_frame = tk.Frame(root, bg="#212129")
    transpiration_rate_frame = tk.Frame(root, bg="#212129")
    subject_frame=tk.Frame(bg="#212129")

    backbutton(subject_frame, bio_frame)

    def bio_f4():
        backbutton(bio_frame, biof4_frame)

        def bio_f4_chap4():
            backbutton(biof4_frame, biof4c4_frame)

            def percentage_diff_in_mass():
                backbutton(biof4c4_frame, percentage_diff_in_mass_frame)

                def percentage_difference_in_mass_calc():
                    final_mass = int(final_mass_entry.get())
                    initial_mass = int(initial_mass_entry.get())
                    if final_mass < 0 or initial_mass < 0:
                        messagebox.showerror(title="Error", message="Final or initial mass cannot be negative")
                    else:
                        percentage_difference_in_mass = ((final_mass - initial_mass) / initial_mass) * 100
                        result_label.config(text=f"{percentage_difference_in_mass:.2f}%")

                percentage_diff_in_mass_label = tk.Label(percentage_diff_in_mass_frame, text="Percentage Difference in Mass", bg="#212129", fg="#08edff", font=("Helvetica", 34))
                final_mass_label = tk.Label(percentage_diff_in_mass_frame, text="Final Mass", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                initial_mass_label = tk.Label(percentage_diff_in_mass_frame, text="Initial Mass", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                result_label = tk.Label(percentage_diff_in_mass_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                final_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))
                initial_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))

                percentage_diff_in_mass_back = tk.Button(percentage_diff_in_mass_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(percentage_diff_in_mass_frame, biof4c4_frame, result_label))
                calculate_button = tk.Button(percentage_diff_in_mass_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=percentage_difference_in_mass_calc)

                percentage_diff_in_mass_label.grid(row=0, column=1, pady=10)
                final_mass_label.grid(row=1, column=0, pady=10)
                initial_mass_label.grid(row=2, column=0, pady=10)
                final_mass_entry.grid(row=1, column=2)
                initial_mass_entry.grid(row=2, column=2)
                calculate_button.grid(row=3, column=1, pady=10)
                result_label.grid(row=4, column=1, pady=10)
                percentage_diff_in_mass_back.grid(row=5, column=1, pady=10)

            percentage_diff_in_mass()

        def bio_f4_chap5():
            backbutton(biof4_frame, biof4c5_frame)

            def enzyme_reaction_rate():
                backbutton(biof4c5_frame, enzyme_reaction_rate_frame)

                def enzyme_reaction_rate_calc():
                    time_taken = int(time_entry.get())
                    if time_taken < 0:
                        messagebox.showerror(title="Error", message="Time cannot be negative")
                    else:
                        enzyme_reaction_rate = 1 / time_taken
                        rounded_rate = round(enzyme_reaction_rate, 4)
                        result_label.config(text=f"{rounded_rate}")

                enzyme_reaction_rate_label = tk.Label(enzyme_reaction_rate_frame, text="Enzyme Reaction Rate", bg="#212129", fg="#08edff", font=("Helvetica", 34))
                time_label = tk.Label(enzyme_reaction_rate_frame, text="Time", bg="#212129", fg="#08edff", font=("Helvetica", 24))
                result_label = tk.Label(enzyme_reaction_rate_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                time_entry = tk.Entry(enzyme_reaction_rate_frame, font=("Helvetica", 16))

                enzyme_reaction_rate_back = tk.Button(enzyme_reaction_rate_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(enzyme_reaction_rate_frame, biof4c5_frame, result_label))
                calculate_button = tk.Button(enzyme_reaction_rate_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=enzyme_reaction_rate_calc)

                enzyme_reaction_rate_label.grid(row=0, column=1, pady=10)
                time_label.grid(row=1, column=0, pady=10)
                time_entry.grid(row=1, column=2)
                calculate_button.grid(row=2, column=1, pady=10)
                result_label.grid(row=3, column=1, pady=10)
                enzyme_reaction_rate_back.grid(row=4, column=1, pady=10)

            enzyme_reaction_rate()

        def bio_f4_chap7():
            backbutton(biof4_frame, biof4c7_frame)

            def energy_value_food_sample():
                backbutton(biof4c7_frame, energy_value_food_sample_frame)

                def energy_value_food_sample_calc():
                    mass_water = int(mass_water_entry.get())
                    temperature_rise = int(temperature_rise_entry.get())
                    mass_food = int(mass_food_entry.get())
                    if mass_food < 0 or mass_water < 0 or temperature_rise < 0:
                        messagebox.showerror(title="Error", message="Mass of water, food, and temperature rise cannot be negative")
                    else:
                        energy_value_food_sample = ((4.2 * mass_water * temperature_rise) / mass_food) * 1000
                        result_label.config(text=f"{energy_value_food_sample:.2f}")

                energy_value_food_sample_label = tk.Label(energy_value_food_sample_frame, text="Energy Value of Food Sample", bg="#212129", fg="#08edff", font=("Helvetica", 34))
                mass_water_label = tk.Label(energy_value_food_sample_frame, text="Mass of Water", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                temperature_rise_label = tk.Label(energy_value_food_sample_frame, text="Temperature Rise", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                mass_food_label = tk.Label(energy_value_food_sample_frame, text="Mass of Food", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                result_label = tk.Label(energy_value_food_sample_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                mass_water_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))
                temperature_rise_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))
                mass_food_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))

                energy_value_food_sample_back = tk.Button(energy_value_food_sample_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(energy_value_food_sample_frame, biof4c7_frame, result_label))
                calculate_button = tk.Button(energy_value_food_sample_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=energy_value_food_sample_calc)

                energy_value_food_sample_label.grid(row=0, column=1, pady=10)
                mass_water_label.grid(row=1, column=0, pady=10)
                temperature_rise_label.grid(row=2, column=0, pady=10)
                mass_food_label.grid(row=3, column=0, pady=10)
                mass_water_entry.grid(row=1, column=2)
                temperature_rise_entry.grid(row=2, column=2)
                mass_food_entry.grid(row=3, column=2)
                calculate_button.grid(row=4, column=1, pady=10)
                result_label.grid(row=5, column=1, pady=10)
                energy_value_food_sample_back.grid(row=6, column=1, pady=10)

            energy_value_food_sample()

    def bio_f5():
        backbutton(bio_frame, biof5_frame)

        def bio_f5_chap9():
            backbutton(biof5_frame, biof5c9_frame)

            def percentage_cover():
                backbutton(biof5c9_frame, percentage_cover_frame)

                def percentage_cover_calc():
                    squares_covered = int(squares_covered_entry.get())
                    total_squares = int(total_squares_entry.get())
                    if squares_covered < 0 or total_squares < 0:
                        messagebox.showerror(title="Error", message="Squares covered or total squares cannot be negative")
                    else:
                        percentage_cover = (squares_covered / total_squares) * 100
                        result_label.config(text=f"{percentage_cover:.2f}%")

                percentage_cover_label = tk.Label(percentage_cover_frame, text="Percentage Cover", bg="#212129", fg="#08edff", font=("Helvetica", 34))
                squares_covered_label = tk.Label(percentage_cover_frame, text="Squares Covered", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                total_squares_label = tk.Label(percentage_cover_frame, text="Total Squares", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                result_label = tk.Label(percentage_cover_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                squares_covered_entry = tk.Entry(percentage_cover_frame, font=("Helvetica", 16))
                total_squares_entry = tk.Entry(percentage_cover_frame, font=("Helvetica", 16))

                percentage_cover_back = tk.Button(percentage_cover_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(percentage_cover_frame, biof5c9_frame, result_label))
                calculate_button = tk.Button(percentage_cover_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=percentage_cover_calc)

                percentage_cover_label.grid(row=0, column=1, pady=10)
                squares_covered_label.grid(row=1, column=0, pady=10)
                total_squares_label.grid(row=2, column=0, pady=10)
                squares_covered_entry.grid(row=1, column=2)
                total_squares_entry.grid(row=2, column=2)
                calculate_button.grid(row=3, column=1, pady=10)
                result_label.grid(row=4, column=1, pady=10)
                percentage_cover_back.grid(row=5, column=1, pady=10)

            percentage_cover()

            def population():
                backbutton(biof5c9_frame, population_frame)

                def population_calc():
                    first_count = int(first_count_entry.get())
                    second_count = int(second_count_entry.get())
                    number_marked = int(number_marked_entry.get())
                    if first_count < 0 or second_count < 0 or number_marked < 0:
                        messagebox.showerror(title="Error", message="First count, second count, or number marked cannot be negative")
                    else:
                        estimated_population = (first_count * second_count) / number_marked
                        result_label.config(text=f"{estimated_population:.2f}")

                population_label = tk.Label(population_frame, text="Population", bg="#212129", fg="#08edff", font=("Helvetica", 34))
                first_count_label = tk.Label(population_frame, text="First Count", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                second_count_label = tk.Label(population_frame, text="Second Count", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                number_marked_label = tk.Label(population_frame, text="Number Marked", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                result_label = tk.Label(population_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                first_count_entry = tk.Entry(population_frame, font=("Helvetica", 16))
                second_count_entry = tk.Entry(population_frame, font=("Helvetica", 16))
                number_marked_entry = tk.Entry(population_frame, font=("Helvetica", 16))

                population_back = tk.Button(population_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(population_frame, biof5c9_frame, result_label))
                calculate_button = tk.Button(population_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=population_calc)

                population_label.grid(row=0, column=1, pady=10)
                first_count_label.grid(row=1, column=0, pady=10)
                second_count_label.grid(row=2, column=0, pady=10)
                number_marked_label.grid(row=3, column=0, pady=10)
                first_count_entry.grid(row=1, column=2)
                second_count_entry.grid(row=2, column=2)
                number_marked_entry.grid(row=3, column=2)
                calculate_button.grid(row=4, column=1, pady=10)
                result_label.grid(row=5, column=1, pady=10)
                population_back.grid(row=6, column=1, pady=10)

            population()

            def transpiration_rate():
                backbutton(biof5c9_frame, transpiration_rate_frame)

                def transpiration_rate_calc():
                    number_leaves = int(number_leaves_entry.get())
                    total_water = int(total_water_entry.get())
                    time = int(time_entry.get())
                    if number_leaves < 0 or total_water < 0 or time < 0:
                        messagebox.showerror(title="Error", message="Number of leaves, total water, or time cannot be negative")
                    else:
                        transpiration_rate = (total_water / number_leaves) / time
                        result_label.config(text=f"{transpiration_rate:.2f}")

                transpiration_rate_label = tk.Label(transpiration_rate_frame, text="Transpiration Rate", bg="#212129", fg="#08edff", font=("Helvetica", 34))
                number_leaves_label = tk.Label(transpiration_rate_frame, text="Number of Leaves", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                total_water_label = tk.Label(transpiration_rate_frame, text="Total Water", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                time_label = tk.Label(transpiration_rate_frame, text="Time", bg="#212129", fg="#90ee90", font=("Helvetica", 24))
                result_label = tk.Label(transpiration_rate_frame, text="", bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))

                number_leaves_entry = tk.Entry(transpiration_rate_frame, font=("Helvetica", 16))
                total_water_entry = tk.Entry(transpiration_rate_frame, font=("Helvetica", 16))
                time_entry = tk.Entry(transpiration_rate_frame, font=("Helvetica", 16))

                transpiration_rate_back = tk.Button(transpiration_rate_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(transpiration_rate_frame, biof5c9_frame, result_label))
                calculate_button = tk.Button(transpiration_rate_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=transpiration_rate_calc)

                transpiration_rate_label.grid(row=0, column=1, pady=10)
                number_leaves_label.grid(row=1, column=0, pady=10)
                total_water_label.grid(row=2, column=0, pady=10)
                time_label.grid(row=3, column=0, pady=10)
                number_leaves_entry.grid(row=1, column=2)
                total_water_entry.grid(row=2, column=2)
                time_entry.grid(row=3, column=2)
                calculate_button.grid(row=4, column=1, pady=10)
                result_label.grid(row=5, column=1, pady=10)
                transpiration_rate_back.grid(row=6, column=1, pady=10)

            transpiration_rate()

    biof4_button = tk.Button(bio_frame, text="F4", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=bio_f4)
    biof5_button = tk.Button(bio_frame, text="F5", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=bio_f5)
    bio_back = tk.Button(bio_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton(bio_frame, subject_frame))

    biof4_button.grid(row=1, column=0)
    biof5_button.grid(row=2, column=0)
    bio_back.grid(row=3, column=0)
    bio_frame.grid()
