class Event:
    def __init__(self,
                 ip: str,
                 time: str,
                 event_type: str):
        self.ip = ip
        self.time = time
        self.event_type = event_type
