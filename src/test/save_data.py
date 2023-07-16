from src.api.endpoints.cardinfo import card_info
from src.api.parameters.cardinfo import *
from src.data.datasets.card import card
from src.data import images

print("")
print("----------------------------------------------------------------------------------------------------")
card_name.value = "Dragão Negro de Olhos Vermelhos"
card_type.value = "Normal Monster"
card_race.value = "Dragon"
card_atk.value = "2400"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_1 = card_info.request()
# print("Response:", api_response_1)
card.save_csv(api_response_1)
card.save_json(api_response_1)
images.save_images(api_response_1)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
card_type.value = "Fusion Monster"
card_attribute.value = "Fire"
card_race.value = "Dragon"
card_atk.value = "3500"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_2 = card_info.request()
# print("Response:", api_response_2)
card.save_csv(api_response_2)
card.save_json(api_response_2)
images.save_images(api_response_2)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
card_archetype.value = "Red-Eyes"
card_type.value = "XYZ Monster"
card_race.value = "Dragon"
card_atk.value = "2800"
card_def.value = "2400"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_3 = card_info.request()
# print("Response:", api_response_3)
card.save_csv(api_response_3)
card.save_json(api_response_3)
images.save_images(api_response_3)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
card_name.value = "Dragão Pêndulo de Olhos Anômalos"
card_scale.value = "4"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_4 = card_info.request()
# print("Response:", api_response_4)
card.save_csv(api_response_4)
card.save_json(api_response_4)
images.save_images(api_response_4)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
card_fname.value = "Metal das Trevas"
card_link.value = "4"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_5 = card_info.request()
# print("Response:", api_response_5)
card.save_csv(api_response_5)
card.save_json(api_response_5)
images.save_images(api_response_5)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
card_name.value = "Pote da Ganância"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_6 = card_info.request()
# print("Response:", api_response_6)
card.save_csv(api_response_6)
card.save_json(api_response_6)
images.save_images(api_response_6)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
card_name.value = "Ruína Generalizada"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_7 = card_info.request()
# print("Response:", api_response_7)
card.save_csv(api_response_7)
card.save_json(api_response_7)
images.save_images(api_response_7)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
card_name.value = "Carta Que Não Existe"
print("Parameters:", str(card_info.filled_parameters()))
print("Endpoint:", card_info.url())
api_response_8 = card_info.request()
# print("Response:", api_response_8)
card.save_csv(api_response_8)
card.save_json(api_response_8)
images.save_images(api_response_8)
card_info.reset_parameters()
print("----------------------------------------------------------------------------------------------------")
