#it's fun, c?
def read_poi(file):
    poi_dict = {}

    #taken from project2
    for line in file:
        line = line.rstrip()
        if len(line) == 0:
            continue
        parts = line.split(' ', 2)
        print(parts[0],parts[1],parts[2])

        poi_dict[parts[2]] = parts[0],parts[1]
    return poi_dict

if __name__ == "__main__":
    read_poi(open("static/data/poi.txt"))
