from src.api.api import Parameter

set_code = Parameter(
    name="setcode",
    data_type="string",
    mandatory=True,
    description="Filter the cards by set code [e.g. 'SDY-046'].",
    value="LDK2-ENJ41"
)

if __name__ == '__main__':
    print("Attribute:", set_code.name, "| Value:", str(set_code.value))
    set_code.value = "LDK2-ENJ39"
    print("Attribute:", set_code.name, "| Value:", str(set_code.value))
