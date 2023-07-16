from src.data.data import Column, Dataset

dataset = Dataset(
    name="image",
    write_mode="overwrite",
    description="Yu-Gi-Oh! card images links.",
    columns=[
        Column("card_id", "id", "integer", primary_key=True),
        Column("image_default", ["card_images", "image_url"], "string"),
        Column("image_small", ["card_images", "image_url_small"], "string"),
        Column("image_cropped", ["card_images", "image_url_cropped"], "string"),
        Column("image_updated_at", "datetime", "timestamp", description="Timestamp of last card images links update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", dataset.name)
    print("Description:", dataset.description)
    print("Write Mode:", dataset.write_mode)
    print("Primary Keys:", str(dataset.primary_keys()))
    print("Columns:", str(dataset.columns()))
