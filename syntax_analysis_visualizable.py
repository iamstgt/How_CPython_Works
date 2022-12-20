import ast
from evaluand import evaluand
from graphviz import Digraph


def visit(node, nodes, pindex, g):
    """ Return a textable AST.

    Output should be the following.
        digraph {
            0 [label=Module]
            1 [label=Expr]
            1 -> 0
            2 [label=Call]
            2 -> 1
            3 [label=Name]
            3 -> 2
            4 [label=Load]
            4 -> 3
            5 [label=Constant]
            5 -> 2
        }

    """
    name = str(type(node).__name__)
    index = len(nodes)
    nodes.append(index)
    g.node(str(index), name)
    if index != pindex:
        g.edge(str(index), str(pindex))
    for n in ast.iter_child_nodes(node):
        visit(n, nodes, index, g)


# Set to png as a format
g = Digraph(format="png")
visit(ast.parse(evaluand), [], 0, g)
# Save as ast.png
g.render("ast")