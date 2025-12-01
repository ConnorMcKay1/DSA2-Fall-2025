print("wowowo")

# Implement Depth First Search

#does the list need to be tuples?
#solved with dictionary
Graph = {
    "A": {"color": "white", "pi": None, "d": 0, "f": 0, "adj": ["B", "C"]},
    "B": {"color": "white", "pi": None, "d": 0, "f": 0, "adj": ["D"]},
    "C": {"color": "white", "pi": None, "d": 0, "f": 0, "adj": []},
    "D": {"color": "white", "pi": None, "d": 0, "f": 0, "adj": []}
}

time = 0    # global time variable for the entire graph


def DepthFirstSearch(G):
    global time

    for u in G:
        G[u]["color"] = "white"
        G[u]["pi"] = None
    time = 0

    for u in G:
        if G[u]["color"] == "white":
            DepthFirstSearch_Visit(G, u)


def DepthFirstSearch_Visit(G, u):
    global time

    time = time + 1
    G[u]["d"] = time
    G[u]["color"] = "gray"

    for v in G[u]["adj"]:
        if G[v]["color"] == "white":
            G[v]["pi"] = u
            DepthFirstSearch_Visit(G, v)

    G[u]["color"] = "black"
    time = time + 1
    G[u]["f"] = time



def RunDFS():
    DepthFirstSearch(Graph)
    for v in Graph:
        print(v, Graph[v])

RunDFS()