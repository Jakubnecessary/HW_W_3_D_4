from models.event import Event

event_1 = Event("16th August 2021", "Connor's Birthday", 1, "Gamer Room", "Sad solo Birthday")
event_2 = Event("22nd April 2021", "Jakub's Birthday", 42, "Bar", "Actually fun Birthday")

events = [event_1, event_2]

def add_new_event(event):
    events.append(event)