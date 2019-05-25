from engine.config import DEFAULT_CONFIG
import engine.actions


class Engine:
    def __init__(self, config=DEFAULT_CONFIG):
        self.config = self._safe_config(config)
        self.towers_destroyed = 0
        self.hero_lvl = 1
        self.shards = 0
        self.currency = 0
        self.reset()

    def _safe_config(self, config):
        safe_config = {}
        for key, default_value in DEFAULT_CONFIG.items():
            value = config[key]
            if (value is None) or (value < 0):
                value = default_value

            if key == "n_towers_per_level" and value <= 0:
                value = default_value

            safe_config[key] = value

        return safe_config

    def reset(self):
        self.towers_destroyed = 0
        self.hero_lvl = self.config["start_hero_lvl"]
        self.shards = self.config["start_shards"]
        self.currency = self.config["start_currency"]

    def action_space(self):
        actions = [engine.actions.ATTACK_TOWER]

        if self.can_level_up():
            actions.append(engine.actions.LEVEL_UP_HERO)

        if self.can_buy_shards():
            actions.append(engine.actions.BUY_SHARDS)

        return actions

    def step(self, action):
        if action == engine.actions.BUY_SHARDS:
            return self.buy_shards()
        elif action == engine.actions.LEVEL_UP_HERO:
            return self.level_up_hero()
        else:
            return self.attack_tower()

    def tower_level(self):
        return 1 + int(self.towers_destroyed / self.config["n_towers_per_level"])

    def attack_tower(self):
        self.towers_destroyed += 1
        power_ratio = self.hero_lvl / self.tower_level()

        self.currency += int(self.config["currency_reward"] * power_ratio)
        self.shards += int(self.config["shard_reward"] * power_ratio)
        return True

    def can_level_up(self):
        return self.shards >= self.config["shards_per_hero_level"]

    def level_up_hero(self):
        if self.can_level_up():
            self.shards -= self.config["shards_per_hero_level"]
            self.hero_lvl += 1
            return True
        return False

    def can_buy_shards(self):
        return self.currency >= self.config["shard_bundle_price"]

    def buy_shards(self):
        if self.can_buy_shards():
            self.currency -= self.config["shard_bundle_price"]
            self.shards += self.config["shard_bundle_amount"]
            return True
        return False

    def game_state(self):
        return {
            "towers_destroyed": self.towers_destroyed,
            "currency": self.currency,
            "shards": self.shards,
            "hero_lvl": self.hero_lvl,
            "tower_lvl": self.tower_level(),
            "actions": self.action_space()
        }
