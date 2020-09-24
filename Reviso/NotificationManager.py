# This will be a package where we keep all the classes relating to the notifications and reminders.
import plyer
import json

class Reminder:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

    def turnToDict(self):
        return {{"date":self.date, "time":self.time, "title":self.title, "description":self.description}}

class ReminderMemory:
    def __init__(self):
        with open("C:\\Users\\44773\\Documents\\Python\\Reviso\\reminders.json") as file:
            self.prev_reminders = json.load(file)

    def add(self, reminder_dict):
        with open(self.prev_reminders, 'a') as file:
            json.dumps(reminder_dict, file)
