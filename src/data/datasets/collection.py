from src.data.data import Column, Dataset

dataset = Dataset(
    name="collection",
    write_mode="overwrite",
    description="Yu-Gi-Oh! card collection information.",
    columns=[
        Column("collection_id", "collection_id", "integer", primary_key=True),
        Column("card_id", "id", "integer", primary_key=True),
        Column("card_set_code", ["card_sets", "set_code"], "string", primary_key=True),
        Column("card_quantity", "quantity", "integer"),
        Column("collection_updated_at", "datetime", "timestamp",
               description="Timestamp of last collection information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", dataset.name)
    print("Description:", dataset.description)
    print("Write Mode:", dataset.write_mode)
    print("Primary Keys:", str(dataset.primary_keys()))
    print("Columns:", str(dataset.columns()))
