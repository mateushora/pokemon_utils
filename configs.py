"""
Module: configs

This module is responsible for loading and managing configuration data for the
Pokémon application. It includes loading type charts, owned Pokémon
data, and cached move types from JSON files. Additionally, it defines the
current Pokémon team.

Attributes:
    POKEMON_TYPE_CHART (dict): A dictionary representing the Pokémon type
        effectiveness chart, loaded from 'pokemon_type_chart.json'.

    ALL_POKEMONS_OWNED (dict): A dictionary containing information about all
        owned Pokémon, loaded from 'pokemon_all_pokemons_owned.json'.

    MOVE_TYPES (dict): A dictionary mapping Pokémon abilities to their
        respective types, loaded from 'pokemon_ability_types_cache.json'.

    CURRENT_POKEMON_TEAM (list): A list of Pokémon names representing the
        current team.
"""

import os
import json

# Load the Pokémon type chart from a JSON file
POKEMON_TYPE_CHART_PATH = os.path.join(
    os.path.dirname(__file__), "data", "pokemon_type_chart.json"
)

with open(POKEMON_TYPE_CHART_PATH, "r") as file:
    POKEMON_TYPE_CHART = json.load(file)

# Load the ALL_POKEMONS_OWNED from a JSON file
ALL_POKEMONS_OWNED_PATH = os.path.join(
    os.path.dirname(__file__), "data", "pokemon_all_pokemons_owned.json"
)

with open(ALL_POKEMONS_OWNED_PATH, "r") as file:
    ALL_POKEMONS_OWNED = json.load(file)

# Load move types from the cache
MOVE_TYPES_PATH = os.path.join(
    os.path.dirname(__file__), "data", "pokemon_ability_types_cache.json"
)

with open(MOVE_TYPES_PATH, "r") as file:
    MOVE_TYPES = json.load(file)


CURRENT_POKEMON_TEAM = [
    "Cubone",
    "Growlithe",
    "Blastoise",
    "Vileplume",
    "Pidgeot",
    "Persian",
]
