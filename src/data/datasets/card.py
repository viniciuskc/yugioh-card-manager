from src.data.data import Column, Dataset

dataset = Dataset(
    name="card",
    write_mode="overwrite",
    description="Yu-Gi-Oh! card information.",
    columns=[
        Column("card_id", "id", "integer", primary_key=True),
        Column("card_name", "name", "string"),
        Column("card_frame_type", "frameType", "string"),
        Column("card_type", "type", "string"),
        Column("card_desc", "desc", "string"),
        Column("card_race", "race", "string"),
        Column("card_attribute", "attribute", "string"),
        Column("card_archetype", "archetype", "string"),
        Column("card_atk", "atk", "integer"),
        Column("card_def", "def", "integer"),
        Column("card_level", "level", "integer"),
        Column("card_scale", "scala", "integer"),
        Column("card_linkval", "linkval", "integer"),
        Column("card_linkmarkers", "linkmarkers", "string", array=True),
        Column("card_tcg_date", ["misc_info", "card_tcg_date"], "date"),
        Column("card_ocg_date", ["misc_info", "card_ocg_date"], "date"),
        Column("card_updated_at", "datetime", "timestamp", description="Timestamp of last card information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", dataset.name)
    print("Description:", dataset.description)
    print("Write Mode:", dataset.write_mode)
    print("Primary Keys:", str(dataset.primary_keys()))
    print("Columns:", str(dataset.columns()))
