from src.data.definition import Column, Dataset

dataset = Dataset(
    name="price",
    write_mode="append",
    description="Yu-Gi-Oh! card set prices information.",
    columns=[
        Column("set_code", "string", primary_key=True),
        Column("set_price", "decimal"),  # TODO: Check best data type (decimal, double, money)
        Column("set_price_created_at", "timestamp", primary_key=True, description="Timestamp when the card set price "
                                                                                  "was retrieved.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name: " + dataset.name)
    print("Description: " + dataset.description)
    print("Write Mode: " + dataset.write_mode)
    print("Primary Keys: " + str(dataset.primary_keys()))
    print("Columns: " + str(dataset.columns()))
