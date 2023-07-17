from src.data.data import Column, Dataset

set_price_dataset = Dataset(
    name="set_price",
    nested_key="card_sets",
    write_mode="append",
    description="Yu-Gi-Oh! card set prices information.",
    columns=[
        Column("set_code", ["card_sets", "set_code"], "string", primary_key=True),
        Column("set_price", ["card_sets", "set_price"], "decimal"),  # TODO: Check best data type (decimal, double, money)
        Column("set_price_created_at", "datetime", "timestamp", primary_key=True,
               description="Timestamp when the card set price was retrieved.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", set_price_dataset.name)
    print("Description:", set_price_dataset.description)
    print("Write Mode:", set_price_dataset.write_mode)
    print("Primary Keys:", str(set_price_dataset.primary_keys()))
    print("Columns:", str(set_price_dataset.columns()))
