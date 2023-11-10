import pendulum as p

def time_zones():
    cities = [
        'Europe/Budapest',
        'Europe/London',
        'Asia/Tokyo',
        'America/New_York'
    ]

    times = []
    for city in cities:
        now = p.now(city)
        now = now.to_datetime_string()
        times.append(now)
    
    for i in range(len(times)):
        print(f'{cities[i]}: {times[i]}')

time_zones()
