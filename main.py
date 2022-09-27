





def main():
    with open('meteorite_landings_data.txt', 'r') as data:

        list_of_items = []
        for item in data:
            stripped_line = item.strip()
            line_list = stripped_line.split('\t')
            list_of_items.append(line_list)

        for i in list_of_items[0]:
            header = i.split()
            print(header)

    print(list_of_items)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()
