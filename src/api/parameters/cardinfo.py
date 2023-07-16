from src.api.api import Parameter

card_archetype = Parameter(
    name="archetype",
    data_type="string",
    description="Filter the cards by archetype (e.g. 'Dark Magician', 'Prank-Kids', 'Blue-Eyes', etc)."
)

card_atk = Parameter(
    name="atk",
    data_type="string",  # TODO: Change to integer and create abstraction for equation symbols
    description="Filter by atk value. Allows to use equation symbols ('lt': less than, 'lte': less than or equals to, "
                "'gt': greater than, 'gte': greater than or equals to) [e.g. 'lt2500': atk is less than 2500]."
)

card_attribute = Parameter(
    name="attribute",
    data_type="string",
    description="Filter by the card attribute (Dark, Divine, Earth, Fire, Light, Water, Wind). Allows to pass "
                "multiple comma separated attributes.",
    options=["Dark", "Divine", "Earth", "Fire", "Light", "Water", "Wind"],
    multi_selection=True
)

card_banlist = Parameter(
    name="banlist",
    data_type="string",
    description="Filter the cards by banlist.",
    options=["Goat", "OCG", "TCG"]
)

card_date_region = Parameter(
    name="dateregion",
    data_type="string",  # TODO: Change to date and force it to be in a single format (e.g. YYYY-MM-DD)
    description="Query release dates for cards and the region of these release dates (OCG or TCG). The date format "
                "can be slightly varied as the API picks up different formats and converts it regardless [e.g. Jan 01 "
                "2000 or 01/01/2000]."
)

card_def = Parameter(
    name="def",
    data_type="string",  # TODO: Change to integer and create abstraction for equation symbols
    description="Filter by def value. Allows to use equation symbols ('lt': less than, 'lte': less than or equals to, "
                "'gt': greater than, 'gte': greater than or equals to) [e.g. 'gt2100': def is greater than 2100]."
)

card_end_date = Parameter(
    name="enddate",
    data_type="string",  # TODO: Change to date and force it to be in a single format (e.g. YYYY-MM-DD)
    description="Query release dates for cards and the region of these release dates (OCG or TCG). The date format "
                "can be slightly varied as the API picks up different formats and converts it regardless [e.g. Jan 01 "
                "2000 or 01/01/2000]."
)

card_fname = Parameter(
    name="fname",
    data_type="string",
    description="A fuzzy search using a string [e.g. 'Magician' will search by all cards with 'Magician' in the name]."
)

card_format = Parameter(
    name="format",
    data_type="string",
    description="Sort the format of the cards (TCG, Goat, OCG Goat, Speed Duel, Rush Duel, Duel Links). Note: Duel "
                "Links is not 100% accurate but is close. Using TCG results in all cards with a set TCG Release Date "
                "and excludes Speed Duel/Rush Duel cards.",
    options=["Duel Links", "Goat", "OCG Goat", "Rush Duel", "Speed Duel", "TCG"]
)

card_has_effect = Parameter(
    name="has_effect",
    data_type="boolean",
    description="Check whether a card actually has an effect or not. Examples of cards that do not have an actual "
                "effect: Black Skull Dragon, LANphorhynchus, etc."
)

card_id = Parameter(
    name="id",
    data_type="integer",
    description="Card password."
)

card_language = Parameter(
    name="language",
    data_type="string",
    description="Card language (None: English, 'FR': French, 'DE': German, 'IT': Italian, 'PT': Portuguese).",
    options=[None, "DE", "FR", "IT", "PT"],
    default_value="PT"
)

card_level = Parameter(
    name="level",
    data_type="string",  # TODO: Change to integer and create abstraction for equation symbols
    description="Filter by card level or rank. Allows to use equation symbols ('lt': less than, 'lte': less than or "
                "equals to, 'gt': greater than, 'gte': greater than or equals to) [e.g. 'lte8': level is less than or "
                "equal to 8]."
    )

card_link = Parameter(
    name="link",
    data_type="string",  # TODO: Change to integer and create abstraction for equation symbols
    description="Filter the cards by link value. Allows to use equation symbols ('lt': less than, 'lte': less than or "
                "equals to, 'gt': greater than, 'gte': greater than or equals to) [e.g. 'gte4': link value is greater "
                "than or equal to 4]."
)

card_linkmarker = Parameter(
    name="linkmarker",
    data_type="string",
    description="Filter the cards by link marker value (Top, Bottom, Left, Right, Bottom-Left, Bottom-Right, Top-Left, "
                "Top-Right). Allows to pass multiple comma separated linkmarkers.",
    options=["Bottom", "Bottom-Left", "Bottom-Right", "Left", "Right", "Top", "Top-Left", "Top-Right"],
    multi_selection=True
)

card_misc = Parameter(
    name="misc",
    data_type="string",
    description="Show additional response info (Card Views, Beta Name, etc). Misc accepts 'Yes'.",
    options=["Yes"]
)

card_name = Parameter(
    name="name",
    data_type="string",
    description="The exact name of the card. It's possible to pass multiple | separated names to this parameter (e.g. "
                "'Baby Dragon|Time Wizard')."
)

card_race = Parameter(
    name="race",
    data_type="string",
    description="Filter by the card race which is officially called type (Rock, Warrior, Insect, etc). It's also used "
                "for Spell/Trap cards (Field, Equip, Counter, etc). Allows to pass multiple comma separated races.",
    options=["Aqua", "Beast-Warrior", "Beast", "Continuous", "Counter", "Creator-God", "Cyberse", "Cyverse", "Dinosaur",
             "Divine-Beast", "Dragon", "Equip", "Fairy", "Field", "Fiend", "Fish", "Insect", "Ishizu", "Joey", "kaiba",
             "Machine", "Mai", "Normal", "Pegasus", "Plant", "Psychic", "Pyro", "Quick-Play", "Reptile", "Ritual",
             "Rock", "Sea Serpent", "Spellcaster", "Thunder", "Warrior", "Winged Beast", "Wyrm", "Yugi", "Zombie"],
    multi_selection=True
)

card_scale = Parameter(
    name="scale",
    data_type="string",  # TODO: Change to integer and create abstraction for equation symbols
    description="Filter the cards by pendulum scale value. Allows to use equation symbols ('lt': less than, 'lte': "
                "less than or equals to, 'gt': greater than, 'gte': greater than or equals to) [e.g. 'lt3': scale "
                "value is less than 3]."
)

card_set = Parameter(
    name="cardset",
    data_type="string",
    description="Filter the cards by card set [e.g. 'Metal Raiders', 'Soul Fusion', etc]."
)

card_sort = Parameter(
    name="sort",
    data_type="string",
    description="Sort the order of the cards (ATK, DEF, Name, Type, Level, ID, New, Relevance).",
    options=["ATK", "DEF", "Name", "Type", "Level", "ID", "New", "Relevance"]
)

card_staple = Parameter(
    name="staple",
    data_type="string",
    description="Check if card is a staple. Staple accepts 'Yes'.",
    options=["Yes"]
)

card_start_date = Parameter(
    name="startdate",
    data_type="string",  # TODO: Change to date and force it to be in a single format (e.g. YYYY-MM-DD)
    description="Query release dates for cards and the region of these release dates (OCG or TCG). The date format "
                "can be slightly varied as the API picks up different formats and converts it regardless [e.g. Jan 01 "
                "2000 or 01/01/2000]."
)

card_type = Parameter(
    name="type",
    data_type="string",
    description="Filter by the type of card (Normal Monster, Effect Monster, Spell Card, Trap Card, etc). Allows to "
                "pass multiple comma separated types.",
    options=["Effect Monster", "Flip Effect Monster", "Flip Monster", "Flip Tuner Effect Monster", "Fusion Monster",
             "Gemini Monster", "Link Monster", "Normal Monster", "Normal Tuner Monster",
             "Pendulum Effect Fusion Monster", "Pendulum Effect Monster", "Pendulum Flip Effect Monster",
             "Pendulum Normal Monster", "Pendulum Tuner Effect Monster", "Ritual Effect Monster", "Ritual Monster",
             "Skill Card", "Spell Card", "Spirit Monster", "Synchro Monster", "Synchro Pendulum Effect Monster",
             "Synchro Tuner Monster", "Token", "Toon Monster", "Trap Card", "Tuner Monster", "Union Effect Monster",
             "XYZ Monster", "XYZ Pendulum Effect Monster"],
    multi_selection=True
)

if __name__ == '__main__':
    print("Attribute:", card_atk.name, "| Value:", str(card_atk.value))
    card_atk.value = 3200
    print("Attribute:", card_atk.name, "| Value:", str(card_atk.value))
