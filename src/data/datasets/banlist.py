from src.data.data import Column, Dataset

banlist = Dataset(
    name="banlist",
    write_mode="overwrite",
    description="Yu-Gi-Oh! banlist information.",
    columns=[
        Column("card_id", "id", "integer", primary_key=True),
        Column("banlist_goat", ["banlist_info", "ban_goat"], "string"),
        Column("banlist_ocg", ["banlist_info", "ban_ocg"], "string"),
        Column("banlist_tcg", ["banlist_info", "ban_tcg"], "string"),
        Column("banlist_updated_at", "datetime", "timestamp",
               description="Timestamp of last banlist information update.")
    ]
)

if __name__ == '__main__':
    print("Dataset Name:", banlist.name)
    print("Description:", banlist.description)
    print("Write Mode:", banlist.write_mode)
    print("Primary Keys:", str(banlist.primary_keys()))
    print("Columns:", str(banlist.columns()))
