


from Meteor_Data_Class import*

def main():
    with open('meteorite_landings_data.txt', 'r') as data:

        list_of_items = []
        mass_list = []
        date_list = []
        for item in data:
            stripped_line = item.strip('\n')
            line_list = stripped_line.split('\t')
            list_of_items.append(MeteorDataEntry(line_list))

        for i in list_of_items:

            if i.mass_g.isnumeric():
                 if int(i.mass_g) > 2900000:
                    mass_list.append(i)

        name_label = 'NAME'
        mass_label = 'MASS (g)'
        print(f'{name_label:<24}{mass_label:<20}')
        print('========================================')
        for i in mass_list:
            print(f'{i.name:<24}{i.mass_g:<20}')

        for i in list_of_items:

            if i.year_of_meteor.isnumeric():
                 if int(i.year_of_meteor) >= 2013:
                    date_list.append(i)

        name_label = 'NAME'
        year_label = 'YEAR'
        print(f'{name_label:<24}{year_label:<20}')
        print('========================================')
        for i in date_list:
            print(f'{i.name:<24}{i.year_of_meteor:<20}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()
