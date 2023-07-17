from src.data.data import Column, Dataset

# TODO: Always save english name and desc or save the language of the card

card_dataset = Dataset(
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
        Column("card_tcg_date", ["misc_info", "tcg_date"], "date"),
        Column("card_ocg_date", ["misc_info", "ocg_date"], "date"),
        Column("card_formats", ["misc_info", "formats"], "string", array=True),
        Column("card_updated_at", "datetime", "timestamp", description="Timestamp of last card information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", card_dataset.name)
    print("Description:", card_dataset.description)
    print("Write Mode:", card_dataset.write_mode)
    print("Primary Keys:", str(card_dataset.primary_keys()))
    print("Columns:", str(card_dataset.columns()))
