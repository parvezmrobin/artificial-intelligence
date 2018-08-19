import random as rnd

true, false = True, False
null = None


def make_random_state():
    return [rnd.randint(0, 7) for i in range(8)]


def slope_of(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2)


def count_check(state):
    c = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j]:
                c += 1
            elif abs(slope_of(i, state[i], j, state[j])) == 1:
                c += 1
    return c


def successor(current_state):
    best_successor = null
    best_successor_check = 100

    check_counts = [[-1 for i in range(8)] for j in range(8)]

    for j in range(8):
        for i in range(8):
            if i == current_state[j]:
                continue
            successor_state = generate_successor(current_state, i, j)
            checks = count_check(successor_state)
            check_counts[j][i] = checks
            if checks < best_successor_check:
                best_successor_check = checks
                best_successor = successor_state

    return best_successor, best_successor_check, check_counts


def generate_successor(current_state, i, j):
    successor_state = [val for val in current_state]
    successor_state[j] = i
    return successor_state


def show_solve(current_state, current_check=null, check_counts=null):
    for j in range(8):
        print("| ", end='')
        for i in range(8):
            if j == current_state[i]:
                print("◉ | ", end='')
            elif check_counts is not null:
                print(check_counts[i][j], "| ", end='')
            else:
                print("  | ", end='')
        print("")
    if current_check is not null:
        print("Checks:", current_check)
    print("")


def simulated_annealing(init_state):
    num_shake = 5
    current_state = init_state
    current_check = count_check(current_state)

    t = 0
    while true:
        t += 1

        next_state, next_check, check_counts = successor(current_state)
        show_solve(current_state, current_check, check_counts)

        if next_check == 0:
            return next_state, t
        if next_check < current_check:
            current_state = next_state
            current_check = next_check
            num_shake = 5
        else:
            current_state = next_state
            current_check = next_check
            num_shake -= 1
            if num_shake == 0:
                return current_state, t

    return current_state, t


def main():
    rnd.seed(-2)
    initial_state = make_random_state()
    optimized_state, num_iter = simulated_annealing(initial_state)
    show_solve(optimized_state, current_check=count_check(optimized_state))


main()
