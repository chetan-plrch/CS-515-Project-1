# 
# Project 1 - Horror game
This repository contains the implementation of a game engine that loads and lets the player play text horror game using a map file in JSON format. 

```
Name: Chetan Prakash Jain
Stevens Login: cjain1@stevens.edu
GitHub Repo: https://github.com/chetan-plrch/project-1
Hours spent on the project: 5 hours for development + 6 hours of testing + 2 hours on README.md
```

## Testing
To test the code, I used a combination of manual and automated testing. For automated testing, I used the pytest and similar framework to write unit tests for each core functionality, module. For manual testing, I played the game using different maps and scenarios to make sure that the game runs smoothly and without errors. I also tested each of the three extensions thoroughly to ensure that they work as intended.
* Eg: Command parsing
    * Incorrect and extra spacing between and around command text. eg: go   south    
    * Incorrect case. eg: GO   SOUTH
    * Incorrect verbs. eg: RHGLH
    * Incorrect commands: eg: $%#@% 4534    4%$%#

## Bugs or Issues
1. Command parsing - 
   * Running into an infinite loop due to recursion - resolved
2. Winning and losing condition not triggering - resolved
3. Separation of classes based upon the use-case of the game
   * Coming up with the states of those classes and behaviours affecting the state to represent it well - resolved
    
## Difficult issue or bug
One of the most challenging issues I encountered was related to the extension that adds winning and losing condition in the game. The issue was related to implementing the key (**win_condition**) and (**lose_condition**) key checks to trigger winning and losing logic, which required multiple functions to interact and modify the game state. After some debugging and refactoring, I managed to implement the feature and make it work as intended.
```
Eg: 
if 'lose_condition' in self.room:
    # Do run the losing logic
    
if 'win_condition' in self.room:
    # Do run the winning logic
```

## Known Issues
I encountered several bugs and issues while working on the project. One issue was related to parsing the JSON map file. Sometimes, the code would fail to parse a map file with a valid JSON format due to some edge cases. I also had some issues with the inventory system, which sometimes resulted in unexpected behavior when picking up or dropping items. But based on my testing I didn't find any bugs in this game

## Extensions
The project also implements three extensions that add new features and verbs to the game:
1. **drop verb** (on the custom map json available on github):

#### Where are they in the map: (Drop doesn't require any change in the map file)

#### How to excerise this verb:
```
> Mysterious Entrance

You find yourself standing in front of a grand entrance with a broken gate and a black cat staring at you. The door is slightly open, inviting you to come inside. As you push it open, you feel a chill run down your spine.

Items: cobweb, dagger, skeleton

Exits: north northeast

What would you like to do? drop cobweb
There's no cobweb with you.
What would you like to do? get dagger
You pick up the dagger.
What would you like to do? inventory  
Inventory:
  dagger
What would you like to do? look
> Mysterious Entrance

You find yourself standing in front of a grand entrance with a broken gate and a black cat staring at you. The door is slightly open, inviting you to come inside. As you push it open, you feel a chill run down your spine.

Items: cobweb, skeleton

Exits: north northeast

What would you like to do? drop daggger
There's no daggger with you.
What would you like to do? drop dagger
You drop the dagger.
What would you like to do? inventory
You're not carrying anything.
What would you like to do? look
> Mysterious Entrance

You find yourself standing in front of a grand entrance with a broken gate and a black cat staring at you. The door is slightly open, inviting you to come inside. As you push it open, you feel a chill run down your spine.

Items: cobweb, skeleton, dagger

Exits: north northeast

What would you like to do? 

```
2. **directions as abbreviations** (on the custom map json available on github):

#### Where are they in the map: (This extension doesn't require any change in the map file)

#### How to excerise this extension:
```
> Mysterious Entrance

You find yourself standing in front of a grand entrance with a broken gate and a black cat staring at you. The door is slightly open, inviting you to come inside. As you push it open, you feel a chill run down your spine.

Items: cobweb, dagger, skeleton

Exits: north northeast

What would you like to do? n
You go north.

> Dreadful Lounge

The air is thick with an unidentifiable scent. The centerpiece of the room is a cursed couch, and a flickering chandelier providing minimal light

Items: cursed couch, old portrait, poisoned wine, secret book

Exits: south north northwest

What would you like to do? no
Incorrect verb, Please try again!
What would you like to do? nw
You go northwest.

> Blessed room

You step into a room that feels different from the others, suddenly you are happy out of nowhere. It's bright and warm. The air smells of lavender. As you look around, you notice various religious symbols and artifacts placed throughout the room, such as a cross hanging on the wall and a Bible on the nightstand, it makes you feel at ease.

Items: cross of jesus, bible, holy water, lamp

Exits: south north northwest southwest

What would you like to do? sout
Incorrect verb, Please try again!
What would you like to do? s
You go south.

> Haunted Bedroom

You open the door to a haunted bedroom that looks like it's straight out of a horror movie. The queen-sized bed has tattered pillows and a skeleton on spikes. A wardrobe with stands in the corner.

Items: bloody knife, creepy doll, ouija board, spiderweb, lamp

Exits: south north northeast southeast

What would you like to do? th
Incorrect verb, Please try again!
What would you like to do? go th
There's no way to go th.
What would you like to do? go southe
There's no way to go southe.
What would you like to do? go south
You go south.

> Dreadful Lounge

The air is thick with an unidentifiable scent. The centerpiece of the room is a cursed couch, and a flickering chandelier providing minimal light

Items: cursed couch, old portrait, poisoned wine, secret book

Exits: south north northwest

What would you like to do? 
```

3. **winning and losing conditions**  (on the custom map json available on github)

### Winning condition

#### Where are they in the map:
```
# This room contains the winning condition:
{
		"name": "Terrifying Exit",
		"desc": "The exit of the house, placed in the right corner a tombstone with your name on it. Graveyard visible from it's window's, and a door leading outside to the graveyard.",
		"items": ["tombstone"],
		"win_condition": {
			"win_prompt": "A ghost appears in front of the exit door. You are scared to hell!",
			"win_items": ["cross of jesus"],
			"win_text": "You scared the ghost away with the 'cross of jesus' you picked and exited the ghost house, you win!",
			"no_win_text": "You don't have the 'cross of jesus' to scare the ghost away! Search for it in the house to exit/win!",
			"optional_description": "For the player to win, they need to have 'cross of jesus' when they land into this room"
		},
		"exits": {
			"south": 9,
			"northwest": 9,
			"southwest": 0
		}
}
```

#### Explanation of the winning condition: 
1. Any room with the following keys and appropriate values can be used to trigger a winning condition:
2. all the keys except optional_description are mandatory for the winning condition to work correctly, failing which the program will error out
3. The keys should be exact in naming and are in lowercase
4. The below is the explanation of the keys:
```
    "win_condition": {
                "win_prompt": A prompt to show something is happening in this room",
                "win_items": items array that are required to trigger the winning condition, without this list of items the winning condition is not successful,
                "win_text": The text to indicate the player that they have won the game
                "no_win_text": In case of player doesn't have all the win_items, this prompt is shown to user to indicate what items they are missing to win this game
                "optional_description": The desciption is of no use in the game, just in the map file to explain this mapping better
    }

```

#### How to exercise winning condition:
```
> Mysterious Entrance

You find yourself standing in front of a grand entrance with a broken gate and a black cat staring at you. The door is slightly open, inviting you to come inside. As you push it open, you feel a chill run down your spine.

Items: cobweb, dagger, skeleton

Exits: north northeast

What would you like to do? go northeast
You go northeast.

> Haunted Bedroom

You open the door to a haunted bedroom that looks like it's straight out of a horror movie. The queen-sized bed has tattered pillows and a skeleton on spikes. A wardrobe with stands in the corner.

Items: bloody knife, creepy doll, ouija board, spiderweb, lamp

Exits: south north northeast southeast

What would you like to do? go north
You go north.

> Blessed room

You step into a room that feels different from the others, suddenly you are happy out of nowhere. It's bright and warm. The air smells of lavender. As you look around, you notice various religious symbols and artifacts placed throughout the room, such as a cross hanging on the wall and a Bible on the nightstand, it makes you feel at ease.

Items: cross of jesus, bible, holy water, lamp

Exits: south north northwest southwest

What would you like to do? get cross of jesus
You pick up the cross of jesus.
What would you like to do? go north
You go north.

> Abandoned Bathroom

You walk into an abandoned bathroom that looks like it hasn't been used in years. The walls and floor are covered in mold, and a rusty bathtub makes your skin crawl. A broken toilet stands in the corner.

Items: bloody handprint, foggy mirror, rusty razor, moldy towels

Exits: south north northeast southeast

What would you like to do? go northeast
You go northeast.

> Haunted Playroom

You step into a haunted playroom that feels like it's designed for kids, but something

Items: ouija board, old rocking horse, music box, sinister puppets

Exits: south north northeast southeast

What would you like to do? inventory
Inventory:
  cross of jesus
What would you like to do? go north
You go north.

> Terrifying Exit

The exit of the house, placed in the right corner a tombstone with your name on it. Graveyard visible from it's window's, and a door leading outside to the graveyard.

Items: tombstone

Exits: south northwest southwest

A ghost appears in front of the exit door. You are scared to hell!

You scared the ghost away with the 'cross of jesus' you picked and exited the ghost house, you win!

You win the game!
```

### Losing conditions

#### Where are they in the map:
```
# This room contains the losing condition:
{
		"name": "Whispering Library",
		"desc": "You walk into an library that feels like it's straight out of a ghost story. Dusty bookcases line the walls, and a haunted wooden table occupies the center of the room. Ghostly armchairs are scattered around the room.",
		"items": ["ancient tome", "skeleton key", "spell book", "cursed scroll", "ghostly whispers"],
		"exits": {
			"south": 6,
			"north": 8,
			"northeast": 8,
			"southeast": 5
		},
		"lose_condition": {
			"lose_prompt": "The library is big. You lost your way back and entered a very dark area, you can't see anything now",
			"lose_text": "You didn't have 'lamp' to find your way back, You die because of fear of darkness!",
			"escape_items": ["lamp"],
			"escape_text": "Thankfully you had a lamp! you found your way back to the entrance of library"
		}
}
```

#### Explanation of the losing condition: 
1. Any room with the following keys and appropriate values can be used to trigger a losing condition:
2. all the keys except optional_description are mandatory for the losing condition to work correctly, failing which the program will error out
3. The keys should be exact in naming and are in lowercase
4. The below is the explanation of the keys:
```
    "lose_condition": {
			"lose_prompt": A prompt to show something is happening in this room,
			"lose_text": The text to indicate the player that they have lost the game,
			"escape_items": The items that are required with the player to not lose and continue playing the game,
			"escape_text": Text that is shown to the user when they have the escape_items in their inventory to indicate they escaped without losing the game and can continue the game
		}
```

#### How to exercise losing condition:
```
> Mysterious Entrance

You find yourself standing in front of a grand entrance with a broken gate and a black cat staring at you. The door is slightly open, inviting you to come inside. As you push it open, you feel a chill run down your spine.

Items: cobweb, dagger, skeleton

Exits: north northeast

What would you like to do? go northeast
You go northeast.

> Haunted Bedroom

You open the door to a haunted bedroom that looks like it's straight out of a horror movie. The queen-sized bed has tattered pillows and a skeleton on spikes. A wardrobe with stands in the corner.

Items: bloody knife, creepy doll, ouija board, spiderweb, lamp

Exits: south north northeast southeast

What would you like to do? go north
You go north.

> Blessed room

You step into a room that feels different from the others, suddenly you are happy out of nowhere. It's bright and warm. The air smells of lavender. As you look around, you notice various religious symbols and artifacts placed throughout the room, such as a cross hanging on the wall and a Bible on the nightstand, it makes you feel at ease.

Items: cross of jesus, bible, holy water, lamp

Exits: south north northwest southwest

What would you like to do? get cross of jesus
You pick up the cross of jesus.
What would you like to do? go northwest
You go northwest.

> Whispering Library

You walk into an library that feels like it's straight out of a ghost story. Dusty bookcases line the walls, and a haunted wooden table occupies the center of the room. Ghostly armchairs are scattered around the room.

Items: ancient tome, skeleton key, spell book, cursed scroll, ghostly whispers

Exits: south north northeast southeast

The library is big. You lost your way back and entered a very dark area, you can't see anything now

You didn't have 'lamp' to find your way back, You die because of fear of darkness!

You lost the game!

```

## Running the Game
To run the game, navigate to the base directory of the cloned repository and run python3 adventure.py [map name]. 
The game can be run using any of the map files in the repository.

## New Map File (also present in repo as loop.map file)
```
[
    {
		"name": "Mysterious Entrance",
		"desc": "You find yourself standing in front of a grand entrance with a broken gate and a black cat staring at you. The door is slightly open, inviting you to come inside. As you push it open, you feel a chill run down your spine.",
		"items": ["cobweb", "dagger", "skeleton"],
		"exits": {
			"north": 1,
			"northeast": 2
		}
	},
	{
		"name": "Dreadful Lounge",
		"desc": "The air is thick with an unidentifiable scent. The centerpiece of the room is a cursed couch, and a flickering chandelier providing minimal light",
		"items": ["cursed couch", "old portrait", "poisoned wine", "secret book"],
		"exits": {
			"south": 0,
			"north": 2,
			"northwest": 3
		}
	},
	{
		"name": "Haunted Bedroom",
		"desc": "You open the door to a haunted bedroom that looks like it's straight out of a horror movie. The queen-sized bed has tattered pillows and a skeleton on spikes. A wardrobe with stands in the corner.",
		"items": ["bloody knife", "creepy doll", "ouija board", "spiderweb", "lamp"],
		"exits": {
			"south": 1,
			"north": 3,
			"northeast": 5,
			"southeast": 0
		}
	},
	{
		"name": "Blessed room",
		"desc": "You step into a room that feels different from the others, suddenly you are happy out of nowhere. It's bright and warm. The air smells of lavender. As you look around, you notice various religious symbols and artifacts placed throughout the room, such as a cross hanging on the wall and a Bible on the nightstand, it makes you feel at ease.",
		"items": ["cross of jesus", "bible", "holy water", "lamp"],
		"exits": {
			"south": 2,
			"north": 4,
			"northwest": 7,
			"southwest": 0
		}
	},
	{
		"name": "Abandoned Bathroom",
		"desc": "You walk into an abandoned bathroom that looks like it hasn't been used in years. The walls and floor are covered in mold, and a rusty bathtub makes your skin crawl. A broken toilet stands in the corner.",
		"items": ["bloody handprint", "foggy mirror", "rusty razor", "moldy towels"],
		"exits": {
			"south": 3,
			"north": 5,
			"northeast": 9,
			"southeast": 2
		}
	},
	{
		"name": "Cursed Kitchen",
		"desc": "You enter a cursed kitchen that seems to have a mind of its own. Appliances turn on and off by themselves, and the central island seems to move around. A creepy dining table stands nearby.",
		"items": ["haunted knife", "possessed blender", "maggoty food", "spilled sauce", "satanic symbols"],
		"exits": {
			"south": 4,
			"north": 6,
			"northwest": 10,
			"southwest": 3
		}
	},
	{
		"name": "Possessed Study",
		"desc": "You step into a possessed study that seems to be haunted by an evil spirit. A demonic wooden desk occupies one corner of the room, and a cursed chair is pulled up to it. A dark floor lamp provides sinister lighting.",
		"items": ["black candle", "demonic book", "cursed pen", "creepy painting", "voodoo doll", "lamp"],
		"exits": {
			"south": 5,
			"north": 7,
			"northwest": 6,
			"southwest": 4
		}
	},
	{
		"name": "Whispering Library",
		"desc": "You walk into an library that feels like it's straight out of a ghost story. Dusty bookcases line the walls, and a haunted wooden table occupies the center of the room. Ghostly armchairs are scattered around the room.",
		"items": ["ancient tome", "skeleton key", "spell book", "cursed scroll", "ghostly whispers"],
		"exits": {
			"south": 6,
			"north": 8,
			"northeast": 8,
			"southeast": 5
		},
		"lose_condition": {
			"lose_prompt": "The library is big. You lost your way back and entered a very dark area, you can't see anything now",
			"lose_text": "You didn't have 'lamp' to find your way back, You die because of fear of darkness!",
			"escape_items": ["lamp"],
			"escape_text": "Thankfully you had a lamp! you found your way back to the entrance of library"
		}
	},
	{
		"name": "Creaky Gym",
		"desc": "You enter a creepy gym that seems to be haunted by the ghosts of previous gym-goers. Rusty exercise equipment lines the walls, and a ghostly mirror covers one entire wall. An old water cooler stands in the corner.",
		"items": ["blood stained towel", "haunted weight", "possessed jump rope", "creepy mannequin", "spooky protein powder"],
		"exits": {
			"south": 7,
			"north": 9,
			"northwest": 6,
			"southwest": 5
		}
	},
	{
		"name": "Haunted Playroom",
		"desc": "You step into a haunted playroom that feels like it's designed for kids, but something",
		"items": ["ouija board", "old rocking horse", "music box", "sinister puppets"],
		"exits": {
			"south": 8,
			"north": 10,
			"northeast": 7,
			"southeast": 4
		}
	},
	{
		"name": "Terrifying Exit",
		"desc": "The exit of the house, placed in the right corner a tombstone with your name on it. Graveyard visible from it's window's, and a door leading outside to the graveyard.",
		"items": ["tombstone"],
		"win_condition": {
			"win_prompt": "A ghost appears in front of the exit door. You are scared to hell!",
			"win_items": ["cross of jesus"],
			"win_text": "You scared the ghost away with the 'cross of jesus' you picked and exited the ghost house, you win!",
			"no_win_text": "You don't have the 'cross of jesus' to scare the ghost away! Search for it in the house to exit/win!",
			"optional_description": "For the player to win, they need to have 'cross of jesus' when they land into this room"
		},
		"exits": {
			"south": 9,
			"northwest": 9,
			"southwest": 0
		}
	}
]
```
