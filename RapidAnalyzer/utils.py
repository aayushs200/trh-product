import pymongo
import json
from bson import json_util
import urllib


class Util():

    @staticmethod
    def make_response(filtered_data):
        list_cur = list(filtered_data)
        # print('filter_res : ',len(list_cur) ,list_cur[0:1])
        json_data = json.loads(json_util.dumps(list_cur, indent=2))
        return json_data


    @staticmethod
    def createConnection():
        try:
            userDict = {1: "upayan", 2:"naveen", 3:"ayush"}
            userIndex = 3
            upayan_mongo = "mongodb+srv://upayan:uvuv#1234@cluster0.t83f4.gcp.mongodb.net/?retryWrites=true&w=majority"
            naveen_mongo = "mongodb+srv://naveen:naveen#123@cluster0.evdmoau.mongodb.net/?retryWrites=true&w=majority"
            # ayush_mongo = "mongodb+srv://ayush:Ayush#123@cluster0.efu62yo.mongodb.net/?retryWrites=true&w=majority"
            ayush_mongo = "mongodb+srv://ayushNew:AyushNew#123@cluster0.efu62yo.mongodb.net/?retryWrites=true&w=majority"

            if userDict[userIndex] == "upayan":
                print("upayan")
                client = pymongo.MongoClient(upayan_mongo)
                # print('client==> ', client)
                return client['test']
            elif userDict[userIndex] == "naveen":
                print("naveen")
                client = pymongo.MongoClient(naveen_mongo)
                # print('client==> ', client)
                return client['tradeHistory_db']
            elif userDict[userIndex] == "ayush":
                print("ayush")
                client = pymongo.MongoClient(ayush_mongo)
                # print('client==> ', client)
                return client['test']
        except Exception as e:
            print('Error occured: ', e)


    @staticmethod
    def sectorIndustry():
        sectorIndustryJson = {
            "Automotive": {
                "Auto Ancillaries": ["The Hi-Tech Gea", "Auto Stampings", "Rico Auto", "Rajratan Global Wire Ltd.", "Lumax Auto Tech", "Bharat Gears",
                                     "Gabriel India", "Jay BharatMarut", "Omax Autos", "Steel Strips Wheels Ltd.", "Autoline Ind", "Motherson SWI",
                                     "Shivam Auto", "Talbros Auto", "Shriram Pistons", "Subros Ltd.", "Hind Composites", "Pricol Ltd.",
                                     "UCAL Fuel", "Munjal Auto Ind", "Rane Madras", "JBM Auto", "Banco Products", "Jamna Auto", "JTEKT India",
                                     "Rane Engine", "Lumax Inds", "Precision Camshafts Ltd.", "PPAP Automotive", "Rane Brake", "Sharda Motor", "Bosch",
                                     "Munjal Showa", "AmarSetco Automotive Ltd.a Raja Batteries Ltd.", "Wheels", "Sundaram Brake", "India Nippon", "Minda Corporation Ltd.",
                                     "Shigan Quantum", "FIEM Ind", "Rane Holdings", "Automotive Axle", "Remsons Industries Ltd.", "Federal-Mogul",
                                     "Suprajit Eng", "Sandhar Technol", "Sundaram-Clayto", "Kinetic Engineering Ltd.", "Ndr Auto Components Ltd.",
                                     "Exide Industries Ltd.", "Setco Automotive Ltd."],

                "Auto Ancillaries - Castings/Forgings": ["Sona BLW", "Universal Autofoundry Ltd."],

                "Auto Ancillaries - Gears": ["LG Balakrishnan and Brothers Ltd.", "Shanthi Gears Ltd.", "RACL Geartech Ltd.", "Him Teknoforge Ltd."],

                "Auto Ancillaries - Others": ["Sansera Eng", "Jay Ushin Ltd.", "ZF Commercial Vehicle Control Systems India Ltd.", "UNO Minda Ltd."],

                "Tyres": ["Elgi Rubber", "JK Tyre and Industries Ltd.", "Ceat", "Apollo Tyres", "TVS Srichakra Ltd.", "Goodyear", "PTL Enterprises",
                          "MRF", "Balkrishna Industries Ltd.", "Tirupati Tyres Ltd."],

                "Auto - 2 & 3 Wheelers": ["Atul Auto", "Endurance Techn", "Hero Motocorp", "Mah Scooters", "Bajaj Auto", "TVS Motor"],

                "Auto - Cars & Jeeps": ["Hindustan Motors Ltd.", "Mahindra and Mahindra Ltd.", "Maruti Suzuki"],

                "Auto - LCVs & HCVs": ["Eicher Motors", "Force Motors", "Ashok Leyland", "Tata Motors", "SML Isuzu"],

                "Automobile - Dealers & Distributors": ["CarTrade Tech"],

                "Auto - Tractors": ["VST Tillers", "HMT", "Escorts Kubota Ltd."]
            },
            "Banking/Finance": {
                "Banks - Private Sector": ["JK Bank", "South Ind Bank", "Karnataka Bank", "Yes Bank", "Federal Bank", "Karur Vysya", "RBL Bank",
                                           "City Union Bank", "DCB Bank", "IDFC First Bank", "IndusInd Bank", "Dhanlaxmi Bank", "Bandhan Bank",
                                           "Axis Bank", "AU Small Finance Bank", "HDFC Bank", "ICICI Bank", "Kotak Mahindra Bank"],

                "Finance - NBFC": ["Poonawalla Fin"],

                "Finance - General": ["Nalwa Sons Investment Ltd.", "DB (International) Stock Brokers Ltd.", "Viji Finance", "IIFL Finance",
                                      "Keynote Finance", "Emkay Global", "Ujjivan Financial Services Ltd.", "Jindal Poly Inv", "Ugro Capital",
                                      "Indbank Merchan", "The Investment", "Khandwala Sec", "Consol Finvest", "NBI Industrial", "Transwarranty",
                                      "MAS Financial S", "Indostar Capita", "Sasta Sundar", "Sundaram", "AB Money", "Ganges Securities Ltd.",
                                      "Motilal Oswal", "Pilani Invest", "Lakshmi Finance", "Geojit Financial Services", "Edelweiss", "Equitas Holding",
                                      "Centrum Capital", "ICICI Prudential", "Choice International Ltd.", "Palash Securities Ltd.", "Dhunseri Investments",
                                      "AAVAS Financiers Ltd.", "21st Century Management Ltd.", "Indo Thai Securities Ltd.", "Mask Investment"],

                "Banks - Public Sector": ["Indian Overseas Bank", "Union Bank", "Bank of India", "Bank of Maharashtra", "Indian Bank",
                                          "Punjab National Bank", "Central Bank of India", "UCO Bank", "Bank of Baroda", "Canara Bank",
                                          "State Bank of India", "Punjab & Sind Bank"],

                "Finance - Investments": ["Dhani Services", "DELPHI WORLD", "STEL Holdings", "BLB Ltd.", "Starteck Finance Ltd.", "Nahar Capital",
                                          "ILandFS Investment Managers Ltd.", "Industrial Investment Trust Ltd.", "Almondz Global Securities Ltd.",
                                          "Monarch Networth Capital Ltd.", "Tata Investment Corporation Ltd.", "Signet Industries Ltd.", "HDFC AMC Ltd.",
                                          "Williamson Magor and Company Ltd.", "Inventure Growth and Securities Ltd.", "BF Investment Ltd.",
                                          "Welspun Investments and Commercials Ltd.", "Nagreeka Capital and Infrastructure Ltd.", "JM Financial Ltd.",
                                          "Central Depository Services Ltd Ltd.", "Religare Enterprises Ltd.", "JSW Holdings Ltd.", "PNB Gilts Ltd.",
                                          "L&T Finance Holdings Ltd.", "Muthoot Capital Services Ltd.", "Bajaj Finserv", "Kalyani Investment Company Ltd.",
                                          "Muthoot Finance", "Onelife Capital Advisors Ltd.", "Prime Securities Ltd.", "Wealth First Portfolio Managers Ltd.",
                                          "Summit Securities Ltd.", "Paisalo Digital Ltd.", "Stampede Capital Ltd.", "Bajaj Holdings", "Hexa Tradex Ltd.",
                                          "Reliance Capital Ltd.", "TCI Finance Ltd.", "Blue Chip India Ltd.", "SIL Investments Ltd.", "Vardhman Holdings Ltd.",
                                          "Ausom Enterprise Ltd.", "Max Financial Services Ltd."]
            },
            "Cement/Construction": {
                "Construction & Contracting - Civil": ["GPT Infra", "Ramky Infra", "Hindustan Construction Company Ltd.", "ITD Cementation",
                                                       "Simplex Infra", "Tarmat Ltd.", "RPP Infra Projects", "J Kumar Infraprojects Ltd.",
                                                       "Welspun Enterprises Ltd.", "Patel Engineering Company Ltd.", "Supreme Infra", "MBL Infra",
                                                       "Gayatri Project", "NCC Ltd.", "Ashoka Buildcon Ltd.", "Man Infraconstruction Ltd.",
                                                       "IRB InvIT Ltd.", "Ahluwalia Contracts India Ltd.", "Mahindra Lifespace Developers Ltd.",
                                                       "JMC Projects", "Unitech Ltd.", "Tantia Constructions Ltd.", "Noida Toll Bridge Company Ltd.",
                                                       "ILandFS Engineering and Construction Company Ltd.", "ARSS Infrastructure Projects Ltd.",
                                                       "Art Nirman Ltd.", "Univastu India Ltd.", "KNR Constructions Ltd.", "Madhucon Projects Ltd.",
                                                       "AJR Infra and Tolling Ltd.", "Setubandhan Infrastructure Ltd.", "SPML Infra",
                                                       "Consolidated Construction Consortium Ltd.", "Kaushalya Infrastructure Development Corporation Ltd"],

                "Ceramics & Granite": ["Madhav Marbles", "Oriental Trimex", "Murudeshwar Ceramics Ltd.", "Nitco Ltd.", "Aro Granite Industries Ltd.",
                                       "Somany Ceramics", "Asian Granito India Ltd.", "Orient Bell Ltd.", "Pokarna Ltd.", "Regency Ceramics Ltd.",
                                       "Cera Sanitaryware Ltd.", "Kajaria Ceramics Ltd.", "Rajdarshan Industries Ltd."],

                "Cement - Major": ["Shree Digvijay Cement Company Ltd.", "Gujarat Sidhee Cement Ltd.", "India Cements Ltd.", "Burnpur Cement Ltd.",
                                   "Giriraj Civil Developers Ltd.", "Ambuja Cements", "Prism Johnson", "Star Cement", "Heidelberg Cement India Ltd.",
                                   "J. K. Cement", "Rain Industries", "Ramco Cements", "UltraTech Cement", "ACC Ltd.", "Shree Cements", "Orient Cement",
                                   "Mangalam Cement", "Birla Corporation Ltd.", "Barak Vally Cements Ltd.", "KCP Ltd.", "JK Lakshmi Cement Ltd.",
                                   "Andhra Cement"],

                "Cement - Products & Building Materials": ["Everest Industries Ltd.", "RHI Magnesita India Ltd.", "Indian Hume Pipe Company Ltd.",
                                                           "HIL Ltd.", "Visaka Industries Ltd.", "Vesuvius India Ltd.", "Sanghi Industries Ltd.",
                                                           "Ramco Industries Ltd.", "IFGL Refractories Ltd."],

                "Cement - Mini": ["Anjani Cement", "Kakatiya Cement", "Deccan Cements", "NCL Industries", "Sagar Cement"]
            },
            "Chemical": {
                "Chemicals": ["Alkali Metals Ltd.", "Himadri Speciality Chemical Ltd.", "Vikas Ecotech Ltd.", "Sree Rayalaseema Hi Strength Hyp Ltd.",
                              "Grauer and Weil (India) Ltd.", "Shree Pushkar Chemicals and Fertilisers Ltd.", "Camlin Fine Sciences Ltd.",
                              "Indo Amines Ltd.", "Indo Borax and Chemicals Ltd.", "Sanginita Chemicals Ltd.", "Vinyl Chemicals (India) Ltd.",
                              "Refex Industries Ltd.", "Ganesh Benzoplast Ltd.", "Punjab Chemicals & Crop Protection Ltd.", "Hindcon Chemicals Ltd.",
                              "Gulshan Polyols Ltd.", "Excel Industries Ltd.", "Vishnu Chemicals Ltd.", "India Glycols Ltd.", "Deepak Nitrite Ltd.",
                              "Thirumalai Chemicals Ltd.", "Jayant Agro-Organics Ltd.", "Panama Petrochem Ltd.", "ORIENTAL AROMATICS Ltd.",
                              "Alkyl Amines Chemicals Ltd.", "Balaji Amines Ltd.", "Aarti Industries Ltd.", "GOCL Corporation Ltd.", "GFL Ltd.",
                              "Chembond Chemicals Ltd.", "Foseco India Ltd.", "Omkar Speciality Chemicals Ltd.", "Gujarat Alkalies and Chemicals Ltd.",
                              "Kanoria Chemicals and Industries Ltd.", "Solar Industries India Ltd.", "Chemfab Alkalis Ltd.", "Mangalam Organics Ltd.",
                              "Tata Chemicals Ltd.", "Gujarat Heavy Chemicals Ltd.", "Aarti Surfactants Ltd.", "Premier Explosives Ltd.",
                              "Linde India Ltd.", "Valiant Organics Ltd.", "Vinati Organics", "Archean Chemical Industries Ltd.", "UPL Ltd.",
                              "Pidilite Industries Ltd.", "Privi Speciality Chemicals Ltd.", "Navin Fluorine International Ltd.", "Neogen Chemicals Ltd.",
                              "Oriental Carbon and Chemicals Ltd.", "BASF India Ltd.", "Standard Industries Ltd.", "Vikas WSP Ltd.", "Seya Industries Ltd.",
                              "Vadivarhe Speciality Chemicals Ltd."],

                "Fertilizers": ["Southern Petrochemical Industries Corporation Ltd.", "National Fertilizers Ltd.", "Fertilisers and Chemicals Travancore Ltd.",
                                "Khaitan Chemicals and Fertilizers Ltd.", "Rashtriya Chemicals and Fertilisers Ltd.", "Oswal Chemicals and Fertilisers Ltd.",
                                "Zuari Industries Ltd.", "Zuari Agro Chemicals Ltd.", "Madras Fertilizers Ltd.", "Chambal Fertilisers and Chemicals Ltd.",
                                "Agri-Tech (India) Ltd.", "Deepak Fertilizers and Petrochemicals Coporation Ltd.", "Gujarat State Fertilizers & Chemicals Ltd.",
                                "Gujarat Narmada Valley Fertilizers & Chemicals Ltd.", "Coromandel International Ltd.", "Mangalore Chemicals and Fertilisers Ltd.",
                                "Nagarjuna Fertilisers and Chemicals Ltd.", "Bohra Industries Ltd."],

                "Edible Oils & Solvent Extraction": ["Gokul Agro Resources Ltd."],

                "Speciality Chemicals": ["Laxmi Organic Industries Ltd.", "Fairchem Organics Ltd.", "Chemcon Speciality Chemicals Ltd.", "Aether Industries Ltd.",
                                         "Clean Science & Technology Ltd.", "Rossari Biotech Ltd.", "Tatva Chintan Pharma Chem Ltd.", "AMI Organics Ltd.",
                                         "Meghmani Finechem Ltd.", "Anupam Rasayan India Ltd."],

                "Petrochemicals": ["DCW Ltd.", "Finolex Industries Ltd.", "Goa Carbon Ltd.", "Bhansali Engineering Polymers Ltd.", "Manali Petrochemicals Ltd.",
                                   "Savita Oil Technologies Ltd.", "Supreme Petrochem Ltd.", "NOCIL Ltd.", "INEOS Styrolution India Ltd.", "Kothari Petrochem Ltd."],

                "Dyes & Pigments": ["Bodal Chemicals Ltd.", "Sudarshan Chemical Industries Ltd.", "Dynemic Products Ltd.", "AksharChem (India) Ltd.",
                                    "Asahi Songwon Colors Ltd.", "Poddar Pigments Ltd.", "Clariant Chemicals India Ltd.", "Kiri Industries Ltd.",
                                    "Mahickra Chemicals Ltd.", "Vidhi Specialty Food Ingredients Ltd."],

                "Pesticides & Agro Chemicals": ["Sharda Cropchem Ltd.", "Nacl Industries Ltd.", "Shreeoswal Seeds & Chemicals Ltd.", "Dhanuka Agritech Ltd.",
                                                "Meghmani Organics Ltd.", "Bhagiradh Chemicals and Industries Ltd.", "Rallis India Ltd.", "PI Industries Ltd.",
                                                "Bayer CropScience Ltd.", "Bharat Rasayan Ltd.", "Insecticides India Ltd.", "Meghmani Organics Ltd."],

                "Lubricants": ["GP Petroleums Ltd.", "Castrol India Ltd.", "Gulf Oil Lubricants India Ltd.", "Tide Water Oil Ltd."],

                "Breweries & Distilleries": ["IFB Agro Industries Ltd."],

                "Pesticides & Agrochemicals": ["India Pesticides Ltd.", "Heranba Industries Ltd."],

                "Paints & Varnishes": ["Shalimar Paints Ltd.", "Kansai Nerolac Paints Ltd.", "Berger Paints India Ltd.", "Sirca Paints India Ltd.",
                                       "Asian Paints Ltd.", "Akzo Nobel India Ltd."],

                "Detergents": ["Tamilnadu Petroproducts Ltd."]
            },
            "Conglomerates": {
                "Diversified": ["SecUR Credentials Ltd.", "Tirupati Forge Ltd.", "General Insurance Corporation of India Ltd.", "Aarvi Encon Ltd.",
                                "Agro Phos India Ltd.", "Priti International Ltd.", "Indian Energy Exchange Ltd.", "NAVA Ltd.", "SBC Exports Ltd.",
                                "Madhya Bharat Agro Products Ltd.", "Century Textiles and Industries Ltd.", "Medico Remedies Ltd.", "Kokuyo Camlin Ltd.",
                                "Prakash Industries Ltd.", "Hindustan Aeronautics Ltd.", "Aster DM Healthcare Ltd.", "Mohini Health & Hygiene Ltd.",
                                "Kesoram Industries Ltd.", "SHAREINDIA Ltd.", "Mahindra Logistics Ltd.", "South West Pinnacle Exploration Ltd.",
                                "NESCO Ltd.", "Grasim Industries Ltd.", "Voltas Ltd.", "RITES Ltd.", "Jash Engineering Ltd.", "Milton Industries Ltd.",
                                "3M India Ltd.", "Crown Lifters Ltd.", "R M Drip & Sprinklers Systems Ltd.", "DCM Shriram Ltd.", "Sintex Industries Ltd.",
                                "Shree Ram Protiens Ltd.", "Globe International Carriers Ltd.", "Gillanders Arbuthnot & Co Ltd.", "SRF Ltd."],

                "Textiles - Processing": ["Bombay Dyeing and Manufacturing Company Ltd."]
            },
            "Consumer Durable": {
                "Consumer Goods - White Goods": ["IFB Industries", "Symphony Ltd.", "Whirlpool", "Blue Star Ltd."],

                "Domestic Appliances": ["TTK Prestige Ltd.", "Butterfly Gandhimathi Appliances Ltd.", "Bajaj Electricals Ltd."]
            },
            "Consumer Non-Durable": {
                "Consumer Goods - Electronic": ["Geekay Wires Ltd.", "D P Wires Ltd.", "Jindal Photo Ltd.", "Mirc Electronics Ltd.", "BPL Ltd.",
                                                "PG Electroplast Ltd."],

                "Personal Care": ["Sanwaria Consumer Ltd.", "JHS Svendgaard Laboratories Ltd.", "Gillette India Ltd.", "Godrej Industries Ltd.",
                                  "Jyothy Labs Ltd.", "Godrej Consumer Products Ltd.", "Marico Ltd.", "Dabur India Ltd.", "Hindustan Unilever Ltd.",
                                  "Colgate Palmolive (India) Ltd.", "Procter and Gamble Hygiene and Health Care Ltd."],

                "Leather Products": ["Sreeleathers Ltd.", "Liberty Shoes Ltd.", "Bhartiya International Ltd.", "Superhouse Ltd.", "Bata India Ltd.",
                                     "Mirza International Ltd.", "Relaxo Footwears Ltd.", "Khadim India Ltd."],

                "Dry Cells": ["Indo-National Ltd.", "Eveready Industries India Ltd."]
            },
            "Engineering": {
                "Bearings": ["Menon Bearings Ltd.", "NRB Industrial Bearings Ltd.", "NRB Bearings Ltd.", "Schaeffler India Ltd.", "SKF India Ltd.",
                             "Timken India Ltd."],

                "Infrastructure - General": ["Bharat Road Network Ltd.", "Jaiprakash Associates Ltd.", "Reliance Industrial Infrastructure Ltd.",
                                             "NBCC (India) Ltd.", "Engineers India Ltd.", "Power Mech Projects Ltd.", "Va Tech Wabag Ltd.",
                                             "Texmaco Infrastructure & Holdings Ltd.", "IRB Infrastructure Developers Ltd.", "Titagarh Wagons Ltd.",
                                             "Sadbhav Engineering Ltd.", "Bharat Heavy Electricals Ltd.", "MEP Infrastructure Developers Ltd.",
                                             "Texmaco Rail and Engineering Ltd.", "HG Infra Engineering Ltd.", "BEML Ltd.", "Thermax Ltd.",
                                             "Sadbhav Infrastructure Projects Ltd.", "Timken India Ltd.", "GMR Airports Infrastructure Ltd.",
                                             "Siemens Ltd.", "Adani Ports and Special Economic Zone Ltd.", "Larsen & Toubro Ltd.", "Jaypee Infratech Ltd.",
                                             "ILandFS Transportation Networks Ltd.", "BGR Energy Systems Ltd.", "SKIL Infrastructure Ltd."],

                "Electrodes & Graphite": ["HEG Ltd.", "Graphite India Ltd.", "Ador Welding Ltd.", "Esab India Ltd.", ""],

                "Engineering - Heavy": ["Praj Industries Ltd.", "Aakash Exploration Services Ltd.", "TRF Ltd.", "TD Power Systems Ltd.", "GMM Pfaudler Ltd.",
                                        "Elecon Engineering Company Ltd.", "Sanghvi Movers Ltd.", "Gujarat Apollo Industries Ltd.", "Windsor Machines Ltd.",
                                        "Ircon International Ltd.", "Walchandnagar Industries Ltd.", "Garden Reach Shipbuilders & Engineers Ltd.",
                                        "Eimco Elecon (India) Ltd.", "Kabra Extrusion Technik Ltd.", "Action Construction Equipment Ltd.",
                                        "Varroc Engineering Ltd."],

                "Electric Equipment": ["Kirloskar Electric Co Ltd.", "De Nora India Ltd.", "Bharat Bijlee Ltd.", "CG Power and Industrial Solutions Ltd.",
                                       "Salzer Electronics Ltd.", "Igarashi Motors Ltd.", "HBL Power Systems Ltd.", "Veto Switchgears and Cables Ltd.",
                                       "Triveni Turbine Ltd.", "Swelect Energy Systems Ltd.", "Havells India Ltd.", "HPL Electric & Power Ltd.", "IMP Powers Ltd.",
                                       "Honda India Power Products Ltd."],

                "Cables - Power & Others": ["Cords Cable Industries Ltd.", "B C Power Controls Ltd.", "KEI Industries Ltd.", "Dynamic Cables Ltd.",
                                            "Universal Cables Ltd.", "Polycab India Ltd."],

                "Power - Transmission & Equipment": ["Transformers and Rectifiers India Ltd.", "Kalpataru Power Transmission Ltd.", "Jyoti Structures Ltd.",
                                                     "A2Z Infra Engineering Ltd.", "GE T&D India Ltd.", "Ujaas Energy Ltd.", "Indo Tech Transformers Ltd.",
                                                     "KEC International Ltd.", "Voltamp Transformers Ltd.", "GE Power India Ltd."],

                "Pumps": ["Dynamatic Technologies Ltd.", "KSB Ltd.", "Shakti Pumps (India) Ltd.", "Roto Pumps Ltd.", "Kirloskar Brothers Ltd."],

                "Textiles - Machinery": ["Lakshmi Machine Works Ltd.", "Indian Card Clothing Ltd."],

                "Machine Tools": ["Kennametal India Ltd.", "Macpower CNC Machines Ltd.", "Lokesh Machines Ltd."],

                "Engines": ["Kirloskar Oil Engines Ltd.", "Greaves Cotton Ltd.", "Swaraj Engines Ltd.", "Cummins India Ltd."],

                "Abrasives": ["Orient Abrasives Ltd.", "Carborundum Universal Ltd.", "Wendt (India) Ltd.", "Grindwell Norton Ltd."],

                "Steel - Medium & Small": ["Bharat Wire Ropes Ltd.", "Manaksia Coated Metals & Industries Ltd."],

                "Compressors": ["Elgi Equipments Ltd.", "Ingersoll Rand (India) Ltd.", "Revathi CP Equipment Ltd."]
            },

            "Food & Beverage": {
                "Sugar": ["KCP Sugar Ind Corp Ltd.", "Uttam Sugar Mills Ltd.", "Ponni Sugars (Erode) Ltd.", "Mawana Sugars Ltd.", "Rana Sugars Ltd.",
                          "Dwarikesh Sugar Industries Ltd.", "Sakthi Sugars Ltd.", "Simbhaoli Sugars Ltd.", "Rajshree Sugars and Chemicals Ltd.",
                          "Dhampur Sugar Mills Ltd.", "Magadh Sugar & Energy Ltd.", "KM Sugar Mills Ltd.", "Dalmia Bharat Sugar and Industries Ltd.",
                          "Dharani Sugars and Chemicals Ltd.", "The Andhra Sugar Ltd.", "Kothari Sugars and Chemicals Ltd.", "Ugar Sugar Works Ltd.",
                          "Avadh Sugar & Energy Ltd.", "Bajaj Hindusthan Sugar Ltd.", "Dalmia Bharat Sugar and Industries Ltd.", "GM Breweries Ltd.",
                          "Bannariamman Sugars Ltd.", "EID Parry (India) Ltd."],

                "Food Processing": ["Hindustan Foods Ltd.", "Umang Dairies Ltd.", "Nakoda Group of Industries Ltd.", "SKM Egg Products Export (India) Ltd.",
                                    "Sarveshwar Foods Ltd.", "Coffee Day Enterprises Ltd.", "ADF Foods Industries Ltd.", "Sheetal Cool Products Ltd.",
                                    "Megastar Foods Ltd.", "Vadilal Industries Ltd.", "Heritage Foods Ltd.", "Hatsun Agro Products Ltd.", "Kohinoor Foods Ltd.",
                                    "Manorama Industries Ltd.", "Apex Frozen Foods Ltd.", "Tasty Bite Eatables Ltd.", "Chaman Lal Setia Exports Ltd.",
                                    "Euro India Fresh Foods Ltd.", "Parag Milk Foods Ltd.", "Prataap Snacks Ltd.", "Vikas Proppant & Granite Ltd.",
                                    "Nestle India Ltd.", "KRBL Ltd.", "Britannia Industries Ltd.", "Varun Beverages Ltd.", "Foods and Inns Ltd."],

                "Plantations - Tea & Coffee": ["Mcleod Russel (India) Ltd.", "Dhunseri Tea & Industries Ltd.", "Jayshree Tea and Industries Ltd.",
                                               "CCL Products India Ltd.", "Naga Dhunseri Group Ltd.", "Harrisons Malyalam Ltd.", "Tata Coffee Ltd.",
                                               "The Grob Tea Company Ltd.", "TATA Consumer Products Ltd.", "United Nilgiri Tea Estates Company Ltd.",
                                               "Rossell India Ltd.", "Bombay Burmah Trading Corporation Ltd."],

                "Breweries & Distilleries": ["Ravi Kumar Distilleries Ltd.", "GM Breweries Ltd.", "Globus Spirits Ltd.", "Pioneer Distilleries Ltd.",
                                             "United Spirits Ltd.", "United Breweries Ltd.", "Tilaknagar Industries Ltd.", "Radico Khaitan Ltd.",
                                             "Som Distilleries and Breweries Ltd."],

                "Petrochemicals": ["Dhunseri Ventures Ltd."],

                "Vanaspati & Oils": ["IVP Ltd.", "BCL Industries Ltd.", "Zydus Wellness Ltd.", "M K Proteins Ltd."]
            },

            "Gold ETF": {
                "Industry": ["ICICI Prudential Gold ETF", "SBI Mutual Fund - Gold Exchange Traded Scheme Ltd.", "Nippon India ETF Gold BeES",
                             "Kotak Mutual Fund - Gold Exchange Traded Fund Ltd.", "HDFC Mutual Fund - Gold Exchange Traded Fund Ltd.",
                             "Invesco India Gold Exchange Traded Fund Ltd."]
            },
            "Technology": {
                "Computers - Software": ["Dev Information Technology Ltd.", "BLACK BOX Ltd.", "Softtech Engineers Ltd.", "Rolta India Ltd.", "Mastek Ltd.",
                                         "Tata Elxsi Ltd.", "Ramco System Ltd.", "COFORGE LIMITED Ltd.", "63 Moons Technologies Ltd.",
                                         "Persistent Systems Ltd.", "Securekloud Technologies Ltd.", "Newgen Software Technologies Ltd.",
                                         "LTIMindtree Ltd.", "Quick Heal Technologies Ltd.", "Intellect Design Arena Ltd.", "Wipro Ltd.",
                                         "MphasiS Ltd.", "Expleo Solutions Ltd.", "Saksoft Ltd.", "Tech Mahindra Ltd.", "3i Infotech Ltd.",
                                         "Hinduja Global Solutions Ltd.", "Zensar Technologies Ltd.", "HCL Technologies Ltd.", "Infosys Ltd.",
                                         "Tata Consultancy Services Ltd.", "Xelpmoc Design and Tech Ltd.", "Oracle Financial Services Software Ltd.",
                                         "Cyient Ltd.", "Sasken Technologies Ltd.", "Mindteck (India) Ltd.", "Silver Touch Technologies Ltd.",
                                         "Ducon Infratechnologies Ltd.", "Adroit Infotech Ltd."],

                "Computers - Software Medium & Small": ["Excel Realty N Infra Ltd.", "Visesh Infotechnics Ltd.", "California Software Ltd.",
                                                        "Cambridge Technology Enterprises Ltd.", "WE WIN LIMITED Ltd.", "LCC Infotech Ltd.",
                                                        "Genesys International Corporation Ltd.", "Dynacons Systems and Solutions Ltd.",
                                                        "InfoBeans Technologies Ltd.", "Goldstone Technologies Ltd.", "Palred Technologies Ltd.",
                                                        "Goldstone Technologies Ltd.", "Usha Martin Education and Solutions Ltd.", "Sonata Software Ltd.",
                                                        "Axiscades Technologies Ltd.", "Trigyn Technologies Ltd.", "Datamatics Global Services Ltd.",
                                                        "ALLSEC Technologies Ltd.", "Aurionpro Solutions Ltd.", "Compucom Software Ltd.",
                                                        "Tanla Platforms Ltd.", "Inspirisys Solutions Ltd.", "RS Software (India) Ltd.",
                                                        "Kellton Tech Solutions Ltd.", "HOV Services Ltd.", "Accelya Solutions India Ltd.",
                                                        "Melstar Infotech Ltd.", "IZMO Ltd.", "Xchanging Solutions Ltd.", "Aurum Proptech Ltd.",
                                                        "Allied Digital Services Ltd.", "Nucleus Software Exports Ltd.", "R Systems International Ltd.",
                                                        "Tera Software Ltd.", "Cybertech Systems and Software Ltd.", "Kernex Microsystems (India) Ltd.",
                                                        "FCS Software Solutions Ltd.", "Intense Technologies Ltd.", "eClerx Services Ltd.", "Vakrangee Ltd.",
                                                        "Cigniti Technologies Ltd.", "Firstsource Solutions Ltd.", "Onward Technologies Ltd.",
                                                        "GSS Infotech Ltd.", "Brightcom Group Ltd.", "Birlasoft Ltd."],

                "Computers - Software - Training": ["NIIT Ltd.", "Zee Learn Ltd.", "Career Point Ltd.", "Aptech Ltd.", "Tree House Education and Accessories Ltd.",
                                                    "Educomp Solutions Ltd.", "MT Educare Ltd."],

                "Computers - Hardware": ["Cerebra Integrated Technologies Ltd.", "MRO-TEK Realty Ltd.", "TVS Electronics Ltd.", "Smartlink Holdings Ltd.",
                                         "HCL Infosystems Ltd.", "Redington Ltd.", "Compuage Infocom Ltd."],

                "IT Services & Consulting": ["E2E Networks Ltd."],

                "Media & Entertainment": ["Nxtdigital Ltd."],

                "Retail": ["Intrasoft Technologies Ltd."]
            },
            "Manufacturing": {
                "Textiles - Readymade Apparels": ["SPL Industries Ltd.", "Kitex Garments Ltd.", "Gokaldas Exports Ltd.", "Pearl Global Industries Ltd.",
                                                  "Indian Terrain Fashions Ltd.", "Celebrity Fashions Ltd.", "Monte Carlo Fashions Ltd.",
                                                  "Lovable Lingerie Ltd.", "United Polyfab Gujarat Ltd.", "VIP Clothing Ltd.", "Nandani Creation Ltd.",
                                                  "Zodiac Clothing Company Ltd.", "KPR Mill Ltd.", "Page Industries Ltd.", "Dollar Industries Ltd."],

                "Electricals": ["Centum Electronics Ltd.", "Goldstar Power Ltd.", "Dixon Technologies Ltd.", "Delta Manufacturing Ltd.", "Hind Rectifiers Ltd.",
                                "Bharat Electronics Ltd.", "Crompton Greaves Consumer Electrical Ltd.", "Genus Power Infrastructures Ltd.",
                                "Servotech Power Systems Ltd."],

                "Textiles - Spinning - Cotton Blended": ["Morarjee Textiles Ltd.", "Reliance Chemotex Industries Ltd.", "Nahar Poly Films Ltd.",
                                                         "Nitin Spinners Ltd.", "Eurotex Industries and Exports Ltd.", "Vardhman Textiles Ltd.",
                                                         "Nagreeka Exports Ltd.", "Salona Cotspin Ltd.", "Lambodhara Textile Ltd.", "Trident Ltd.",
                                                         "Vardhman Polytex Ltd.", "DCM Ltd.", "Indo Count Industries Ltd.", "Maral Overseas Ltd.",
                                                         "Ginni Filaments Ltd.", "Super Spinning Mills Ltd.", "Vishal Fabrics Ltd.", "Ashima Ltd.",
                                                         "Shiva Texyarn Ltd.", "Ambika Cotton Mills Ltd.", "Suryalakshmi Cotton Mills Ltd."],

                "Textiles - Spinning - Synthetic Blended": ["RSWM Ltd.", "Reliance Chemotex Industries Ltd.", "Banswara Syntex Ltd.", "Sangam (India) Ltd.",
                                                            "Indo Rama Synthetics (India) Ltd.", "Damodar Industries Ltd."],

                "Paper": ["Magnum Ventures Ltd.", "Ruchira Papers Ltd.", "Star Paper Mills Ltd.", "AMJ Land Ltd.", "Pudumjee Paper Products Ltd.",
                          "Emami Paper Mills Ltd.", "Seshasayee Paper and Boards Ltd.", "JK Paper Ltd.", "Shreyans Industries Ltd.", "Andhra Paper Ltd.",
                          "West Coast Paper Mills Ltd.", "Tamil Nadu Newsprint and Papers Ltd.", "NR Agarwal Industries Ltd.", "Astron Paper & Board Mill Ltd.",
                          "Shree Rama Newsprint Ltd.", "Ballarpur Industries Ltd.", "Genus Paper & Boards Ltd.", "Malu Paper Mills Ltd.", "3p Land Holdings Ltd."],

                "Plastics": ["TPL Plastech Ltd.", "Arrow Greentech Ltd.", "Premier Polyfilm Ltd.", "Mold-Tek Packaging Ltd.", "Kriti Industries (India) Ltd.",
                             "Tainwala Chemicals and Plastics (India) Ltd.", "Cosmo First Ltd.", "Sintex Plastics Technology Ltd.", "Jain Irrigation Systems Ltd.",
                             "Kingfa Science & Technology Ltd.", "Tokyo Plast International Ltd.", "Texmo Pipes and Products Ltd.", "Pearl Polymers Ltd.",
                             "Tijaria Polypipes Ltd.", "Plastiblends India Ltd.", "Astral Ltd.", "Fiberweb India Ltd.", "Supreme Industries Ltd.",
                             "Nilkamal Ltd.", "Mayur Uniquoters Ltd.", "Hitech Corporation Ltd.", "Pil Italica Lifestyle Ltd."],

                "Textiles - Hosiery & Knitwear": ["Nahar Spinning Mills Ltd.", "TT Ltd.", "Bhandari Hosiery Exports Ltd.", "Rupa and Company Ltd.",
                                                  "Pioneer Embroideries Ltd."],

                "Packaging": ["Time Technoplast Ltd.", "AMD Industries Ltd.", "Polyplex Corporation Ltd.", "Kanpur Plastipacks Ltd.", "Jindal Poly Films Ltd.",
                              "Huhtamaki India Ltd.", "Uflex Ltd.", "Ester Industries Ltd.", "Oricon Enterprises Ltd.", "Shree Rama Multi Tech Ltd.",
                              "Xpro India Ltd.", "Radha Madhav Corporation Ltd.", "Emmbi Industries Ltd.", "Worth Peripherals Ltd.", "Rollatainers Ltd.",
                              "EPL Ltd.", "Everest Kanto Cylinder Ltd.", "Gujarat Raffia Industries Ltd.", "Flexituff Ventures International Ltd.",
                              "Bkm industries Ltd."],

                "Textiles - Composite Mills": ["Nahar Industrial Enterprises Ltd.", "Ruby Mills Ltd.", "Loyal Textiles Mills Ltd.",
                                               "Soma Textiles and Industries Ltd."],

                "Textiles - Weaving": ["BSL Ltd.", "Welspun India Ltd.", "Alok Industries Ltd.", "Orbit Exports Ltd.", "Donear Industries Ltd.",
                                       "Siyaram Silk Mills Ltd."],

                "Castings & Forgings": ["Kalyani Forge Ltd.", "Metalyst Forgings Ltd.", "Mahindra CIE Automotive Ltd.", "Electrosteel Castings Ltd.",
                                        "Alicon Castalloy Ltd.", "Steelcast Ltd.", "Ramkrishna Forgings Ltd.", "LGB Forge Ltd.", "Nelcast Ltd.",
                                        "Jayaswal Neco Industries Ltd.", "Hilton Metal Forging Ltd.", "Bharat Forge Ltd.", "MM Forgings Ltd.",
                                        "Sintercom India Ltd."],

                "Textiles - Denim": ["Nandan Denim Ltd.", "Arvind Ltd.", "Aarvee Denim and Exports Ltd."],

                "Textiles - General": ["Bannari Amman Spinning Mills Ltd.", "Sutlej Textiles and Industries Ltd.", "Alps Industries Ltd.",
                                       "Bang Overseas Ltd.", "PDS Ltd.", "Globe Textiles India Ltd.", "Garware Technical Fibres Ltd.", "STL Global Ltd.",
                                       "Akshar Spintex Ltd.", "TCNS Clothing Co Ltd.", "Cantabil Retail India Ltd.", "Jindal Worldwide Ltd."],

                "Textiles - Synthetic & Silk": ["Thomas Scott India Ltd.", "Eastern Silk Industries Ltd.", "Himatsingka Seide Ltd.", "Zenith Exports Ltd."],

                "Textiles - Processing": ["Weizmann Ltd.", "Ganesha Ecosphere Ltd.", "Sarla Performance Fibers Ltd.", "AYM Syntex Ltd.", "Lux Industries Ltd.",
                                          "Mohit Industries Ltd."],

                "Textiles - Manmade": ["Sumeet Industries Ltd.", "Century Enka Ltd.", "Vardhman Acrylics Ltd.", "JBF Industries Ltd.", "Paras Petrofils Ltd."],

                "Fasteners": ["Lakshmi Precision Screws Ltd.", "Sterling Tools Ltd.", "Sundram Fasteners Ltd.", "GKW Ltd."],

                "Textiles - Woollen & Worsted": ["Raymond Ltd."],

                "Glass & Glass Products": ["La Opala RG Ltd.", "HLE Glascoat Ltd.", "Borosil Renewables Ltd.", "Asahi India Glass Ltd."]

            },
            "Media": {
                "Media & Entertainment": ["Raj Television Network Ltd.", "Cinevista Ltd.", "Tips Industries Ltd.", "Eros International Media Ltd.",
                                          "PVR Ltd.", "Silly Monks Entertainment Ltd.", "Hindustan Media Ventures Ltd.", "Entertainment Network India Ltd.",
                                          "Prime Focus Ltd.", "DB Corp Ltd.", "Den Networks Ltd.", "INOX Leisure Ltd.", "Balaji Telefilms Ltd.",
                                          "Shemaroo Entertainment Ltd.", "TV18 Broadcast Ltd.", "Hathway Cable and Datacom Ltd.", "UFO Moviez India Ltd.",
                                          "Pritish Nandy Communications Ltd.", "HT Media Ltd.", "Mukta Arts Ltd.", "GTPL Hathway Ltd.", "Dish TV India Ltd.",
                                          "Next Mediaworks Ltd.", "Cyber Media (India) Ltd.", "Touchwood Entertainment Ltd.", "Saregama India Ltd.",
                                          "Zee Media Corporation Ltd.", "TV Today Network Ltd.", "Jagran Prakashan Ltd.", "Diligent Media Corporation Ltd.",
                                          "Music Broadcast Ltd.", "Zee Entertainment Enterprises Ltd.", "Cineline India Ltd.", "Sun TV Network Ltd.",
                                          "New Delhi Television Ltd.", "Siti Networks Ltd.", "TV Vision Ltd."]
            },

            "Metals & Mining": {
                "Mining & Minerals": ["Ashapura Minechem Ltd.", "Sarthak Metals Ltd.", "Maithan Alloys Ltd.", "Orissa Minerals Development Company Ltd.",
                                      "Vedanta Ltd.", "Indian Metals & Ferro Alloys Ltd.", "NMDC Ltd.", "Gujarat Mineral Development Corporation Ltd.",
                                      "MOIL Ltd.", "Coal India Ltd."],
                "Steel - Medium & Small": ["Mukand Ltd.", "Bedmutha Industries Ltd.", "Incredible Industries Ltd.", "Usha Martin Ltd.", "Kamdhenu Ltd.",
                                           "Shah Alloys Ltd.", "SAL Steel Ltd.", "Hisar Metal Ltd.", "Shivalik Bimetal Controls Ltd.", "Jindal Stainless Ltd.",
                                           "Vardhman Special Steels Ltd.", "Technocraft Industries (India) Ltd."],

                "Steel - Sponge Iron": ["KIOCL Ltd.", "Jindal Steel & Power Ltd.", "Sarda Energy and Minerals Ltd.", "Jai Balaji Industries Ltd.",
                                        "Godawari Power & Ispat Ltd.", "Tata Steel Long Products Ltd.", "Vaswani Industries Ltd.", "Gyscoal Alloys Ltd.",
                                        "Ankit Metal and Power Ltd.", "JSW Ispat Special Products Ltd.", "MSP Steel & Power Ltd."],

                "Steel - CR & HR Strips": ["Mahamaya Steel Industries Ltd.", "Pennar Industries Ltd."],

                "Steel - Pig Iron": ["Kirloskar Ferrous Industries Ltd.", "Tata Metaliks Ltd.", "Sathavahana Ispat Ltd."],

                "Steel - Rolling": ["ISMT Ltd.", "Sunflag Iron and Steel Company Ltd.", "Kalyani Steels Ltd.", "Manaksia Ltd."],

                "Aluminium": ["Euro Panel Products Ltd.", "National Aluminium Company Ltd.", "Century Extrusions Ltd.", "Maan Aluminium Ltd.",
                              "Hardwyn India Ltd.", "Manaksia Aluminium Company Ltd."],

                "Steel - Tubes & Pipes": ["Surya Roshni Ltd.", "Jindal Saw Ltd.", "Zenith Steel Pipes & Industries Ltd.", "Oil Country Tubular Ltd.",
                                          "Welspun Corp Ltd.", "Man Industries (India) Ltd.", "Hi-Tech Pipes Ltd.", "Good Luck India Ltd.",
                                          "Gandhi Special Tubes Ltd.", "Maharashtra Seamless Ltd.", "Prakash Steelage Ltd.", "APL Apollo Tubes Ltd.",
                                          "Ratnamani Metals and Tubes Ltd."],
                "Steel - Large": ["Steel Authority of India Ltd.", "JSW Steel Ltd.", "Visa Steel Ltd.", "Manaksia Steels Ltd.",
                                  "Jindal Stainless (Hisar) Ltd.", "Steel Exchange India Ltd."],

                "Metals - Non Ferrous": ["Cubex Tubings Ltd.", "Hindustan Copper Ltd.", "Sagardeep Alloys Ltd.", "Hindustan Zinc Ltd.", "Ram Ratna Wires Ltd.",
                                         "Precision Wires India Ltd.", "Gravita India Ltd.", "Bhagyanagar India Ltd."],

                "Steel - GP & GC Sheets": ["Jai Corp Ltd.", "National Steel & Agro Industries Ltd."],

                "Ferro Manganese": ["Jainam Ferro Alloys Ltd."],

                "Iron & Steel": ["Shyam Metalics & Energy Ltd.", "Hariom Pipe Industries Ltd.", "Venus Pipes and Tubes Ltd.", "Mangalam Worldwide Ltd."],

                "Metals - Castings/Forgings": ["Rolex Rings Ltd."]
            },
            "Miscellaneous": {
                "Miscellaneous": ["Kridhan Infra Ltd.", "Steel City Securities Ltd.", "Jet Freight Logistics Ltd.", "Stylam Industries Ltd.",
                                  "Dredging Corporation India Ltd.", "Beardsell Ltd.", "KDDL Ltd.", "Greenlam Industries Ltd.", "Solex Energy Ltd.",
                                  "Bombay Super Hybrid Seeds Ltd.", "Omfurn India Ltd.", "Suumaya Industries Ltd.", "Lexus Granito(India) Ltd.",
                                  "Cupid Ltd.", "Shanti Overseas (India) Ltd.", "Mallcom (India) Ltd.", "Rail Vikas Nigam Ltd.", "Titan Company Ltd.",
                                  "Bohra Industries Ltd.", "New India Assurance Company Ltd.", "Shankara Building Products Ltd.", "Kaya Ltd.",
                                  "Mishra Dhatu Nigam Ltd.", "D. P. Abhushan Ltd.", "Pulz Electronics Ltd.", "ICE Make Refrigeration Ltd.",
                                  "Techindia Nirman Ltd.", "Wonderla Holidays Ltd.", "Future Enterprises DVR Ltd.", "Arvind Fashions Ltd.",
                                  "BSE Ltd.", "Vimta Labs Ltd.", "Trejhara Solutions Ltd.", "Just Dial Ltd.", "Confidence Petroleum Ltd.",
                                  "Banka Bioloo Ltd.", "SMS Lifesciences India Ltd.", "SAKUMA EXPORTS LTD. Ltd.", "One Point One Solutions Ltd.",
                                  "CL Educate Ltd.", "Bharat Dynamics Ltd.", "Moksh Ornaments Ltd.", "Lasa Supergenerics Ltd.", "Vikas Lifecare Ltd.",
                                  "CARE Ratings Ltd.", "JITF Infralogistics Ltd.", "SIS Ltd.", "Future Market Networks Ltd.", "Godrej Agrovet Ltd.",
                                  "Spencer Retail Ltd.", "Archidply Industries Ltd.", "Mittal Life Style Ltd Ltd.", "Pritika Auto Industries Ltd.",
                                  "Pansari Developers Ltd.", "JAIN IRRIGATION SYSTEMS Ltd.", "Banaras Beads Ltd.", "Gateway Distriparks Ltd.",
                                  "Infibeam Avenues Ltd.", "The Anup Engineering Ltd.", "Greenply Industries Ltd.", "Century Plyboards Ltd.",
                                  "Jubilant Industries Ltd.", "Cheviot Company Ltd.", "TeamLease Services Ltd.", "Prakash Pipes Ltd.", "CRISIL Ltd.",
                                  "Dishman Carbogen Amcis Ltd.", "Sukhjit Starch and Chemicals Ltd.", "Libas Consumer Products Ltd.", "Sheela Foam Ltd.",
                                  "RPSG VENTURES Ltd.", "BLS International Services Ltd.", "MSTC Ltd.", "Focus Lighting & Fixtures Ltd.",
                                  "Matrimony.com Ltd.", "Aspinwall and Company Ltd.", "Krishana Phoschem Ltd.", "Laxmi Cotspin Ltd.",
                                  "ICRA Ltd.", "Cheviot Company Ltd.", "Archidply Industries Ltd.", "Thomas Cook (India) Ltd.", "Venkys Ltd.",
                                  "BLS International Services Ltd.", "Galaxy Surfactants Ltd.", "Fine Organics Industries Ltd.", "MMP Industries Ltd.",
                                  "Multi Commodity Exchange of India Ltd.", "Amber Enterprises India Ltd.", "Dredging Corporation India Ltd.",
                                  "Syngene International Ltd.", "Kaveri Seed Company Ltd.", "Maheshwari Logistics Ltd.", "5paisa Capital Ltd.",
                                  "Laxmi Cotspin Ltd.", "Sikko Industries Ltd.", "Nippon Life India Asset Management Ltd.", "Akash Infraprojects Ltd.",
                                  "Arvee Laboratories Ltd.", "Continental Seeds And Chemicals Ltd.", "Nippon Life India Asset Management Ltd.",
                                  "Felix Industries Ltd.", "Jay Jalaram Technologies Ltd.", "Future Lifestyle Fashions Ltd.", "Kewal Kiran Clothing Ltd.",
                                  "Vedant Fashions Ltd.", "Go Fashion India Ltd.", "Medplus Health Services Ltd.", "Trent Ltd.", "Shoppers Stop Ltd.",
                                  "Foce India Ltd.", "Avenue Supermarts Ltd.", "V-Mart Retail Ltd.", "Aditya Birla Fashion & Retail Ltd.",
                                  "Future Enterprises Ltd.", "Heads UP Ventures Ltd.", "Agarwal Industrial Corporation Ltd.", ""]
            },
            "Oil & Gas": {
                "Oil Drilling And Exploration": ["Jindal Drilling Industries Ltd.", "Deep Energy Resources Ltd.", "GAIL India Ltd.", "Aban Offshore Ltd.",
                                                 "Asian Energy Services Ltd.", "Gujarat Gas Ltd.", "Oil India Ltd.", "Selan Exploration Technology Ltd.",
                                                 "Petronet LNG Ltd.", "Oil and Natural Gas Corporation Ltd.", "Hindustan Oil Exploration Company Ltd.",
                                                 "Gujarat State Petronet Ltd.", "Indraprastha Gas Ltd."],

                "Refineries": ["Chennai Petroleum Corporation Ltd.", "Mangalore Refinery and Petrochemicals Ltd.", "Reliance Industries Ltd.",
                               "Indian Oil Corporation Ltd.", "Mahanagar Gas Ltd.", "Bharat Petroleum Corporation Ltd.", "Hindustan Petroleum Corporation Ltd."]
            },
            "Pharmaceuticals": {
                "Pharmaceuticals & Drugs": ["Ind-Swift Laboratories Ltd.", "Nectar Lifesciences Ltd.", "Zota Health Care Ltd.", "Hester Biosciences Ltd.",
                                            "IOL Chemicals and Pharmaceuticals Ltd.", "Wanbury Ltd.", "Syncom Formulations Ltd.", "Alpa Laboratories Ltd.",
                                            "Morepen Laboratories Ltd.", "Ajanta Pharma Ltd.", "Dr Lal PathLabs Ltd.", "Bal Pharma Ltd.", "Alembic Ltd.",
                                            "Procter & Gamble Health Ltd.", "Nath Bio-Genes Ltd.", "Astec Lifesciences Ltd.", "TTK Healthcare Ltd.",
                                            "Biofil Chemicals and Pharmaceuticals Ltd.", "Venus Remedies Ltd.", "Bafna Pharmaceuticals Ltd.", "Aarti Drugs Ltd.",
                                            "Themis Medicare Ltd.", "Shilpa Medicare Ltd.", "Brooks Laboratories Ltd.", "Kilitch Drugs (India) Ltd.",
                                            "Orchid Pharma Ltd.", "Advanced Enzyme Technologies Ltd.", "RPG Life Sciences Ltd.", "Sequent Scientific Ltd.",
                                            "Pfizer Ltd.", "Albert David Ltd.", "Lincoln Pharmaceuticals Ltd.", "Caplin Point Laboratories Ltd.",
                                            "Abbott India Ltd.", "Jubilant Pharmova Ltd.", "Strides Pharma Science Ltd.", "Unichem Laboratories Ltd.",
                                            "Panacea Biotec Ltd.", "Indoco Remedies Ltd.", "Vaishali Pharma Ltd.", "JB Chemicals and Pharmaceuticals Ltd.",
                                            "Hikal Ltd.", "AstraZeneca Pharma Ltd.", "Jagsonpal Pharmaceuticals Ltd.", "Ortin Laboratories Ltd.",
                                            "Ind-Swift Ltd.", "Medicamen Biotech Ltd.", "GlaxoSmithKline Pharmaceuticals Ltd.", "Laurus Labs Ltd.",
                                            "Lyka Labs Ltd.", "Granules India Ltd.", "NGL Fine Chem Ltd.", "Sanofi India Ltd.", "Marksans Pharma Ltd.",
                                            "Sun Pharmaceutical Industries Ltd.", "Neuland Laboratories Ltd.", "SMS Pharmaceuticals Ltd.", "FDC Ltd.",
                                            "Cipla Ltd.", "Dr Reddys Laboratories Ltd.", "Krebs Biochemicals & Industries Ltd.", "Ipca Laboratories Ltd.",
                                            "Alembic Pharmaceuticals Ltd.", "Glenmark Pharma Ltd.", "Torrent Pharmaceuticals Ltd.", "Wockhardt Ltd.",
                                            "Biocon Ltd.", "Aurobindo Pharma Ltd.", "Kopran Ltd.", "Zydus Lifesciences Ltd.", "Divis Laboratories Ltd.",
                                            "Suven Life Sciences Ltd.", "Alkem Laboratories Ltd.", "Gufic Biosciences Ltd.", "Natco Pharma Ltd.",
                                            "Sun Pharma Advanced Research Company Ltd.", "Piramal Enterprises Ltd.", "Vivimed Labs Ltd.", "Lupin Ltd.",
                                            "Beta Drugs Ltd.", "Mangalam Drugs & Organics Ltd."]
            },
            "Retail/Real Estate": {
                "Construction - Residential & Commercial Complexes": ["Macrotech Developers Ltd.", "Shriram Properties Ltd.", "Sonu Infratech Ltd.",
                                                                      "Eldeco Housing and Industries Ltd."],

                "Construction & Contracting - Real Estate": ["DB Realty Ltd.", "PVP Ventures Ltd.", "Shradha Infraprojects Ltd.", "Prozone Intu Properties Ltd.",
                                                             "Housing Development and Infrastructure Ltd.", "Housing & Urban Development Corporation Ltd.",
                                                             "Phoenix Mills Ltd.", "Emami Realty Ltd.", "Dhruv Consultancy Services Ltd.", "Godrej Properties Ltd.",
                                                             "Indiabulls Real Estate Ltd.", "Parsvnath Developers Ltd.", "Brigade Enterprises Ltd.",
                                                             "Oberoi Realty Ltd.", "Hubtown Ltd.", "Sunteck Realty Ltd.", "Kolte-Patil Developers Ltd.",
                                                             "PNC Infratech Ltd.", "Puravankara Ltd.", "Prestige Estates Projects Ltd.", "Omaxe Ltd.",
                                                             "Landmark Property Development Company Ltd.", "Marathon Nextgen Realty Ltd.", "Sobha Ltd.",
                                                             "DLF Ltd.", "Anant Raj Ltd.", "Nila Infrastructures Ltd.", "Sumit Woods Ltd.", "TARC Ltd.",
                                                             "Nila Infrastructures Ltd.", "Hemisphere Properties India Ltd.", "Mindspace Business Parks REIT Ltd."]
            },
            "Services": {
                "Shipping": ["Lancer Containers Lines Ltd.", "Accuracy Shipping Ltd.", "Reliance Naval and Engineering Ltd.", "Shipping Corporation of India Ltd.",
                             "Essar Shipping Ltd.", "Gujarat Pipavav Port Ltd.", "Great Eastern Shipping Company Ltd.", "Mercator Ltd.", "Shreyas Shipping Ltd.",
                             "Seamec Ltd."],
                "Hotels": ["Speciality Restaurants Ltd.", "EIH Ltd.", "Lemon Tree Hotels Ltd.", "Chalet Hotels Ltd.", "Kamat Hotels (India) Ltd.",
                           "EIH Associated Hotels Ltd.", "Mahindra Holidays and Resorts India Ltd.", "India Tourism Development Corporation Ltd.",
                           "Asian Hotels (East) Ltd.", "Indian Hotels Company Ltd.", "Oriental Hotels Ltd.", "Advani Hotels and Resorts (India) Ltd.",
                           "Country Club Hospitality & Holidays Ltd.", "TGB Banquets and Hotels Ltd.", "Asian Hotels (East) Ltd.", "HLV Ltd.",
                           "Royal Orchid Hotels Ltd.", "The Byke Hospitality Ltd.", "Taj GVK Hotels & Resorts Ltd."],

                "Couriers": ["Gati Ltd.", "Blue Dart Express Ltd."],

                "Transport & Logistics": ["Arshiya Ltd.", "Sical Logistics Ltd.", "Allcargo Logistics Ltd.", "Snowman Logistics Ltd.", "Total Transport Systems Ltd.",
                                          "Ritco Logistics Ltd.", "Orissa Bengal Carrier Ltd.", "Navkar Corporation Ltd.", "SpiceJet Ltd.", "Jet Airways Ltd.",
                                          "Interglobe Aviation Ltd.", "Future Supply Chain Solutions Ltd.", "Transport Corporation of India Ltd.",
                                          "Container Corporation of India Ltd.", "VRL Logistics Ltd.", "Jalan Transolutions Ltd."],

                "Hospitals & Medical Services": ["Shalby Ltd.", "Kovai Medical Center and Hospital Ltd.", "Indraprastha Medical Corporation Ltd.",
                                                 "Bajaj Healthcare Ltd.", "Thyrocare Technologies Ltd.", "Healthcare Global Enterprises Ltd.",
                                                 "Poly Medicure Ltd.", "Fortis Healthcare Ltd.", "Narayana Hrudayalaya Ltd.", "Metropolis Healthcare Ltd.",
                                                 "Apollo Hospitals Enterprises Ltd.", "Lotus Eye Care Hospital Ltd."],

                "Diamond Cutting & Jewellery & Precious Metals": ["PC Jeweller Ltd.", "Tribhovandas Bhimji Zaveri Ltd.", "Renaissance Global Ltd.",
                                                                  "Lypsa Gems and Jewellery Ltd.", "Rajesh Exports Ltd.", "Thangamayil Jewellery Ltd.",
                                                                  "Goldiam International Ltd.", "Goenka Diamond and Jewels Ltd."],

                "Trading": ["Swan Energy Ltd.", "State Trading Corporation of India Ltd.", "MMTC Ltd.", "Adani Enterprises Ltd.", "PTC India Ltd.",
                            "India Motor Parts and Accessories Ltd.", "Uniphos Enterprises Ltd.", "Control Print Ltd.", "Shaily Engineering Plastics Ltd."]
            },
            "Telecom": {
                "Telecommunications - Service": ["Vodafone Idea Ltd.", "Tata Communications Ltd.", "Bharti Airtel Ltd.", "Uniinfo Telecom Services Ltd.",
                                                 "Olectra Greentech Ltd.", "Mahanagar Telephone Nigam Ltd.", "Tata Teleservices (Maharashtra) Ltd.",
                                                 "OnMobile Global Ltd."],

                "Cables - Telephone": ["Vindhya Telelink Ltd.", "Paramount Communications Ltd.", "CMI Ltd.", "Birla Cable Ltd.", "Finolex Cables Ltd.",
                                       "Surana Telecom and Power Ltd.", "Sterlite Technologies Ltd.", "Tamilnadu Telecommunications Ltd.",
                                       "Aksh Optifibre Ltd."],

                "Telecommunications - Equipment": ["Shyam Telecom Ltd.", "NELCO Ltd.", "GTL Ltd.", "HFCL Ltd.", "ITI Ltd.", "Kavveri Telecom Products Ltd.",
                                                   "Tejas Networks Ltd.", "GTL Infrastructure Ltd.", "INDUS TOWERS Ltd.", "Honeywell Automation Ltd.",
                                                   "Digispice Technologies Ltd."]
            },

            "Tobacco": {
                "Cigarettes": ["VST Industries Ltd.", "Golden Tobacco Ltd.", "Kothari Products Ltd.", "ITC Ltd."]
            },

            "Utilities": {
                "Power - Generation & Distribution": ["JSW Energy Ltd.", "Indowind Energy Ltd.", "Schneider Electric Infrastructure Ltd.",
                                                      "NLC India Ltd.", "RattanIndia Power Ltd.", "Reliance Infrastructure Ltd.", "NHPC Ltd.",
                                                      "Mitcon Consultancy and Engineering Services Ltd.", "Gujarat Industries Power Co. Ltd.",
                                                      "BF Utilities Ltd.", "Power Grid Corporation of India Ltd.", "DPSC Ltd.", "CESC Ltd.",
                                                      "The Tata Power Company Ltd.", "Torrent Power Ltd.", "NTPC Ltd.", "DPSC Ltd.", "SJVN Ltd.",
                                                      "Reliance Power Ltd.", "Inox Wind Ltd.", "Orient Green Power Company Ltd.", "S E Power Ltd.",
                                                      "Energy Development Company Ltd.", "GVK Power & Infrastructure Ltd.", "Suzlon Energy Ltd."]
            }

        }

        return sectorIndustryJson
