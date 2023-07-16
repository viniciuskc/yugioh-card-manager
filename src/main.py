from os import system
from src.api.api import get_images_dict
import search

# TODO: File not working, finish refactoring the api definitions and then refactor methods in this file


def menu_home():
    """Clears the terminal screen and displays the welcome message."""

    system('clear')
    welcome_message = "===============================================\n" \
                      "Welcome to Yu-Gi-Oh! Card Manager by viniciuskc\n" \
                      "==============================================="
    print(welcome_message)


def menu_search():
    """Displays the search options menu."""

    valid_search = False

    option_message = "\nWhich information do you want to search for?\n" \
                     "\t[1] Card\n" \
                     "\t[2] Card set\n" \
                     "\t[3] Random card\n" \
                     "\t[q] Quit\n" \
                     "> Enter an option: "
    option_input = str(input(option_message)).lower()

    match option_input:
        case "1":
            response = search.search_card()
            exit_select = False
            while not exit_select:
                exit_select = menu_select(response)
            valid_search = True

        case "2":
            search.search_card_set()
            valid_search = True

        case "3":
            response = search.search_random_card()
            images_dict = get_images_dict(response)
            writer.save_image_files(images_dict)
            valid_search = True

        case "q":
            exit()

        case _:
            print(f"\n[ERROR] [{option_input}] option not recognized. Please enter a valid option.")
            valid_search = False

    return valid_search


def menu_select(response):
    """Displays the results selection menu for a search response."""

    valid_select = False

    select_message = "\nResults options:\n" \
                     "\t[1] View card details\n" \
                     "\t[2] Save all cards data\n" \
                     "\t[3] Save all cards images\n" \
                     "\t[4] Save all cards data and images\n" \
                     "\t[c] Cancel\n" \
                     "\t[q] Quit\n" \
                     "> Enter an option: "
    select_input = str(input(select_message)).lower()

    match select_input:
        case "1":
            search.search_card_details(response)
            # TODO: Implement extra menu method to choose saving data, images or both from the selected card
            valid_select = True

        case "2":
            writer.save_data_in_csv(response, "collection")
            valid_select = True

        case "3":
            images_dict = get_images_dict(response)
            writer.save_image_files(images_dict)
            valid_select = True

        case "4":
            writer.save_data_in_csv(response, "collection")
            # TODO: Save only images of cards with quantity > 0
            images_dict = get_images_dict(response)
            writer.save_image_files(images_dict)
            valid_select = True

        case "c":
            valid_select = True

        case "q":
            exit()

        case _:
            print(f"\n[ERROR] [{select_input}] option not recognized. Please enter a valid option.")
            valid_select = False

    return valid_select


def menu_restart():
    """Displays the restart menu."""

    valid_restart = False

    restart_message = "\n> Do you want to do another operation? [y] Yes | [n] No: "
    restart_input = str(input(restart_message)).lower()

    match restart_input:
        case "y":
            valid_restart = True
        case "n":
            exit()
        case _:
            print(f"\n[ERROR] [{restart_input}] option not recognized. Please enter a valid option.")
            valid_restart = False

    return valid_restart


if __name__ == '__main__':

    menu_home()
    exit_menu = False

    while not exit_menu:
        exit_search = menu_search()
        if exit_search:
            exit_restart = False
            while not exit_restart:
                exit_restart = menu_restart()
