from src.data.definition import Column, Dataset

dataset = Dataset(
    name="set",
    write_mode="overwrite",
    description="Yu-Gi-Oh! card sets information.",
    columns=[
        Column("card_id", "integer", primary_key=True),
        Column("set_name", "string"),
        Column("set_code", "string"),
        Column("set_rarity", "string"),
        Column("set_rarity_code", "string"),
        Column("set_updated_at", "timestamp", description="Timestamp of last card set information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name: " + dataset.name)
    print("Description: " + dataset.description)
    print("Write Mode: " + dataset.write_mode)
    print("Primary Keys: " + str(dataset.primary_keys()))
    print("Columns: " + str(dataset.columns()))
