from TravelAgent import TravelAgent
def main():
    #now make Travelagent and go the the city by travel
    travel_agent = TravelAgent('GO Jaan')
    trip_info1 =travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '05/07/2022')
    # print('aircraft',trip_info1.aircraft)
    # print('price', trip_info1.cost)
    trip_cities = ['DUB', 'SYD', 'ORD', 'LHR', 'JFK', 'DAC' ]
    trip_info2 = travel_agent.set_trip_multi_city_flexible_round(trip_cities, '20/11/2022')
    print('price', trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)
    

if __name__ == '__main__':
    main()