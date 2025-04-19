import os
import json
import time
import requests


def get_pokemon_types(pokemon_names, cache_file="data/pokemon_types_cache.json"):
    """
    Fetches types for a list of Pokémon names from the PokéAPI or a local cache.

    Args:
        pokemon_names (list): List of Pokémon names as strings.
        cache_file (str): Path to the JSON file used for caching Pokémon types.

    Returns:
        dict: Dictionary mapping Pokémon names to a list of their types.
    """
    # Load the cache if it exists
    if os.path.exists(cache_file):
        with open(cache_file, "r") as file:
            pokemon_types = json.load(file)
    else:
        pokemon_types = {}

    for name in pokemon_names:
        if name in pokemon_types:
            # Use cached data
            continue

        clean_name = (
            name.lower()
            .replace("♀", "-f")
            .replace("♂", "-m")
            .replace(".", "")
            .replace("'", "")
            .replace(" ", "-")
        )
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{clean_name}")
            if response.status_code == 200:
                data = response.json()
                types = [t["type"]["name"] for t in data["types"]]
                pokemon_types[name] = types
            else:
                print(
                    f"Could not fetch data for {name} (status code {response.status_code})"
                )
        except Exception as e:
            print(f"Error fetching data for {name}: {e}")

        # To respect API rate limits
        time.sleep(0.5)

    # Save the updated cache
    with open(cache_file, "w") as file:
        json.dump(pokemon_types, file, indent=4)

    return {name: pokemon_types.get(name, []) for name in pokemon_names}


def get_ability_type(ability_name, cache_file="data/pokemon_ability_types_cache.json"):
    """
    Fetches the type of a Pokémon ability from a local cache.

    Args:
        ability_name (str): Name of the Pokémon ability.
        cache_file (str): Path to the JSON file used for caching ability types.

    Returns:
        str: The type or effect of the ability, or None if not found.
    """
    # Load the cache if it exists
    if os.path.exists(cache_file):
        with open(cache_file, "r") as file:
            ability_types = json.load(file)
    else:
        ability_types = {}

    # Return the ability type or None if not found
    return ability_types.get(ability_name.lower())
