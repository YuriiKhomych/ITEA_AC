
class Subscriber:
    def __init__(self, publisher):
        self.publisher = publisher

    def communicate(self, request):
        return self.publisher.api(request)
