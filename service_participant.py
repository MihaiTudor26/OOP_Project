from entity_participant import Participant
from entity import Event
class ParticipantService:
    def __init__(self):
        self.__participant_list =[Participant("Alin","poza1","SummerFest"),Participant("Adrian","poza2","BigFest")]

    def participant_registration(self,new_inregistration,event):
        if event.get_number_participant()>=event.get_max_seats():
            raise ValueError("There are no seats available!")
        else:
            self.__participant_list.append(new_inregistration)
            new_number_participant=event.get_number_participant()+1
            event.set_number_participant(new_number_participant)
        return self.__participant_list

    def get_all_participant(self):
        if len(self.__participant_list) == 0:
            raise ValueError("No perticipant!")
        return self.__participant_list


