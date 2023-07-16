from src.data.data import Column, Dataset

card_set_price = Dataset(
    name="price",
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
    print("Dataset Name:", card_set_price.name)
    print("Description:", card_set_price.description)
    print("Write Mode:", card_set_price.write_mode)
    print("Primary Keys:", str(card_set_price.primary_keys()))
    print("Columns:", str(card_set_price.columns()))
