class EventDispatcher:
    _events = {}

    @staticmethod
    def subscribe(event_name, callback):
        if event_name not in EventDispatcher._events:
            EventDispatcher._events[event_name] = []
        EventDispatcher._events[event_name].append(callback)

    @staticmethod
    def dispatch(event_name, *args, **kwargs):
        if event_name in EventDispatcher._events:
            for callback in EventDispatcher._events[event_name]:
                callback(*args, **kwargs)
        
