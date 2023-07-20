class Event:
    def __init__(self, ID, title,city_name,number_participant,max_seats,start_date,end_date):
        self.__ID = ID
        self.__title = title
        self.__city_name = city_name
        self.__number_participant =number_participant
        self.__max_seats = max_seats
        self.__start_date = start_date
        self.__end_date = end_date
        

    def get_id(self):
       return self.__ID

    def get_title(self):
        return self.__title


    def get_city_name(self):
        return self.__city_name

    def get_number_participant(self):
        return self.__number_participant

    def get_max_seats(self):
        return self.__max_seats

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def set_id(self,new_id):
        self.__ID=new_id

    def set_title(self,new_title):
        self.__title=new_title

    def set_city_name(self,new_city_name):
        self.__city_name=new_city_name

    def set_number_participant(self,new_number_participant):
        self.__number_participant=new_number_participant

    def set_max_seats(self,new_max_seats):
        self.__max_seats=new_max_seats

    def set_start_date(self,new_start_date):
        self.__start_date=new_start_date

    def set_end_date(self,new_end_date):
        self.__end_date=new_end_date

    def __str__(self):
        return "ID: {0}, title: {1}, city: {2}, number_participant: {3}, max_seats: {4},start_date: {5}, end_date: {6}".format(self.__ID, self.__title,self.__city_name,self.__number_participant,self.__max_seats,self.__start_date,self.__end_date)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_id() == other.get_id() and other.get_title() == self.get_title() and other.get_city_name() == self.get_city_name() and other.get_number_participant() == self.get_number_participant() and other.get_max_seats() == self.get_max_seats()  and other.get_end_date() == self.get_end_date()











