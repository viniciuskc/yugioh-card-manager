from src.api.endpoints.cardinfo import api
from src.api.parameters import cardinfo
from src.data.datasets.card import dataset
from src.writer import images

cardinfo.card_type.value = "Fusion Monster"
cardinfo.card_attribute.value = "Fire"
cardinfo.card_race.value = "Dragon"
cardinfo.card_atk.value = 3500
print("------------------------------------------------------------")
print("Parameters:", str(api.filled_parameters()))
print("Endpoint:", api.url())
api_response = api.request()
print("Response:", api_response)
print("------------------------------------------------------------")
print("Dataset Name:", dataset.name)
print("Description:", dataset.description)
print("Write Mode:", dataset.write_mode)
print("Primary Keys:", str(dataset.primary_keys()))
print("Columns:", str(dataset.columns()))
print("------------------------------------------------------------")
dataset.save_csv(api_response)
print("------------------------------------------------------------")
dataset.save_json(api_response)
print("------------------------------------------------------------")
images.save_images(api_response)
