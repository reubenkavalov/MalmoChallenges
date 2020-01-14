import random
import operator

items=['pumpkin', 'sugar', 'egg', 'egg', 'red_mushroom', 'planks', 'planks']

food_recipes = {'pumpkin_pie': ['pumpkin', 'egg', 'sugar'],
                'pumpkin_seeds': ['pumpkin'],
                'bowl': ['planks', 'planks'],
                'mushroom_stew': ['bowl', 'red_mushroom']}

rewards_map = {'pumpkin': -5, 'egg': -25, 'sugar': -10,
               'pumpkin_pie': 100, 'pumpkin_seeds': -50,
               'planks': -5, 'bowl': -1, 'red_mushroom': 5, 'mushroom_stew': 100}


def is_solution(reward):
    return reward == 200


def get_curr_state(items):
    state_dict = {k: v for k, v in sorted(items, key=lambda item: item[1])}
    state = tuple(state_dict.items())
    return state


def choose_action(curr_state, possible_actions, eps, q_table):
    rnd = random.random()
    if rnd < eps:
        print('Random Action')
        action = random.choice(possible_actions)
    else:
        possible_q_values = q_table[curr_state].items()
        biggest_q_action = max(possible_q_values, key=operator.itemgetter(1))[0]
        y = q_table[curr_state][biggest_q_action]
        x = biggest_q_action
        biggest_q_dict = {x:y}
        for action, q_value in possible_q_values:
            if q_value == y:
                biggest_q_dict[action] = q_value
        action = random.choice([k for k, v in biggest_q_dict.items()])
    return action
