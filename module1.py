from pymongo import MongoClient as mc
ls = mc("localhost", 27017)
db = ls.traveldb
coll = db.cities

if __name__ == "__main__":
    

    city = input("Where are you travelling today? ")
    city_info = list(coll.find({"city": city}, {"_id":False}))

    if city_info : 
        print(f'{city_info[0]["city"]}, {city_info[0]["country"]} is {city_info[0]["distance"]} km away. You have the following {len(city_info[0]["poi"])} point(s) of interest there.')
        for i in city_info[0]["poi"]:
            print(f"\t\t-{i}")
        point = input("Enter a list Points of Interest for this city separated by comma: ")
        new_cities = point.split(",")
        old_cities = city_info[0]["poi"]
        try:
            coll.update_one({"city" : city}, {"$set" : {'poi' : old_cities + new_cities}})
            print("Point(s) of Interest Added")
        except:
            print("Sorry couldn't add")
    else :
        
        ask_add  = input(f"{city} is not in the database. Do you want to add it now (Y/N)? ")
        if(ask_add == "Y" or ask_add == "y") :
                new_country = input(f"What country is {city} in?")
                new_distance  = input(f"How far is {city} from planet Jupiter?")
                new_poi = input(f"Enter a list Points of Interest for {city} separated by comma: ")
                try: 
                    if(new_country == "" or new_distance == "" or new_poi == ""):
                        raise Exception
                    result = coll.insert_one(
                        {"city": city, "country" : new_country, "distance" : new_distance, "poi" : new_poi.split(",")})
                    if result.acknowledged == True :
                        print(f"Success, The following id was generated for this city : {result.inserted_id}")
                except:
                    print("Sorry, unable to add this city and points of interest list at this time")
        elif(ask_add == "N" or ask_add == "n"):
            print("Then bye")
 
                

          

        





