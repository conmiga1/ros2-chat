class Bob(Node):
    def __init__(self):
        super().__init__('bob')
        self.srv = self.create_service(Chatbot, 'chatbot', self.handle_request)
        self.replies = [
            "Alice, good to meet you!",
            "Yeah, we arrived last week.",
            "It's exciting! It's much busier than the last city we lived in. I was working in Seattle for the last 3 years.",
            "Actually, I'm not married. I moved here with my dog, Charles. We are very close.",
            "What about you?",
            "How old are they?",
            "Oh, great. That age is a lot of fun.",
        ]
        self.i = 0

    def handle_request(self, request, response):
        response.sentence = self.replies[self.i]
        self.i += 1
        return response
