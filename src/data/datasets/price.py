from src.data.data import Column, Dataset

price = Dataset(
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
    print("Dataset Name:", price.name)
    print("Description:", price.description)
    print("Write Mode:", price.write_mode)
    print("Primary Keys:", str(price.primary_keys()))
    print("Columns:", str(price.columns()))
