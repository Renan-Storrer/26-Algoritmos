def period_permanece(start, end):
    if start is None or end is None:
        return False
    if not isinstance(start, int) or not isinstance(end, int):
        return False
    elif start < 0 or end < 0:
        return False
    elif start > end:
        return False

    return True

def study_schedule(permanence_period, target_time):
    count = 0
    
    if target_time is None:
        return None

    for start_time, end_time in permanence_period:
        if not period_permanece(start_time, end_time):
            return None
        if (target_time >= start_time) and (target_time <= end_time):
            count += 1

    return count