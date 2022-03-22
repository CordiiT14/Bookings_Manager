class Event:

    def __init__(self, event_title, date, time, event_type, description, archive = False, id = None):
        self.event_title = event_title
        self.date = date
        self.time = time
        self.event_type = event_type
        self.description = description
        self.archive = archive
        self.id = id 
