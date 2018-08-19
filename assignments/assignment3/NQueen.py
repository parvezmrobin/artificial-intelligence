from random import randint, seed

true, false = True, False
null = None


def printf(*args):
    print(*args, end='')


class NQueen:

    def __init__(self, state=null):
        if state is null:
            self.state = NQueen.make_random_state()
        else:
            self.state = state

        self.check = NQueen.count_check(self.state)

    @staticmethod
    def make_random_state(n=8):
        return [randint(0, n - 1) for i in range(n)]

    @staticmethod
    def slope_of(x1, y1, x2, y2):
        return (y1 - y2) / (x1 - x2)

    @staticmethod
    def count_check(state):
        c = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if state[i] == state[j]:
                    c += 1
                elif abs(NQueen.slope_of(i, state[i], j, state[j])) == 1:
                    c += 1
        return c

    def successor(self):
        best_successor = null
        best_successor_check = 100

        check_counts = [[-1 for i in range(8)] for j in range(8)]

        for j in range(8):
            for i in range(8):
                if i == self.state[j]:
                    continue
                successor_state = self.make_successor(i, j)
                checks = NQueen.count_check(successor_state)
                check_counts[j][i] = checks
                if checks < best_successor_check:
                    best_successor_check = checks
                    best_successor = successor_state

        return best_successor, best_successor_check, check_counts

    def make_successor(self, i, j):
        successor_state = [val for val in self.state]
        successor_state[j] = i
        return successor_state

    @staticmethod
    def show_solve(current_state, current_check=null, check_counts=null):
        n = len(current_state)

        for j in range(n):
            printf("|")
            for i in range(n):
                if j == current_state[i]:
                    printf("██|")
                elif check_counts is not null:
                    val = check_counts[i][j]
                    if val < 10:
                        val = str(val) + " |"
                    else:
                        val = str(val) + "|"
                    printf(val)
                else:
                    printf("  |")
            print("")
        if current_check is not null:
            print("Checks:", current_check)

    def optimize(self, print_steps=false, total_shoulder_check=10):
        num_shake = total_shoulder_check

        t = 0
        while true:
            t += 1

            next_state, next_check, check_counts = self.successor()
            if print_steps:
                NQueen.show_solve(self.state, self.check, check_counts)
                print("───────────────────────────────────────")

            if next_check == 0:
                self.state = next_state
                self.check = next_check
                return t
            if next_check < self.check:
                self.state = next_state
                self.check = next_check
                num_shake = total_shoulder_check
            else:
                self.state = next_state
                self.check = next_check
                num_shake -= 1
                if num_shake == 0:
                    return t

        return t


def main():
    n_queen = NQueen()
    n_queen.optimize(print_steps=true)
    NQueen.show_solve(n_queen.state, n_queen.check)


seed(122)
main()
