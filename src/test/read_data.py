from pandas import read_csv
from src.data.datasets import card, price, set

print("\n--- Card -------------------------------------------------------------------------------------------\n")

print("Dataset Name:", card.card_dataset.name)
print("Description:", card.card_dataset.description)
print("Primary Keys:", str(card.card_dataset.primary_keys()))
print("Columns:", str(card.card_dataset.columns()))

card_csv_path = card.card_dataset.path("csv")
card_csv_limit = 25

print(f"\nFirst {card_csv_limit} rows saved in {card_csv_path}:\n")
card_csv_data = read_csv(card_csv_path)
card_csv_summary = card_csv_data[["card_id", "card_name", "card_updated_at"]].head(card_csv_limit)
print(card_csv_summary)

print("\n--- Price ------------------------------------------------------------------------------------------\n")

print("Dataset Name:", price.price_dataset.name)
print("Description:", price.price_dataset.description)
print("Primary Keys:", str(price.price_dataset.primary_keys()))
print("Columns:", str(price.price_dataset.columns()))

price_csv_path = price.price_dataset.path("csv")
price_csv_limit = 25

print(f"\nFirst {price_csv_limit} rows saved in {price_csv_path}:\n")
price_csv_data = read_csv(price_csv_path)
price_csv_summary = price_csv_data[
    ["card_id",
     "price_cardmarket",
     "price_coolstuffinc",
     "price_tcgplayer"]
].head(card_csv_limit)
print(price_csv_summary)

print("\n--- Card Set ---------------------------------------------------------------------------------------\n")

print("Dataset Name:", set.set_dataset.name)
print("Description:", set.set_dataset.description)
print("Primary Keys:", str(set.set_dataset.primary_keys()))
print("Columns:", str(set.set_dataset.columns()))

set_csv_path = set.set_dataset.path("csv")
set_csv_limit = 25

print(f"\nFirst {set_csv_limit} rows saved in {set_csv_path}:\n")
set_csv_data = read_csv(set_csv_path)
set_csv_summary = set_csv_data[["card_id", "set_code", "set_rarity"]].head(set_csv_limit)
print(set_csv_summary)

print("\n--- End --------------------------------------------------------------------------------------------")