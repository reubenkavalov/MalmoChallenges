import random

items=['pumpkin', 'sugar', 'egg', 'egg']

food_recipes = {'pumpkin_pie': ['pumpkin', 'egg', 'sugar'],
                'pumpkin_seeds': ['pumpkin']}

rewards_map = {'pumpkin': -5, 'egg': -25, 'sugar': -10,
               'pumpkin_pie': 100, 'pumpkin_seeds': -50}

def is_solution(reward):
    return reward == 0

def get_curr_state(items):
    state_dict = {k: v for k, v in sorted(items, key=lambda item: item[1])}
    state = tuple(state_dict.items())
    return state

def choose_action(curr_state, possible_actions, eps, q_table):
    rnd = random.random()
    a = random.randint(0, len(possible_actions) - 1)
    return possible_actions[a]
