import sys
from antlr4 import *
from graph import GraphLexer, GraphParser, GraphListener

import networkx as nx
import matplotlib.pyplot as plt

class GraphLoader(GraphListener):
    def __init__(self, graph):
        self.g = graph 

    def exitEdge(self, ctx):
        fromVertex = ctx.vertex(0).ID().getText()
        toVertex = ctx.vertex(1).ID().getText()
        weight = ctx.NUM().getText()
        print(f"add fromVertex={fromVertex} toVertex={toVertex} weight={weight}")
        self.g.add_edge(fromVertex, toVertex, weight=weight)

def main(argv):
    input = FileStream(argv[1])
    lexer = GraphLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GraphParser(stream)
    tree = parser.graph()

    G = nx.Graph()
    listener = GraphLoader(G)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    nx.draw(G)
    plt.show()

if __name__ == '__main__':
    main(sys.argv)
