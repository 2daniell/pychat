class EventDispatcher:
    
    listeners = {};
    
    @staticmethod
    def subscribe(event, callback):
        if (event in EventDispatcher.listeners):
            EventDispatcher.listeners[event].append(callback);
        else:
            EventDispatcher.listeners[event] = [callback];
            
    @staticmethod
    def dispatch(event, *args, **kwargs):
        if (event in EventDispatcher.listeners):
            for callback in EventDispatcher.listeners[event]:
                callback(*args, **kwargs);