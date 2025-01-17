# -*- coding: utf-8 -*-
from hearthstone.entities import Entity

from entity.spell_entity import SpellEntity


class LETL_005P4(SpellEntity):
    """
        魔爆术5
        对所有敌人造成$8点伤害。0对所有敌人造成$9点伤害。0对所有敌人造成$10点伤害。0对所有敌人造成$11点伤害。0对所有敌人造成$12点伤害。
    """

    def __init__(self, entity: Entity):
        super().__init__(entity)
        self.damage = 0

    def play(self, hero, target):
        pass

