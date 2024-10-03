def find_combinations(score, max_play, results=None, current_combination=None):
    if results is None:
        results = []
    if current_combination is None:
        current_combination = [0, 0, 0, 0, 0]  # [TD+2pt, TD+FG, TD, FG, Safety]

    # Base case: If the score is zero, add the current combination to results
    if score == 0:
        results.append(current_combination[:])
        return

    # Recursively try different scoring plays, ensuring non-increasing order
    if score >= 8 and max_play >= 8:
        current_combination[0] += 1
        find_combinations(score - 8, 8, results, current_combination)
        current_combination[0] -= 1
    if score >= 7 and max_play >= 7:
        current_combination[1] += 1
        find_combinations(score - 7, 7, results, current_combination)
        current_combination[1] -= 1
    if score >= 6 and max_play >= 6:
        current_combination[2] += 1
        find_combinations(score - 6, 6, results, current_combination)
        current_combination[2] -= 1
    if score >= 3 and max_play >= 3:
        current_combination[3] += 1
        find_combinations(score - 3, 3, results, current_combination)
        current_combination[3] -= 1
    if score >= 2 and max_play >= 2:
        current_combination[4] += 1
        find_combinations(score - 2, 2, results, current_combination)
        current_combination[4] -= 1

def display_combinations(score):
    results = []
    find_combinations(score, 8, results)

    print(f"Possible combinations of scoring plays if a team’s score is {score}:")
    for combination in results:
        print(f"{combination[0]} TD + 2pt, {combination[1]} TD + FG, {combination[2]} TD, {combination[3]} 3pt FG, {combination[4]} Safety")

def main():
    while True:
        score = int(input("Enter the NFL score (0 or 1 to STOP): "))
        if score <= 1:
            print("Exiting program.")
            break
        display_combinations(score)

if __name__ == "__main__":
    main()
