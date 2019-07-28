from metalite.core import Engine
import metalite.actions

import numpy as np
import matplotlib.pyplot as plt


def strategy1():
    engine = Engine()
    [engine.attack_tower() for _ in range(10)]
    print(engine.game_state())


def strategy2():
    engine = Engine()
    [engine.attack_tower() for _ in range(5)]
    engine.level_up_hero()
    [engine.attack_tower() for _ in range(5)]
    print(engine.game_state())


def simulate(heuristic):
    engine = Engine()
    steps = 0
    while engine.game_state()["hero_lvl"] < 50:
        action = heuristic(engine.action_space(), engine.game_state())
        engine.step(action)
        steps += 1

    return steps, engine.game_state()


def heuristic_random(actions, game_state):
    return np.random.choice(actions)


def heuristic_greedy(actions, game_state):
    if metalite.actions.LEVEL_UP_HERO in actions:
        return metalite.actions.LEVEL_UP_HERO

    if metalite.actions.BUY_SHARDS in actions:
        return metalite.actions.BUY_SHARDS

    return metalite.actions.ATTACK_TOWER


def main():
    np.random.seed(1337)
    metric = []
    for i in range(500):
        steps, gs = simulate(heuristic_random)
        metric.append(gs["towers_destroyed"])

    plt.hist(metric)
    plt.show()


if __name__ == "__main__":
    main()
