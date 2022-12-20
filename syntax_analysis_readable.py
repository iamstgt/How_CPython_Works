import ast
from evaluand import evaluand


def walk(node, indent=0):
    """ Return a human-readable AST """
    print(' ' * indent, end='')
    print(node.__class__, end='')
    if hasattr(node, 'lineno'):
        msg = ': {lineno}'.format(lineno=node.lineno)
        print(msg, end='')
    print()
    for child in ast.iter_child_nodes(node):
        walk(child, indent=indent+4)


walk(ast.parse(evaluand))