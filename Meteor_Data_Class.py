class MeteorDataEntry:
    def __innit__(self, name, id, nametype, recclass, mass, fall, year, reclat, reclong, GeoLocation, States, Counties):
        self.name = name
        self.identification = id
        self.name_type = nametype
        self.rec_class = recclass
        self.mass_g = mass
        self.fall = fall
        self.year_of_meteor = year
        self.reclat_lattitude = reclat
        self.reclong_longitude = reclong
        self.geo_location = GeoLocation
        self.state_found = States
        self.counties_found = Counties