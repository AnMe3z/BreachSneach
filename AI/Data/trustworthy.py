import csv, random

header = ['id', 'entity', 'year', 'records', 'organization', 'type', 'method', 'sources']

# dopustimi danni ot koito da se zimat na random
entities = ['3Com', 'Corp 3M', 'Company A.G.', 'Edwards', 'Inc. Abbott', 'Laboratories Abercrombie', '&', 'Fitch', 'Co. ABM', 'Industries', 'Incorporated Ace', 'Hardware', 'Corporation ACT', 'Manufacturing', 'Inc. Acterna', 'Corp. Adams', 'Resources', '&', 'Energy,', 'Inc. ADC', 'Telecommunications,', 'Inc. Adelphia', 'Communications', 'Corporation Administaff,', 'Inc. Adobe', 'Systems', 'Incorporated Adolph', 'Coors', 'Company Advance', 'Auto', 'Parts,', 'Inc. Advanced', 'Micro', 'Devices,', 'Inc. AdvancePCS,', 'Inc. Advantica', 'Restaurant', 'Group,', 'Inc. The', 'AES', 'Corporation Aetna', 'Inc. Affiliated', 'Computer', 'Services,', 'Inc. AFLAC', 'Incorporated AGCO', 'Corporation Agilent', 'Technologies,', 'Inc. Agway', 'Inc. Apartment', 'Investment', 'and', 'Management', 'Company Air', 'Products', 'and', 'Chemicals,', 'Inc. Airborne,', 'Inc. Airgas,', 'Inc. AK', 'Steel', 'Holding', 'Corporation Alaska', 'Air', 'Group,', 'Inc. Alberto-Culver', 'Company Albertson', 'Inc. Alcoa', 'Inc. Alleghany', 'Corporation Allegheny', 'Energy,', 'Inc. Allegheny', 'Technologies', 'Incorporated Allergan,', 'Inc. ALLETE,', 'Inc. Alliant', 'Energy', 'Corporation Allied', 'Waste', 'Industries,', 'Inc. Allmerica', 'Financial', 'Corporation The', 'Allstate', 'Corporation ALLTEL', 'Corporation The', 'Alpine', 'Group,', 'Inc. Amazon.com,', 'Inc. AMC', 'Entertainment', 'Inc. American', 'Power', 'Conversion', 'Corporation Amerada', 'Hess', 'Corporation AMERCO Ameren', 'Corporation America', 'West', 'Holdings', 'Corporation American', 'Axle', '&', 'Manufacturing', 'Holdings,', 'Inc. American', 'Eagle', 'Outfitters,', 'Inc. American', 'Electric', 'Power', 'Company,', 'Inc. American', 'Express', 'Company American', 'Financial', 'Group,', 'Inc. American', 'Greetings', 'Corporation American', 'International', 'Group,', 'Inc. American', 'Standard', 'Companies', 'Inc. American', 'Water', 'Works', 'Company,', 'Inc. AmerisourceBergen', 'Corporation Ames', 'Department', 'Stores,', 'Inc. Amgen', 'Inc. Amkor', 'Inc. TruServ', 'Corporation TRW', 'Inc TXU', 'Corp Tyson', 'Foods', 'Inc U.S.', 'Bancorp U.S.', 'Industries', 'Inc. UAL', 'Corporation UGI', 'Corporation Unified', 'Western', 'Grocers', 'Inc Union', 'Pacific', 'Corporation Union', 'Planters', 'Corp Unisource', 'Energy', 'Corp Unisys', 'Corporation United', 'Auto', 'Group', 'Inc United', 'Defense', 'Industries', 'Inc. United', 'Parcel', 'Service', 'Inc United', 'Rentals', 'Inc United', 'Stationers', 'Inc United', 'Technologies', 'Corporation UnitedHealth', 'Group', 'Incorporated Unitrin', 'Inc Universal', 'Corporation Universal', 'Forest', 'Products', 'Inc Universal', 'Health', 'Services', 'Inc Unocal', 'Corporation Unova', 'Inc UnumProvident', 'Corporation URS', 'Corporation US', 'Airways', 'Group', 'Inc US', 'Oncology', 'Inc USA', 'Interactive USFreighways', 'Corporation USG', 'Corporation UST', 'Inc Valero', 'Energy', 'Corporation Valspar', 'Corporation Value', 'City', 'Department', 'Stores', 'Inc Varco', 'International', 'Inc Vectren', 'Corporation Veritas', 'Software', 'Corporation Verizon', 'Communications', 'Inc VF', 'Corporation Viacom', 'Inc Viad', 'Corp Viasystems', 'Group', 'Inc Vishay', 'Intertechnology', 'Inc Visteon', 'Corporation Volt', 'Information', 'Sciences', 'Inc Vulcan', 'Materials', 'Company W.R.', 'Berkley', 'Corporation W.R.', 'Grace', '&', 'Co W.W.', 'Grainger', 'Inc Wachovia', 'Corporation Wakenhut', 'Corporation Walgreen', 'Co Wallace', 'Computer', 'Services', 'Inc Wal-Mart', 'Stores', 'Inc Walt', 'Disney', 'Co Walter', 'Industries', 'Inc Washington', 'Mutual', 'Inc Washington', 'Post', 'Co. Waste', 'Management', 'Inc Watsco', 'Inc Weatherford', 'International', 'Inc Weis', 'Markets', 'Inc. Wellpoint', 'Health', 'Networks', 'Inc Wells', 'Fargo', '&', 'Company Wendy', 'International', 'Inc Werner', 'Enterprises', 'Inc WESCO', 'International', 'Inc Western', 'Digital', 'Inc Western', 'Gas', 'Resources', 'Inc WestPoint', 'Stevens', 'Inc Weyerhauser', 'Company WGL', 'Holdings']
year = 2010 # kym tova shte se dobavq random chislo ot 1 do 13
type = ['Orphanage', 
        'Hospital', 
        'Bank', 
        'Supermarket', 
        'Hardware Store', 
        'School', 
        'Shooting Range', 
        'Kindergarden', 
        'Goverment', 
        'Non-Profit',
        'Train Station',
        'Small Business',
        'Local Shop',
        'Pizzaria',
        'Sandwitch Shop',
        'Burget Franchaise']
method = ['Malware',
          'DoS Attack',
          'DDoS Attack',
          'Phishing',
          'Spoofing',
          'Identity-Based Attack',
          'Code Injections Attack',
          'Supply chain Attack',
          'Insider Attack',
          'Man In The Middle Attack',
          'SQL Injection Attack',
          'Zero-Day Exploit Attack',
          'DNS Tunneling Attack',
          '51% Attack',
          'Business Email Compromise Attack',
          'Cryptojacking Attack',
          'Drive-by Attack',
          'Cross-site Scripting Attack'
          ]

with open('ai/data/trust-database.csv', 'w') as file:
    writer = csv.writer(file)

with open('ai/data/trust-database.csv', 'w') as file:
    writer = csv.writer(file)
    i = 0

    while i <= 10000 :
        a = random.randint(0, 100000)
        b = random.randint(0,1000)
        i+=1
        data = [i, entities[random.randint(0, len(entities)-1)], year + random.randint(0, 13), i * a, type[random.randint(0, len(type)-1)], method[random.randint(0, len(method)-1)]]
        writer.writerow(data)
        