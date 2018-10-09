import graphviz as gv




def add_node(g, par_lbl, chil_lbl, children):
    if isinstance(children, list):
        g.node(chil_lbl)
    elif children is None:
        g.node(chil_lbl, "Pruned")
    else:
        g.node(chil_lbl, str(children))
    g.edge(par_lbl, chil_lbl)
    if isinstance(children, list):
        for i, child in enumerate(children):
            lbl = chil_lbl + str(i + 1)
            add_node(g, chil_lbl, lbl, child)


def show_tree(tree):
    g = gv.Graph('Root', format='png')
    g.node('node1')

    for i, value in enumerate(tree):
        add_node(g, 'node1', 'node1' + str(i + 1), value)
    g.view()


tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 1
pruned = 0


def children(branch, depth, alpha, beta):
    global tree
    global root
    global pruned
    i = 0
    for cj, child in enumerate(branch):
        if type(child) is list and child is not None:
            (nalpha, nbeta) = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:
                beta = nalpha if nalpha < beta else beta
            else:
                alpha = nbeta if nbeta > alpha else alpha
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
            if alpha >= beta:
                pruned += 1
                for j in range(cj + 1, len(branch)):
                    branch[j] = None
                show_tree(tree)
                break
    if depth == root:
        tree = alpha if root == 0 else beta
    return alpha, beta


def alphabeta(in_tree=tree, start=root, upper=-15, lower=15):
    global tree
    global pruned
    global root

    (alpha, beta) = children(tree, start, upper, lower)

    if __name__ == "__main__":
        print("(alpha, beta): ", alpha, beta)
        print("Result: ", tree)
        print("Times pruned: ", pruned)

    return (alpha, beta, tree, pruned)


if __name__ == "__main__":
    alphabeta()
