def get_grade_text(score):
    if 2.0 <= score < 3:
        return 'Fail'
    if 3.0 <= score < 3.5:
        return 'Poor'
    if 4.0 <= score < 4.5:
        return 'Good'
    if 5.0 <= score < 5.5:
        return 'Very good'
    if 5.50 <= score < 6:
        return 'Excellent'


score = float(input())
print(get_grade_text(score))
