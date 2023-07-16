from src.api.endpoints.cardinfo import card_info
from src.api.parameters.cardinfo import *
from src.data.datasets.card import card
from src.data import images

card_type.value = "Fusion Monster"
card_attribute.value = "Fire"
card_race.value = "Dragon"
card_atk.value = 3500
print("------------------------------------------------------------")
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response = card_info.request()
print("Response:", api_response)
print("------------------------------------------------------------")
print("Dataset Name:", card.name)
print("Description:", card.description)
print("Write Mode:", card.write_mode)
print("Primary Keys:", str(card.primary_keys()))
print("Columns:", str(card.columns()))
print("------------------------------------------------------------")
card.save_csv(api_response)
print("------------------------------------------------------------")
card.save_json(api_response)
print("------------------------------------------------------------")
images.save_images(api_response)
