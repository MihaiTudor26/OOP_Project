from ui import EventUI
from service import EventService
from service_participant import ParticipantService
service = EventService()
service_participant=ParticipantService()
ui = EventUI(service,service_participant)
ui.run()
