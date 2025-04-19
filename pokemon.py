import sys

# custom modules
from learn import quiz
from api import get_pokemon_types, get_ability_type
from info import find_best_pokemon
from configs import CURRENT_POKEMON_TEAM, ALL_POKEMONS_OWNED


def main():
    if len(sys.argv) < 2:
        print("Please provide a mode to run: quiz, types, current, all, or ability")
        return

    mode = sys.argv[1].lower()

    if mode == "quiz":
        quiz()
    elif mode == "types":
        if len(sys.argv) < 3:
            print("Please provide at least one Pokémon name for the 'types' mode.")
            return

        pokemon_names = sys.argv[2:]  # Accept multiple Pokémon names
        types_dict = get_pokemon_types(pokemon_names)
        for pokemon_name in pokemon_names:
            if pokemon_name in types_dict:
                print(f"{pokemon_name}: {', '.join(types_dict[pokemon_name])}")
            else:
                print(f"Could not fetch types for {pokemon_name}.")
    elif mode == "current":
        if len(sys.argv) < 3:
            print(
                "Please provide at least one enemy Pokémon name for the 'current' mode."
            )
            return

        enemy_pokemon = sys.argv[2:]  # Accept multiple enemy Pokémon names
        if not CURRENT_POKEMON_TEAM:
            print(
                "Your current Pokémon team is empty. Please update CURRENT_POKEMON_TEAM in configs.py."
            )
            return

        results = find_best_pokemon(CURRENT_POKEMON_TEAM, enemy_pokemon)
        for enemy, data in results.items():
            enemy_types = ", ".join(data["enemy_types"])
            header = f"### Against {enemy.title()} ({enemy_types}): ###"
            print(f"{'#' * len(header)}")
            print(header)
            print(f"{'#' * len(header)}")

            # Damage Section
            print("  Damage:")
            for name, types, best_moves, strongest_move_value in data["damage"]:
                if best_moves:
                    print(
                        f"      - {name} ({', '.join(types)} - {', '.join(best_moves)})"
                    )
                else:
                    print(f"      - {name} ({', '.join(types)})")

            # Resistance Section
            print("  Resistance:")
            print("    Immune:")
            for pokemon in data["resistance"]["immune"]:
                print(f"      - {pokemon}")

            print("    Weak:")
            for pokemon in data["resistance"]["weak"]:
                print(f"      - {pokemon}")
            print()
    elif mode == "all":
        if len(sys.argv) < 3:
            print("Please provide at least one enemy Pokémon name for the 'all' mode.")
            return

        enemy_pokemon = sys.argv[2:]  # Accept multiple enemy Pokémon names
        if not ALL_POKEMONS_OWNED:
            print(
                "You do not own any Pokémon. Please update ALL_POKEMONS_OWNED in configs.py."
            )
            return

        results = find_best_pokemon(ALL_POKEMONS_OWNED, enemy_pokemon)
        for enemy, data in results.items():
            enemy_types = ", ".join(data["enemy_types"])
            header = f"### Against {enemy.title()} ({enemy_types}): ###"
            print(f"{'#' * len(header)}")
            print(header)
            print(f"{'#' * len(header)}")

            # Damage Section
            print("  Damage:")
            for name, types, best_moves, strongest_move_value in data["damage"]:
                if best_moves:
                    print(
                        f"      - {name} ({', '.join(types)} - {', '.join(best_moves)})"
                    )
                else:
                    print(f"      - {name} ({', '.join(types)})")

            # Resistance Section
            print("  Resistance:")
            print("    Immune:")
            for pokemon in data["resistance"]["immune"]:
                print(f"      - {pokemon}")

            print("    Weak:")
            for pokemon in data["resistance"]["weak"]:
                print(f"      - {pokemon}")
            print()
    elif mode == "ability":
        if len(sys.argv) < 3:
            print(
                "Please provide at least one Pokémon ability name for the 'ability' mode."
            )
            return

        ability_names = sys.argv[2:]  # Accept multiple ability names
        for ability_name in ability_names:
            ability_effect = get_ability_type(ability_name)
            if ability_effect:
                print(f"Ability '{ability_name}': {ability_effect}")
            else:
                print(f"Could not fetch information for ability '{ability_name}'.")
    else:
        print(
            f"Unknown mode: {mode}. Available modes: quiz, types, current, all, ability"
        )


if __name__ == "__main__":
    main()
