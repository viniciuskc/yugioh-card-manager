from pandas import read_csv, read_json
from src.data.datasets.card import card

print("")
print("----------------------------------------------------------------------------------------------------")
print("Dataset Name:", card.name)
print("Description:", card.description)
print("Primary Keys:", str(card.primary_keys()))
print("Columns:", str(card.columns()))
print("----------------------------------------------------------------------------------------------------")
card_csv_path = card.path("csv")
card_csv_limit = 25
print(f"First {card_csv_limit} rows saved in {card_csv_path}:")
card_csv_data = read_csv(card_csv_path)
card_csv_summary = card_csv_data[["card_id", "card_name", "card_updated_at"]].head(card_csv_limit)
print(card_csv_summary)
print("----------------------------------------------------------------------------------------------------")
card_json_path = card.path("json")
card_json_limit = 25
print(f"First {card_json_limit} rows saved in {card_json_path}:")
card_json_data = read_json(card_json_path, lines=True, dtype=False, convert_dates=False)
card_json_summary = card_json_data[["card_id", "card_name", "card_updated_at"]].head(card_json_limit)
print(card_json_summary)
print("----------------------------------------------------------------------------------------------------")
