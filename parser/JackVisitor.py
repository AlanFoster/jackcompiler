# Generated from Jack.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JackParser import JackParser
else:
    from JackParser import JackParser

# This class defines a complete generic visitor for a parse tree produced by JackParser.

class JackVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JackParser#program.
    def visitProgram(self, ctx:JackParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#classDec.
    def visitClassDec(self, ctx:JackParser.ClassDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#className.
    def visitClassName(self, ctx:JackParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#classVarDec.
    def visitClassVarDec(self, ctx:JackParser.ClassVarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#varName.
    def visitVarName(self, ctx:JackParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#subRoutineDec.
    def visitSubRoutineDec(self, ctx:JackParser.SubRoutineDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#subroutineName.
    def visitSubroutineName(self, ctx:JackParser.SubroutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#parameterList.
    def visitParameterList(self, ctx:JackParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#subroutineBody.
    def visitSubroutineBody(self, ctx:JackParser.SubroutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#varDec.
    def visitVarDec(self, ctx:JackParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#typedVariable.
    def visitTypedVariable(self, ctx:JackParser.TypedVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#typeName.
    def visitTypeName(self, ctx:JackParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#statements.
    def visitStatements(self, ctx:JackParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#statement.
    def visitStatement(self, ctx:JackParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#letStatement.
    def visitLetStatement(self, ctx:JackParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#ifStatement.
    def visitIfStatement(self, ctx:JackParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#whileStatement.
    def visitWhileStatement(self, ctx:JackParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#doStatement.
    def visitDoStatement(self, ctx:JackParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#returnStatement.
    def visitReturnStatement(self, ctx:JackParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#binaryExpression.
    def visitBinaryExpression(self, ctx:JackParser.BinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#nestedExpression.
    def visitNestedExpression(self, ctx:JackParser.NestedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#arrayReference.
    def visitArrayReference(self, ctx:JackParser.ArrayReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#unaryExpression.
    def visitUnaryExpression(self, ctx:JackParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#atom.
    def visitAtom(self, ctx:JackParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#subroutineExpression.
    def visitSubroutineExpression(self, ctx:JackParser.SubroutineExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#subroutineCall.
    def visitSubroutineCall(self, ctx:JackParser.SubroutineCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#subroutineTarget.
    def visitSubroutineTarget(self, ctx:JackParser.SubroutineTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#expressionList.
    def visitExpressionList(self, ctx:JackParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JackParser#keywordConstant.
    def visitKeywordConstant(self, ctx:JackParser.KeywordConstantContext):
        return self.visitChildren(ctx)



del JackParser