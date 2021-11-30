from datetime import datetime

import re
import configuration


def list_to_string(given_list):
    final_str = ''
    return final_str.join(given_list)


def splitter(log_str, separator, number_of_elements, issued_element):
    split_string = log_str.split(separator)
    hits = len(split_string)
    if hits == number_of_elements:
        return split_string
    else:
        temp_list = split_string[:issued_element]
        last_issued_element = issued_element + (len(split_string) - number_of_elements) + 1
        merged_missing_elements = split_string[issued_element:last_issued_element]
        merged_string = list_to_string(merged_missing_elements)
        temp_list.append(merged_string)
        final_list = temp_list + split_string[last_issued_element:]
        return final_list


def extract_date(log_line):
    return datetime.strptime(log_line.split("|")[0], configuration.TIME_FORMAT)


def extract_users(user_string):
    split_string = splitter(user_string, "'", 5, 3)
    adm_nickname = split_string[3]
    adm_user_id = re.findall("[0-9]+", split_string[4])[0]
    registered_user_id = re.findall("[0-9]+", split_string[0])[0]
    return adm_nickname, adm_user_id, registered_user_id


def search_logs():
    clients_registered = []
    with open('logs.txt', 'r', encoding="utf8") as f:
        for line in f:
            if configuration.REGISTER_USER_STATEMENT_0 in line or configuration.REGISTER_USER_STATEMENT_1 in line:
                registration_datetime = extract_date(line)
                if configuration.last_user_date < registration_datetime:
                    split_log = splitter(line, '|', 5, 4)
                    main_log = split_log[4]
                    ts3_adm_nickname, ts3_adm_user_id, ts3_registered_user_id = extract_users(main_log)
                    clients_registered.append({
                        "datetime": registration_datetime,
                        "user_id": ts3_registered_user_id,
                        "adm_user_id": ts3_adm_user_id,
                        "adm_nick": ts3_adm_nickname
                    })
    return clients_registered
