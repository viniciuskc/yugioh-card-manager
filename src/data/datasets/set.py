from src.data.data import Column, Dataset

card_set = Dataset(
    name="set",
    write_mode="overwrite",
    description="Yu-Gi-Oh! card sets information.",
    columns=[
        Column("card_id", "id", "integer", primary_key=True),
        Column("set_name", ["card_sets", "set_name"], "string"),
        Column("set_code", ["card_sets", "set_code"], "string"),
        Column("set_rarity", ["card_sets", "set_rarity"], "string"),
        Column("set_rarity_code", ["card_sets", "set_rarity_code"], "string"),
        Column("set_updated_at", "datetime", "timestamp", description="Timestamp of last card set information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", card_set.name)
    print("Description:", card_set.description)
    print("Write Mode:", card_set.write_mode)
    print("Primary Keys:", str(card_set.primary_keys()))
    print("Columns:", str(card_set.columns()))
