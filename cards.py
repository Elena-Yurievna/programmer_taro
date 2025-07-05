import random

CARDS = [
    {
        "title": "Rubber Duck",
        "emoji": "🧘‍♂️",
        "description": "Talk to the duck. The answer will come."
    },
    {
        "title": "Legacy Bug",
        "emoji": "🐛",
        "description": "It was broken long before you got here."
    },
    {
        "title": "Push to Prod",
        "emoji": "🚀",
        "description": "Time to deploy. It will either fly or explode."
    },
    {
        "title": "Overengineer",
        "emoji": "🧂",
        "description": "It could’ve been simple. But you made it majestic."
    },
    {
        "title": "Hot Fix",
        "emoji": "🪤",
        "description": "A quick patch that will stay forever. Probably in prod."
    },
    {
        "title": "Dependency Hell",
        "emoji": "🔥",
        "description": "You updated one thing, and everything else broke."
    },
    {
        "title": "Senior’s Magic",
        "emoji": "🎩",
        "description": "It works. Don’t ask how. Just don’t touch it."
    },
    {
        "title": "Frontend’s Fault",
        "emoji": "😡",
        "description": "Backend is fine. Make sure the frontend knows how APIs work."
    },
    {
        "title": "Blame Someone Else",
        "emoji": "🤷",
        "description": "Check git blame. The name may surprise you."
    },
    {
        "title": "Unexpected Day Off",
        "emoji": "😵‍💫",
        "description": "A perfect day to do absolutely nothing."
    },
    {
        "title": "No Coffee, No Debug",
        "emoji": "☕",
        "description": "Coffee is your debugger. First coffee, then code."
    },
    {
        "title": "Quit — and it gets better",
        "emoji": "🔥",
        "description": "Sometimes the only fix is to leave the project forever."
    },
    {
        "title": "Works on My Machine",
        "emoji": "💾",
        "description": "Locally, you are a god. Prod is another universe."
    },
    {
        "title": "Read the Docs",
        "emoji": "📚",
        "description": "The answer exists. You just have to actually read."
    },
    {
        "title": "No Specs, No Clue",
        "emoji": "📜",
        "description": "They called you a dreamer. You just needed a spec."
    },
    {
        "title": "Not My Job",
        "emoji": "🤑",
        "description": "Stay in your lane. Let someone else fix it."
    },
    {
        "title": "Monday Problem",
        "emoji": "😑",
        "description": "Ignore it for now. Go do something mildly enjoyable."
    },
    {
        "title": "Take Sick Leave",
        "emoji": "🏖",
        "description": "A great day to enjoy doing absolutely nothing."
    },
    {
        "title": "Deadline Approaches",
        "emoji": "⏳",
        "description": "Only caffeine and miracles remain. Code like there’s no tomorrow."
    },
    {
        "title": "Ancient Code Curse",
        "emoji": "🧟‍♂️",
        "description": "Old code demands new blood. You are the sacrifice."
    },
    {
        "title": "It’s Not a Bug",
        "emoji": "🧠",
        "description": "It’s a feature. Everything is working as intended."
    },
]

def draw_cards(n=3):
    """Return n random cards from the deck"""
    return random.sample(CARDS, k=n)
