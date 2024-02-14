from collections import defaultdict, deque

def min_relatives_for_gift(city_size, num_relationships, relationships, john, dave):
    graph = defaultdict(list)
    for i in range(num_relationships):
        person1, person2 = relationships[i]
        graph[person1].append(person2)
        graph[person2].append(person1)

    visited = set()
    queue = deque([(john, 0)])
    while queue:
        person, distance = queue.popleft()
        if person == dave:
            return distance
        visited.add(person)
        for relative in graph[person]:
            if relative not in visited:
                queue.append((relative, distance + 1))
    return -1