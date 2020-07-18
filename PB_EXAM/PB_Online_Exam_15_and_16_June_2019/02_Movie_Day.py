time_for_shoots = int(input())
amount_scenes = int(input())
scene_time = int(input())

preparation = int(time_for_shoots * 0.15)
time_for_scene_shooting = amount_scenes * scene_time
total_time = time_for_scene_shooting + preparation

if total_time > time_for_shoots:
    diff = total_time - time_for_shoots
    print(f"Time is up! To complete the movie you need {diff} minutes.")
else:
    diff1 = time_for_shoots - total_time
    print(f"You managed to finish the movie on time! You have {diff1} minutes left!")
