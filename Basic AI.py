def calculate_pass_probability(study_hours, sleep_hours):

    if study_hours < 1:
        study_score = 0.2
    elif 1 <= study_hours <= 3:
        study_score = 0.6
    elif 3 < study_hours <= 6:
        study_score = 0.9
    else:
        study_score = 1.0

    if sleep_hours < 6:
        sleep_score = 0.4
    elif 6 <= sleep_hours <= 9:
        sleep_score = 0.9 
    else:
        sleep_score = 0.7

    study_weight = 0.7
    sleep_weight = 0.3

    probability = (study_score * study_weight + sleep_score * sleep_weight) * 100

    return round(probability, 2)

x = float(input("Enter study hours: "))
y = float(input("Enter sleep hours: "))

print(f"Probability of passing: {calculate_pass_probability(x, y)}%")