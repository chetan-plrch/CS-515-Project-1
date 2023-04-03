import json
import sys
import re

# All the verbs of the game
verbs = {
    "go": 'go',
    "look": 'look',
    "get": 'get',
    "inventory": 'inventory',
    "drop": 'drop',
    "quit": 'quit'
}

# Directions made dynamic by centralizing the data of all directions in direction_abbreviations dict. Change the key (
# the abbreviation) and the direction name (the value - same as used in map file) and this game is good to go.
direction_abbreviations = {
    "n": "north",
    "e": "east",
    "w": "west",
    "s": "south",
    "ne": "northeast",
    "nw": "northwest",
    "se": "southeast",
    "sw": "southwest"
}


# Player class to isolate and modularize player related state and behavior into one
class Player:
    def __init__(self, name):
        self.inventory = []
        self.name = name

    def take_item(self, item):
        self.inventory.append(item)

    def give_item(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        return self.inventory


# GameEngine class to isolate and modularize engine related state and actions/behaviours into one
class GameEngine:
    def __init__(self):
        self.room = None
        self.map = None
        self.file = None
        self.person = None
        self.continue_game = True

    def load_map(self, file_name):
        f = open(file_name)
        data = json.load(f)
        self.file = f
        self.map = data
        self.room = self.map[0]

    def join_game(self, person):
        self.person = person

    def display_room(self):
        print('>', self.room['name'] + '\n')
        print(self.room['desc'] + '\n')
        if ('items' in self.room) and (len(self.room['items']) > 0):
            print('Items:', ', '.join(self.room['items']) + '\n')
        print('Exits:', ' '.join(list(self.room['exits'])) + '\n')

    def multiple_ways_string(self, possible_values):
        sen = ''
        for idx, v in enumerate(possible_values):
            if idx == 0:
                sen += f'{v} '
            elif idx == (len(possible_values) - 1):
                sen += f'or {v}'
            else:
                sen += f', {v}'
        return sen + '?'

    def check_multiple_exit(self, action):
        possible_exits = []
        multiple = [action]
        for ext in self.room['exits']:
            if ext.startswith(action):
                possible_exits.append(ext)

        try:
            if possible_exits.index(action) >= 0:
                return multiple
        except ValueError:
            if len(possible_exits) > 1:
                multiple.extend(possible_exits)
                return multiple
            return multiple

    def go_verb_action(self, action):
        try:
            multiple_exits = self.check_multiple_exit(action)
            if len(multiple_exits) == 1:
                room_id = self.room['exits'][action]
                self.room = self.map[room_id]
                print(f'You go {action}.' + '\n')
                self.display_room()
            else:
                print(f'Did you want to go', self.multiple_ways_string(multiple_exits))
        except KeyError as e:
            print(f'There\'s no way to go {action}.')

    def go_verb(self, action):
        self.go_verb_action(action)

    def look_verb(self, action):
        self.display_room()

    def get_verb(self, item):
        if 'items' in self.room:
            if item in self.room['items']:
                self.person.take_item(item)
                self.room['items'].remove(item)
                print(f'You pick up the {item}.')
            else:
                print(f'There\'s no {item} anywhere.')
        else:
            print(f'There\'s no {item} anywhere.')

    def drop_verb(self, item):
        if item in self.person.get_inventory():
            self.person.give_item(item)
            if self.room is None:
                self.room.items = []
            self.room['items'].append(item)
            print(f'You drop the {item}.')
        else:
            print(f'There\'s no {item} with you.')

    def inventory_verb_action(self, action):
        if len(self.person.inventory) == 0:
            print("You're not carrying anything.")
        else:
            print('Inventory:')
            for item in self.person.inventory:
                print(f'  {item}')

    def inventory_verb(self, action):
        self.inventory_verb_action(action)

    def check_win_condition(self):
        won = False
        if 'win_condition' in self.room:
            win_prompt = self.room['win_condition']['win_prompt']
            win_items = self.room['win_condition']['win_items']
            win_text = self.room['win_condition']['win_text']
            no_win_text = self.room['win_condition']['no_win_text']
            print(win_prompt)
            if set(win_items).issubset(set(self.person.inventory)):
                print('\n' + win_text)
                won = True
            else:
                print('\n' + no_win_text)
        return won

    def check_lose_condition(self):
        lose = False
        if 'lose_condition' in self.room:
            lose = True
            lose_prompt = self.room['lose_condition']['lose_prompt']
            escape_items = self.room['lose_condition']['escape_items']
            escape_text = self.room['lose_condition']['escape_text']
            lose_text = self.room['lose_condition']['lose_text']
            print(lose_prompt)
            if set(escape_items).issubset(set(self.person.inventory)):
                print('\n' + escape_text)
                lose = False
            else:
                print('\n' + lose_text)
        return lose

    def quit_verb(self):
        self.exit_game()

    def get_user_input(self):
        verb = ''
        action = ''
        skip = False
        cmd = input('What would you like to do? ')
        cmds = re.sub(' +', ' ', cmd.strip().lower()).split()

        if len(cmds) == 0:
            skip = True
            return [verb, action, skip]

        if len(cmds) == 1:
            vb = cmds[0]
            verb = vb.lower()
        else:
            vb = cmds[0]
            atn = ' '.join(cmds[1:])
            verb = vb.lower()
            action = atn.lower()

        all_verbs = list(verbs) + list(direction_abbreviations.keys())
        if verb not in all_verbs:
            print('Incorrect verb, Please try again!')
            skip = True
        elif verb == 'go':
            if action == '':
                print("Sorry, you need to 'go' somewhere.")
                skip = True
        elif verb == 'get' or verb == 'drop':
            if action == '':
                print(f'Sorry, you need to \'{verb}\' something.')
                skip = True

        return [verb, action, skip]

    def run(self):
        self.display_room()
        while self.continue_game:
            try:
                [verb, action, skip] = self.get_user_input()
                if skip: continue

                if verb in direction_abbreviations.keys():
                    action = direction_abbreviations[verb]
                    verb = 'go'

                if verb == verbs['go']:
                    self.go_verb(action)

                    won = self.check_win_condition()
                    lost = self.check_lose_condition()

                    if won:
                        print('\nYou win the game!\n')
                        self.continue_game = False
                    elif lost:
                        print('\nYou lost the game!\n')
                        self.continue_game = False
                elif verb == verbs['look']:
                    self.look_verb(action)
                elif verb == verbs['get']:
                    self.get_verb(action)
                elif verb == verbs['inventory']:
                    self.inventory_verb(action)
                elif verb == verbs['drop']:
                    self.drop_verb(action)
                elif verb == verbs['quit']:
                    self.exit_game()
            except EOFError:
                print(f'\nUse \'quit\' to exit.')

    def exit_game(self):
        self.continue_game = False
        self.map = None
        self.person = None
        self.room = None
        self.file.close()
        print('Goodbye!')


def run_game():
    map_filename = sys.argv[1]
    g = GameEngine()
    p = Player('John')
    g.load_map(map_filename)
    g.join_game(p)
    g.run()


run_game()
