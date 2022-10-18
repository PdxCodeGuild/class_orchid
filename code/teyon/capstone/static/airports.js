console.log("string")
const airportData = {
    "AAL": {
        "location": "Aalborg",
        "airport": "AAL"
    },
    "GLA": {
        "location": "Glasgow",
        "airport": "GLA"
    },
    "OKA": {
        "location": "Okinawa",
        "airport": "OKA"
    },
    "AAR": {
        "location": "Aarhus",
        "airport": "AAR"
    },
    "PIK": {
        "location": "Glasgow Prestwick",
        "airport": "PIK"
    },
    "OKC": {
        "location": "Oklahoma City",
        "airport": "OKC"
    },
    "ABD": {
        "location": "Abadan",
        "airport": "ABD"
    },
    "GOM": {
        "location": "Goma",
        "airport": "GOM"
    },
    "OMA": {
        "location": "Omaha",
        "airport": "OMA"
    },
    "ABA": {
        "location": "Abakan",
        "airport": "ABA"
    },
    "GNU": {
        "location": "Goodnew Bay",
        "airport": "GNU"
    },
    "ONT": {
        "location": "Ontario",
        "airport": "ONT"
    },
    "ABR": {
        "location": "Aberdeen",
        "airport": "ABR"
    },
    "YYR": {
        "location": "Goose Bay",
        "airport": "YYR"
    },
    "ORN": {
        "location": "Oran",
        "airport": "ORN"
    },
    "ABZ": {
        "location": "Aberdeen",
        "airport": "ABZ"
    },
    "GKA": {
        "location": "Goroka",
        "airport": "GKA"
    },
    "ORB": {
        "location": "Orebro",
        "airport": "ORB"
    },
    "AHB": {
        "location": "Abha",
        "airport": "AHB"
    },
    "GOT": {
        "location": "Gothenburg",
        "airport": "GOT"
    },
    "MCO": {
        "location": "Orlando",
        "airport": "MCO"
    },
    "ABJ": {
        "location": "Abidjan",
        "airport": "ABJ"
    },
    "LPA": {
        "location": "Gran Canaria",
        "airport": "LPA"
    },
    "OSA": {
        "location": "Osaka",
        "airport": "OSA"
    },
    "ABI": {
        "location": "Abilene",
        "airport": "ABI"
    },
    "GCM": {
        "location": "Grand Cayman",
        "airport": "GCM"
    },
    "ITM": {
        "location": "Osaka Itami",
        "airport": "ITM"
    },
    "AUH": {
        "location": "Abu Dhabi",
        "airport": "AUH"
    },
    "GFK": {
        "location": "Grand Fork",
        "airport": "GFK"
    },
    "KIX": {
        "location": "International",
        "airport": "KIX"
    },
    "ABV": {
        "location": "Abuja",
        "airport": "ABV"
    },
    "GRR": {
        "location": "Grand Rapids",
        "airport": "GRR"
    },
    "OSH": {
        "location": "Oshkosh",
        "airport": "OSH"
    },
    "ACA": {
        "location": "Acapulco",
        "airport": "ACA"
    },
    "GDT": {
        "location": "Grand Turk",
        "airport": "GDT"
    },
    "OSI": {
        "location": "Osijek",
        "airport": "OSI"
    },
    "AGV": {
        "location": "Acarigua",
        "airport": "AGV"
    },
    "YQU": {
        "location": "Grande Prairie",
        "airport": "YQU"
    },
    "OSL": {
        "location": "Oslo",
        "airport": "OSL"
    },
    "ACC": {
        "location": "Accra",
        "airport": "ACC"
    },
    "KGX": {
        "location": "Grayling",
        "airport": "KGX"
    },
    "FBU": {
        "location": "Oslo Fornebu",
        "airport": "FBU"
    },
    "ADK": {
        "location": "Adak Island",
        "airport": "ADK"
    },
    "GRZ": {
        "location": "Graz",
        "airport": "GRZ"
    },
    "GEN": {
        "location": "Oslo Gardermoen",
        "airport": "GEN"
    },
    "ADA": {
        "location": "Adana",
        "airport": "ADA"
    },
    "GTF": {
        "location": "Great Falls",
        "airport": "GTF"
    },
    "ZOS": {
        "location": "Osorno",
        "airport": "ZOS"
    },
    "ADD": {
        "location": "Addis Ababa",
        "airport": "ADD"
    },
    "GRB": {
        "location": "Green Bay",
        "airport": "GRB"
    },
    "OST": {
        "location": "Ostend",
        "airport": "OST"
    },
    "ADL": {
        "location": "Adelaide",
        "airport": "ADL"
    },
    "GSO": {
        "location": "Greensboro",
        "airport": "GSO"
    },
    "YOW": {
        "location": "Ottawa",
        "airport": "YOW"
    },
    "ADE": {
        "location": "Aden",
        "airport": "ADE"
    },
    "GLH": {
        "location": "Greenville",
        "airport": "GLH"
    },
    "OUA": {
        "location": "Ouagadougou",
        "airport": "OUA"
    },
    "AER": {
        "location": "Adler",
        "airport": "AER"
    },
    "GSP": {
        "location": "Greenville",
        "airport": "GSP"
    },
    "OXR": {
        "location": "Oxnard/Ventura",
        "airport": "OXR"
    },
    "AGA": {
        "location": "Agadir",
        "airport": "AGA"
    },
    "PGV": {
        "location": "Greenville",
        "airport": "PGV"
    },
    "PPG": {
        "location": "Pago Pago",
        "airport": "PPG"
    },
    "AGU": {
        "location": "Aguascaliente",
        "airport": "AGU"
    },
    "GND": {
        "location": "Grenada",
        "airport": "GND"
    },
    "PLM": {
        "location": "Palembang",
        "airport": "PLM"
    },
    "AMD": {
        "location": "Ahmedabad",
        "airport": "AMD"
    },
    "GNB": {
        "location": "Grenoble",
        "airport": "GNB"
    },
    "PMO": {
        "location": "Palermo",
        "airport": "PMO"
    },
    "AJA": {
        "location": "Ajaccio",
        "airport": "AJA"
    },
    "GRQ": {
        "location": "Groningen",
        "airport": "GRQ"
    },
    "PSP": {
        "location": "Palm Springs",
        "airport": "PSP"
    },
    "KKI": {
        "location": "Akiachak",
        "airport": "KKI"
    },
    "GDL": {
        "location": "Guadalajara",
        "airport": "GDL"
    },
    "PMI": {
        "location": "Palma de Mallorca",
        "airport": "PMI"
    },
    "AKI": {
        "location": "Akiak",
        "airport": "AKI"
    },
    "GUM": {
        "location": "Guam",
        "airport": "GUM"
    },
    "PFN": {
        "location": "Panama City",
        "airport": "PFN"
    },
    "AXT": {
        "location": "Akita",
        "airport": "AXT"
    },
    "CAN": {
        "location": "Guangzhou",
        "airport": "CAN"
    },
    "PTY": {
        "location": "Panama City",
        "airport": "PTY"
    },
    "CAK": {
        "location": "Akron/Canton",
        "airport": "CAK"
    },
    "GUA": {
        "location": "Guatemala City",
        "airport": "GUA"
    },
    "PAC": {
        "location": "Panama City Paitilla",
        "airport": "PAC"
    },
    "ABT": {
        "location": "Al-Baha",
        "airport": "ABT"
    },
    "GYE": {
        "location": "Guayaquil",
        "airport": "GYE"
    },
    "PPT": {
        "location": "Papeete",
        "airport": "PPT"
    },
    "ABY": {
        "location": "Albany",
        "airport": "ABY"
    },
    "GCI": {
        "location": "Guernsey",
        "airport": "GCI"
    },
    "PFO": {
        "location": "Paphos",
        "airport": "PFO"
    },
    "ALB": {
        "location": "Albany",
        "airport": "ALB"
    },
    "KWL": {
        "location": "Guilin",
        "airport": "KWL"
    },
    "PBM": {
        "location": "Paramaribo",
        "airport": "PBM"
    },
    "YAL": {
        "location": "Albert Bay",
        "airport": "YAL"
    },
    "KWE": {
        "location": "Guiyang",
        "airport": "KWE"
    },
    "ORG": {
        "location": "Hoop",
        "airport": "ORG"
    },
    "ABQ": {
        "location": "Albuquerque",
        "airport": "ABQ"
    },
    "GPT": {
        "location": "Gulfport",
        "airport": "GPT"
    },
    "PAR": {
        "location": "Paris",
        "airport": "PAR"
    },
    "AXD": {
        "location": "Aleandroupolis",
        "airport": "AXD"
    },
    "GUC": {
        "location": "Gunnison ",
        "airport": "GUC"
    },
    "CDG": {
        "location": "Paris Charles de Gaulle",
        "airport": "CDG"
    },
    "ALP": {
        "location": "Aleppo",
        "airport": "ALP"
    },
    "HAG": {
        "location": "Hagen",
        "airport": "HAG"
    },
    "LBG": {
        "location": "Paris Le Bourget",
        "airport": "LBG"
    },
    "ESF": {
        "location": "Alexandria",
        "airport": "ESF"
    },
    "HAK": {
        "location": "Haikou",
        "airport": "HAK"
    },
    "FJR": {
        "location": "Paris Orly ORY Al-Fujairah",
        "airport": "FJR"
    },
    "HAS": {
        "location": "Hail",
        "airport": "HAS"
    },
    "PSC": {
        "location": "Pasco",
        "airport": "PSC"
    },
    "ALG": {
        "location": "Algiers",
        "airport": "ALG"
    },
    "HKD": {
        "location": "Hakodate",
        "airport": "HKD"
    },
    "PUF": {
        "location": "Pau",
        "airport": "PUF"
    },
    "ALC": {
        "location": "Alicante",
        "airport": "ALC"
    },
    "YHZ": {
        "location": "Halifax",
        "airport": "YHZ"
    },
    "PEN": {
        "location": "Penang",
        "airport": "PEN"
    },
    "AET": {
        "location": "Allakaket",
        "airport": "AET"
    },
    "YUX": {
        "location": "Hall Beach",
        "airport": "YUX"
    },
    "PNS": {
        "location": "Pensacola",
        "airport": "PNS"
    },
    "ABE": {
        "location": "Allentown",
        "airport": "ABE"
    },
    "HAM": {
        "location": "Hamburg",
        "airport": "HAM"
    },
    "PIA": {
        "location": "Peoria",
        "airport": "PIA"
    },
    "ALA": {
        "location": "Alma Ata",
        "airport": "ALA"
    },
    "YHM": {
        "location": "Hamilton",
        "airport": "YHM"
    },
    "PEI": {
        "location": "Pereira",
        "airport": "PEI"
    },
    "AOR": {
        "location": "Alor Setar",
        "airport": "AOR"
    },
    "PHF": {
        "location": "Williamsburg",
        "airport": "PHF"
    },
    "PGF": {
        "location": "Perpignan",
        "airport": "PGF"
    },
    "AOO": {
        "location": "Altoona",
        "airport": "AOO"
    },
    "HGH": {
        "location": "Hangzhou",
        "airport": "HGH"
    },
    "KPV": {
        "location": "Perryville",
        "airport": "KPV"
    },
    "HAN": {
        "location": "AMA Hanoi",
        "airport": "HAN"
    },
    "PER": {
        "location": "Perth",
        "airport": "PER"
    },
    "AHT": {
        "location": "Amchitka",
        "airport": "AHT"
    },
    "HAJ": {
        "location": "Hanover",
        "airport": "HAJ"
    },
    "PSR": {
        "location": "Pescara",
        "airport": "PSR"
    },
    "AMM": {
        "location": "Amman",
        "airport": "AMM"
    },
    "HRE": {
        "location": "Harare",
        "airport": "HRE"
    },
    "PEW": {
        "location": "Peshawar",
        "airport": "PEW"
    },
    "ATQ": {
        "location": "Amritsar",
        "airport": "ATQ"
    },
    "HRB": {
        "location": "Harbin",
        "airport": "HRB"
    },
    "PSG": {
        "location": "Petersburg",
        "airport": "PSG"
    },
    "AMS": {
        "location": "Amsterdam",
        "airport": "AMS"
    },
    "HRL": {
        "location": "Harlingen",
        "airport": "HRL"
    },
    "PHL": {
        "location": "Philadelphia",
        "airport": "PHL"
    },
    "HAR": {
        "location": "Airport SPL Harrisburg",
        "airport": "HAR"
    },
    "PNE": {
        "location": "Philadelphia North",
        "airport": "PNE"
    },
    "ANC": {
        "location": "Anchorage",
        "airport": "ANC"
    },
    "HFD": {
        "location": "Hartford",
        "airport": "HFD"
    },
    "PNH": {
        "location": "Phnom Penh",
        "airport": "PNH"
    },
    "MRI": {
        "location": "Field",
        "airport": "MRI"
    },
    "BNH": {
        "location": "Hartford Barnes",
        "airport": "BNH"
    },
    "PHX": {
        "location": "Phoenix",
        "airport": "PHX"
    },
    "AOI": {
        "location": "Ancona",
        "airport": "AOI"
    },
    "BDL": {
        "location": "Bradley",
        "airport": "BDL"
    },
    "SCF": {
        "location": "Municipal",
        "airport": "SCF"
    },
    "ANS": {
        "location": "Andahuaylas",
        "airport": "ANS"
    },
    "HDY": {
        "location": "Hat Yai",
        "airport": "HDY"
    },
    "HKT": {
        "location": "Phuket",
        "airport": "HKT"
    },
    "AZA": {
        "location": "Anguilla",
        "airport": "AZA"
    },
    "HAU": {
        "location": "Haugesund",
        "airport": "HAU"
    },
    "PIR": {
        "location": "Pierre",
        "airport": "PIR"
    },
    "ANI": {
        "location": "Aniak",
        "airport": "ANI"
    },
    "HAV": {
        "location": "Havana",
        "airport": "HAV"
    },
    " SA": {
        "location": "Pisa",
        "airport": " SA"
    },
    "AKA": {
        "location": "Ankang",
        "airport": "AKA"
    },
    "YHY": {
        "location": "Hay River",
        "airport": "YHY"
    },
    "PIT": {
        "location": "Pittsburgh",
        "airport": "PIT"
    },
    "ANK": {
        "location": "Ankara",
        "airport": "ANK"
    },
    "HFE": {
        "location": "Hefei",
        "airport": "HFE"
    },
    "PIU": {
        "location": "Piura",
        "airport": "PIU"
    },
    "ESB": {
        "location": "Ankara Esenboga",
        "airport": "ESB"
    },
    "HLN": {
        "location": "Helena",
        "airport": "HLN"
    },
    "PTU": {
        "location": "Platinum",
        "airport": "PTU"
    },
    "NCY": {
        "location": "Annecy",
        "airport": "NCY"
    },
    "AGH": {
        "location": "Helsingborg",
        "airport": "AGH"
    },
    "PYM": {
        "location": "Plymouth",
        "airport": "PYM"
    },
    "AYT": {
        "location": "Antalya",
        "airport": "AYT"
    },
    "HEL": {
        "location": "Helsinki",
        "airport": "HEL"
    },
    "PIH": {
        "location": "Pocatello",
        "airport": "PIH"
    },
    "TNR": {
        "location": "Antananarivo",
        "airport": "TNR"
    },
    "HER": {
        "location": "Heraklion",
        "airport": "HER"
    },
    "PNI": {
        "location": "Pohnpei",
        "airport": "PNI"
    },
    "ANU": {
        "location": "Antigua",
        "airport": "ANU"
    },
    "HMO": {
        "location": "Hermosillo",
        "airport": "HMO"
    },
    "PTP": {
        "location": "Point \u00e0 Pitre",
        "airport": "PTP"
    },
    "ANF": {
        "location": "Antofagasta",
        "airport": "ANF"
    },
    "ITO": {
        "location": "Hilo",
        "airport": "ITO"
    },
    "PNR": {
        "location": "Pointe Noire",
        "airport": "PNR"
    },
    "ANR": {
        "location": "Antwerp",
        "airport": "ANR"
    },
    "HIJ": {
        "location": "Hiroshima",
        "airport": "HIJ"
    },
    "PSE": {
        "location": "Ponce",
        "airport": "PSE"
    },
    "ANV": {
        "location": "Anvik",
        "airport": "ANV"
    },
    "SGN": {
        "location": "Ho Chi Minh City",
        "airport": "SGN"
    },
    "PDL": {
        "location": "Ponta Delgada",
        "airport": "PDL"
    },
    "AOJ": {
        "location": "Aomori",
        "airport": "AOJ"
    },
    "HET": {
        "location": "Hohhot",
        "airport": "HET"
    },
    "POR": {
        "location": "Pori",
        "airport": "POR"
    },
    "APW": {
        "location": "Apia",
        "airport": "APW"
    },
    "HCR": {
        "location": "Holy Cross",
        "airport": "HCR"
    },
    "PMV": {
        "location": "Porlamar",
        "airport": "PMV"
    },
    "ATW": {
        "location": "Appleton",
        "airport": "ATW"
    },
    "HOM": {
        "location": "Homer",
        "airport": "HOM"
    },
    "PAP": {
        "location": "Port au Prince",
        "airport": "PAP"
    },
    "AQJ": {
        "location": "Aqaba",
        "airport": "AQJ"
    },
    "HKG": {
        "location": "Hong Kong",
        "airport": "HKG"
    },
    "PLZ": {
        "location": "Port Elizabeth",
        "airport": "PLZ"
    },
    "ACV": {
        "location": "Arcata Eureka",
        "airport": "ACV"
    },
    "HNL": {
        "location": "Honolulu",
        "airport": "HNL"
    },
    "POG": {
        "location": "Port Gentil",
        "airport": "POG"
    },
    "ARC": {
        "location": "Arctic Village",
        "airport": "ARC"
    },
    "MKK": {
        "location": "Hoolehua ",
        "airport": "MKK"
    },
    "PGM": {
        "location": "Port Graham",
        "airport": "PGM"
    },
    "ARE": {
        "location": "Arecibo",
        "airport": "ARE"
    },
    "HPB": {
        "location": "Hooper Bay",
        "airport": "HPB"
    },
    "PHC": {
        "location": "Port Harcourt",
        "airport": "PHC"
    },
    "AQP": {
        "location": "Arequipa",
        "airport": "AQP"
    },
    "HKN": {
        "location": "Hoskins",
        "airport": "HKN"
    },
    "PHE": {
        "location": "Port Hedland",
        "airport": "PHE"
    },
    "ARI": {
        "location": "Arica",
        "airport": "ARI"
    },
    "HOU": {
        "location": "Houston",
        "airport": "HOU"
    },
    "PTH": {
        "location": "Port Heiden",
        "airport": "PTH"
    },
    "AUA": {
        "location": "Aruba",
        "airport": "AUA"
    },
    "SGR": {
        "location": "Houston Hull Field",
        "airport": "SGR"
    },
    "POM": {
        "location": "Port Moresby",
        "airport": "POM"
    },
    "ASC": {
        "location": "Ascension",
        "airport": "ASC"
    },
    "IAH": {
        "location": "Intercontinental",
        "airport": "IAH"
    },
    "POS": {
        "location": "Port of Spain Trinidad",
        "airport": "POS"
    },
    "AVL": {
        "location": "Asheville",
        "airport": "AVL"
    },
    "HUS": {
        "location": "Hughes",
        "airport": "HUS"
    },
    "PVH": {
        "location": "Port Velho",
        "airport": "PVH"
    },
    "AKJ": {
        "location": "Ashikawa",
        "airport": "AKJ"
    },
    "HUY": {
        "location": "Humberside",
        "airport": "HUY"
    },
    "VLI": {
        "location": "Port Vila",
        "airport": "VLI"
    },
    "HTS": {
        "location": "Ashland Huntington",
        "airport": "HTS"
    },
    "HSV": {
        "location": "Huntsville",
        "airport": "HSV"
    },
    "PDX": {
        "location": "Portland",
        "airport": "PDX"
    },
    "ASM": {
        "location": "Asmara",
        "airport": "ASM"
    },
    "HSL": {
        "location": "Huslia",
        "airport": "HSL"
    },
    "OVD": {
        "location": "Asturias",
        "airport": "OVD"
    },
    "HYA": {
        "location": "Hyannis",
        "airport": "HYA"
    },
    "OPO": {
        "location": "Porto",
        "airport": "OPO"
    },
    "ASU": {
        "location": "Asuncion",
        "airport": "ASU"
    },
    "HYD": {
        "location": "Hyderabad",
        "airport": "HYD"
    },
    "POA": {
        "location": "Porto Alegre",
        "airport": "POA"
    },
    " SW": {
        "location": "Aswan",
        "airport": " SW"
    },
    "IGU": {
        "location": "Iguassu Falls",
        "airport": "IGU"
    },
    "PRG": {
        "location": "Prague",
        "airport": "PRG"
    },
    "ATH": {
        "location": "Athens",
        "airport": "ATH"
    },
    "ILI": {
        "location": "Iliamna",
        "airport": "ILI"
    },
    "PQI": {
        "location": "Presque Isle",
        "airport": "PQI"
    },
    "ATL": {
        "location": "Atlanta",
        "airport": "ATL"
    },
    "IND": {
        "location": "Indianapolis",
        "airport": "IND"
    },
    "YXS": {
        "location": "Prince George",
        "airport": "YXS"
    },
    "JAO": {
        "location": "Atlanta Beaver Ruin",
        "airport": "JAO"
    },
    "INN": {
        "location": "Innsbruck",
        "airport": "INN"
    },
    "YPR": {
        "location": "Prince Rupert",
        "airport": "YPR"
    },
    "JAJ": {
        "location": "Atlanta Perimeter",
        "airport": "JAJ"
    },
    "YEV": {
        "location": "Inuvik",
        "airport": "YEV"
    },
    "PVD": {
        "location": "Providence",
        "airport": "PVD"
    },
    "AIY": {
        "location": "Atlantic City",
        "airport": "AIY"
    },
    "IPH": {
        "location": "Ipoh",
        "airport": "IPH"
    },
    "PLS": {
        "location": "Providenciales",
        "airport": "PLS"
    },
    "ACY": {
        "location": "Field",
        "airport": "ACY"
    },
    "YFB": {
        "location": "Iqaluit",
        "airport": "YFB"
    },
    "SCC": {
        "location": "Deadhorse",
        "airport": "SCC"
    },
    "ATT": {
        "location": "Atmautluak",
        "airport": "ATT"
    },
    "IQQ": {
        "location": "Iquique",
        "airport": "IQQ"
    },
    "PCL": {
        "location": "Pucallpa",
        "airport": "PCL"
    },
    "AKL": {
        "location": "Auckland",
        "airport": "AKL"
    },
    "IMT": {
        "location": "Iron Mountain",
        "airport": "IMT"
    },
    "PBC": {
        "location": "Puebla",
        "airport": "PBC"
    },
    "AGS": {
        "location": "Augusta",
        "airport": "AGS"
    },
    "IFN": {
        "location": "Isfahan",
        "airport": "IFN"
    },
    "PYH": {
        "location": "Puerto Ayachucho",
        "airport": "PYH"
    },
    "AUS": {
        "location": "Austin",
        "airport": "AUS"
    },
    "IRP": {
        "location": "Isiro",
        "airport": "IRP"
    },
    "PBL": {
        "location": "Puerto Cabello",
        "airport": "PBL"
    },
    "AYP": {
        "location": "Ayacucho",
        "airport": "AYP"
    },
    "ISB": {
        "location": "Islamabad",
        "airport": "ISB"
    },
    "PXM": {
        "location": "Puerto Escondido",
        "airport": "PXM"
    },
    "BGW": {
        "location": "Baghdad Al Muthana",
        "airport": "BGW"
    },
    "ISC": {
        "location": "Mary\u2019s",
        "airport": "ISC"
    },
    "PEM": {
        "location": "Puerto Maldonado",
        "airport": "PEM"
    },
    "SDA": {
        "location": "International",
        "airport": "SDA"
    },
    "TSO": {
        "location": "Isles of Scil Tresco",
        "airport": "TSO"
    },
    "PMC": {
        "location": "Puerto Montt",
        "airport": "PMC"
    },
    "BAH": {
        "location": "Bahrain",
        "airport": "BAH"
    },
    "ISP": {
        "location": "Macarthur",
        "airport": "ISP"
    },
    "PZO": {
        "location": "Puerto Ordaz",
        "airport": "PZO"
    },
    "BFL": {
        "location": "Bakersfield",
        "airport": "BFL"
    },
    "IST": {
        "location": "Istanbul",
        "airport": "IST"
    },
    "POP": {
        "location": "Puerto Plata",
        "airport": "POP"
    },
    "DPS": {
        "location": "Bali Island Denpasar",
        "airport": "DPS"
    },
    "ITH": {
        "location": "Ithaca",
        "airport": "ITH"
    },
    "PVR": {
        "location": "Puerto Vallarta",
        "airport": "PVR"
    },
    "BBA": {
        "location": "Balmaceda",
        "airport": "BBA"
    },
    "KIB": {
        "location": "Ivanoff Bay",
        "airport": "KIB"
    },
    "PUQ": {
        "location": "Punta Arenas",
        "airport": "PUQ"
    },
    "BWI": {
        "location": "Baltimore",
        "airport": "BWI"
    },
    "IZM": {
        "location": "Izmir",
        "airport": "IZM"
    },
    "PUS": {
        "location": "Pusan",
        "airport": "PUS"
    },
    "MTN": {
        "location": "Baltimore Gl. Martin",
        "airport": "MTN"
    },
    "ADB": {
        "location": "Menderes",
        "airport": "ADB"
    },
    "FNJ": {
        "location": "Pyongyang",
        "airport": "FNJ"
    },
    "BKO": {
        "location": "Bamako",
        "airport": "BKO"
    },
    "IGL": {
        "location": "Izmir Cigli Military",
        "airport": "IGL"
    },
    "TAO": {
        "location": "Qingdao",
        "airport": "TAO"
    },
    "BND": {
        "location": "Bandar Abbas",
        "airport": "BND"
    },
    "JAC": {
        "location": "Jackson",
        "airport": "JAC"
    },
    "YQB": {
        "location": "Quebec",
        "airport": "YQB"
    },
    "BWN": {
        "location": "Bandar Seri Bagawan",
        "airport": "BWN"
    },
    "JAN": {
        "location": "Jackson",
        "airport": "JAN"
    },
    "UET": {
        "location": "Quetta",
        "airport": "UET"
    },
    "BLR": {
        "location": "Bangalore",
        "airport": "BLR"
    },
    "JAX": {
        "location": "Jacksonville",
        "airport": "JAX"
    },
    "KWN": {
        "location": "Quinhagak",
        "airport": "KWN"
    },
    "BKK J": {
        "location": "Bangkok",
        "airport": "BKK J"
    },
    "JAI": {
        "location": "aipur",
        "airport": "JAI"
    },
    "UIO": {
        "location": "Quito",
        "airport": "UIO"
    },
    "BGR": {
        "location": "Bangor",
        "airport": "BGR"
    },
    "CGK": {
        "location": "Jakarta",
        "airport": "CGK"
    },
    "RBA": {
        "location": "Rabat",
        "airport": "RBA"
    },
    "BGF": {
        "location": "Bangui",
        "airport": "BGF"
    },
    "JKT": {
        "location": "Jakarta",
        "airport": "JKT"
    },
    "RAB": {
        "location": "Rabaul",
        "airport": "RAB"
    },
    "BJL": {
        "location": "Banjul",
        "airport": "BJL"
    },
    "HLP": {
        "location": "Perdana Kusuma",
        "airport": "HLP"
    },
    "RDU": {
        "location": "Raleigh/Durham",
        "airport": "RDU"
    },
    "BAV": {
        "location": "Baotou",
        "airport": "BAV"
    },
    "JVL": {
        "location": "Janesville",
        "airport": "JVL"
    },
    "RGN": {
        "location": "Rangoon/Yangon",
        "airport": "RGN"
    },
    "BGI": {
        "location": "Barbados",
        "airport": "BGI"
    },
    "JED": {
        "location": "Jeddah",
        "airport": "JED"
    },
    "RAP": {
        "location": "Rapid City",
        "airport": "RAP"
    },
    "BCN": {
        "location": "Barcelona",
        "airport": "BCN"
    },
    "JER": {
        "location": "Jersey",
        "airport": "JER"
    },
    "RAR": {
        "location": "Rarotonga",
        "airport": "RAR"
    },
    "BLA": {
        "location": "Barcelona",
        "airport": "BLA"
    },
    "TNA": {
        "location": "Jinan",
        "airport": "TNA"
    },
    "REC": {
        "location": "Recife",
        "airport": "REC"
    },
    "BDU": {
        "location": "Bardufoss",
        "airport": "BDU"
    },
    "JNB": {
        "location": "Johannesburg",
        "airport": "JNB"
    },
    "RDV": {
        "location": "Red Devil",
        "airport": "RDV"
    },
    "BRI": {
        "location": "Bari",
        "airport": "BRI"
    },
    "JON": {
        "location": "Johnston Island",
        "airport": "JON"
    },
    "RDD": {
        "location": "Redding",
        "airport": "RDD"
    },
    "BNS": {
        "location": "Barinas",
        "airport": "BNS"
    },
    "JHB": {
        "location": "Johor Bahru",
        "airport": "JHB"
    },
    "YQR": {
        "location": "Regina",
        "airport": "YQR"
    },
    "BRM": {
        "location": "Barquisimeto",
        "airport": "BRM"
    },
    "JKG": {
        "location": "Jonkoping",
        "airport": "JKG"
    },
    "RNO": {
        "location": "Reno",
        "airport": "RNO"
    },
    "BAQ": {
        "location": "Barranquilla",
        "airport": "BAQ"
    },
    "JJI": {
        "location": "Juanjui",
        "airport": "JJI"
    },
    "YRB": {
        "location": "Resolute",
        "airport": "YRB"
    },
    "BRW": {
        "location": "Barrow",
        "airport": "BRW"
    },
    "JUB": {
        "location": "Juba",
        "airport": "JUB"
    },
    "REK": {
        "location": "Reykjavik",
        "airport": "REK"
    },
    "BSL": {
        "location": "Basle",
        "airport": "BSL"
    },
    "JUL": {
        "location": "Juliaca",
        "airport": "JUL"
    },
    "RIC": {
        "location": "Richmond",
        "airport": "RIC"
    },
    "BSR": {
        "location": "Basra",
        "airport": "BSR"
    },
    "JNU": {
        "location": "Juneau",
        "airport": "JNU"
    },
    "RIX": {
        "location": "Riga",
        "airport": "RIX"
    },
    "BIA": {
        "location": "Bastia",
        "airport": "BIA"
    },
    "KBL": {
        "location": "Kabul",
        "airport": "KBL"
    },
    "RSC": {
        "location": "Riga Skulte",
        "airport": "RSC"
    },
    "BIK": {
        "location": "Biak",
        "airport": "BIK"
    },
    "KAD": {
        "location": "Kaduna",
        "airport": "KAD"
    },
    "RMI": {
        "location": "Rimini",
        "airport": "RMI"
    },
    "BTR": {
        "location": "Baton Rouge",
        "airport": "BTR"
    },
    "KOJ": {
        "location": "Kagoshima",
        "airport": "KOJ"
    },
    "RIO": {
        "location": "Rio de Janeiro",
        "airport": "RIO"
    },
    "BTL": {
        "location": "Battle Creek",
        "airport": "BTL"
    },
    "OGG": {
        "location": "Kahului",
        "airport": "OGG"
    },
    "GIG": {
        "location": "Internacional",
        "airport": "GIG"
    },
    "MBS": {
        "location": "Bay City/Saginaw",
        "airport": "MBS"
    },
    "KOA": {
        "location": "Kailua",
        "airport": "KOA"
    },
    "SDU": {
        "location": "Dumont",
        "airport": "SDU"
    },
    "BPT": {
        "location": "Beaumont",
        "airport": "BPT"
    },
    "AZO": {
        "location": "Kalamazoo",
        "airport": "AZO"
    },
    "RGL": {
        "location": "Rio Gallegos",
        "airport": "RGL"
    },
    "WBQ": {
        "location": "Beaver",
        "airport": "WBQ"
    },
    "FCA": {
        "location": "Kalispell",
        "airport": "FCA"
    },
    "RIJ": {
        "location": "Rioja",
        "airport": "RIJ"
    },
    "EIS": {
        "location": "Beef Island Tortola",
        "airport": "EIS"
    },
    "KLG": {
        "location": "Kalskag",
        "airport": "KLG"
    },
    "RUH": {
        "location": "Riyadh",
        "airport": "RUH"
    },
    "BJS": {
        "location": "Beijing",
        "airport": "BJS"
    },
    "KAL": {
        "location": "Kaltag",
        "airport": "KAL"
    },
    "ROA": {
        "location": "Roanoke",
        "airport": "ROA"
    },
    "PEK": {
        "location": "Beijing",
        "airport": "PEK"
    },
    "KNB": {
        "location": "Kanab",
        "airport": "KNB"
    },
    "RTB": {
        "location": "Roatan",
        "airport": "RTB"
    },
    "NAY": {
        "location": "Airport",
        "airport": "NAY"
    },
    "KGA": {
        "location": "Kananga",
        "airport": "KGA"
    },
    "ROC": {
        "location": "Rochester",
        "airport": "ROC"
    },
    "BEW": {
        "location": "Beira",
        "airport": "BEW"
    },
    "KAN": {
        "location": "Kano",
        "airport": "KAN"
    },
    "RST": {
        "location": "Rochester",
        "airport": "RST"
    },
    "BEY": {
        "location": "Beirut",
        "airport": "BEY"
    },
    "MKC": {
        "location": "Kansas City",
        "airport": "MKC"
    },
    "RFD": {
        "location": "Rockford",
        "airport": "RFD"
    },
    "BEL": {
        "location": "Belem",
        "airport": "BEL"
    },
    "MCI": {
        "location": "International",
        "airport": "MCI"
    },
    "RWI": {
        "location": "Rocky Mount/Wilson",
        "airport": "RWI"
    },
    "BFS": {
        "location": "Belfast",
        "airport": "BFS"
    },
    "KHH": {
        "location": "Kaohsiung",
        "airport": "KHH"
    },
    "ROM": {
        "location": "Rome",
        "airport": "ROM"
    },
    "BHD": {
        "location": "Belfast Belfast City",
        "airport": "BHD"
    },
    "KHI": {
        "location": "Karachi",
        "airport": "KHI"
    },
    "CIA": {
        "location": "Rome Clampino",
        "airport": "CIA"
    },
    "BEG": {
        "location": "Belgrade",
        "airport": "BEG"
    },
    "KGF": {
        "location": "Karaganda",
        "airport": "KGF"
    },
    "FCO": {
        "location": "Rome Fiumicino",
        "airport": "FCO"
    },
    "BZE": {
        "location": "Belize",
        "airport": "BZE"
    },
    "KRP": {
        "location": "Karup",
        "airport": "KRP"
    },
    "ROL": {
        "location": "Roosevelt",
        "airport": "ROL"
    },
    "TZA": {
        "location": "Belize Municipal",
        "airport": "TZA"
    },
    "KUK": {
        "location": "Kasigluk",
        "airport": "KUK"
    },
    "ROW": {
        "location": "Roswell",
        "airport": "ROW"
    },
    "BLI": {
        "location": "Bellingham",
        "airport": "BLI"
    },
    "KSF": {
        "location": "Kassel",
        "airport": "KSF"
    },
    "ROP": {
        "location": "Rota",
        "airport": "ROP"
    },
    "BHZ": {
        "location": "Belo Horizonte",
        "airport": "BHZ"
    },
    "KTM": {
        "location": "Kathmandu",
        "airport": "KTM"
    },
    "RTM": {
        "location": "Rotterdam",
        "airport": "RTM"
    },
    "BEN": {
        "location": "Benghazi",
        "airport": "BEN"
    },
    "LIH": {
        "location": "Kauai Is",
        "airport": "LIH"
    },
    "URO": {
        "location": "Rouen",
        "airport": "URO"
    },
    "BGO": {
        "location": "Bergen",
        "airport": "BGO"
    },
    "ENA": {
        "location": "Kenai",
        "airport": "ENA"
    },
    "RBY": {
        "location": "Ruby",
        "airport": "RBY"
    },
    "BER": {
        "location": "Berlin",
        "airport": "BER"
    },
    "KER": {
        "location": "Kerman",
        "airport": "KER"
    },
    "RSH": {
        "location": "Russian Mission",
        "airport": "RSH"
    },
    "SXF": {
        "location": "Berlin Schonefeld",
        "airport": "SXF"
    },
    "KTN": {
        "location": "Ketchikan",
        "airport": "KTN"
    },
    "SCN": {
        "location": "Saarbruecken",
        "airport": "SCN"
    },
    "TXL": {
        "location": "Berlin Tegel",
        "airport": "TXL"
    },
    "KHV": {
        "location": "Khabarovsk",
        "airport": "KHV"
    },
    "SMF": {
        "location": "Sacramento",
        "airport": "SMF"
    },
    "THF": {
        "location": "Berlin Tempelhof",
        "airport": "THF"
    },
    "IEV": {
        "location": "Kiev",
        "airport": "IEV"
    },
    "SPN": {
        "location": "Saipan",
        "airport": "SPN"
    },
    "BDA": {
        "location": "Bermuda",
        "airport": "BDA"
    },
    "KBP": {
        "location": "Kiev Borispol",
        "airport": "KBP"
    },
    "SID": {
        "location": "Sal",
        "airport": "SID"
    },
    "BRN": {
        "location": "Bern",
        "airport": "BRN"
    },
    "KGL": {
        "location": "Kigali",
        "airport": "KGL"
    },
    "SLC": {
        "location": "Salt Lake City",
        "airport": "SLC"
    },
    "BET": {
        "location": "Bethel",
        "airport": "BET"
    },
    "JRO": {
        "location": "Kilimanjaro",
        "airport": "JRO"
    },
    "SLW": {
        "location": "Saltillo",
        "airport": "SLW"
    },
    "BTT": {
        "location": "Bettles",
        "airport": "BTT"
    },
    "ILE": {
        "location": "Killeen",
        "airport": "ILE"
    },
    "SSA": {
        "location": "Salvador",
        "airport": "SSA"
    },
    "KIM": {
        "location": "Kimberley",
        "airport": "KIM"
    },
    "SZG": {
        "location": "Salzburg",
        "airport": "SZG"
    },
    "BIQ": {
        "location": "Biarritz",
        "airport": "BIQ"
    },
    "KND": {
        "location": "Kindu",
        "airport": "KND"
    },
    "ADZ": {
        "location": "San Andres Island",
        "airport": "ADZ"
    },
    "BIO": {
        "location": "Bilbao",
        "airport": "BIO"
    },
    "KVC": {
        "location": "King Cover",
        "airport": "KVC"
    },
    "SJT": {
        "location": "San Angelo",
        "airport": "SJT"
    },
    "BIL": {
        "location": "Billings",
        "airport": "BIL"
    },
    "AKN": {
        "location": "King Salm",
        "airport": "AKN"
    },
    "SAT": {
        "location": "San Antonio",
        "airport": "SAT"
    },
    "BLL": {
        "location": "Billund",
        "airport": "BLL"
    },
    "KIN": {
        "location": "Kingston",
        "airport": "KIN"
    },
    "SVZ": {
        "location": "San Antonio",
        "airport": "SVZ"
    },
    "BGM": {
        "location": "Binghamton",
        "airport": "BGM"
    },
    "KTP": {
        "location": "Kingston Tinson",
        "airport": "KTP"
    },
    "SAN": {
        "location": "San Diego",
        "airport": "SAN"
    },
    "BTU": {
        "location": "Bintulu",
        "airport": "BTU"
    },
    "FIH": {
        "location": "Kinshasa",
        "airport": "FIH"
    },
    "SFO": {
        "location": "San Francisco",
        "airport": "SFO"
    },
    "BHM": {
        "location": "Birmingham",
        "airport": "BHM"
    },
    "KPN": {
        "location": "Kipnuk",
        "airport": "KPN"
    },
    "EMB": {
        "location": "Embarkadero",
        "airport": "EMB"
    },
    "BHX": {
        "location": "Birmingham",
        "airport": "BHX"
    },
    "KRN": {
        "location": "Kiruna",
        "airport": "KRN"
    },
    "SJC": {
        "location": "San Jose",
        "airport": "SJC"
    },
    "BXO": {
        "location": "Bissau",
        "airport": "BXO"
    },
    "FKI": {
        "location": "Kisangani",
        "airport": "FKI"
    },
    "SJO": {
        "location": "San Jose",
        "airport": "SJO"
    },
    "BLZ": {
        "location": "Blantyre",
        "airport": "BLZ"
    },
    "KLU": {
        "location": "Klagenfurt",
        "airport": "KLU"
    },
    " SJD": {
        "location": "San Jose Los Cabos",
        "airport": " SJD"
    },
    "BFN": {
        "location": "Bloemfontein",
        "airport": "BFN"
    },
    "TYS": {
        "location": "Knoxville",
        "airport": "TYS"
    },
    "SJU": {
        "location": "San Juan",
        "airport": "SJU"
    },
    "BMI": {
        "location": "Bloomington",
        "airport": "BMI"
    },
    "KCZ": {
        "location": "Kochi",
        "airport": "KCZ"
    },
    "SIG": {
        "location": "San Juan Isla Grande",
        "airport": "SIG"
    },
    "BVB": {
        "location": "Boa Vista",
        "airport": "BVB"
    },
    "ADQ": {
        "location": "Kodiak",
        "airport": "ADQ"
    },
    "SLP": {
        "location": "San Luis Potosi",
        "airport": "SLP"
    },
    "BOO": {
        "location": "Bodo",
        "airport": "BOO"
    },
    "KMQ": {
        "location": "Komatsu",
        "airport": "KMQ"
    },
    "SAP": {
        "location": "San Pedro Sula",
        "airport": "SAP"
    },
    "BOG": {
        "location": "Bogota",
        "airport": "BOG"
    },
    "KKH": {
        "location": "Kongiganak",
        "airport": "KKH"
    },
    "SAL": {
        "location": "San Salvador",
        "airport": "SAL"
    },
    "BOI": {
        "location": "Boise",
        "airport": "BOI"
    },
    "ROR": {
        "location": "Koror",
        "airport": "ROR"
    },
    "SOM": {
        "location": "San Tome",
        "airport": "SOM"
    },
    "BLQ": {
        "location": "Bologna",
        "airport": "BLQ"
    },
    "KSA": {
        "location": "Kosrae",
        "airport": "KSA"
    },
    "SAH": {
        "location": "Sanaa",
        "airport": "SAH"
    },
    "BOM": {
        "location": "Bombay",
        "airport": "BOM"
    },
    "BKI": {
        "location": "Kota Kinabalu",
        "airport": "BKI"
    },
    "SDP": {
        "location": "Sand Point",
        "airport": "SDP"
    },
    "BON": {
        "location": "Bonaire",
        "airport": "BON"
    },
    "OTZ": {
        "location": "Kotzebue",
        "airport": "OTZ"
    },
    "SDK": {
        "location": "Sandakan",
        "airport": "SDK"
    },
    "BOD": {
        "location": "Bordeaux",
        "airport": "BOD"
    },
    "KYU": {
        "location": "Koyukuk",
        "airport": "KYU"
    },
    "SBA": {
        "location": "Santa Barbara",
        "airport": "SBA"
    },
    "KJA": {
        "location": "Boston BOS Krasnoyarsk",
        "airport": "KJA"
    },
    "SRZ": {
        "location": "Santa Cruz",
        "airport": "SRZ"
    },
    "WBU": {
        "location": "Boulder",
        "airport": "WBU"
    },
    "KRS": {
        "location": "Kristiansand",
        "airport": "KRS"
    },
    "VVI": {
        "location": "Santa Cruz",
        "airport": "VVI"
    },
    "YVO": {
        "location": "Bourlamaq/Val D\u2019or",
        "airport": "YVO"
    },
    "KUL": {
        "location": "Kuala Lumpur",
        "airport": "KUL"
    },
    "SMX": {
        "location": "Santa Maria",
        "airport": "SMX"
    },
    "BOH": {
        "location": "Bournemouth",
        "airport": "BOH"
    },
    "KCH": {
        "location": "Kuching",
        "airport": "KCH"
    },
    "SCL": {
        "location": "Santiago",
        "airport": "SCL"
    },
    "BZN": {
        "location": "Bozeman",
        "airport": "BZN"
    },
    "KMJ": {
        "location": "Kumamoto",
        "airport": "KMJ"
    },
    "SCQ": {
        "location": "Santiago de Compostela",
        "airport": "SCQ"
    },
    "KMG": {
        "location": "Kunming",
        "airport": "KMG"
    },
    "SDQ": {
        "location": "Santo Domingo",
        "airport": "SDQ"
    },
    "BRD": {
        "location": "Brainerd",
        "airport": "BRD"
    },
    "KUO": {
        "location": "Kuopio",
        "airport": "KUO"
    },
    "STD": {
        "location": "Santo Domingo",
        "airport": "STD"
    },
    "BSB": {
        "location": "Brasilia",
        "airport": "BSB"
    },
    "KUH": {
        "location": "Kushiro",
        "airport": "KUH"
    },
    "SYX": {
        "location": "Sanya",
        "airport": "SYX"
    },
    "BTS": {
        "location": "Bratislava",
        "airport": "BTS"
    },
    "YGW": {
        "location": "Kuujjuarap",
        "airport": "YGW"
    },
    "SLZ": {
        "location": "Sao Luiz",
        "airport": "SLZ"
    },
    "BZV": {
        "location": "Brazzaville",
        "airport": "BZV"
    },
    "KWI": {
        "location": "Kuwait",
        "airport": "KWI"
    },
    "SAO": {
        "location": "Sao Paulo",
        "airport": "SAO"
    },
    "BRE": {
        "location": "Bremen",
        "airport": "BRE"
    },
    "KWA": {
        "location": "Kwajalein",
        "airport": "KWA"
    },
    "CGH": {
        "location": "Sao Paulo Congonhas",
        "airport": "CGH"
    },
    "BES": {
        "location": "Brest",
        "airport": "BES"
    },
    "KWJ": {
        "location": "Kwangju",
        "airport": "KWJ"
    },
    "GRU": {
        "location": "Sao Paulo Guarulhos",
        "airport": "GRU"
    },
    "BDR": {
        "location": "Bridgeport",
        "airport": "BDR"
    },
    "KWT": {
        "location": "Kwethluk",
        "airport": "KWT"
    },
    "VCP": {
        "location": "Sao Paulo Viracopos",
        "airport": "VCP"
    },
    "BNE": {
        "location": "Brisbane",
        "airport": "BNE"
    },
    "KWK": {
        "location": "Kwigillingok",
        "airport": "KWK"
    },
    "TMS": {
        "location": "Sao Tome Island",
        "airport": "TMS"
    },
    "LCE": {
        "location": "Bristol BRS La Ceiba",
        "airport": "LCE"
    },
    "SPK": {
        "location": "Sapporo",
        "airport": "SPK"
    },
    "BRO": {
        "location": "Brownsville",
        "airport": "BRO"
    },
    "LSE": {
        "location": "La Crosse",
        "airport": "LSE"
    },
    "CTS": {
        "location": "Sapporo Chitose",
        "airport": "CTS"
    },
    "BRU": {
        "location": "Brussels",
        "airport": "BRU"
    },
    "YGL": {
        "location": "La Grande",
        "airport": "YGL"
    },
    "OKD": {
        "location": "Sapporo Okadama",
        "airport": "OKD"
    },
    "BGA": {
        "location": "Bucaramanga",
        "airport": "BGA"
    },
    "LPB": {
        "location": "La Paz",
        "airport": "LPB"
    },
    "SRQ": {
        "location": "Sarasota/ Bradenton",
        "airport": "SRQ"
    },
    "BUH": {
        "location": "Bucharest",
        "airport": "BUH"
    },
    "LAP": {
        "location": "La Paz Mex",
        "airport": "LAP"
    },
    "YAM": {
        "location": "Sault Ste. Marie",
        "airport": "YAM"
    },
    "BBU": {
        "location": "Bucharest Baneasa",
        "airport": "BBU"
    },
    "LBU": {
        "location": "Labuan",
        "airport": "LBU"
    },
    "SAV": {
        "location": "Savannah",
        "airport": "SAV"
    },
    "OTP": {
        "location": "Bucharest Otopeni",
        "airport": "OTP"
    },
    "LAE": {
        "location": "Lae",
        "airport": "LAE"
    },
    "SCM": {
        "location": "Scammon Bay",
        "airport": "SCM"
    },
    "BUD": {
        "location": "Budapest",
        "airport": "BUD"
    },
    "LFT": {
        "location": "Lafayette",
        "airport": "LFT"
    },
    "AVP": {
        "location": "Scranton Wilkes-Barre",
        "airport": "AVP"
    },
    "BUE": {
        "location": "Buenos Aires",
        "airport": "BUE"
    },
    "LOS": {
        "location": "Lagos",
        "airport": "LOS"
    },
    "SEA": {
        "location": "Seattle",
        "airport": "SEA"
    },
    "AEP": {
        "location": "Newbery",
        "airport": "AEP"
    },
    "SNA": {
        "location": "Ana",
        "airport": "SNA"
    },
    "SDX": {
        "location": "Sedona",
        "airport": "SDX"
    },
    "EZE": {
        "location": "Ministro Pistarini",
        "airport": "EZE"
    },
    "LDU": {
        "location": "Lahad Datu",
        "airport": "LDU"
    },
    "SOV": {
        "location": "Seldovia",
        "airport": "SOV"
    },
    "BJM": {
        "location": "Bujumbura",
        "airport": "BJM"
    },
    "LHE": {
        "location": "Lahore",
        "airport": "LHE"
    },
    "SDJ": {
        "location": "Sendai",
        "airport": "SDJ"
    },
    "BUQ": {
        "location": "Bulawayo",
        "airport": "BUQ"
    },
    "LCH": {
        "location": "Lake Charles",
        "airport": "LCH"
    },
    "SEL": {
        "location": "Seoul",
        "airport": "SEL"
    },
    "BDG": {
        "location": "Bundaberg Blanding",
        "airport": "BDG"
    },
    "LNY": {
        "location": "Lanai City",
        "airport": "LNY"
    },
    "SPE": {
        "location": "Sepulot",
        "airport": "SPE"
    },
    "BUR": {
        "location": "Burbank",
        "airport": "BUR"
    },
    "LGK": {
        "location": "Langkawi",
        "airport": "LGK"
    },
    "SWD": {
        "location": "Seward",
        "airport": "SWD"
    },
    "BTV": {
        "location": "Burlington",
        "airport": "BTV"
    },
    "LAN": {
        "location": "Lansing",
        "airport": "LAN"
    },
    "SVQ": {
        "location": "Seville",
        "airport": "SVQ"
    },
    "BUZ": {
        "location": "Bushehr",
        "airport": "BUZ"
    },
    "LHW": {
        "location": "Lanzhou",
        "airport": "LHW"
    },
    "SHX": {
        "location": "Shageluk",
        "airport": "SHX"
    },
    "BTM": {
        "location": "Butte",
        "airport": "BTM"
    },
    "LRD": {
        "location": "Laredo",
        "airport": "LRD"
    },
    "SHA": {
        "location": "Shanghai",
        "airport": "SHA"
    },
    "CNS": {
        "location": "Cairns",
        "airport": "CNS"
    },
    "LCA": {
        "location": "Larnaca",
        "airport": "LCA"
    },
    "SNN": {
        "location": "Shannon",
        "airport": "SNN"
    },
    "CAI": {
        "location": "Cairo",
        "airport": "CAI"
    },
    "LSP": {
        "location": "Las Piedras",
        "airport": "LSP"
    },
    "SWA": {
        "location": "Shantou/Swatow",
        "airport": "SWA"
    },
    "CJA": {
        "location": "Cajamarca",
        "airport": "CJA"
    },
    "LAS": {
        "location": "Las Vegas",
        "airport": "LAS"
    },
    "SHJ": {
        "location": "Sharjah",
        "airport": "SHJ"
    },
    "CJC": {
        "location": "Calama",
        "airport": "CJC"
    },
    "VGT": {
        "location": "Terminal",
        "airport": "VGT"
    },
    "SYA": {
        "location": "Shemya Islands",
        "airport": "SYA"
    },
    "CCU": {
        "location": "Calcutta",
        "airport": "CCU"
    },
    "LST": {
        "location": "Launceston",
        "airport": "LST"
    },
    "SHE": {
        "location": "Shenyang",
        "airport": "SHE"
    },
    "YYC": {
        "location": "Calgary",
        "airport": "YYC"
    },
    "LAW": {
        "location": "Lawton",
        "airport": "LAW"
    },
    "SZX": {
        "location": "Shenzhen",
        "airport": "SZX"
    },
    "CLO": {
        "location": "Cali",
        "airport": "CLO"
    },
    "LEH": {
        "location": "Le Havre",
        "airport": "LEH"
    },
    "LWK": {
        "location": "Lerwick / Tingwall",
        "airport": "LWK"
    },
    "CCJ": {
        "location": "Calicut",
        "airport": "CCJ"
    },
    "LBA": {
        "location": "Leeds",
        "airport": "LBA"
    },
    "SCS": {
        "location": "Scatsta",
        "airport": "SCS"
    },
    "CLY": {
        "location": "Calvi",
        "airport": "CLY"
    },
    "LER": {
        "location": "Leinster",
        "airport": "LER"
    },
    "LSI": {
        "location": "Sumuburgh",
        "airport": "LSI"
    },
    "YCB": {
        "location": "Cambridge Bay",
        "airport": "YCB"
    },
    "LEJ": {
        "location": "Leipzig",
        "airport": "LEJ"
    },
    "SJW": {
        "location": "Shijiazhuang",
        "airport": "SJW"
    },
    "CGR": {
        "location": "Campo Grande",
        "airport": "CGR"
    },
    "YQL": {
        "location": "Lethbridge",
        "airport": "YQL"
    },
    "SYZ": {
        "location": "Shiraz",
        "airport": "SYZ"
    },
    "CAJ": {
        "location": "Canaima",
        "airport": "CAJ"
    },
    "LXA": {
        "location": "Lhasa",
        "airport": "LXA"
    },
    "SHV": {
        "location": "Shreveport",
        "airport": "SHV"
    },
    "CUN": {
        "location": "Cancun",
        "airport": "CUN"
    },
    "LBV": {
        "location": "Libreville",
        "airport": "LBV"
    },
    "SBW": {
        "location": "Sibu",
        "airport": "SBW"
    },
    "CGI": {
        "location": "Cape Girardeau",
        "airport": "CGI"
    },
    "LGG": {
        "location": "Liege",
        "airport": "LGG"
    },
    "SIP": {
        "location": "Simferopol",
        "airport": "SIP"
    },
    "CPT": {
        "location": "Cape Town",
        "airport": "CPT"
    },
    "LIL": {
        "location": "Lille",
        "airport": "LIL"
    },
    "SIN": {
        "location": "Singapore",
        "airport": "SIN"
    },
    "CCS": {
        "location": "Caracas",
        "airport": "CCS"
    },
    "LLW": {
        "location": "Lilongwe",
        "airport": "LLW"
    },
    "QPG": {
        "location": "Singapore Paya Lebar",
        "airport": "QPG"
    },
    "CWL": {
        "location": "Cardiff",
        "airport": "CWL"
    },
    "LIM": {
        "location": "Lima",
        "airport": "LIM"
    },
    "XSP": {
        "location": "Singapore Seletar",
        "airport": "XSP"
    },
    "CNM": {
        "location": "Carlsbad",
        "airport": "CNM"
    },
    "LIG": {
        "location": "Limoges",
        "airport": "LIG"
    },
    "FSD": {
        "location": "Sioux Falls",
        "airport": "FSD"
    },
    "CTG": {
        "location": "Cartagena",
        "airport": "CTG"
    },
    "LNK": {
        "location": "Lincoln",
        "airport": "LNK"
    },
    "SIT": {
        "location": "Sitka",
        "airport": "SIT"
    },
    "CUP": {
        "location": "Carupano",
        "airport": "CUP"
    },
    "LNZ": {
        "location": "Linz",
        "airport": "LNZ"
    },
    "SLQ": {
        "location": "Sleetmute",
        "airport": "SLQ"
    },
    "AAA": {
        "location": "Casablanca",
        "airport": "AAA"
    },
    "LIS": {
        "location": "Lisbon",
        "airport": "LIS"
    },
    "SOF": {
        "location": "Sofia",
        "airport": "SOF"
    },
    "CAS": {
        "location": "Casablanca Anfa",
        "airport": "CAS"
    },
    "LIT": {
        "location": "Little Rock",
        "airport": "LIT"
    },
    "SKO": {
        "location": "Sokoto",
        "airport": "SKO"
    },
    "CMN": {
        "location": "Mohamed V",
        "airport": "CMN"
    },
    "LPL": {
        "location": "Liverpool",
        "airport": "LPL"
    },
    "SXW": {
        "location": "Soldotna",
        "airport": "SXW"
    },
    "CPR": {
        "location": "Casper",
        "airport": "CPR"
    },
    "LVI": {
        "location": "Livingstone",
        "airport": "LVI"
    },
    "SGD": {
        "location": "Sonderborg",
        "airport": "SGD"
    },
    "CTA": {
        "location": "Catania",
        "airport": "CTA"
    },
    "LJU": {
        "location": "Ljubljana",
        "airport": "LJU"
    },
    "SFJ": {
        "location": "Sondre Stromfjord",
        "airport": "SFJ"
    },
    "CAY": {
        "location": "Cayenne",
        "airport": "CAY"
    },
    "LOB": {
        "location": "Lobito",
        "airport": "LOB"
    },
    "SBN": {
        "location": "South Bend",
        "airport": "SBN"
    },
    "CEB": {
        "location": "Cebu",
        "airport": "CEB"
    },
    "LFW": {
        "location": "Lome",
        "airport": "LFW"
    },
    "SGF": {
        "location": "Springfield",
        "airport": "SGF"
    },
    "CDC": {
        "location": "Cedar City",
        "airport": "CDC"
    },
    "LON": {
        "location": "London",
        "airport": "LON"
    },
    "SPI": {
        "location": "Springfield",
        "airport": "SPI"
    },
    "CID": {
        "location": "City",
        "airport": "CID"
    },
    "RUN": {
        "location": "St. Denis de La Reunion",
        "airport": "RUN"
    },
    "CHH": {
        "location": "Chachapoyas",
        "airport": "CHH"
    },
    "LCY": {
        "location": "London City Airport",
        "airport": "LCY"
    },
    "SGU": {
        "location": "St. George",
        "airport": "SGU"
    },
    "CIK": {
        "location": "Chalkyits",
        "airport": "CIK"
    },
    "LGW": {
        "location": "London Gatwick",
        "airport": "LGW"
    },
    "STG": {
        "location": "St. George Island",
        "airport": "STG"
    },
    "CMI": {
        "location": "Champaign",
        "airport": "CMI"
    },
    "LHR": {
        "location": "London Heathrow",
        "airport": "LHR"
    },
    "YYT": {
        "location": "St. Johns",
        "airport": "YYT"
    },
    "CGQ": {
        "location": "Changchun",
        "airport": "CGQ"
    },
    "ETN": {
        "location": "London Luton",
        "airport": "ETN"
    },
    "SKB": {
        "location": "St. Kitts",
        "airport": "SKB"
    },
    "CSX": {
        "location": "Changsha",
        "airport": "CSX"
    },
    "STN": {
        "location": "London Stansted",
        "airport": "STN"
    },
    "STL": {
        "location": "St. Louis",
        "airport": "STL"
    },
    "CHS": {
        "location": "Charleston",
        "airport": "CHS"
    },
    "LGB": {
        "location": "Long Beach",
        "airport": "LGB"
    },
    "SLU": {
        "location": "St. Lucia",
        "airport": "SLU"
    },
    "CLT": {
        "location": "Charlotte",
        "airport": "CLT"
    },
    "LTO": {
        "location": "Loreto",
        "airport": "LTO"
    },
    "UVF": {
        "location": "St. Lucia Hewanorra",
        "airport": "UVF"
    },
    "CHA": {
        "location": "Chattanooga",
        "airport": "CHA"
    },
    "LAX": {
        "location": "Los Angeles",
        "airport": "LAX"
    },
    "SXM": {
        "location": "St. Maarten",
        "airport": "SXM"
    },
    "CYF": {
        "location": "Chefornak",
        "airport": "CYF"
    },
    "KSM": {
        "location": "St. Mary\u2019s",
        "airport": "KSM"
    },
    "CJU": {
        "location": "Cheju",
        "airport": "CJU"
    },
    "LMM": {
        "location": "Los Mochis",
        "airport": "LMM"
    },
    "LED": {
        "location": "St. Petersburg",
        "airport": "LED"
    },
    "CTU": {
        "location": "Chengdu",
        "airport": "CTU"
    },
    "SDF": {
        "location": "Louisville",
        "airport": "SDF"
    },
    "STT": {
        "location": "St. Thomas",
        "airport": "STT"
    },
    "CTM": {
        "location": "Chetumal",
        "airport": "CTM"
    },
    "LDE": {
        "location": "Lourdes/Tarbes",
        "airport": "LDE"
    },
    "SVD": {
        "location": "St. Vincent",
        "airport": "SVD"
    },
    "VAK": {
        "location": "Chevak",
        "airport": "VAK"
    },
    "LAD": {
        "location": "Luanda",
        "airport": "LAD"
    },
    "HUX": {
        "location": "Sta Cruz Huat",
        "airport": "HUX"
    },
    "CNX": {
        "location": "Chiang Mai",
        "airport": "CNX"
    },
    "LBB": {
        "location": "Lubbock",
        "airport": "LBB"
    },
    "SVG": {
        "location": "Stavanger",
        "airport": "SVG"
    },
    "CHI": {
        "location": "Chicago",
        "airport": "CHI"
    },
    "FBM": {
        "location": "Lubumbashi",
        "airport": "FBM"
    },
    "SBS": {
        "location": "Steamboat Spring",
        "airport": "SBS"
    },
    "CGX": {
        "location": "Meigs",
        "airport": "CGX"
    },
    "LKO": {
        "location": "Lucknow",
        "airport": "LKO"
    },
    "SVS": {
        "location": "Stevens Village",
        "airport": "SVS"
    },
    "MDW": {
        "location": "Chicago Midway",
        "airport": "MDW"
    },
    "LUD": {
        "location": "Ludwigshafen",
        "airport": "LUD"
    },
    "STO": {
        "location": "Stockholm",
        "airport": "STO"
    },
    "ORD": {
        "location": "Chicago O\u2019Hare",
        "airport": "ORD"
    },
    "LUG": {
        "location": "Lugano",
        "airport": "LUG"
    },
    "ARN": {
        "location": "Stockholm Arlanda",
        "airport": "ARN"
    },
    "CZA": {
        "location": "Chichenitza",
        "airport": "CZA"
    },
    "LLA": {
        "location": "Lulea",
        "airport": "LLA"
    },
    "BMA": {
        "location": "Stockholm Bromma",
        "airport": "BMA"
    },
    "CIX": {
        "location": "Chiclayo",
        "airport": "CIX"
    },
    "LUB": {
        "location": "Lumid Pau",
        "airport": "LUB"
    },
    "SCK": {
        "location": "Stockton",
        "airport": "SCK"
    },
    "CIC": {
        "location": "Chico",
        "airport": "CIC"
    },
    "LUN": {
        "location": "Lusaka",
        "airport": "LUN"
    },
    "SRV": {
        "location": "Stony River",
        "airport": "SRV"
    },
    "KCL": {
        "location": "Chignik",
        "airport": "KCL"
    },
    "LUX": {
        "location": "Luxembourg",
        "airport": "LUX"
    },
    "SXB": {
        "location": "Strasbourg",
        "airport": "SXB"
    },
    "CUU": {
        "location": "Chihuahua",
        "airport": "CUU"
    },
    "LXR": {
        "location": "Luxor",
        "airport": "LXR"
    },
    "STR": {
        "location": "Stuttgart",
        "airport": "STR"
    },
    "HIB": {
        "location": "Chisholm",
        "airport": "HIB"
    },
    "LYS": {
        "location": "Lyon",
        "airport": "LYS"
    },
    "YSB": {
        "location": "Sudbury",
        "airport": "YSB"
    },
    "CGP": {
        "location": "Chittagong",
        "airport": "CGP"
    },
    "MST": {
        "location": "Maastricht",
        "airport": "MST"
    },
    "SUI": {
        "location": "Sukhumi",
        "airport": "SUI"
    },
    "CKG": {
        "location": "Chongqing",
        "airport": "CKG"
    },
    "MCN": {
        "location": "Macon",
        "airport": "MCN"
    },
    "SDL": {
        "location": "Sundsvall",
        "airport": "SDL"
    },
    "CHC": {
        "location": "Christchurch",
        "airport": "CHC"
    },
    "MSN": {
        "location": "Madison",
        "airport": "MSN"
    },
    "SUB": {
        "location": "Surabaya",
        "airport": "SUB"
    },
    "CHU": {
        "location": "Chuathbaluk",
        "airport": "CHU"
    },
    "MAA": {
        "location": "Madras",
        "airport": "MAA"
    },
    "SUV": {
        "location": "Suva",
        "airport": "SUV"
    },
    "CVG": {
        "location": "Cincinnati",
        "airport": "CVG"
    },
    "MAD": {
        "location": "Madrid",
        "airport": "MAD"
    },
    "SVX": {
        "location": "Sverdlovsk Ekaterinburg",
        "airport": "SVX"
    },
    "CME": {
        "location": "Ciudad Del Carmen",
        "airport": "CME"
    },
    "GDX": {
        "location": "Magadan",
        "airport": "GDX"
    },
    "SYD": {
        "location": "Sydney",
        "airport": "SYD"
    },
    "CLE": {
        "location": "Cleveland",
        "airport": "CLE"
    },
    "SEZ": {
        "location": "Mahe Island",
        "airport": "SEZ"
    },
    "SYR": {
        "location": "Syracuse",
        "airport": "SYR"
    },
    "BKL": {
        "location": "Lakefront",
        "airport": "BKL"
    },
    "MIU": {
        "location": "Maiduguri",
        "airport": "MIU"
    },
    "TBZ": {
        "location": "Tabriz",
        "airport": "TBZ"
    },
    "CBB": {
        "location": "Cochabamba",
        "airport": "CBB"
    },
    "MAJ": {
        "location": "Majuro",
        "airport": "MAJ"
    },
    "TUU": {
        "location": "Tabuk",
        "airport": "TUU"
    },
    "COK": {
        "location": "Cochin",
        "airport": "COK"
    },
    "AGP": {
        "location": "Malaga",
        "airport": "AGP"
    },
    "TCQ": {
        "location": "Tacna",
        "airport": "TCQ"
    },
    "COE": {
        "location": "Coeur D\u2019Alene",
        "airport": "COE"
    },
    "MLE": {
        "location": "Male",
        "airport": "MLE"
    },
    "TAE": {
        "location": "Taegu Korea",
        "airport": "TAE"
    },
    "CDB": {
        "location": "Cold Bay",
        "airport": "CDB"
    },
    "MMA": {
        "location": "Malmo",
        "airport": "MMA"
    },
    "TXG": {
        "location": "Taichung",
        "airport": "TXG"
    },
    "CLQ": {
        "location": "Colima",
        "airport": "CLQ"
    },
    "MAL": {
        "location": "Malongo",
        "airport": "MAL"
    },
    "TIF": {
        "location": "Taif",
        "airport": "TIF"
    },
    "CLL": {
        "location": "College Station",
        "airport": "CLL"
    },
    "TPE": {
        "location": "Malta MLA Taipei",
        "airport": "TPE"
    },
    "CGN": {
        "location": "Cologne",
        "airport": "CGN"
    },
    "MDC": {
        "location": "Manado",
        "airport": "MDC"
    },
    "TSA": {
        "location": "Taipei Shung Shan",
        "airport": "TSA"
    },
    "CMB": {
        "location": "Colombo",
        "airport": "CMB"
    },
    "MGA": {
        "location": "Managua",
        "airport": "MGA"
    },
    "TYN": {
        "location": "Taiyuan",
        "airport": "TYN"
    },
    "COS": {
        "location": "Colorado Springs",
        "airport": "COS"
    },
    "MAO": {
        "location": "Manaus",
        "airport": "MAO"
    },
    "TAK": {
        "location": "Takamatsu",
        "airport": "TAK"
    },
    "CAE": {
        "location": "Columbia",
        "airport": "CAE"
    },
    "MAN": {
        "location": "Manchester",
        "airport": "MAN"
    },
    "TYL": {
        "location": "Talara",
        "airport": "TYL"
    },
    "COU": {
        "location": "Columbia",
        "airport": "COU"
    },
    "MHT": {
        "location": "Manchester",
        "airport": "MHT"
    },
    "TLH": {
        "location": "Tallahassee",
        "airport": "TLH"
    },
    "CMH": {
        "location": "Columbus",
        "airport": "CMH"
    },
    "MNL": {
        "location": "Manila",
        "airport": "MNL"
    },
    "TLL": {
        "location": "Tallinn",
        "airport": "TLL"
    },
    "CSG": {
        "location": "Columbus",
        "airport": "CSG"
    },
    "ZLO": {
        "location": "Manzanillo",
        "airport": "ZLO"
    },
    "TMR": {
        "location": "Tamanrasset",
        "airport": "TMR"
    },
    "UBS": {
        "location": "Columbus",
        "airport": "UBS"
    },
    "MPM": {
        "location": "Maputo",
        "airport": "MPM"
    },
    "TPA": {
        "location": "Tampa",
        "airport": "TPA"
    },
    "CKY": {
        "location": "Conakry",
        "airport": "CKY"
    },
    "MAR": {
        "location": "Maracaibo",
        "airport": "MAR"
    },
    "TMP": {
        "location": "Tampere",
        "airport": "TMP"
    },
    "CCP": {
        "location": "Concepcion",
        "airport": "CCP"
    },
    "MBX": {
        "location": "Maribor",
        "airport": "MBX"
    },
    "TAL": {
        "location": "Tanana",
        "airport": "TAL"
    },
    "CPH": {
        "location": "Copenhagen",
        "airport": "CPH"
    },
    "PKB": {
        "location": "Marietta Parkersburg",
        "airport": "PKB"
    },
    "TNG": {
        "location": "Tangier",
        "airport": "TNG"
    },
    "RKE": {
        "location": "Roskilde",
        "airport": "RKE"
    },
    "MWA": {
        "location": "Marion",
        "airport": "MWA"
    },
    "TPP": {
        "location": "Tarapoto",
        "airport": "TPP"
    },
    "CPO": {
        "location": "Copiapo",
        "airport": "CPO"
    },
    "MQT": {
        "location": "Marquette",
        "airport": "MQT"
    },
    "TAS": {
        "location": "Tashkent",
        "airport": "TAS"
    },
    "CDV": {
        "location": "Cordova",
        "airport": "CDV"
    },
    "RAK": {
        "location": "Marrakech",
        "airport": "RAK"
    },
    "TWU": {
        "location": "Tawau",
        "airport": "TWU"
    },
    "ORK": {
        "location": "Cork",
        "airport": "ORK"
    },
    "MRS": {
        "location": "Marseille",
        "airport": "MRS"
    },
    "MME": {
        "location": "Teesside",
        "airport": "MME"
    },
    "ELM": {
        "location": "Corning Elmira",
        "airport": "ELM"
    },
    "MLL": {
        "location": "Marshall",
        "airport": "MLL"
    },
    "TGU": {
        "location": "Tegucigalpa",
        "airport": "TGU"
    },
    "CZE": {
        "location": "Coro",
        "airport": "CZE"
    },
    "MVY": {
        "location": "Martha\u2019s Vineyard",
        "airport": "MVY"
    },
    "THR": {
        "location": "Tehran",
        "airport": "THR"
    },
    "CRP": {
        "location": "Corpus Christie",
        "airport": "CRP"
    },
    "MHD": {
        "location": "Mashad",
        "airport": "MHD"
    },
    "SDV": {
        "location": "Tel Aviv Yafo Sde Dov",
        "airport": "SDV"
    },
    "NGW": {
        "location": "Cabaniss Field",
        "airport": "NGW"
    },
    "MAM": {
        "location": "Matamoros",
        "airport": "MAM"
    },
    "TLV": {
        "location": "Tel Aviv Yafo Tel Aviv",
        "airport": "TLV"
    },
    "CUX": {
        "location": "Cuddihy Field",
        "airport": "CUX"
    },
    "MYJ": {
        "location": "Matsuyama",
        "airport": "MYJ"
    },
    "ZCO": {
        "location": "Temuco",
        "airport": "ZCO"
    },
    "COO": {
        "location": "Cotonou",
        "airport": "COO"
    },
    "MUN": {
        "location": "Maturin",
        "airport": "MUN"
    },
    "TCI": {
        "location": "Tenerife",
        "airport": "TCI"
    },
    "GXQ": {
        "location": "Coyhaique",
        "airport": "GXQ"
    },
    "MRU": {
        "location": "Mauritius",
        "airport": "MRU"
    },
    "TFN": {
        "location": "Rodeos",
        "airport": "TFN"
    },
    "CZM": {
        "location": "Cozumel",
        "airport": "CZM"
    },
    "MAZ": {
        "location": "Mayaguez",
        "airport": "MAZ"
    },
    "TFS": {
        "location": "Sofia",
        "airport": "TFS"
    },
    "CKD": {
        "location": "Crokked Creek",
        "airport": "CKD"
    },
    "MZT": {
        "location": "Mazatlan",
        "airport": "MZT"
    },
    "TER": {
        "location": "Terceira",
        "airport": "TER"
    },
    "CZS": {
        "location": "Cruzeiro Do Sul",
        "airport": "CZS"
    },
    "MDK": {
        "location": " Mbandaka",
        "airport": "MDK"
    },
    "YXT": {
        "location": " Terrace",
        "airport": "YXT"
    },
    "CUE": {
        "location": "Cuenca",
        "airport": "CUE"
    },
    "MJM": {
        "location": "Mbuji Mayi",
        "airport": "MJM"
    },
    "TXK": {
        "location": "Texarkana",
        "airport": "TXK"
    },
    "CGB": {
        "location": "Cuiaba",
        "airport": "CGB"
    },
    "MFE": {
        "location": "McAllen",
        "airport": "MFE"
    },
    "SKG": {
        "location": "Thessaloniki",
        "airport": "SKG"
    },
    "CPX": {
        "location": "Culebra",
        "airport": "CPX"
    },
    "MCG": {
        "location": "McGrath",
        "airport": "MCG"
    },
    "YQT": {
        "location": "Thunder Bay",
        "airport": "YQT"
    },
    "CUL": {
        "location": "Culiacan",
        "airport": "CUL"
    },
    "MES": {
        "location": "Medan",
        "airport": "MES"
    },
    "TSN": {
        "location": "Tianjin",
        "airport": "TSN"
    },
    "CUM": {
        "location": "Cumana",
        "airport": "CUM"
    },
    "MDE": {
        "location": "Medellin",
        "airport": "MDE"
    },
    "TIJ": {
        "location": "Tijuana",
        "airport": "TIJ"
    },
    "CUR": {
        "location": "Curacao",
        "airport": "CUR"
    },
    "MFR": {
        "location": "Medford",
        "airport": "MFR"
    },
    "TSR": {
        "location": "Timisoara",
        "airport": "TSR"
    },
    "CWB": {
        "location": "Curitiba",
        "airport": "CWB"
    },
    "MED": {
        "location": "Medina",
        "airport": "MED"
    },
    "TGI": {
        "location": "Tingo Maria",
        "airport": "TGI"
    },
    "CUZ": {
        "location": "Cusco",
        "airport": "CUZ"
    },
    "MKR": {
        "location": "Meekatharp",
        "airport": "MKR"
    },
    "TAB": {
        "location": "Tobago",
        "airport": "TAB"
    },
    "DKR": {
        "location": "Dakar",
        "airport": "DKR"
    },
    "MYU": {
        "location": "Mekoryuk",
        "airport": "MYU"
    },
    "OOK": {
        "location": "Toksook Bay",
        "airport": "OOK"
    },
    "DLM": {
        "location": "Dalaman",
        "airport": "DLM"
    },
    "MEL": {
        "location": "Melbourne",
        "airport": "MEL"
    },
    "TKS": {
        "location": "Tokushima",
        "airport": "TKS"
    },
    "DLC": {
        "location": "Dalian",
        "airport": "DLC"
    },
    "MLB": {
        "location": "Melbourne",
        "airport": "MLB"
    },
    "TYO": {
        "location": "Tokyo",
        "airport": "TYO"
    },
    "DAL": {
        "location": "Dallas Love Field",
        "airport": "DAL"
    },
    "KAH": {
        "location": "Heliport",
        "airport": "KAH"
    },
    "HND": {
        "location": "Tokyo Haneda",
        "airport": "HND"
    },
    "DFW": {
        "location": "Fort Worth",
        "airport": "DFW"
    },
    "MEB": {
        "location": "Melbourne Essendon",
        "airport": "MEB"
    },
    "NRT": {
        "location": "Tokyo Narita Airport",
        "airport": "NRT"
    },
    "DAM": {
        "location": "Damascus",
        "airport": "DAM"
    },
    "MEM": {
        "location": "Memphis",
        "airport": "MEM"
    },
    "TOL": {
        "location": "Toledo",
        "airport": "TOL"
    },
    "DNV": {
        "location": "Danville",
        "airport": "DNV"
    },
    "MDZ": {
        "location": "Mendoza",
        "airport": "MDZ"
    },
    "TBU": {
        "location": "Tongatapu",
        "airport": "TBU"
    },
    "DAR": {
        "location": "Dar Es Salaam",
        "airport": "DAR"
    },
    "MID": {
        "location": "Merida",
        "airport": "MID"
    },
    "TOP": {
        "location": "Topeka",
        "airport": "TOP"
    },
    "DRW": {
        "location": "Darwin",
        "airport": "DRW"
    },
    "MRD": {
        "location": "Merida",
        "airport": "MRD"
    },
    "YTO": {
        "location": "Toronto",
        "airport": "YTO"
    },
    "DVO": {
        "location": "Davao",
        "airport": "DVO"
    },
    "MEI": {
        "location": "Meridian",
        "airport": "MEI"
    },
    "YYZ": {
        "location": "Toronto",
        "airport": "YYZ"
    },
    "DAY": {
        "location": "Dayton",
        "airport": "DAY"
    },
    "MEX": {
        "location": "Mexico City",
        "airport": "MEX"
    },
    "YTZ": {
        "location": "Toronto Island",
        "airport": "YTZ"
    },
    "DAB": {
        "location": "Daytona Beach",
        "airport": "DAB"
    },
    "MIA": {
        "location": "Miami",
        "airport": "MIA"
    },
    "TRC": {
        "location": "Torreon",
        "airport": "TRC"
    },
    "DEC": {
        "location": "Decatur",
        "airport": "DEC"
    },
    "JDM": {
        "location": "Heliport",
        "airport": "JDM"
    },
    "TTJ": {
        "location": "Tottori",
        "airport": "TTJ"
    },
    "YDF": {
        "location": "Deer Lake",
        "airport": "YDF"
    },
    "MPB": {
        "location": "Base",
        "airport": "MPB"
    },
    "TLN": {
        "location": "Toulon/Hyeres",
        "airport": "TLN"
    },
    "DEL": {
        "location": "Delhi",
        "airport": "DEL"
    },
    "MAF": {
        "location": "Midland",
        "airport": "MAF"
    },
    "TLS": {
        "location": "Toulouse",
        "airport": "TLS"
    },
    "DTA": {
        "location": "Delta",
        "airport": "DTA"
    },
    "MIL": {
        "location": "Milan",
        "airport": "MIL"
    },
    "TOY": {
        "location": "Toyama",
        "airport": "TOY"
    },
    "DEN": {
        "location": "Denver",
        "airport": "DEN"
    },
    "LIN": {
        "location": "Milan Linate",
        "airport": "LIN"
    },
    "TVC": {
        "location": "Traverse City",
        "airport": "TVC"
    },
    "DSM": {
        "location": "Des Moines",
        "airport": "DSM"
    },
    "MXP": {
        "location": "Milan Malpensa",
        "airport": "MXP"
    },
    "TTN": {
        "location": "Trenton",
        "airport": "TTN"
    },
    "DTT": {
        "location": "Detroit",
        "airport": "DTT"
    },
    "BGY": {
        "location": "Milan Orio al Serio",
        "airport": "BGY"
    },
    "TRI": {
        "location": "Tri-City",
        "airport": "TRI"
    },
    "DTW": {
        "location": "Detroit",
        "airport": "DTW"
    },
    "SWK": {
        "location": "Milan Segrate",
        "airport": "SWK"
    },
    "TRS": {
        "location": "Trieste",
        "airport": "TRS"
    },
    "MLF": {
        "location": "Milford",
        "airport": "MLF"
    },
    "TIP": {
        "location": "Tripoli",
        "airport": "TIP"
    },
    "DET": {
        "location": "Detroit City",
        "airport": "DET"
    },
    "MKE": {
        "location": "Milwaukee",
        "airport": "MKE"
    },
    "TRV": {
        "location": "Trivandrum",
        "airport": "TRV"
    },
    "MTT": {
        "location": "Minatitlan",
        "airport": "MTT"
    },
    "TMT": {
        "location": "Trombetas",
        "airport": "TMT"
    },
    "YIP": {
        "location": "Detroit Willow Run",
        "airport": "YIP"
    },
    "MRV": {
        "location": "Mineralnye",
        "airport": "MRV"
    },
    "TOS": {
        "location": "Tromso",
        "airport": "TOS"
    },
    "MSP": {
        "location": "Minneapolis",
        "airport": "MSP"
    },
    "TRD": {
        "location": "Trondheim",
        "airport": "TRD"
    },
    "DHA": {
        "location": "Dhahran",
        "airport": "DHA"
    },
    "MOT": {
        "location": "Minot",
        "airport": "MOT"
    },
    "TRU": {
        "location": "Trujillo",
        "airport": "TRU"
    },
    "MSQ": {
        "location": "Minsk",
        "airport": "MSQ"
    },
    "TKK": {
        "location": "Truk",
        "airport": "TKK"
    },
    "DAC": {
        "location": "Dhaka",
        "airport": "DAC"
    },
    "MYY": {
        "location": "Miri",
        "airport": "MYY"
    },
    "TUS": {
        "location": "Tucson",
        "airport": "TUS"
    },
    "DLG": {
        "location": "Dillingham",
        "airport": "DLG"
    },
    "MSO": {
        "location": "Missoula",
        "airport": "MSO"
    },
    "TUL": {
        "location": "Tulsa",
        "airport": "TUL"
    },
    "DJE": {
        "location": "Djerba",
        "airport": "DJE"
    },
    "KMI": {
        "location": "Miyazaki",
        "airport": "KMI"
    },
    "TLT": {
        "location": "Tuluksak",
        "airport": "TLT"
    },
    "JIB": {
        "location": "Djibouti",
        "airport": "JIB"
    },
    "MOB": {
        "location": "Mobile",
        "airport": "MOB"
    },
    "TBP": {
        "location": "Tumbes",
        "airport": "TBP"
    },
    "DOH": {
        "location": "Doha",
        "airport": "DOH"
    },
    "MLI": {
        "location": "Moline",
        "airport": "MLI"
    },
    "TUN": {
        "location": "Tunis",
        "airport": "TUN"
    },
    "DCF": {
        "location": "Dominica Cane Field",
        "airport": "DCF"
    },
    "MBA": {
        "location": "Mombasa",
        "airport": "MBA"
    },
    "WTL": {
        "location": "Tuntutulia",
        "airport": "WTL"
    },
    "DOM": {
        "location": "Hall",
        "airport": "DOM"
    },
    "YQM": {
        "location": "Moncton",
        "airport": "YQM"
    },
    "TNK": {
        "location": "Tununak",
        "airport": "TNK"
    },
    "DHN": {
        "location": "Dothan",
        "airport": "DHN"
    },
    "MLU": {
        "location": "Monroe",
        "airport": "MLU"
    },
    "TRN": {
        "location": "Turin",
        "airport": "TRN"
    },
    "DLA": {
        "location": "Douala",
        "airport": "DLA"
    },
    "MLW": {
        "location": "Monrovia",
        "airport": "MLW"
    },
    "TKU": {
        "location": "Turku",
        "airport": "TKU"
    },
    "DRS": {
        "location": "Dresden",
        "airport": "DRS"
    },
    "ROB": {
        "location": "International",
        "airport": "ROB"
    },
    "TCL": {
        "location": "Tuscaloosa",
        "airport": "TCL"
    },
    "DXB": {
        "location": "Dubai",
        "airport": "DXB"
    },
    "MBJ": {
        "location": "Montego Bay",
        "airport": "MBJ"
    },
    "TGZ": {
        "location": "Tuxtla Gutierrez",
        "airport": "TGZ"
    },
    "DUB": {
        "location": "Dublin",
        "airport": "DUB"
    },
    "MTY": {
        "location": "Monterrey",
        "airport": "MTY"
    },
    "TWF": {
        "location": "Twin Falls",
        "airport": "TWF"
    },
    "DLH": {
        "location": "Duluth",
        "airport": "DLH"
    },
    "MVD": {
        "location": "Montevideo",
        "airport": "MVD"
    },
    "TYR": {
        "location": "Tyler",
        "airport": "TYR"
    },
    "DGO": {
        "location": "Durango",
        "airport": "DGO"
    },
    "MGM": {
        "location": "Montgomery",
        "airport": "MGM"
    },
    "UBJ": {
        "location": "Ube",
        "airport": "UBJ"
    },
    "DRO": {
        "location": "Durango",
        "airport": "DRO"
    },
    "MPL": {
        "location": "Montpellier",
        "airport": "MPL"
    },
    "UKI": {
        "location": "Ukiah",
        "airport": "UKI"
    },
    "DUR": {
        "location": "Durban",
        "airport": "DUR"
    },
    "YMQ": {
        "location": "Montreal",
        "airport": "YMQ"
    },
    "ULN": {
        "location": "Ulan Bator",
        "airport": "ULN"
    },
    "DUS": {
        "location": "Dusseldorf",
        "airport": "DUS"
    },
    "YUL": {
        "location": "International",
        "airport": "YUL"
    },
    "UME": {
        "location": "Umea",
        "airport": "UME"
    },
    "DUT": {
        "location": "Dutch Harbor",
        "airport": "DUT"
    },
    "YMX": {
        "location": "International",
        "airport": "YMX"
    },
    "UNK": {
        "location": "Unalakleet",
        "airport": "UNK"
    },
    "ELS": {
        "location": "East London",
        "airport": "ELS"
    },
    "MLM": {
        "location": "Morelia",
        "airport": "MLM"
    },
    "URC": {
        "location": "Urumqi",
        "airport": "URC"
    },
    "EMA": {
        "location": "East Midlands",
        "airport": "EMA"
    },
    "YVA": {
        "location": "Moroni",
        "airport": "YVA"
    },
    "VAA": {
        "location": "Vaasa",
        "airport": "VAA"
    },
    "IPC": {
        "location": "Easter Island",
        "airport": "IPC"
    },
    "HAH": {
        "location": "International",
        "airport": "HAH"
    },
    "YWK": {
        "location": "Wabush",
        "airport": "YWK"
    },
    "EDI": {
        "location": "Edinburgh",
        "airport": "EDI"
    },
    "MOW": {
        "location": "Moscow",
        "airport": "MOW"
    },
    "ACT": {
        "location": "Waco",
        "airport": "ACT"
    },
    "YEA": {
        "location": "Edmonton",
        "airport": "YEA"
    },
    "DME": {
        "location": "Domodedovo",
        "airport": "DME"
    },
    "VLD": {
        "location": "Valdosta",
        "airport": "VLD"
    },
    "YEG": {
        "location": "Edmonton Albert Int\u2019l",
        "airport": "YEG"
    },
    "SVO": {
        "location": "Sheremetyevo",
        "airport": "SVO"
    },
    "VLC": {
        "location": "Valencia",
        "airport": "VLC"
    },
    "YXD": {
        "location": "Edmonton Municipal",
        "airport": "YXD"
    },
    "VKO": {
        "location": "Moscow Vnukovo",
        "airport": "VKO"
    },
    "VLN": {
        "location": "Valencia",
        "airport": "VLN"
    },
    "YED": {
        "location": "Field",
        "airport": "YED"
    },
    "HGU": {
        "location": "Mount Hagen",
        "airport": "HGU"
    },
    "VLV": {
        "location": "Valera",
        "airport": "VLV"
    },
    "EEK": {
        "location": "Eek",
        "airport": "EEK"
    },
    "FMO": {
        "location": "Muenster",
        "airport": "FMO"
    },
    "VLL": {
        "location": "Valladolid",
        "airport": "VLL"
    },
    "VPS": {
        "location": "Eglin Afb/Valparaiso",
        "airport": "VPS"
    },
    "MLH": {
        "location": "Mulhouse",
        "airport": "MLH"
    },
    "YVR": {
        "location": "Vancouver",
        "airport": "YVR"
    },
    "EIN": {
        "location": "Eindhoven",
        "airport": "EIN"
    },
    "MUC": {
        "location": "Munich",
        "airport": "MUC"
    },
    "WAW": {
        "location": "Warsaw",
        "airport": "WAW"
    },
    "ELP": {
        "location": "El Paso",
        "airport": "ELP"
    },
    "MCT": {
        "location": "Muscat",
        "airport": "MCT"
    },
    "WAS": {
        "location": "Washington",
        "airport": "WAS"
    },
    "ESR": {
        "location": "El Salvador",
        "airport": "ESR"
    },
    "MKG": {
        "location": "Muskegon",
        "airport": "MKG"
    },
    "IAD": {
        "location": "International",
        "airport": "IAD"
    },
    "ETH": {
        "location": "Elat",
        "airport": "ETH"
    },
    "MYR": {
        "location": "Myrtle Beach",
        "airport": "MYR"
    },
    "DCA": {
        "location": "Washington National",
        "airport": "DCA"
    },
    "EKO": {
        "location": "Elko",
        "airport": "EKO"
    },
    "NDJ": {
        "location": "N\u2019djamena",
        "airport": "NDJ"
    },
    "VST": {
        "location": "Vasteras",
        "airport": "VST"
    },
    "ELY": {
        "location": "Ely",
        "airport": "ELY"
    },
    "NAN": {
        "location": "Nadi",
        "airport": "NAN"
    },
    "YQH": {
        "location": "Watson Lake",
        "airport": "YQH"
    },
    "ENS": {
        "location": "Enschede",
        "airport": "ENS"
    },
    "NGS": {
        "location": "Nagasaki",
        "airport": "NGS"
    },
    "AUW": {
        "location": "Wausau",
        "airport": "AUW"
    },
    "EBB": {
        "location": "Entebbe",
        "airport": "EBB"
    },
    "NGO": {
        "location": "Nagoya",
        "airport": "NGO"
    },
    "VXO": {
        "location": "Vaxjo",
        "airport": "VXO"
    },
    "ECN": {
        "location": "Ercan",
        "airport": "ECN"
    },
    "NBO": {
        "location": "Nairobi",
        "airport": "NBO"
    },
    "WLG": {
        "location": "Wellington",
        "airport": "WLG"
    },
    "EVN": {
        "location": "Erevan",
        "airport": "EVN"
    },
    "WIL": {
        "location": "Nairobi",
        "airport": "WIL"
    },
    "EAT": {
        "location": "Wenatchee",
        "airport": "EAT"
    },
    "ERF": {
        "location": "Erfurt",
        "airport": "ERF"
    },
    "KHN": {
        "location": "Nanchang",
        "airport": "KHN"
    },
    "VEE": {
        "location": "Venetie",
        "airport": "VEE"
    },
    "ERI": {
        "location": "Erie",
        "airport": "ERI"
    },
    "ENC": {
        "location": "Nancy",
        "airport": "ENC"
    },
    "VCE": {
        "location": "Venice",
        "airport": "VCE"
    },
    "EUG": {
        "location": "Eugene",
        "airport": "EUG"
    },
    "YSR": {
        "location": "Nanisivik",
        "airport": "YSR"
    },
    "TSF": {
        "location": "Venice Treviso",
        "airport": "TSF"
    },
    "EVV": {
        "location": "Evansville",
        "airport": "EVV"
    },
    "NKG": {
        "location": "Nanjing",
        "airport": "NKG"
    },
    "VER": {
        "location": "Veracruz",
        "airport": "VER"
    },
    "EVE": {
        "location": "Evenes",
        "airport": "EVE"
    },
    "NNG": {
        "location": "Nanning",
        "airport": "NNG"
    },
    "VEL": {
        "location": "Vernal",
        "airport": "VEL"
    },
    "EXT": {
        "location": "Exeter",
        "airport": "EXT"
    },
    "NTE": {
        "location": "Nantes",
        "airport": "NTE"
    },
    "VRN": {
        "location": "Verona",
        "airport": "VRN"
    },
    "FAI": {
        "location": "Fairbanks",
        "airport": "FAI"
    },
    "ACK": {
        "location": "Nantucket",
        "airport": "ACK"
    },
    "PBI": {
        "location": "West Palm Beach",
        "airport": "PBI"
    },
    "EWB": {
        "location": "Bedford",
        "airport": "EWB"
    },
    "WNA": {
        "location": "Napakiak",
        "airport": "WNA"
    },
    "HPN": {
        "location": "Westchester",
        "airport": "HPN"
    },
    "KFP": {
        "location": "False Pass",
        "airport": "KFP"
    },
    "PKA": {
        "location": "Napaskiak",
        "airport": "PKA"
    },
    "LEB": {
        "location": "White River",
        "airport": "LEB"
    },
    "FAR": {
        "location": "Fargo",
        "airport": "FAR"
    },
    "APF": {
        "location": "Naples",
        "airport": "APF"
    },
    "YXY": {
        "location": "Whitehorse",
        "airport": "YXY"
    },
    "FAO": {
        "location": "Faro",
        "airport": "FAO"
    },
    "NAP": {
        "location": "Naples",
        "airport": "NAP"
    },
    "ICT": {
        "location": "Wichita",
        "airport": "ICT"
    },
    "FAY": {
        "location": "Fayetteville",
        "airport": "FAY"
    },
    "BNA": {
        "location": "Nashville",
        "airport": "BNA"
    },
    "SPS": {
        "location": "Wichita Falls",
        "airport": "SPS"
    },
    "FYV": {
        "location": "Fayetteville",
        "airport": "FYV"
    },
    "NAS": {
        "location": "Nassau",
        "airport": "NAS"
    },
    "YYJ": {
        "location": "Victoria",
        "airport": "YYJ"
    },
    "FEZ": {
        "location": "Fez",
        "airport": "FEZ"
    },
    "NAT": {
        "location": "Natal",
        "airport": "NAT"
    },
    "VIE": {
        "location": "Vienna",
        "airport": "VIE"
    },
    "FIL": {
        "location": "Fillmore",
        "airport": "FIL"
    },
    "NEU": {
        "location": "Neuchatel",
        "airport": "NEU"
    },
    "VTE": {
        "location": "Vientiane",
        "airport": "VTE"
    },
    "FLG": {
        "location": "Flagstaff",
        "airport": "FLG"
    },
    "EWN": {
        "location": "New Bern",
        "airport": "EWN"
    },
    "VQS": {
        "location": "Vieques",
        "airport": "VQS"
    },
    "FNT": {
        "location": "Flint",
        "airport": "FNT"
    },
    "MSY": {
        "location": "New Orleans",
        "airport": "MSY"
    },
    "VSA": {
        "location": "Villahermosa",
        "airport": "VSA"
    },
    "FLR": {
        "location": "Florence",
        "airport": "FLR"
    },
    "NYC": {
        "location": "New York",
        "airport": "NYC"
    },
    "ILM": {
        "location": "Wilmington",
        "airport": "ILM"
    },
    "MSL": {
        "location": "Florence",
        "airport": "MSL"
    },
    "JFK": {
        "location": "Kennedy",
        "airport": "JFK"
    },
    "VNO": {
        "location": "Vilnius",
        "airport": "VNO"
    },
    "FRS": {
        "location": "Flores",
        "airport": "FRS"
    },
    "LGA": {
        "location": "New York La Guardia",
        "airport": "LGA"
    },
    "WDH": {
        "location": "Windhoek",
        "airport": "WDH"
    },
    "YVP": {
        "location": "Fort Chima",
        "airport": "YVP"
    },
    "EWR": {
        "location": "New York Newark",
        "airport": "EWR"
    },
    "ERS": {
        "location": "Windhoek Eros",
        "airport": "ERS"
    },
    "FMY": {
        "location": "Fort Myers",
        "airport": "FMY"
    },
    "SWF": {
        "location": "Newburgh",
        "airport": "SWF"
    },
    "YQG": {
        "location": "Windsor",
        "airport": "YQG"
    },
    "YYE": {
        "location": "Fort Nelson",
        "airport": "YYE"
    },
    "NCL": {
        "location": "Newcastle",
        "airport": "NCL"
    },
    "YWG": {
        "location": "Winnipeg",
        "airport": "YWG"
    },
    "YXJ": {
        "location": "Fort St. John",
        "airport": "YXJ"
    },
    "WWT": {
        "location": "Newtok",
        "airport": "WWT"
    },
    "VIT": {
        "location": "Vitoria",
        "airport": "VIT"
    },
    "FOR": {
        "location": "Fortaleza",
        "airport": "FOR"
    },
    "IAG": {
        "location": "Niagara Falls",
        "airport": "IAG"
    },
    "VVO": {
        "location": "Vladivostok",
        "airport": "VVO"
    },
    "FRA": {
        "location": "Frankfurt",
        "airport": "FRA"
    },
    "NIM": {
        "location": "Niamey",
        "airport": "NIM"
    },
    "WRG": {
        "location": "Wrangell",
        "airport": "WRG"
    },
    "YFC": {
        "location": "Fredericton",
        "airport": "YFC"
    },
    "NCE": {
        "location": "Nice",
        "airport": "NCE"
    },
    "WUH": {
        "location": "Wuhan",
        "airport": "WUH"
    },
    "FPO": {
        "location": "Freeport",
        "airport": "FPO"
    },
    "NME": {
        "location": "Nightmute",
        "airport": "NME"
    },
    "XMN": {
        "location": "Xiamen",
        "airport": "XMN"
    },
    "FNA": {
        "location": "Freetown",
        "airport": "FNA"
    },
    "KIJ": {
        "location": "Niigata",
        "airport": "KIJ"
    },
    "SIA": {
        "location": "Xian",
        "airport": "SIA"
    },
    "HGS": {
        "location": "Freetown Hastings",
        "airport": "HGS"
    },
    "FNI": {
        "location": "Nimes",
        "airport": "FNI"
    },
    "YKM": {
        "location": "Yakima",
        "airport": "YKM"
    },
    "FAT": {
        "location": "Fresno",
        "airport": "FAT"
    },
    "NGB": {
        "location": "Ningbo",
        "airport": "NGB"
    },
    "YAK": {
        "location": "Yakutat",
        "airport": "YAK"
    },
    "FDH": {
        "location": "Friedrichshafen",
        "airport": "FDH"
    },
    "INI": {
        "location": "Nis",
        "airport": "INI"
    },
    "GAJ": {
        "location": "Yamagata",
        "airport": "GAJ"
    },
    "FDF": {
        "location": "Ft de France",
        "airport": "FDF"
    },
    "OME": {
        "location": "Nome",
        "airport": "OME"
    },
    "YNT": {
        "location": "Yantai",
        "airport": "YNT"
    },
    "FPR": {
        "location": "Ft Pierce",
        "airport": "FPR"
    },
    "ORF": {
        "location": "Norfolk",
        "airport": "ORF"
    },
    "YAP": {
        "location": "Yap Caroline Island",
        "airport": "YAP"
    },
    "YFS": {
        "location": "Ft Simpson",
        "airport": "YFS"
    },
    "NSK": {
        "location": "Norilsk",
        "airport": "NSK"
    },
    "YZF": {
        "location": "Yellowknife",
        "airport": "YZF"
    },
    " FSM": {
        "location": "Ft Smith",
        "airport": " FSM"
    },
    "YVQ": {
        "location": "Norman Wells",
        "airport": "YVQ"
    },
    "INC": {
        "location": "Yinchuang",
        "airport": "INC"
    },
    "FWA": {
        "location": "Ft Wayne",
        "airport": "FWA"
    },
    "NRK": {
        "location": "Norrkoping",
        "airport": "NRK"
    },
    "YMS": {
        "location": "Yurimaguas",
        "airport": "YMS"
    },
    "FYU": {
        "location": "Ft Yukon",
        "airport": "FYU"
    },
    "NWI": {
        "location": "Norwich",
        "airport": "NWI"
    },
    "UUS": {
        "location": "Yuzhno-Sakhalinsk",
        "airport": "UUS"
    },
    "FUK": {
        "location": "Fukuoka",
        "airport": "FUK"
    },
    "NKC": {
        "location": "Nouakchott",
        "airport": "NKC"
    },
    "ZCL": {
        "location": "Zacatecas",
        "airport": "ZCL"
    },
    "FNC": {
        "location": "Funchal",
        "airport": "FNC"
    },
    "NOU": {
        "location": "Noumea",
        "airport": "NOU"
    },
    "ZAG": {
        "location": "Zagreb",
        "airport": "ZAG"
    },
    "FOC": {
        "location": "Fuzhou",
        "airport": "FOC"
    },
    "GEA": {
        "location": "Noumea Magenta",
        "airport": "GEA"
    },
    "ZAH": {
        "location": "Zahedan",
        "airport": "ZAH"
    },
    "GNV": {
        "location": "Gainesvile",
        "airport": "GNV"
    },
    "OVB": {
        "location": "Novosibirsk",
        "airport": "OVB"
    },
    "ZNZ": {
        "location": "Zanzibar",
        "airport": "ZNZ"
    },
    "GAL": {
        "location": "Galena",
        "airport": "GAL"
    },
    "NLD": {
        "location": "Nuevo Laredo",
        "airport": "NLD"
    },
    "ZAZ": {
        "location": "Zaragoza",
        "airport": "ZAZ"
    },
    "GOU": {
        "location": "Garoua",
        "airport": "GOU"
    },
    "NUL": {
        "location": "Nulato",
        "airport": "NUL"
    },
    "ZHA": {
        "location": "Zhanjiang",
        "airport": "ZHA"
    },
    "ELQ": {
        "location": "Gassim",
        "airport": "ELQ"
    },
    "NUP": {
        "location": "Nunapitchuk",
        "airport": "NUP"
    },
    "CGO": {
        "location": "Zhengzhou",
        "airport": "CGO"
    },
    "GAU": {
        "location": "Gauhati",
        "airport": "GAU"
    },
    "NUE": {
        "location": "Nuremberg",
        "airport": "NUE"
    },
    "ZIH": {
        "location": "Zihuatanejo",
        "airport": "ZIH"
    },
    "GMA": {
        "location": "Gemena",
        "airport": "GMA"
    },
    "OAK": {
        "location": "Oakland",
        "airport": "OAK"
    },
    "ZRH": {
        "location": "Zurich",
        "airport": "ZRH"
    },
    "GVA": {
        "location": "Geneva",
        "airport": "GVA"
    },
    "OAX": {
        "location": "Oaxaca",
        "airport": "OAX"
    },
    "GOA": {
        "location": "Genoa",
        "airport": "GOA"
    },
    "OIT": {
        "location": "Oita",
        "airport": "OIT"
    },
    "GGG": {
        "location": "Longview",
        "airport": "GGG"
    },
    "OKJ": {
        "location": "Okayama",
        "airport": "OKJ"
    }
}



// export default airportData