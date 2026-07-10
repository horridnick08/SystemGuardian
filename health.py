def calculate_health(cpu, ram, disk):

    score = 100

    score -= cpu * 0.2
    score -= ram * 0.3
    score -= disk * 0.1

    return round(max(score, 0), 2)