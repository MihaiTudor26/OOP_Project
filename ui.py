
from entity import Event
from entity_participant import Participant
from service import EventService
from service_participant import ParticipantService

class EventUI:
    def __init__(self, service: EventService, service_participant: ParticipantService):
        self.__service = service
        self.__service_participant=service_participant

    def __principal_menu(self):
        print("1.Organizer Mode")
        print("2.Participant Mode")
        print("3.Exit")
    def __print_menu(self):
       print("1.Add event")
       print("2.Delete event")
       print("3.Modify event")
       print("4.View event")
       print("5.View event from city")
       print("6.Show participants")
       print("0.Exit")

    def __print_menu_participant(self):
       print("1.View event")
       print("2.Participant Registration")
       print("0.Exit")
       
    def __validate_id(self, ID: str):
        try:
            int(ID)
        except Exception:
            raise ValueError("Maximum seats is not a number!")

    def __validate_number_participant(self, number_participant: str):
        try:
            int(number_participant)
        except Exception:
            raise ValueError("Number of participant is not a number!")

    def __validate_maximum_seats(self, max_seats: str):
        try:
            int(max_seats)
        except Exception:
            raise ValueError("Maximum seats is not a number!")

    def __add_event(self):
        ID = input("ID: ")
        title= input("Title event: ")
        city_name=input("City name event: ")
        number_participant=input("Number of participant: ")
        max_seats=input("Maximum seats event: ")
        start_data_time=input("Start data time: ")
        end_data_time=input("End data time: ")

        self.__validate_id(ID)
        self.__validate_maximum_seats(max_seats)
        self.__validate_number_participant(number_participant)
        self.__service.add_event(Event(int(ID),title,city_name,int(number_participant),int(max_seats),start_data_time,end_data_time))

    def __participant_registration(self):
        name = input("Name: ")
        link= input("Link: ")
        list_of_event=input("Name of event: ")

        ID = input("ID: ")
        title = input("Title event: ")
        city_name = input("City name event: ")
        number_participant = input("Number of participant: ")
        max_seats = input("Maximum seats event: ")
        start_data_time = input("Start data time: ")
        end_data_time = input("End data time: ")
        self.__service_participant.participant_registration(Participant(name,link,list_of_event),Event(int(ID),title,city_name,int(number_participant),int(max_seats),start_data_time,end_data_time))

    def __show_all_events(self):
        for event in self.__service.get_all_events():
            print(event)

    def __delete_event(self):
        ID=input("Introduceti id: ")
        title = input("Title event: ")
        city_name = input("City name event: ")
        number_participant = input("Number of participant: ")
        max_seats = input("Maximum seats event: ")
        start_data_time = input("Start data time: ")
        end_data_time = input("End data time: ")

        self.__validate_id(ID)
        self.__validate_maximum_seats(max_seats)
        self.__validate_number_participant(number_participant)
        self.__service.delete_event(Event(int(ID),title,city_name,int(number_participant),int(max_seats),start_data_time,end_data_time))

    def __modify_event(self):
        ID = input("Introduceti id: ")
        title = input("Title event: ")
        city_name = input("City name event: ")
        number_participant = input("Number of participant: ")
        max_seats = input("Maximum seats event: ")
        start_data_time = input("Start data time: ")
        end_data_time = input("End data time: ")

        nID = input("Introduceti newid: ")
        ntitle = input("Title newevent: ")
        ncity_name = input("City newname event: ")
        nnumber_participant = input("Number of participant: ")
        nmax_seats = input("newMaximum seats event: ")
        nstart_data_time = input("newStart data time: ")
        nend_data_time = input("newEnd data time: ")

        self.__validate_id(ID)
        self.__validate_maximum_seats(max_seats)
        self.__validate_number_participant(number_participant)
        self.__service.modify_events(Event(int(ID),title,city_name,int(number_participant),int(max_seats),start_data_time,end_data_time),int(nID), ntitle, ncity_name, int(nnumber_participant),int(nmax_seats), nstart_data_time, nend_data_time)

    def __event_city(self):
        city_name = input("City name event: ")
        print(self.__service.view_event_from_city(city_name))


    def __show_all_participant(self):
        for participant in self.__service_participant.get_all_participant():
            print(participant)


    def run(self):
        while True:
            self.__principal_menu()
            try:
                command = int(input("Choose the command: ").strip())
                if command ==1:
                    print("Organizer Menu:")
                    self.__print_menu()
                    try:
                       command_organizer = int(input("Choose the command: ").strip())
                       if command_organizer == 0:
                          break
                       elif command_organizer == 1:
                          self.__add_event()
                       elif command_organizer == 2:
                          self.__delete_event()
                       elif command_organizer == 3:
                          self.__modify_event()
                       elif command_organizer== 4:
                          self.__show_all_events()
                       elif command_organizer == 5:
                          self.__event_city()
                       elif command_organizer == 6:
                          self.__show_all_participant()
                    except Exception as error:
                       print(error)
                elif command == 2:
                    print("Participant Menu:")
                    self.__print_menu_participant()
                    try:
                       command_participant = int(input("Choose the command: ").strip())
                       if command_participant == 0:
                          break
                       elif command_participant == 1:
                          self.__show_all_events()
                       elif command_participant == 2:
                          self.__participant_registration()
                    except Exception as error:
                       print(error)
                elif command == 3:
                    break
            except Exception as error:
                print(error)




