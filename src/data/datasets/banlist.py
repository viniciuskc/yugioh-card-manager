from src.data.definition import Column, Dataset

dataset = Dataset(
    name="banlist",
    write_mode="overwrite",
    description="Yu-Gi-Oh! banlist information.",
    columns=[
        Column("card_id", "integer", primary_key=True),
        Column("banlist_goat", "string"),
        Column("banlist_ocg", "string"),
        Column("banlist_tcg", "string"),
        Column("banlist_updated_at", "timestamp", description="Timestamp of last banlist information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name: " + dataset.name)
    print("Description: " + dataset.description)
    print("Write Mode: " + dataset.write_mode)
    print("Primary Keys: " + str(dataset.primary_keys()))
    print("Columns: " + str(dataset.columns()))
