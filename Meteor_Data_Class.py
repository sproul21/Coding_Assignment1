class MeteorDataEntry:
    def __init__(self, meteor_data):

        self.name = meteor_data[0]
        self.identification = meteor_data[1]
        self.name_type = meteor_data[2]
        self.rec_class = meteor_data[3]
        self.mass_g = meteor_data[4]
        self.fall = meteor_data[5]
        self.year_of_meteor = meteor_data[6]
        self.reclat_lattitude = meteor_data[7]
        self.reclong_longitude = meteor_data[8]
        self.geo_location = meteor_data[9]
        self.state_found = meteor_data[10]
        self.counties_found = meteor_data[11]


    def printdata(self):

        print(self.name)


 #   def mass_filter(self):
  #      if self.mass_g.isnumeric():
   #         if self.mass_g > 2900000
    #            list.append(self)