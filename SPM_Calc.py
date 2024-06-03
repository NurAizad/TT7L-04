#bio functions
def calculate_percentage_difference_in_mass():
    try:
        final_mass = int(entry_enter_final_mass.get())
        initial_mass = int(entry_enter_initial_mass.get())
        percentage_difference_in_mass = ((final_mass-initial_mass)/initial_mass)*0.01
        label_percentage_difference_in_mass.config(text=f"{percentage_difference_in_mass}")
    except ValueError:
        print("please enter numbers")  

def calculate_enzyem_reaction_rate():
    try:
        time_taken=int(entry_time_taken.get())    
        enzyme_reaction_rate = 1/time_taken
        rounded_rate=round(enzyme_reaction_rate,4)
        label_enzyme_reaction_rate.config(text=f"{rounded_rate}")
    except ValueError:
        print('please enter numbers') 

def calculate_energy_value_food_sample():
    try:
        mass_water=int(entry_mass_water.get())
        temperature_rise=(entry_temperature_rise.get())
        mass_food=(entry_mass_food.get())
        energy_value_food_sample = ((4.2*mass_water*temperature_rise)/mass_food*1000)
        label_energy_value_food_sample.config(text=f"{energy_value_food_sample}")
    except ValueError:
        print('please enter numbers')     

def calculate_percentage_cover():
    try:
        number_of_squares_containing_a_species = int(entry_enter_number_of_squares_containing_a_species.get())
        Total_number_of_squares = int(entry_enter_total_number_of_squares.get())
        percentage_cover = number_of_squares_containing_a_species/Total_number_of_squares*100
        label_percentage_cover.config(text=f"{percentage_cover}")
    except ValueError:
        print('please enter numbers')     
def calculate_population():
    try:
        first_catch_number = int(entry_first_catch_number.get())    
        second_catch_number = int (entry_second_catch_number.get())
        marked_second_catch_number = int(entry_marked_second_catch_number.get())
        population = (first_catch_number*second_catch_number/marked_second_catch_number)
        label_population.config(text=f"{population}")
    except ValueError:
        print('please enter numbers')    

def transpiration_rate():
    try:
        distance_moved_by_air_bubble_from_x_to_y = int(entry_distance_moved_by_air_bubble_from_x_to_y.get())     
        time = int(entry_time)  
        transpiration_rate = distance_moved_by_air_bubble_from_x_to_y/time
        label_transpiration_rate.config(text=f"{transpiration_rate}")
    except ValueError:
        print('please enter numbers')  


#bio widgets f4 c4
entry_enter_final_mass = ttk.Entry(c4_f4_bio_window)
label_enter_initial_mass = tk.Label(c4_f4_bio_window, text='enter initial mass:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_enter_initial_mass = ttk.Entry(c4_f4_bio_window)
label_percentage_difference_in_mass = tk.Label(c4_f4_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
button_calculate_percentage_difference_in_mass = ttk.Button(c4_f4_bio_window, text='calculate percentage difference in mass', command=calculate_percentage_difference_in_mass)
#bio widgets f4 c5
label_enter_time_taken = tk.Label(c5_f4_bio_window, text='enter time taken:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_time_taken = ttk.Entry(c5_f4_bio_window)
label_enzyme_reaction_rate = tk.Label(c5_f4_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
button_calculate_enzyme_reaction_rate = ttk.Button(c5_f4_bio_window, text='calcuate enzyme reaction rate', command=calculate_enzyem_reaction_rate)
#bio widgets f4 c7
label_mass_water = tk.Label(c7_f4_bio_window, text='enter mass water',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_mass_water = ttk.Entry (c7_f4_bio_window)
label_mass_food = tk.Label(c7_f4_bio_window, text='enter mass of food',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_mass_food = ttk.Entry (c7_f4_bio_window)
label_temperature_rise = tk.Label(c7_f4_bio_window, text='temperature rise',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_temperature_rise = ttk.Entry (c7_f4_bio_window)
label_energy_value_food_sample = tk.Label(c7_f4_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
button_calculate_energy_value_food_sample = ttk.Button(c7_f4_bio_window, text='calcuate energy value food sample', command=calculate_energy_value_food_sample)
#bio widgets f5 c9
label_enter_number_of_squares_containing_a_species = tk.Label(c9_f4_bio_window, text='enter number of squares containing a species',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_enter_number_of_squares_containing_a_species=ttk.Entry(c9_f5_bio_window)
label_enter_total_number_of_squares =  tk.Label(c9_f4_bio_window, text='enter total number of squares',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_enter_total_number_of_squares=ttk.Entry(c9_f5_bio_window)
label_percentage_cover =  tk.Label(c7_f4_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)

label_first_catch_number = tk.Label(c9_f5_bio_window, text='enter first catch number:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_first_catch_number = ttk.Entry(c9_f5_bio_window)
label_second_catch_number =  tk.Label(c9_f5_bio_window, text='enter second catch number:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_second_catch_number = ttk.Entry(c9_f5_bio_window)
label_marked_second_catch_number =  tk.Label(c9_f5_bio_window, text='enter marked second catch number:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_marked_second_catch_number = ttk.Entry(c9_f5_bio_window)
label_population = tk.Label(c9_f5_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
button_population_size = ttk.Button(c9_f5_bio_window, text='population size', command=calculate_population)

label_distance_moved_by_air_bubble_from_x_to_y = tk.Label(c9_f5_bio_window, text='distance moved by air bubble from x to y:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_distance_moved_by_air_bubble_from_x_to_y = ttk.Entry(c9_f5_bio_window)
label_time = tk.Label(c9_f5_bio_window, text='enter time taken:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
entry_time = ttk.Entry(c9_f5_bio_window)
label_transpiration_rate = tk.Label(c9_f5_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
button_transpiration_rate = ttk.Button(c9_f5_bio_window, text='transpiration rate', command=transpiration_rate)
