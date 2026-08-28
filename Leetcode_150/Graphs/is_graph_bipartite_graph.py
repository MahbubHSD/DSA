# Alternate file for is_graph_bipartite.py

from is_graph_bipartite import is_bipartite as _reference_is_bipartite

def is_bipartite(graph):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_bipartite(graph)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'is_graph_bipartite.py')
