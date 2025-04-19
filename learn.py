import random
from configs import POKEMON_TYPE_CHART


def quiz():
    """
    Conducts an interactive Pokémon type quiz.

    This function randomly selects a Pokémon type and prompts the user to input
    their guesses for which types are strong against, weak against, immune to,
    and not very effective against the chosen type. The user's answers are
    evaluated against the correct answers from the `POKEMON_TYPE_CHART`.

    Inputs:
        - STRONG: Types that are strong against the chosen type.
        - WEAK: Types that are weak against the chosen type.
        - IMMUNE: Types that are immune to the chosen type.
        - NOT VERY EFFECTIVE: Types that receive not very effective damage from the chosen type.

    Outputs:
        For each category (strong, weak, immune, not very effective):
        - Correct answers provided by the user.
        - Incorrect answers provided by the user.
        - Correct answers that the user missed.

    Note:
        The `POKEMON_TYPE_CHART` dictionary must be defined and contain the type
        effectiveness data for this function to work correctly.
    """
    chosen_type = random.choice(list(POKEMON_TYPE_CHART.keys()))
    print(f"\nPokémon Type: {chosen_type.capitalize()}")

    user_strong = (
        input("Which types are STRONG against this type? (comma separated): ")
        .lower()
        .split(",")
    )
    user_weak = (
        input("Which types are WEAK against this type? (comma separated): ")
        .lower()
        .split(",")
    )
    user_immune = (
        input("Which types are IMMUNE to this type? (comma separated): ")
        .lower()
        .split(",")
    )
    user_not_effective = (
        input(
            "Which types receive NOT VERY EFFECTIVE damage from this type? (comma separated): "
        )
        .lower()
        .split(",")
    )

    correct = POKEMON_TYPE_CHART[chosen_type]

    def evaluate(user_list, correct_list):
        user_list = [x.strip() for x in user_list if x.strip()]
        correct_set = set(correct_list)
        user_set = set(user_list)
        return user_set & correct_set, user_set - correct_set, correct_set - user_set

    for category, user_input in zip(
        ["strong", "weak", "immune", "not_effective"],
        [user_strong, user_weak, user_immune, user_not_effective],
    ):
        correct_answers = correct[category]
        right, wrong, missed = evaluate(user_input, correct_answers)
        print(f"\n{category.upper().replace('_', ' ')}:")
        print(f"  ✔️ Correct: {sorted(right)}")
        print(f"  ❌ Wrong: {sorted(wrong)}")
        print(f"  ❓ Missed: {sorted(missed)}")
