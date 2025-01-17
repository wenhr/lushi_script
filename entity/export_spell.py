# -*- coding: utf-8 -*-
import json
import os
import re

from tqdm import tqdm

from mercenaries import MERCENARIES
from hearthstone.mercenaryxml import load
import requests

dbfData = {}


def loadjson():
    # file_list = requests.get("https://api.hearthstonejson.com/v1/").text
    # ver_list = list(map(int, re.findall("/v1/(\d+)/all/", file_list)))
    # new_version = max(ver_list)
    # print(f"new_version: {new_version}")
    # print("loading card_data...")
    # cardJson_data = ""
    # cardJson_File = f'{new_version}.json'
    #
    # cardJson_url = f'https://api.hearthstonejson.com/v1/{new_version}/zhCN/cards.json'
    # print(f"--online mode({cardJson_url})")
    # cardJson_req = requests.get(cardJson_url, stream=True)
    # cardJson_byte = b''
    # pbar = tqdm(total=-1, unit='B', unit_scale=True)
    # for chunk in cardJson_req.iter_content(chunk_size=1024):
    #     assert chunk != None
    #     cardJson_byte += chunk
    #     pbar.update(1024)
    # pbar.close()
    # cardJson_data = cardJson_byte.decode()
    # assert cardJson_data != ""
    # ---------------------------------
    cardJson_File = '124497.json'
    with open(cardJson_File, "r", encoding='utf-8') as f:
        cardJson_data = f.read()
        # f.write(cardJson_data)

    cardData_temp = json.loads(cardJson_data)
    assert cardData_temp is not None
    print("loaded card_json successfully!")
    cardData = {}
    for c in cardData_temp:
        cardData[c['id']] = c
        dbfData[c['dbfId']] = c
    return cardData


def run():
    cardData = loadjson()

    m = MERCENARIES
    sim_path = os.path.join(os.getcwd(), "cards")
    print("loading sim_data from", sim_path)
    mer = load(locale='zhCN')
    cardData = loadjson()
    for i, m in mer[0].items():
        ids = m.skin_dbf_ids
        did = ''
        for i in ids:
            if i == 77388 or i == 77389:
                continue
            did = i
            break
        # print(dbfData[id])
        # if not id.startswith('LETL_030H'):
        #     continue
        id = dbfData[did]['id']
        print(cardData[id]['name'])
        folder_path = os.path.join(sim_path, id[:-3])
        ex = os.path.exists(folder_path)
        if not ex:
            os.mkdir(folder_path)
        with open(os.path.join(folder_path, "__init__.py"), 'w+', encoding='utf-8') as f:
            muban = """# -*- coding: utf-8 -*-
"""
            f.write(muban)
            pass

        for spell in m.specializations:
            abl = spell['abilities']
            for ab in abl:
                abdid = ab['tiers'][-1]['dbf_id']
                id = dbfData[abdid]['id']
            # print(abl['tiers'][-1][:-3])
                name = cardData[id]['id']
                print(cardData[name]['name'])

                file_path = os.path.join(folder_path, name[:-3] + '.py')
                with open(file_path, 'a+', encoding='utf-8') as f:
                    f.seek(0)
                    content = f.read()
                    if "class" in content:
                        continue
                    muban = f"""# -*- coding: utf-8 -*-
from hearthstone.entities import Entity

from entity.spell_entity import SpellEntity


class {name[:-3]}(SpellEntity):
    \"\"\"
        {cardData[name]['name']}
        {cardData[name]['text']}
    \"\"\"

    def __init__(self, entity: Entity):
        super().__init__(entity)
        self.damage = 0

    def play(self, hero, target):
        pass

"""
                    f.write(muban)

        for equ in m.equipment:

            eq = equ['tiers'][-1]['dbf_id']
            # print(dbfData[eq])
            id = dbfData[eq]['id']
            # print(equip['tiers'][-1][:-3])
            name = cardData[id]['id']
            print(cardData[id]['name'])

            file_path = os.path.join(folder_path, name[:-3] + '.py')
            with open(file_path, 'a+', encoding='utf-8') as f:
                f.seek(0)
                content = f.read()
                if "class" in content:
                    continue
                muban = f"""# -*- coding: utf-8 -*-
from hearthstone.entities import Entity

from entity.spell_entity import SpellEntity


class {name[:-3]}(SpellEntity):
    \"\"\"
        {cardData[name]['name']}
        {cardData[name]['text']}
    \"\"\"

    def __init__(self, entity: Entity):
        super().__init__(entity)

    def equip(self, hero):
        pass

            """
                f.write(muban)

    pass


if __name__ == '__main__':
    # mer = load(locale='zhCN')
    # cardData = loadjson()
    # for i, m in mer[0].items():
    #     ids = m.skin_dbf_ids
    #     id = ''
    #     for i in ids:
    #         id = i
    #         break
    #     # print(dbfData[id])
    #     for spell in m.specializations:
    #         abl = spell['abilities']
    #         for ab in abl:
    #             abdid = ab['tiers'][-1]['dbf_id']
    #             # print(dbfData[abdid])
    #
    #     for equ in m.equipment:
    #
    #         eq = equ['tiers'][-1]['dbf_id']
    #         print(dbfData[eq])
    #
    #     break
    # pass

    run()
