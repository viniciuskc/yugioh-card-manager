from src.data.data import Column, Dataset

dataset = Dataset(
    name="price",
    write_mode="append",
    description="Yu-Gi-Oh! card prices information.",
    columns=[
        Column("card_id", "id", "integer", primary_key=True),
        Column("price_amazon", ["card_prices", "amazon_price"], "decimal"),  # TODO: Check best data type (decimal, double, money)
        Column("price_cardmarket", ["card_prices", "cardmarket_price"], "decimal"),  # TODO: Check best data type (decimal, double, money)
        Column("price_coolstuffinc", ["card_prices", "coolstuffinc_price"], "decimal"),  # TODO: Check best data type (decimal, double, money)
        Column("price_ebay_price", ["card_prices", "ebay_price"], "decimal"),  # TODO: Check best data type (decimal, double, money)
        Column("price_tcgplayer", ["card_prices", "tcgplayer_price"], "decimal"),  # TODO: Check best data type (decimal, double, money)
        Column("price_created_at", "datetime", "timestamp", primary_key=True,
               description="Timestamp when the card prices were retrieved.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", dataset.name)
    print("Description:", dataset.description)
    print("Write Mode:", dataset.write_mode)
    print("Primary Keys:", str(dataset.primary_keys()))
    print("Columns:", str(dataset.columns()))
