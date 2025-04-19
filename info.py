# custom modules
from api import get_pokemon_types
from configs import POKEMON_TYPE_CHART, ALL_POKEMONS_OWNED, MOVE_TYPES


def find_best_pokemon(my_pokemon, enemy_pokemon):
    """
    Analyzes the type matchups between your Pokémon and enemy Pokémon to determine
    the best Pokémon to use in battle.

    Args:
        my_pokemon (list): List of your Pokémon names.
        enemy_pokemon (list): List of enemy Pokémon names.

    Returns:
        dict: A dictionary where keys are enemy Pokémon names and values are
              dictionaries containing:
              - 'enemy_types': List of the enemy Pokémon's types.
              - 'damage': List of tuples representing your Pokémon, their types,
                their best moves, and the strongest move's expected damage, sorted
                in descending order of damage.
              - 'resistance': A dictionary with:
                - 'immune': List of your Pokémon that are immune to the enemy's types.
                - 'weak': List of your Pokémon that are weak to the enemy's types.
    """
    # Get types for both your Pokémon and enemy Pokémon
    my_pokemon_types = get_pokemon_types(my_pokemon)
    enemy_pokemon_types = get_pokemon_types(enemy_pokemon)

    results = {}

    for enemy in enemy_pokemon:
        if enemy not in enemy_pokemon_types:
            print(f"Could not fetch types for enemy Pokémon: {enemy}")
            continue

        enemy_types = enemy_pokemon_types[enemy]
        damage_list = []
        immune_against_enemy = []
        weak_against_enemy = []

        for my_poke in my_pokemon:
            if my_poke not in my_pokemon_types:
                print(f"Could not fetch types for your Pokémon: {my_poke}")
                continue

            my_types = my_pokemon_types[my_poke]
            best_moves = get_best_moves(my_poke, my_types, enemy_types)

            # Add Pokémon to the damage list with its best moves
            if best_moves:
                strongest_move_value = float(best_moves[0].split("[")[1].strip("]"))
                damage_list.append(
                    (my_poke, my_types, best_moves, strongest_move_value)
                )

            # Check for resistance (immune and weak)
            is_immune = any(
                enemy_type in POKEMON_TYPE_CHART[my_type]["immune"]
                for my_type in my_types
                for enemy_type in enemy_types
            )
            is_weak = any(
                my_type in POKEMON_TYPE_CHART[enemy_type]["strong"]
                for enemy_type in enemy_types
                for my_type in my_types
            )

            if is_immune:
                immune_against_enemy.append(f"{my_poke} ({', '.join(my_types)})")
            if is_weak:
                weak_against_enemy.append(f"{my_poke} ({', '.join(my_types)})")

        # Sort the damage list by strongest move's expected damage in descending order
        damage_list.sort(key=lambda x: x[3], reverse=True)

        # Add results for this enemy Pokémon
        results[enemy] = {
            "enemy_types": enemy_types,
            "damage": damage_list,
            "resistance": {
                "immune": immune_against_enemy,
                "weak": weak_against_enemy,
            },
        }

    return results


def get_best_moves(pokemon_name, pokemon_types, enemy_types):
    """
    Get the best moves for a Pokémon based on its types, the enemy's types,
    and move effectiveness.

    Args:
        pokemon_name (str): Name of the Pokémon.
        pokemon_types (list): List of the Pokémon's types.
        enemy_types (list): List of the enemy Pokémon's types.

    Returns:
        list: List of moves that match the Pokémon's types, are strong against
              the enemy's types, and are sorted by expected power
              (power * accuracy * effectiveness).
    """
    if pokemon_name not in ALL_POKEMONS_OWNED:
        return []

    moves = ALL_POKEMONS_OWNED[pokemon_name]
    best_moves = []

    for move in moves:
        move_lower = move.lower()
        if move_lower in MOVE_TYPES:
            move_data = MOVE_TYPES[move_lower]
            move_type = move_data["type"]
            move_power = move_data["power"]
            move_accuracy = (
                move_data["accuracy"] if move_data["accuracy"] is not None else 100
            )

            # Skip moves with null or zero power
            if move_power is None or move_power == 0:
                continue

            # Calculate effectiveness against the enemy's types
            effectiveness = 1.0
            for enemy_type in enemy_types:
                if enemy_type in POKEMON_TYPE_CHART[move_type]["strong"]:
                    effectiveness *= 2.0
                elif enemy_type in POKEMON_TYPE_CHART[move_type]["not_effective"]:
                    effectiveness *= 0.5
                elif enemy_type in POKEMON_TYPE_CHART[move_type]["immune"]:
                    effectiveness *= 0.0

            # Apply STAB (Same-Type Attack Bonus) if the move's type matches the Pokémon's type
            if move_type in pokemon_types:
                effectiveness *= 1.5

            # Calculate expected power (power * accuracy * effectiveness)
            expected_power = move_power * (move_accuracy / 100) * effectiveness

            # Only include moves with non-zero effectiveness
            if effectiveness > 0:
                best_moves.append((move, expected_power))

    # Sort moves by expected power in descending order
    best_moves.sort(key=lambda x: x[1], reverse=True)

    # Return move names with their expected power
    return [f"{move}[{expected_power:.1f}]" for move, expected_power in best_moves]
