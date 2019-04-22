# Generated from Jack.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JackParser import JackParser
else:
    from JackParser import JackParser

# This class defines a complete listener for a parse tree produced by JackParser.
class JackListener(ParseTreeListener):

    # Enter a parse tree produced by JackParser#prog.
    def enterProg(self, ctx:JackParser.ProgContext):
        pass

    # Exit a parse tree produced by JackParser#prog.
    def exitProg(self, ctx:JackParser.ProgContext):
        pass


    # Enter a parse tree produced by JackParser#classDec.
    def enterClassDec(self, ctx:JackParser.ClassDecContext):
        pass

    # Exit a parse tree produced by JackParser#classDec.
    def exitClassDec(self, ctx:JackParser.ClassDecContext):
        pass


    # Enter a parse tree produced by JackParser#className.
    def enterClassName(self, ctx:JackParser.ClassNameContext):
        pass

    # Exit a parse tree produced by JackParser#className.
    def exitClassName(self, ctx:JackParser.ClassNameContext):
        pass


    # Enter a parse tree produced by JackParser#classVarDec.
    def enterClassVarDec(self, ctx:JackParser.ClassVarDecContext):
        pass

    # Exit a parse tree produced by JackParser#classVarDec.
    def exitClassVarDec(self, ctx:JackParser.ClassVarDecContext):
        pass


    # Enter a parse tree produced by JackParser#varName.
    def enterVarName(self, ctx:JackParser.VarNameContext):
        pass

    # Exit a parse tree produced by JackParser#varName.
    def exitVarName(self, ctx:JackParser.VarNameContext):
        pass


    # Enter a parse tree produced by JackParser#subRoutineDec.
    def enterSubRoutineDec(self, ctx:JackParser.SubRoutineDecContext):
        pass

    # Exit a parse tree produced by JackParser#subRoutineDec.
    def exitSubRoutineDec(self, ctx:JackParser.SubRoutineDecContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineName.
    def enterSubroutineName(self, ctx:JackParser.SubroutineNameContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineName.
    def exitSubroutineName(self, ctx:JackParser.SubroutineNameContext):
        pass


    # Enter a parse tree produced by JackParser#parameterList.
    def enterParameterList(self, ctx:JackParser.ParameterListContext):
        pass

    # Exit a parse tree produced by JackParser#parameterList.
    def exitParameterList(self, ctx:JackParser.ParameterListContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineBody.
    def enterSubroutineBody(self, ctx:JackParser.SubroutineBodyContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineBody.
    def exitSubroutineBody(self, ctx:JackParser.SubroutineBodyContext):
        pass


    # Enter a parse tree produced by JackParser#varDec.
    def enterVarDec(self, ctx:JackParser.VarDecContext):
        pass

    # Exit a parse tree produced by JackParser#varDec.
    def exitVarDec(self, ctx:JackParser.VarDecContext):
        pass


    # Enter a parse tree produced by JackParser#typeName.
    def enterTypeName(self, ctx:JackParser.TypeNameContext):
        pass

    # Exit a parse tree produced by JackParser#typeName.
    def exitTypeName(self, ctx:JackParser.TypeNameContext):
        pass


    # Enter a parse tree produced by JackParser#statements.
    def enterStatements(self, ctx:JackParser.StatementsContext):
        pass

    # Exit a parse tree produced by JackParser#statements.
    def exitStatements(self, ctx:JackParser.StatementsContext):
        pass


    # Enter a parse tree produced by JackParser#statement.
    def enterStatement(self, ctx:JackParser.StatementContext):
        pass

    # Exit a parse tree produced by JackParser#statement.
    def exitStatement(self, ctx:JackParser.StatementContext):
        pass


    # Enter a parse tree produced by JackParser#letStatement.
    def enterLetStatement(self, ctx:JackParser.LetStatementContext):
        pass

    # Exit a parse tree produced by JackParser#letStatement.
    def exitLetStatement(self, ctx:JackParser.LetStatementContext):
        pass


    # Enter a parse tree produced by JackParser#ifStatement.
    def enterIfStatement(self, ctx:JackParser.IfStatementContext):
        pass

    # Exit a parse tree produced by JackParser#ifStatement.
    def exitIfStatement(self, ctx:JackParser.IfStatementContext):
        pass


    # Enter a parse tree produced by JackParser#whileStatement.
    def enterWhileStatement(self, ctx:JackParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by JackParser#whileStatement.
    def exitWhileStatement(self, ctx:JackParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by JackParser#doStatement.
    def enterDoStatement(self, ctx:JackParser.DoStatementContext):
        pass

    # Exit a parse tree produced by JackParser#doStatement.
    def exitDoStatement(self, ctx:JackParser.DoStatementContext):
        pass


    # Enter a parse tree produced by JackParser#returnStatement.
    def enterReturnStatement(self, ctx:JackParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by JackParser#returnStatement.
    def exitReturnStatement(self, ctx:JackParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by JackParser#expression.
    def enterExpression(self, ctx:JackParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JackParser#expression.
    def exitExpression(self, ctx:JackParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JackParser#term.
    def enterTerm(self, ctx:JackParser.TermContext):
        pass

    # Exit a parse tree produced by JackParser#term.
    def exitTerm(self, ctx:JackParser.TermContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineCall.
    def enterSubroutineCall(self, ctx:JackParser.SubroutineCallContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineCall.
    def exitSubroutineCall(self, ctx:JackParser.SubroutineCallContext):
        pass


    # Enter a parse tree produced by JackParser#expressionList.
    def enterExpressionList(self, ctx:JackParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by JackParser#expressionList.
    def exitExpressionList(self, ctx:JackParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by JackParser#op.
    def enterOp(self, ctx:JackParser.OpContext):
        pass

    # Exit a parse tree produced by JackParser#op.
    def exitOp(self, ctx:JackParser.OpContext):
        pass


    # Enter a parse tree produced by JackParser#unaryOp.
    def enterUnaryOp(self, ctx:JackParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by JackParser#unaryOp.
    def exitUnaryOp(self, ctx:JackParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by JackParser#keywordConstant.
    def enterKeywordConstant(self, ctx:JackParser.KeywordConstantContext):
        pass

    # Exit a parse tree produced by JackParser#keywordConstant.
    def exitKeywordConstant(self, ctx:JackParser.KeywordConstantContext):
        pass


