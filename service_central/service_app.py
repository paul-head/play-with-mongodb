import nosql.mongo_setup as mongo_setup
from nosql.car import Car
from nosql.engine import Engine
from nosql.servicehistory import ServiceHistory


def main():
    print_header()
    config_mongo()
    user_loop()


def print_header():
    print('----------------------------------------------')
    print('|                                             |')
    print('|           SERVICE CENTRAL v.02              |')
    print('|               demo edition                  |')
    print('|                                             |')
    print('----------------------------------------------')
    print()


def config_mongo():
    mongo_setup.global_init()


def user_loop():
    while True:
        print("Available actions:")
        print(" * [a]dd car")
        print(" * [l]ist cars")
        print(" * [f]ind car")
        print(" * [p]oor serviced")
        print(" * perform [s]ervice")
        print(" * e[x]it")
        print()
        ch = input("> ").strip().lower()
        if ch == 'a':
            add_car()
        elif ch == 'l':
            list_cars()
        elif ch == 's':
            service_car()
        elif ch == 'p':
            show_poor_serviced_cars()
        elif not ch or ch == 'x':
            print("Goodbye")
            break


def add_car():
    model = input('What is the model: ')
    make = input('What is the make: ')
    year = int(input('Year built?: '))

    car = Car()
    car.year = year
    car.make = make
    car.model = model

    engine = Engine()
    engine.horsepower = 590
    engine.mpg = 22
    engine.liters = 4.0

    car.engine = engine

    car.save()


def list_cars():
    cars = Car.objects().order_by('-year')
    for car in cars:
        print(f'{car.make} -- {car.model} with vin {car.vi_number} (year {car.year})')
        print(f'{len(car.service_history)} of service records\n')
        for s in car.service_history:
            print('   * ${:,.0f} {}'.format(s.price, s.description))
    print()


def service_car():
    # vin = input('What is the vin of the car to service? ')
    # car = Car.objects().filter(vi_number=vin).first()
    # if not car:
    #     print('Car with VIN {} not found'.format(vin))
    #     return

    # print('We will service '+ car.model)
    # service = ServiceHistory()
    # service.price = float(input('What is the price? '))
    # service.description = input('What type of service is this? ')
    # service.customers_rating = int(input('How happy our costumer? [1-5]'))

    # car.service_history.append(service)
    # car.save()

    vin = input('What is the vin of the car to service? ')
    service = ServiceHistory()
    service.price = float(input('What is the price? '))
    service.description = input('What type of service is this? ')
    service.customers_rating = int(input('How happy our costumer? [1-5] '))

    updated = Car.objects(vi_number=vin).update_one(push__service_history=service)
    if updated ==0:
        print("Car with VIN {} not found!\n".format(vin))
        return


def show_poor_serviced_cars():
    level = int(input('What max level of satisfaction are we looking for? [1-5] '))

    #  {'service_history.customres_reting': {$lte: level} }
    cars = Car.objects(service_history__customers_rating__lte=level)
    for car in cars:
        print()
        print(f'{car.make} -- {car.model} with vin {car.vi_number} (year {car.year})')
        print(f'{len(car.service_history)} of service records\n')
        for s in car.service_history:
            print('   * Stisfaction: {} ${:,.0f} {}\n'.format(s.customers_rating, s.price, s.description))


if __name__ == '__main__':
    main()
