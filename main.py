import api
import input
import writer

if __name__ == '__main__':
    file_name_prefix = "ygoprodeck_cardsetsinfo_"

    params = input.get_valid_params(input.input_params_get_card_info)
    data = api.get_card_info(params=params)
    writer.write_json_file(file_name_prefix, data)
