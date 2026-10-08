Number_of_exercises = 6
Sets_per_exercise = 4
Reps_per_set = 10
Average_weight_per_rep = 60
session_duration_in_minutes = 45
# calculations
total_sets = Number_of_exercises * Sets_per_exercise
total_reps = total_sets * Reps_per_set
total_volume = total_reps * Average_weight_per_rep
reps_per_minute = total_reps / session_duration_in_minutes

print(f"Total set: {total_sets}")
print(f"Total reps: {total_reps}")
print(f"Total volume: {total_volume} kg")
print(f"Reps_per_minute: {reps_per_minute}")
if total_volume>10000: 
        print("Exceeded 10000 kg target: True")
else: 
        print("Exceeded 10000 kg target: False")
                             