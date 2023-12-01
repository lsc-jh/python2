
# install with py -m pip install pendulum
import pendulum as p
from mypackage import base as mp

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


def using_mypackage():
    num_1 = 33
    num_2 = 24

    avg = mp.average(num_1, num_2)
    print(avg)
    po = mp.power(num_1, num_2)
    print(po)
    print(mp.prime_finder(20))
    print(mp.matrix_generator())


using_mypackage()
