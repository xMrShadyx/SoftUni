# ⦁	Рекордът в секунди – реално число;
# ⦁	Разстоянието в метри – реално число;
# ⦁	Времето в секунди, за което плува разстояние от 1 м. - реално число.
import math

rec_in_sec = float(input())
dist_in_meters = float(input())
time_insec_1m = float(input())

need_to_swim = dist_in_meters * time_insec_1m
added_time = dist_in_meters / 15
added_time = math.floor(added_time)
added_time = added_time * 12.5

total_time = need_to_swim + added_time
left_time = total_time - rec_in_sec

if rec_in_sec > total_time:
  print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
elif rec_in_sec <= total_time:
  print(f'No, he failed! He was {left_time:.2f} seconds slower.')