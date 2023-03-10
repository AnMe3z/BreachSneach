import csv, random

header = ['id', 'entity', 'year', 'records', 'type', 'method']

# dopustimi danni ot koito da se zimat na random
entities = ['Acme', 'Adroit', 'Agile', 'Allure', 'Ambrosia', 'Amplify', 'Anchor', 'Apex', 'Aquila', 'Arctic', 'Arista', 'Ascent', 'Ascension', 'Asteria', 'Astra', 'Atlas', 'Atmos', 'Aurora', 'Avant', 'Avenue', 'Bask', 'Beacon', 'Beeswax', 'Bene', 'Bison', 'Blaze', 'Bloom', 'Blu', 'Bluebird', 'Bluestone', 'Boost', 'Borealis', 'Breezy', 'Bright', 'Brio', 'Brook', 'Buckle', 'Cactus', 'Calm', 'Calypso', 'Canary', 'Candor', 'Cape', 'Capital', 'Caramel', 'Cascade', 'Castle', 'Catalyst', 'Cedar', 'Celestial', 'Cerulean', 'Champ', 'Chase', 'Chroma', 'Cinder', 'Circuit', 'Citadel', 'Cityscape', 'Clarity', 'Climb', 'Cloud', 'Coastal', 'Comet', 'Compass', 'Concord', 'Connect', 'Constellation', 'Copper', 'Coral', 'Cornerstone', 'Cosmic', 'Cove', 'Crest', 'Crystal', 'Cub', 'Cypress', 'Dapper', 'Dawn', 'Daybreak', 'Delta', 'Dew', 'Diamond', 'Direct', 'Discover', 'Dolphin', 'Dove', 'Dream', 'Dynamo', 'Eagle', 'Echo', 'Eclipse', 'Elevate', 'Ember', 'Empower', 'Encore', 'Endeavor', 'Endless', 'Endurance', 'Energy', 'Enlighten', 'Ensemble', 'Envy', 'Epiphany', 'Equinox', 'Era', 'Essence', 'Eternal', 'Euphoria', 'Evoke', 'Exalt', 'Excel', 'Expedite', 'Expert', 'Explorer', 'Express', 'Falcon', 'Fathom', 'Feather', 'Fiesta', 'Finesse', 'Fireside', 'Flame', 'Flare', 'Flourish', 'Flow', 'Fluent', 'Focus', 'Forge', 'Fortune', 'Foster', 'Fountain', 'Fox', 'Fresh', 'Fusion', 'Galaxy', 'Gaze', 'Gentle', 'Glacier', 'Glisten', 'Glow', 'Golden', 'Grace', 'Gradient', 'Grand', 'Gravity', 'Green', 'Grow', 'Guardian', 'Halo', 'Harmony', 'Harvest', 'Haven', 'Heart', 'Heirloom', 'Helix', 'Heritage', 'Hero', 'Horizon', 'Illuminate', 'Imagine', 'Impact', 'Impress', 'Infinity', 'Innovate', 'Insight', 'Inspire', 'Integrity', 'Interact', 'Invent', 'Invoke', 'Iris', 'Island', 'Ivory', 'Jade', 'Journey', 'Jubilee', 'Jungle', 'Keystone', 'Kinetic', 'Kudos', 'Lagoon', 'Lark', 'Launch', 'Lavender', 'Legacy', 'Legend', 'Leopard', 'Liberate', 'Magnetic', 'Majestic', 'Momentum', 'Meridian', 'Millennium', 'Mighty', 'Mingle', 'Mirage', 'Mission', 'Mist', 'Momentum', 'Monarch', 'Moonbeam', 'Morning', 'Motivate', 'Mountain', 'Mystic', 'Myth', 'Nebula', 'Nexus', 'Nimble', 'Nirvana', 'Noble', 'Nomad', 'Nova', 'Nurture', 'Oasis', 'Oceanic', 'Octave', 'Odyssey', 'Onyx', 'Optimize', 'Oracle', 'Orbit', 'Organic', 'Orient', 'Origin', 'Outlook', 'Ovation', 'Overdrive', 'Overland', 'Overlook', 'Owl', 'Pace', 'Pacific', 'Palm', 'Panorama', 'Paradigm', 'Paragon', 'Paramount', 'Patriot', 'Peak', 'Pegasus', 'Pelican', 'Pendulum', 'Perception', 'Perennial', 'Performance', 'Perpetual', 'Perspective', 'Phoenix', 'Pinnacle', 'Pioneer', 'Pixel', 'Platinum', 'Polaris', 'Polished', 'Poppy', 'Portico', 'Positive', 'Precision', 'Premier', 'Prestige', 'Prime', 'Prism', 'Proactive', 'Prodigy', 'Progress', 'Prospect', 'Proven', 'Pulse', 'Puma', 'Quest', 'Quick', 'Radiance', 'Rainbow', 'Raven', 'Recharge', 'Redwood', 'Reflection', 'Refresh', 'Regal', 'Regenerate', 'Relax', 'Reliance', 'Reliable', 'Renew', 'Resilient', 'Resource', 'Revive', 'Revolution', 'Ripple', 'Rise', 'River', 'Roam', 'Robust', 'Rock', 'Rose', 'Royal', 'Sage', 'Sapphire', 'Savvy', 'Scenic', 'Scope', 'Seamless', 'Seasons', 'Secure', 'Sequoia', 'Serene', 'Shine', 'Shoreline', 'Sierra', 'Signature', 'Silk', 'Silver', 'Simplicity', 'Sky', 'Sleek', 'Smile', 'Smooth', 'Solar', 'Solstice', 'Soul', 'Sound', 'Sovereign', 'Spectrum', 'Speed', 'Spice', 'Spirit', 'Spirited', 'Splash', 'Spotlight', 'Spring', 'Sprout', 'Stamina', 'Star', 'Stardust', 'Stargaze', 'Starlight', 'Starlit', 'Starry', 'Stellar', 'Stride', 'Strobe', 'Strong', 'Sublime', 'Succeed', 'Summit', 'Sundance', 'Sundial', 'Sunny', 'Sunrise', 'Sunset', 'Super', 'Supreme', 'Surge', 'Swift', 'Symphony', 'Synergy', 'Talisman', 'Tangerine', 'Taurus', 'Tempest', 'Tempo', 'Terra', 'Terrace', 'Thunder', 'Tidal', 'Timeless', 'Timely', 'Titan', 'Topaz', 'Torch', 'Tradition', 'Trail', 'Tranquil', 'Transcend', 'Transit', 'Ultrasonic', 'Unicorn', 'Union', 'Unique', 'Unison', 'Unity', 'Universe', 'Unleash', 'Unlock', 'Unplugged', 'Unwind', 'Upbeat', 'Upcycle', 'Upgrade', 'Uplift', 'Upright', 'Upscale', 'Upstart', 'Uptrend', 'Urgent', 'Usher', 'Utilize', 'Vacation', 'Valiant', 'Valley', 'Valor', 'Vantage', 'Vault', 'Velocity', 'Vendetta', 'Venture', 'Veranda', 'Verdant', 'Veritas', 'Vertex', 'Verve', 'Vestige', 'Vibrant', 'Victory', 'Vigor', 'Viking', 'Village', 'Vintage', 'Violet', 'Vision', 'Vital', 'Viva', 'Vivid', 'Vogue', 'Voice', 'Volcano', 'Voltage', 'Volume', 'Vortex', 'Voyage', 'Wander', 'Wave', 'Wealth', 'Weave', 'Web', 'Wedge', 'Weekend', 'Welcome', 'Wellness', 'West', 'Whisper', 'Whole', 'Wicked', 'Wilderness', 'Willow', 'Wind', 'Wing', 'Winning', 'Winter', 'Wire', 'Wise', 'Wish', 'Wizard', 'Wonder', 'Woodland', 'Workshop', 'Worldwide', 'Worthy', 'Xenon', 'Xpand', 'Xpress', 'Yacht', 'Yearn', 'Yellow', 'Yoga', 'Zenith', 'Zeppelin', 'Zero', 'Zest', 'Zion', 'Zone', 'Zephyr', 'Zigzag', 'Zipper', 'Zodiac', 'Zoom', 'Able', 'Accent', 'Acclaim', 'Accolade', 'Accord', 'Achieve', 'Acme', 'Actuate', 'Acumen', 'Admire', 'Adorn', 'Advance', 'Advent', 'Adventure', 'Aegis', 'Affinity', 'Agile', 'Aim', 'Air', 'Airstream', 'Alacrity', 'Alchemy', 'Alert', 'Alliance', 'Ally', 'Alpha', 'Alpine', 'Altitude', 'Ambassador', 'Ambient', 'Amber', 'Amble', 'Amity', 'Anchorage', 'Angelic', 'Angular', 'Animated', 'Anthem', 'Antique', 'Aperçu', 'Apex', 'Apollo', 'Apothecary', 'Aqua', 'Aquamarine', 'Arbor', 'Arcadia', 'Arch']
year = 2010 # kym tova shte se dobavq random chislo ot 1 do 13
type = ['Orphanage', 
        'Hospital', 
        'Bank', 
        'Supermarket', 
        'Hardware Store', 
        'School', 
        'Shooting Range', 
        'Kindergarden', 
        'Government', 
        'Non-Profit',
        'Train Station',
        'Small Business',
        'Local Shop',
        'Pizzeria',
        'Sandwitch Shop',
        'Burget Franchaise']
method = ['Malware',
          'DoS Attack',
          'Worm Virus',
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

with open('Data/trustWorthy-database(Test).csv', 'w') as file: #write file
    writer = csv.writer(file)

with open('Data/trustWorthy-database(Test).csv', 'w') as file: #write file
    writer = csv.writer(file)
    i = 0

    while i <= 2000 : #number of entries
        a = random.randint(0, 100000)
        b = random.randint(0,1000)
        i+=1
        data = [i, entities[random.randint(0, len(entities)-1)], year + random.randint(0, 13), i * a, type[random.randint(0, len(type)-1)], method[random.randint(0, len(method)-1)]]
        writer.writerow(data)
        