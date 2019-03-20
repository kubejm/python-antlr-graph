# Generated from Graph.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete listener for a parse tree produced by GraphParser.
class GraphListener(ParseTreeListener):

    # Enter a parse tree produced by GraphParser#graph.
    def enterGraph(self, ctx:GraphParser.GraphContext):
        pass

    # Exit a parse tree produced by GraphParser#graph.
    def exitGraph(self, ctx:GraphParser.GraphContext):
        pass


    # Enter a parse tree produced by GraphParser#vertex.
    def enterVertex(self, ctx:GraphParser.VertexContext):
        pass

    # Exit a parse tree produced by GraphParser#vertex.
    def exitVertex(self, ctx:GraphParser.VertexContext):
        pass


    # Enter a parse tree produced by GraphParser#edge.
    def enterEdge(self, ctx:GraphParser.EdgeContext):
        pass

    # Exit a parse tree produced by GraphParser#edge.
    def exitEdge(self, ctx:GraphParser.EdgeContext):
        pass


