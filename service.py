from entity import Event
from entity_participant import Participant

class EventService:
    def __init__(self):
        self.__event_list =[Event(0,"SummerFest","Sibiu",10,1200,"1/10/2023","16/10/2023"),Event(1,"BigFest","Brasov",100,2500,"12/07/2023","25/07/2023")]


    def add_event(self,new_event):
        for event in self.__event_list:
            if event == new_event:
                raise ValueError(f'The Event {event} already exists!')
        self.__event_list.append(new_event)

    def __get_event_position(self, event):
        for i in range(len(self.__event_list)):
            if self.__event_list[i] == event:
                return i
        return None

    def delete_event(self, event_to_delete):
        event_index=self.__get_event_position(event_to_delete)
        if event_index is None:
            raise ValueError(f'Event {event_to_delete} does not exist!')
        del self.__event_list[event_index]

    def get_all_events(self):
        if len(self.__event_list) == 0:
            raise ValueError("No events!")
        return self.__event_list


    def modify_events(self,event_to_modify,new_id,new_title,new_city_name,new_number_participant,new_max_seats,new_start_date,new_end_date):
        event_index_to_modify = self.__get_event_position(event_to_modify)
        if event_index_to_modify is None:
            raise ValueError(f'Event {event_to_modify} does not exist!')
        self.__event_list[event_index_to_modify].set_id(new_id)
        self.__event_list[event_index_to_modify].set_title(new_title)
        self.__event_list[event_index_to_modify].set_city_name(new_city_name)
        self.__event_list[event_index_to_modify].set_number_participant(new_number_participant)
        self.__event_list[event_index_to_modify].set_max_seats(new_max_seats)
        self.__event_list[event_index_to_modify].set_start_date(new_start_date)
        self.__event_list[event_index_to_modify].set_end_date(new_end_date)

    def view_event_from_city(self,city):
        list_event_city=[]
        if len(self.__event_list) == 0:
            raise ValueError("No events!")
        for event in self.__event_list:
            if event.get_city_name()==city:
                list_event_city.append(event.get_title())
        return list_event_city



    
    



