def create_lua_store_pack():
    author_name = input("Enter the author name: ")
    pack_name = input("Enter the pack name: ")
    unlock_level = input("Enter the unlock level: ")
    
    tower_pools = []
    affix_pools = []
    for i in range(1, 6):
        towers = input(f"Enter tier {i} tower names separated by commas: ")
        affixes = input(f"Enter tier {i} affix names separated by commas: ")
        tower_list = '{' + ', '.join([f"'{tower.strip()}'" for tower in towers.split(',')]) + '}'
        affix_list = '{' + ', '.join([f"'{affix.strip()}'" for affix in affixes.split(',')]) + '}'
        tower_pools.append(tower_list)
        affix_pools.append(affix_list)
    
    lua_script = f'''store_pack({{
        author = "{author_name}",
        tower_pool = {{
            {tower_pools[0]}, -- tier 1 towers
            {tower_pools[1]}, -- tier 2 towers
            {tower_pools[2]},
            {tower_pools[3]},
            {tower_pools[4]}
        }},
        affix_pool = {{
            {affix_pools[0]}, -- tier 1 affixes
            {affix_pools[1]}, -- tier 2 affixes
            {affix_pools[2]},
            {affix_pools[3]},
            {affix_pools[4]}
        }},
        shop_spaces = {{
            {{towers = 3, affixes = 1}},
            {{towers = 4, affixes = 1}},
            {{towers = 4, affixes = 2}},
            {{towers = 5, affixes = 2}},
            {{towers = 6, affixes = 2}}
        }}
    }}, '{pack_name}', {unlock_level})'''

create_lua_store_pack()
