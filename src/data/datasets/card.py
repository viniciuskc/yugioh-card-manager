from src.data.definition import Column, Dataset

dataset = Dataset(
    name="card",
    write_mode="overwrite",
    description="Yu-Gi-Oh! card information.",
    columns=[
        Column("card_id", "integer", primary_key=True),
        Column("card_name", "string"),
        Column("card_frame_type", "string"),
        Column("card_type", "string"),
        Column("card_desc", "string"),
        Column("card_race", "string"),
        Column("card_attribute", "string"),
        Column("card_archetype", "string"),
        Column("card_atk", "integer"),
        Column("card_def", "integer"),
        Column("card_level", "integer"),
        Column("card_scale", "integer"),
        Column("card_linkval", "integer"),
        Column("card_linkmarkers", "string", array=True),
        Column("card_tcg_date", "date"),
        Column("card_ocg_date", "date"),
        Column("card_updated_at", "timestamp", description="Timestamp of last card information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name: " + dataset.name)
    print("Description: " + dataset.description)
    print("Write Mode: " + dataset.write_mode)
    print("Primary Keys: " + str(dataset.primary_keys()))
    print("Columns: " + str(dataset.columns()))
