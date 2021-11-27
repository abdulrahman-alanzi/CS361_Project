tree = {
    'A': [ ['B',2], ['C',1] ],
    'B': [ ['A',2], ['D',4], ['E',3] ],
    'C': [ ['A',1], ['D',10], ['E',7] ],
    'D': [ ['B',4], ['C',10], ['F',5] ],
    'E': [ ['B',3], ['C',7], ['F',5] ],
    'F': [ ['D',5], ['E',5] ]
}

heuristic = {'A': 10, 'B': 8, 'C': 10, 'D': 7, 'E': 3, 'F': 0}

cost = {'A':0}


def AStarSearch():
    global tree, heuristic
    closed = []             # closed nodes
    opened = [['A', 10]]     # opened nodes

    '''find the visited nodes'''
    while True:
        fn = [i[1] for i in opened]     # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # current node
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == 'F':        # break the loop if node G has been found
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})            # add nodes to cost dictionary
            fn_node = cost[node] + heuristic[item[0]] + item[1]     # calculate f(n) of current node
            temp = [item[0], fn_node]
            opened.append(temp)                                     # store f(n) of current node in array opened

    '''find optimal sequence'''
    trace_node = 'F'                        # correct optimal tracing node, initialize as node G
    optimal_sequence = ['F']                # optimal node sequence
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]           # current node
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
            change the correct optimal tracing node to current node'''
            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()              # reverse the optimal sequence

    return closed, optimal_sequence


if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))
 