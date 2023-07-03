import json
from datetime import datetime


class Memory:
    def __init__(self):
        self.message_history = [{"role": "system", "content": ""}]
        self.time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    
    def add_message(self, message):
        self.message_history.append(message)
        
        serialized_messages = json.dumps(self.message_history, indent=4)
 
        with open(f"./store/{self.time_now}.json", "w") as file:
            file.write(serialized_messages)
    