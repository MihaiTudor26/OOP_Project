class Participant:
    def __init__(self, name,link,list_of_event):
        self.__name = name
        self.__link = link
        self.__list_of_event = list_of_event


    def get_name(self):
        return self.__name
    def get_link(self):
        return self.__link
    def get_list_of_event(self):
        return self.__list_of_event

    def __str__(self):
        return "name: {0}, link: {1}, list_of_event: {2}".format(self.__name, self.__link,self.__list_of_event)

    def __repr__(self):
        return str(self)

