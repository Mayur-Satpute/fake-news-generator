import random

# Word banks
subjects = [
    "Arjun Kapoor’s Angry Stare", "Mumbaikars", "IIT Baba", "Budget Middle Class",
    "Vishal Mega Mart Jhola", "RCB Fans", "Flat-Earthers", "Lazy Students",
    "Influencers", "Conspiracy Theorists", "Cricketers", "TikTok Trolls",
    "YouTubers", "Aliens", "Talking Dogs", "Superheroes", "Chefs", "Gamers",
    "Politicians", "Celebrities"
]

actions = [
    "accidentally predict", "celebrate", "explode over", "laugh at",
    "call out", "mimic", "dance with", "cry over", "ban", "launch",
    "invent", "warn about", "trade for samosas", "hide under the bus",
    "go viral for", "be memed about", "trend with", "reject", "approve", "banter about"
]

objects = [
    "Makhana Board", "$4000 jhola", "aura farming in monsoon", "a failed prophecy",
    "IPL victory chant", "Budget memes", "glare reaction", "teleporting chaiwala",
    "self-cleaning slippers", "mind-reading goat", "robot dosa maker", "talking mirror",
    "chocolate vaccine", "invisible slippers", "viral TikTok sound", "hologram girlfriend",
    "nano chapatis", "banana-powered car", "dream recorder", "magic samosas"
]

places = [
    "in Mumbai floods", "inside Parliament", "on Instagram Reels", "in Silicon Valley",
    "at IPL final", "on TikTok", "in WhatsApp groups", "on Mars", "at the Taj Mahal",
    "under your bed", "on a Zoom call", "inside a meme template", "in Bihar",
    "at a McDonald’s", "in your dreams", "on YouTube Shorts", "at a wedding",
    "in the Indian Railways", "at an IIT campus", "in a political speech"
]


def generate_fake_news():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places)
    return f"----------BREAKING NEWS----------\n📰:{subject} {action} {obj} {place}!"

# User interaction loop
while True:
    print("\n" + generate_fake_news())
    
    again = input("Generate another? (y/n): ").strip().lower()
    if again == "n":
        print("Thanks for playing! Goodbye 👋")
        break

