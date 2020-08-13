import csv

def louput(my_list):
    # output txt
    # with open('output.txt', 'w') as output_file:
    #    for item in my_list:
    #        output_file.write("%s\n" % item)
    # output csv
    keys = my_list[0].keys()
    with open('output.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(my_list)