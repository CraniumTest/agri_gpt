class AgriGPTInterface:
    def __init__(self):
        self.init_components()

    def init_components(self):
        # Initialize mocked components for demonstration
        print("Initializing AgriGPT Components...")

    def get_user_input(self):
        # Simulate user input for the demo
        return input("Ask AgriGPT: ")

    def run(self):
        print("Welcome to AgriGPT - Your Intelligent Farm Management Assistant.")
        while True:
            user_input = self.get_user_input()
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting. Have a great day!")
                break
            response = self.process_input(user_input)
            print(f"AgriGPT: {response}")

    def process_input(self, user_input):
        # This function would be more complex; involves NLP, for now, using mock responses
        return f"Processing '{user_input}'. Recommendation: [Mock Recommendation]"


if __name__ == "__main__":
    app = AgriGPTInterface()
    app.run()
