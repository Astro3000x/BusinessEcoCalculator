##BusinessEcoMETER##

# Imports
import requests
import time

#Declare Data
power_sources = {
  "u.s. states": {
      "alabama": "Natural Gas",
      "alaska": "Natural Gas",
      "arizona": "Solar",
      "arkansas": "Natural Gas",
      "california": "Renewables",
      "colorado": "Natural Gas",
      "connecticut": "Natural Gas",
      "delaware": "Natural Gas",
      "florida": "Natural Gas",
      "georgia": "Natural Gas",
      "hawaii": "Oil",
      "idaho": "Hydropower",
      "illinois": "Nuclear",
      "indiana": "Coal",
      "iowa": "Wind",
      "kansas": "Wind",
      "kentucky": "Coal",
      "louisiana": "Natural Gas",
      "maine": "Hydropower",
      "maryland": "Natural Gas",
      "massachusetts": "Natural Gas",
      "michigan": "Natural Gas",
      "minnesota": "Renewables",
      "mississippi": "Natural Gas",
      "missouri": "Coal",
      "montana": "Coal",
      "nebraska": "Natural Gas",
      "nevada": "Renewables",
      "new hampshire": "Natural Gas",
      "new jersey": "Natural Gas",
      "new mexico": "Natural Gas",
      "new york": "Natural Gas",
      "north carolina": "Natural Gas",
      "north dakota": "Coal",
      "ohio": "Natural Gas",
      "oklahoma": "Natural Gas",
      "oregon": "Hydropower",
      "pennsylvania": "Natural Gas",
      "rhode island": "Natural Gas",
      "south carolina": "Nuclear",
      "south dakota": "Wind",
      "tennessee": "Hydropower",
      "texas": "Natural Gas",
      "utah": "Coal",
      "vermont": "Renewables",
      "virginia": "Natural Gas",
      "washington": "Hydropower",
      "west virginia": "Coal",
      "wisconsin": "Natural Gas",
      "wyoming": "Coal",
  },
  "canadian provinces": {
      "alberta": "Natural Gas",
      "british columbia": "Hydropower",
      "manitoba": "Hydropower",
      "new brunswick": "Natural Gas",
      "newfoundland and labrador": "Hydropower",
      "nova scotia": "Coal",
      "ontario": "Nuclear",
      "prince edward island": "Wind",
      "quebec": "Hydropower",
      "saskatchewan": "Coal",
      "yukon": "Hydropower",
      "northwest territories": "Diesel",
      "nunavut": "Diesel",
  }
}
industrial_machine_power = {
  "Electric Motors": 5000,  # 5 kW
  "Industrial Air Compressors": 8500,            # 8.5 kW
  "Welding Machines": 10500,                     # 10.5 kW
  "CNC Machines": 6000,                          # 6 kW
  "Industrial Ovens": 17500,                     # 17.5 kW
  "Industrial Refrigerators/Freezers": 5500,     # 5.5 kW
  "Pumps": 13500,        # 13.5 kW
  "Industrial Blenders/Mixers": 3000,            # 3 kW
  "Hydraulic Presses": 9000,                     # 9 kW
  "Electric Forklifts": 3500,                    # 3.5 kW
  "Industrial Fans": 25500,              # 25.5 kW
  "Palletizers and Depalletizers": 6000,         # 6 kW
  "Conveyor Systems": 2750,                      # 2.75 kW
  "Molding Machines": 17500,                     # 17.5 kW
  "Laser Cutters": 9000,                         # 9 kW
  "Grinders": 5500,                 # 5.5 kW
  "Vibratory Feeders": 1750,                     # 1.75 kW
  "Printing Presses": 9000,                      # 9 kW
  "Steam Boilers": 27500,                        # 27.5 kW
  "Chillers": 52500,                # 52.5 kW
  "Industrial Lathes": 11000,                    # 11 kW
  "Electroplating Equipment": 16500              # 16.5 kW
}



power_sources_with_emissions = {
  "natural gas": 450,  # grams CO2 per 1000 watts
  "hydropower": 1,      # grams CO2 per 1000 watts
  "solar": 50,          # grams CO2 per 1000 watts
  "oil": 900,           # grams CO2 per 1000 watts
  "nuclear": 0,         # grams CO2 per 1000 watts (considered low emissions)
  "coal": 1000,         # grams CO2 per 1000 watts
  "wind": 10,           # grams CO2 per 1000 watts
  "biomass": 100,       # grams CO2 per 1000 watts
  "diesel": 850,        # grams CO2 per 1000 watts
}

# Example usage:




#Main Code

print("Business Emissions Calculator")
print("For all text inputs please no special characters or spaces.")
print("-----------------")

brk = False
while brk == False:
  busname = str(input("Enter your business name to get started\n"))
  try:
    datatxt = open(f"{busname}data.txt", "x")
    brk = True
  except:
    print("-----------------")
    print("File already exists.")
    print("Overwrite File? (y/n)\n")
    if input() == "y":
      datatxt = open(f"{busname}data.txt", "w")
      brk = True
    else:
      brk = False
    
print("-----------------")
print(f"Welcome {busname}")
print("-----------------")
source = False
while source == False:
  location = input("Enter your location to get started. Canada: CA, United States: US\n")
  state = input("Enter your state/province to get started. (E.g.: California, Ontario)\n")
  if location.lower() == "ca":
    print("-----------------")
    state = state.lower()
    try:
      print("Your power source(s) are:",power_sources["canadian provinces"][state])
      
      source = True
    except:
      print("Invalid Province name, please try again.")
    power_source = power_sources["canadian provinces"][state]
  elif location.lower() == "us":
    print("-----------------")
    try:
      print("Your power source(s) are:",power_sources["u.s. states"][state])
      
      source = True
    except:
      print("Invalid State name please try again.")
    power_source = power_sources["u.s. states"][state]
  else:
    print("-----------------")
    print("You did not enter a valid country location, please try again.")



print(f"Carbon Emissions per 1000 watts: {power_sources_with_emissions[power_source.lower()]}g")
emissions = power_sources_with_emissions[power_source.lower()]

machines = input(f"Enter the name of the machine(s) you are using, splitting each with a comma (,). (E.g.: Electric Motors), for a full list of machines please type 'list'\n")

if machines.lower() == "list":
    print(industrial_machine_power.keys(),"\n")
    machines = input(f"Enter the name of the machine(s) you are using (case sensitive), splitting each with a comma (,). (E.g.: Electric Motors)\n")
else:
  pass
print("-----------------")
machines = machines.split(",")
totalemissions = 0
for m in machines:
  print(f"Carbon Emissions per hour of {m}: {industrial_machine_power[m] * emissions}g")
  totalemissions += industrial_machine_power[m] * emissions
print(f"Total Emissions: {totalemissions}")
print("-----------------")
print(f"Total Emissions per hour: {totalemissions/1000}kg")
trees = totalemissions/1000 * 24 * 365/10
print(f"Total Trees Needed To Offset Emissions in One Year: {trees}")
print("-----------------")
savedata = input("Would you like to save your data? (y/n)\n")
if savedata.lower() == "y":
  writedata = open(f"{busname}data.txt","a")
  writedata.write(f"{busname} Emissions Report:\n Location:{state}\nPower Source:{power_source}\nTotal Emissions Per Hour: {totalemissions/1000}kg\n\nMade with Business Emissions Calculator")

print(f"Thank you for using Business Eco Meter, {busname}")