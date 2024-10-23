def solution(edges):
    answer = []
    append_node = 0
    donut = 0
    stick = 0
    eight = 0
    node_count = {}

    for find_append_node in edges:
        if find_append_node[0] in node_count:
            node_count[find_append_node[0]] += 1
        else:
            node_count[find_append_node[0]] = 0

    append_node = max(node_count, key=node_count.get)

    def find(n):
        count = set()
        check = 0
        for i in edges:
            if i[0] == n:
                count.add(i[0])
                n = i[1]
        for x in count:
            for y in edges:
                if y[0] == x:
                    check += 1
                    if check == 2:
                        return "eight"
        for j in edges:
            if j[0] == n:
                if j[1] == n:
                    return "donut"
                n = j[1]
        return "stick"
    check = set()
    for find_graph in edges:
        if find_graph[0] == append_node and find_graph[1] not in check:
            check.add(find_graph[1])
            graph_type = find(find_graph[1])
            if graph_type == "eight":
                eight += 1
            elif graph_type == "donut":
                donut += 1
            else:
                stick += 1

    answer.append(append_node)
    answer.append(donut)
    answer.append(stick)
    answer.append(eight)
    return answer

print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
