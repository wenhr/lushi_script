# -*- coding: utf-8 -*-
from hearthstone.entities import Entity

from entity.spell_entity import SpellEntity


class LETL_246(SpellEntity):
    """
        大地践踏5
        对所有敌人造成$10点伤害，并使其下回合的速度值减慢（3）点。0对所有敌人造成$12点伤害，并使其下回合的速度值减慢（3）点。0对所有敌人造成$13点伤害，并使其下回合的速度值减慢（3）点。0对所有敌人造成$14点伤害，并使其下回合的速度值减慢（3）点。0对所有敌人造成$15点伤害，并使其下回合的速度值减慢（3）点。
    """

    def __init__(self, entity: Entity):
        super().__init__(entity)
        self.damage = 0

    def play(self, hero, target):
        pass

