import pygame

FPS = 60
# background color
BG_COLOR = (48, 39, 32)
# Extend color
EXTEND_BG_COLOR = (24, 89, 117)

# Font file path
FONT_PATH = "suissnord.otf"

# Sprite file path
SPRITE_PATH = 'sprites'

# A 2D vector to manage the position of the blocks on the screen
vec = pygame.math.Vector2

TILE_SIZE = 50
FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_EXTEND_W, FIELD_EXTEND_H  = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_EXTEND_W, FIELD_RES[1] * FIELD_EXTEND_H

# The inital offset is set for the top middle of the screen
INIT_OFFSET = vec(FIELD_W // 2, 0)

#
ANIM_TIME = 250

# The key is the direction the value is how much it is moved
DIRECTION_KEYS = {'L' : vec(-1, 0), 'R': vec(1, 0), 'D': vec(0, 1)}

# Shape layouts, the first block is always the pivot point for rotations
SHAPES = {
    'O': [(0, 0), (0, -1), (1,-1), (1, 0)],
    'I': [(0, 0), (0, -1), (0, 1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (0, -1), (-1, -1), (1, 0)],
    'L': [(0, 0), (0, -1), (0, -2), (1, 0)],
    'J': [(0, 0), (0, -1), (0, -2), (-1, 0)],
    'T': [(0, 0), (0, -1), (1, -1), (-1, -1)]
}

QUESTIONS = [
    ('B)', "What is the primary cause of global warming? A) Deforestation B) Greenhouse gases C) Overpopulation"),
    ('C)', "Which of these is a renewable energy source? A) Coal B) Natural gas C) Solar"),
    ('A)', "What does biodiversity refer to? A) Variety of life in an ecosystem B) Number of forests in an area C) Availability of clean water"),
    ('B)', "Which gas is most responsible for the greenhouse effect? A) Oxygen B) Carbon dioxide C) Helium"),
    ('A)', "What is the process of cutting down trees without replanting called? A) Deforestation B) Afforestation C) Reforestation"),
    ('C)', "Which of the following is not a fossil fuel? A) Oil B) Coal C) Wind"),
    ('B)', "What does 'sustainable development' mean? A) Using resources without future considerations B) Development that meets present needs without harming future generations C) Rapid industrialization"),
    ('A)', "Which type of pollution is caused by excessive sound? A) Noise pollution B) Air pollution C) Soil pollution"),
    ('C)', "What is the main reason for the ozone layer's depletion? A) Carbon emissions B) Deforestation C) CFCs (chlorofluorocarbons)"),
    ('A)', "Which of the following contributes to acid rain? A) Sulfur dioxide emissions B) Methane emissions C) Oxygen production"),
    ('C)', "What does 'carbon footprint' measure? A) Carbon in the soil B) Forest area lost C) Total greenhouse gases produced by an individual or organization"),
    ('B)', "Which is the largest freshwater reservoir on Earth? A) Rivers B) Glaciers C) Lakes"),
    ('A)', "What is the main threat to coral reefs? A) Rising ocean temperatures B) Overfishing C) Tourism"),
    ('C)', "What is the term for planting trees to combat deforestation? A) Soil reclamation B) Erosion C) Afforestation"),
    ('B)', "What is the primary source of plastic waste in oceans? A) Industrial waste B) Improperly disposed plastic from households C) Fishing nets"),
    ('A)', "Which of these gases is responsible for acid rain? A) Sulfur dioxide B) Carbon dioxide C) Nitrogen"),
    ('C)', "What percentage of the Earth's surface is covered by water? A) 29% B) 50% C) 71%"),
    ('B)', "Which renewable energy source relies on the heat from the Earth's interior? A) Wind energy B) Geothermal energy C) Solar energy"),
    ('A)', "What is eutrophication? A) Overgrowth of algae due to excess nutrients B) Soil erosion caused by wind C) Excessive deforestation"),
    ('C)', "What is the main goal of the Paris Agreement? A) Reduce deforestation B) End plastic pollution C) Limit global warming to below 2°C"),
    ('A)', "Which of these is an effect of deforestation? A) Loss of biodiversity B) Increased water resources C) Improved air quality"),
    ('B)', "Which type of farming reduces environmental impact? A) Intensive farming B) Organic farming C) Industrial farming"),
    ('C)', "Which of the following is a consequence of global warming? A) Decreased hurricanes B) Increased rainfall C) Rising sea levels"),
    ('A)', "What are biodegradable materials? A) Materials that can be broken down by bacteria or other organisms B) Synthetic materials C) Materials that remain in the environment indefinitely"),
    ('C)', "Which of the following is a method to conserve water? A) Leaving taps open B) Washing cars frequently C) Rainwater harvesting"),
    ('B)', "What is composting? A) Burning waste materials B) Converting organic waste into fertilizer C) Recycling plastics"),
    ('A)', "What does the '3Rs' in waste management stand for? A) Reuse, Reduce, Recycle B) Renew, Refill, Recycle C) Reduce, Refill, Replant"),
    ('C)', "What is the primary source of energy for the Earth? A) Wind B) Fossil fuels C) Sun"),
    ('A)', "Which of the following is an example of non-point source pollution? A) Runoff from agricultural fields B) Factory emissions C) Oil spills"),
    ('C)', "What is the main cause of smog? A) Overfishing B) Deforestation C) Car emissions"),
    ('A)', "Which of these is an endangered species? A) African elephant B) House sparrow C) Grey wolf"),
    ('C)', "Which layer of the atmosphere contains the ozone layer? A) Troposphere B) Mesosphere C) Stratosphere"),
    ('B)', "Which practice helps in reducing soil erosion? A) Clear-cutting B) Crop rotation C) Overgrazing"),
    ('A)', "What is the main cause of urban heat islands? A) Concrete and asphalt surfaces B) Overpopulation C) Increased vegetation"),
    ('C)', "Which type of energy is derived from organic matter? A) Geothermal energy B) Wind energy C) Biomass energy"),
    ('A)', "Which of these practices is environmentally friendly? A) Recycling materials B) Burning waste C) Using plastic bags"),
    ('B)', "What is the process of water turning into vapor? A) Condensation B) Evaporation C) Precipitation"),
    ('C)', "Which natural phenomenon can be intensified by climate change? A) Earthquakes B) Volcanic eruptions C) Hurricanes"),
    ('B)', "What is the main component of smog? A) Nitrogen B) Ozone C) Oxygen"),
    ('A)', "What is the leading cause of species extinction? A) Habitat loss B) Overhunting C) Pollution"),
    ('C)', "Which of these countries produces the most carbon emissions? A) India B) United States C) China"),
    ('B)', "What is the main purpose of wetlands? A) Waste disposal B) Water purification and flood control C) Industrial use"),
    ('C)', "What is the term for planting crops and trees together? A) Crop rotation B) Monoculture C) Agroforestry"),
    ('A)', "Which international day is celebrated to raise environmental awareness? A) Earth Day B) Global Warming Day C) Biodiversity Day"),
    ('C)', "What is the main component of acid rain? A) Hydrochloric acid B) Carbonic acid C) Sulfuric acid"),
    ('B)', "What does the term 'greenwashing' refer to? A) Planting trees B) Marketing deceptive eco-friendly claims C) Recycling plastics"),
    ('A)', "Which is the largest source of ocean oil pollution? A) Land runoff B) Offshore drilling C) Shipping accidents"),
    ('C)', "What is the best way to reduce plastic pollution? A) Dump plastic waste in landfills B) Burn plastic waste C) Ban single-use plastics"),
    ('B)', "Which of the following gases contributes to ocean acidification? A) Methane B) Carbon dioxide C) Nitrogen"),
    ('C)', "What is the main purpose of renewable energy? A) Generate profit for corporations B) Increase fossil fuel use C) Reduce environmental impact"),
]