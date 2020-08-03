def tallest_people(**people):
    sorted_list = sorted(people.items())
    tall = max(people.values())
    for key, val in sorted_list:
        if val == tall:
            print(key, ":", val)


person = {"Jackie": 176, "Wilson": 185, "Saersha": 165, "Roman": 185, "Abram": 169}
tallest_people(**person)
