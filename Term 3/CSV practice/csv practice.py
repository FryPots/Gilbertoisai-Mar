import csv

def import_accidents_per_year(filename: str) -> dict:
    incidents: dict = {}
    fatal_crashes: dict = {}
    with open(file=filename, mode="r", newline="") as table:
        data = csv.reader(next(table))
        data = csv.reader(table)
        for row in data:
            year = row[0]
            year_data = {
            "Fatalities": row[1],
            "Injuries": row[2],
            "Crashes": row[3],
            "Fatal Crashes": row[4],
            "Distraction Affected Fatal Crashes":                   row[5],
            "Fatal Crashes involving Cell Phone Use":               row[6],
            "Fatal Crashes involving Excessive Speed":              row[7],
            "Fatal Crashes while Driving under the Influence":      row[8],
            "Fatal Crashes involving Fatigue or Illness":           row[9]}
            
            incidents[year] = year_data
        return incidents
            
##,,,,,,,,,Fatal Crashes involving Fatigue or Illness            
                
def main():
    incidents = import_accidents_per_year("accidents.csv")
    for i in incidents:
        print(i)
    search = input("Select a year and type it: ")
    if incidents.get(search) != None:
        result = incidents[search]
        option = 0
        for keys in result:
            print(f"{option}. {keys}")
            option += 1
        search = input("Type the info you want to get: ").capitalize()
        if [search.isnumeric(), search.isdigit()] == [True, True]:
            keys = (list(result))
            print(f"\n{keys[int(search)]}:    {result[keys[int(search)]]}")
        else:
            if search in result:
                print(f"\n{search}:     {result[search]}")
            else:
                print("Not Found :(")
    input()
    main()

main()