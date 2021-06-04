#TODO:
# -One or more security guards
# -At least one security guard every day
# -Get days without security guards
# -n amount of days
# -Given schedule


schedule = [
    ['1-3', '5', '7-9'], 
    ['2-6', '12-13', '15'],
    ['10', '20'],
]

given_days = 28


def get_days_without(sched, amount_days):
    """[Gets the days without a security guard around the Google building.]

    Args:
        sched ([Array]): [An Array of the schedule of all the security guards]
        amount_days ([Number]): [The amount of days in a month]

    Returns:
        [Array]: [The List of days without a security guard]
    """
    days = []
    days_with_sec = []
    for i in range(1, amount_days + 1):
        days.append(i)
    for i in schedule:
        for j in i:
            # print(j)
            try:
                days_with_sec.append(int(j))
            except ValueError:
                for m in range(int(j.split("-")[0]), int(j.split("-")[1])+1):
                    days_with_sec.append(int(m))
                    
    days_without = list(set(days) - set(days_with_sec))
    return (days_without)

if __name__ == '__main__':
    print(get_days_without(schedule, given_days))
