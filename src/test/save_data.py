from src.api.endpoints.cardinfo import card_info_api
from src.api.parameters.cardinfo import *
from src.data.datasets import banlist, card, image, price, set, set_price
from src.data import images

print("")
print("--- Request 1 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_name.value = "Dragão Negro de Olhos Vermelhos"
card_type.value = "Normal Monster"
card_race.value = "Dragon"
card_atk.value = "2400"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_1 = card_info_api.request()
# print("Response:", api_response_1)

banlist.banlist_dataset.save_csv(api_response_1)
card.card_dataset.save_csv(api_response_1)
image.image_dataset.save_csv(api_response_1)
price.price_dataset.save_csv(api_response_1)
set.set_dataset.save_csv(api_response_1)
set_price.set_price_dataset.save_csv(api_response_1)

card.card_dataset.save_json(api_response_1)

images.save_images(api_response_1)

card_info_api.reset_parameters()

print("--- Request 2 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_type.value = "Fusion Monster"
card_attribute.value = "Fire"
card_race.value = "Dragon"
card_atk.value = "3500"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_2 = card_info_api.request()
# print("Response:", api_response_2)

banlist.banlist_dataset.save_csv(api_response_2)
card.card_dataset.save_csv(api_response_2)
image.image_dataset.save_csv(api_response_2)
price.price_dataset.save_csv(api_response_2)
set.set_dataset.save_csv(api_response_2)
set_price.set_price_dataset.save_csv(api_response_2)

card.card_dataset.save_json(api_response_2)

images.save_images(api_response_2)

card_info_api.reset_parameters()

print("--- Request 3 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_archetype.value = "Red-Eyes"
card_type.value = "XYZ Monster"
card_race.value = "Dragon"
card_atk.value = "2800"
card_def.value = "2400"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_3 = card_info_api.request()
# print("Response:", api_response_3)

banlist.banlist_dataset.save_csv(api_response_3)
card.card_dataset.save_csv(api_response_3)
image.image_dataset.save_csv(api_response_3)
price.price_dataset.save_csv(api_response_3)
set.set_dataset.save_csv(api_response_3)
set_price.set_price_dataset.save_csv(api_response_3)

card.card_dataset.save_json(api_response_3)

images.save_images(api_response_3)

card_info_api.reset_parameters()

print("--- Request 4 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_name.value = "Dragão Pêndulo de Olhos Anômalos"
card_scale.value = "4"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_4 = card_info_api.request()
# print("Response:", api_response_4)

banlist.banlist_dataset.save_csv(api_response_4)
card.card_dataset.save_csv(api_response_4)
image.image_dataset.save_csv(api_response_4)
price.price_dataset.save_csv(api_response_4)
set.set_dataset.save_csv(api_response_4)
set_price.set_price_dataset.save_csv(api_response_4)

card.card_dataset.save_json(api_response_4)

images.save_images(api_response_4)

card_info_api.reset_parameters()

print("--- Request 5 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_fname.value = "Metal das Trevas"
card_link.value = "4"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_5 = card_info_api.request()
# print("Response:", api_response_5)

banlist.banlist_dataset.save_csv(api_response_5)
card.card_dataset.save_csv(api_response_5)
image.image_dataset.save_csv(api_response_5)
price.price_dataset.save_csv(api_response_5)
set.set_dataset.save_csv(api_response_5)
set_price.set_price_dataset.save_csv(api_response_5)

card.card_dataset.save_json(api_response_5)

images.save_images(api_response_5)

card_info_api.reset_parameters()

print("--- Request 6 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_name.value = "Pote da Ganância"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_6 = card_info_api.request()
# print("Response:", api_response_6)

banlist.banlist_dataset.save_csv(api_response_6)
card.card_dataset.save_csv(api_response_6)
image.image_dataset.save_csv(api_response_6)
price.price_dataset.save_csv(api_response_6)
set.set_dataset.save_csv(api_response_6)
set_price.set_price_dataset.save_csv(api_response_6)

card.card_dataset.save_json(api_response_6)

images.save_images(api_response_6)

card_info_api.reset_parameters()

print("--- Request 7 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_name.value = "Ruína Generalizada"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_7 = card_info_api.request()
# print("Response:", api_response_7)

banlist.banlist_dataset.save_csv(api_response_7)
card.card_dataset.save_csv(api_response_7)
image.image_dataset.save_csv(api_response_7)
price.price_dataset.save_csv(api_response_7)
set.set_dataset.save_csv(api_response_7)
set_price.set_price_dataset.save_csv(api_response_7)

card.card_dataset.save_json(api_response_7)

images.save_images(api_response_7)

card_info_api.reset_parameters()

print("--- Request 8 --------------------------------------------------------------------------------------")

card_language.value = "PT"
card_name.value = "Carta Que Não Existe"

print("Parameters:", str(card_info_api.filled_parameters()))
print("Endpoint:", card_info_api.url())
api_response_8 = card_info_api.request()
# print("Response:", api_response_8)

banlist.banlist_dataset.save_csv(api_response_8)
card.card_dataset.save_csv(api_response_8)
image.image_dataset.save_csv(api_response_8)
price.price_dataset.save_csv(api_response_8)
set.set_dataset.save_csv(api_response_8)
set_price.set_price_dataset.save_csv(api_response_8)

card.card_dataset.save_json(api_response_8)

images.save_images(api_response_8)

card_info_api.reset_parameters()

print("--- End --------------------------------------------------------------------------------------------")
