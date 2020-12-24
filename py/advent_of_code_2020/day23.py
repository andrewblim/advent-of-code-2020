class DictCircularLL():

    def __init__(self, vals):
        self.nodes = {}
        for i in range(len(vals)-1):
            self.nodes[vals[i]] = (vals[i-1], vals[i+1])
        self.nodes[vals[len(vals)-1]] = (vals[len(vals)-2], vals[0])
        self.head = vals[0]

    def popleft(self):
        prev, next = self.nodes[self.head]
        self.nodes[prev] = (self.nodes[prev][0], next)
        self.nodes[next] = (prev, self.nodes[next][1])
        val = self.head
        del self.nodes[val]
        self.head = next
        return val

    def insert_after(self, val_at, val):
        next = self.nodes[val_at][1]
        self.nodes[val_at] = (self.nodes[val_at][0], val)
        self.nodes[val] = (val_at, next)
        self.nodes[next] = (val, self.nodes[next][1])

    def append(self, val):
        self.insert_after(self.nodes[self.head][0], val)

    def to_list(self):
        x = []
        cur = self.head
        for i in range(len(self.nodes)):
            x.append(cur)
            cur = self.nodes[cur][1]
        return x


def make_move(cups):
    current_cup = cups.popleft()
    move_cup1 = cups.popleft()
    move_cup2 = cups.popleft()
    move_cup3 = cups.popleft()
    destination_cup = current_cup - 1
    if destination_cup < 1:
        destination_cup = len(cups.nodes) + 4
    while destination_cup in [move_cup1, move_cup2, move_cup3]:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = len(cups.nodes) + 4
    cups.insert_after(destination_cup, move_cup3)
    cups.insert_after(destination_cup, move_cup2)
    cups.insert_after(destination_cup, move_cup1)
    cups.append(current_cup)
    return cups


if __name__ == "__main__":
    cups = DictCircularLL([3, 2, 7, 4, 6, 5, 1, 8, 9])
    print("Part 1:")
    for _ in range(100):
        make_move(cups)
    cups = cups.to_list()
    print(cups)
    i = cups.index(1)
    print("".join([str(x) for x in cups[(i+1):] + cups[:i]]))
    print("Part 2:")
    cups2 = DictCircularLL([3, 2, 7, 4, 6, 5, 1, 8, 9] + list(range(10, 1_000_001)))
    for i in range(10_000_000):
        if i % 500_000 == 0:
            print(i)
        make_move(cups2)
    x = cups2.nodes[1][1]
    y = cups2.nodes[x][1]
    print(x*y)
