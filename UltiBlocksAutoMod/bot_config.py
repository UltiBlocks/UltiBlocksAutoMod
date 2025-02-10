bots={}

from .bots.remindmebot import iteration as remindmebot
bots["remindmebot"]={
    "name":"remindmebot",
    "prettyname":"Reminder Bot",
    "description":"A bot that reminds users on their talk pages when they add '/remindme' to a talk page",
    "function":remindmebot
}

from .bots.remindmebot import iteration as sandboxbot
bots["sandboxbot"]={
    "name":"sandboxbot",
    "prettyname":"Sandbox Clearing Bot",
    "description":"A bot that clears the global sandbox if no human has edited it for 4 hours",
    "function":sandboxbot
}