input

noCharacters = [",", "-", ".", "!", "?", "'", "#"]

release = []

answers = ["hi there", "hi there", "good, you?", "good, you?", "good!", "great.", "good.",
"aw, I'm sorry", "aw, I'm sorry", "ChatDrone Python", "the sky :P", "great, you?",
"yeah, I know right!", "you too! Finally! I've been dying to meet you.",
"it has.", "top of the mornin', milady!",
"evenin', darling. What's for supper?", "and to you, too!", "what's poppin'?",
"sup my dude.", "sup!", "what's up?", "cool.", "cool!", "sounds good!", "awesome!",
"ahaha, okay.", "seriously?", "come on!", "cool.", "POOOOOOLLOOOOO", "thanks!",
"you're nice!", "so are you.", "I know, right.", "Right???", "yup.", "I thought so too.",
"Really and truly.", "Really? That's so cool.", "So, how was your day?", "Haha, I know.",
"haha, your funny.", "hehe", "LOLLL", "ah, alright.", "sleep well",
"I know, right!", "I guess.", "Sure, lol", "What's poppin'?", "ChatDrone Python.",
"I was made by scratch.mit.edu/users/HappyParakeet. Visit me there!", "I have to say, Star Wars: The Last Jedi is the bomb.",
"Ready Player One by Ernst Cline is a must-read. Absolute favorite! I can't wait for the 2018 movie!", "In my free time, I read.",
"Awesome! What was your favorite part?"]

valid_inputs = ["hello", "hi", "how are you", "how are you doing", "im good", "good", "fine",
"bad", "not so good", "whats your name", "whats up", "hows everything", "long time no see",
"nice to meet you", "its been a while", "good morning", "good evening", "good afternoon", "yo", "hey",
"hey man", "hey dude", "yes", "ya", "sure", "definitely", "no", "naw", "nah", "nope", "marco",
"thats cool", "thats nice", "youre nice", "cool", "awesome", "neat", "thats cool", "really",
"same", "your welcome", "good talk", "food", "haha", "lol", "its okay",
"im going to bed", "this is awkward", "this is wierd", "thanks", "sup", "who are you", "who made you",
"what is your favorite movie", "what is your favorite book", "what do you do in your free time", "me too"]

print "Be sure to click inside of the chat box!"
print "Meet ChatDrone Python! You can use caps, punctuation, and add phrases that we did't have before!"

def start():
  got_it = 0
  for i in range (len(valid_inputs)):
    if chat == valid_inputs[i]:
     print answers[i]
     got_it += 1
     break
  if got_it == 0:
    print "Sorry, I do not know that word or phrase. Reply 'yes' if you would like to add it."
    addition = input(' ')
    if addition == "yes":
      print "Type what the input is, here."
      valid_inputs.append(input(' '))
      print "Type what the output to this phrase is here."
      answers.append(input(' '))
      print "Added! Now you can try it!"
      addition = "00"

while True:
  chat = input(' ')
  for letter in chat:
    if letter not in noCharacters:
      add_release = (letter.lower())
      release.append(add_release)
  chat = ""
  for i in range(0, len(release)):
    chat = chat + release[i]
  release = []
  start()