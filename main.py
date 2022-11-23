import api
import input
import writer

if __name__ == '__main__':

    file_name_prefix_card_info = "ygoprodeck_card_info_"
    file_name_prefix_image = "ygoprodeck_card_image_"

    params = input.get_valid_params(input.input_params_get_card_info)

    data = api.get_card_info(params=params)

    writer.write_json_file(file_name_prefix_card_info, data)
    writer.save_images(file_name_prefix_image, data)
