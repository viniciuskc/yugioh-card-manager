from src.data.data import Column, Dataset

set_dataset = Dataset(
    name="set",
    nested_key="card_sets",
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
    print("Dataset Name:", set_dataset.name)
    print("Description:", set_dataset.description)
    print("Write Mode:", set_dataset.write_mode)
    print("Primary Keys:", str(set_dataset.primary_keys()))
    print("Columns:", str(set_dataset.columns()))
