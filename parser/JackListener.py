# Generated from Jack.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JackParser import JackParser
else:
    from JackParser import JackParser

# This class defines a complete listener for a parse tree produced by JackParser.
class JackListener(ParseTreeListener):

    # Enter a parse tree produced by JackParser#program.
    def enterProgram(self, ctx:JackParser.ProgramContext):
        pass

    # Exit a parse tree produced by JackParser#program.
    def exitProgram(self, ctx:JackParser.ProgramContext):
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


    # Enter a parse tree produced by JackParser#typedVariable.
    def enterTypedVariable(self, ctx:JackParser.TypedVariableContext):
        pass

    # Exit a parse tree produced by JackParser#typedVariable.
    def exitTypedVariable(self, ctx:JackParser.TypedVariableContext):
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


    # Enter a parse tree produced by JackParser#binaryExpression.
    def enterBinaryExpression(self, ctx:JackParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by JackParser#binaryExpression.
    def exitBinaryExpression(self, ctx:JackParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by JackParser#nestedExpression.
    def enterNestedExpression(self, ctx:JackParser.NestedExpressionContext):
        pass

    # Exit a parse tree produced by JackParser#nestedExpression.
    def exitNestedExpression(self, ctx:JackParser.NestedExpressionContext):
        pass


    # Enter a parse tree produced by JackParser#arrayReference.
    def enterArrayReference(self, ctx:JackParser.ArrayReferenceContext):
        pass

    # Exit a parse tree produced by JackParser#arrayReference.
    def exitArrayReference(self, ctx:JackParser.ArrayReferenceContext):
        pass


    # Enter a parse tree produced by JackParser#unaryExpression.
    def enterUnaryExpression(self, ctx:JackParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by JackParser#unaryExpression.
    def exitUnaryExpression(self, ctx:JackParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by JackParser#atom.
    def enterAtom(self, ctx:JackParser.AtomContext):
        pass

    # Exit a parse tree produced by JackParser#atom.
    def exitAtom(self, ctx:JackParser.AtomContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineExpression.
    def enterSubroutineExpression(self, ctx:JackParser.SubroutineExpressionContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineExpression.
    def exitSubroutineExpression(self, ctx:JackParser.SubroutineExpressionContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineCall.
    def enterSubroutineCall(self, ctx:JackParser.SubroutineCallContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineCall.
    def exitSubroutineCall(self, ctx:JackParser.SubroutineCallContext):
        pass


    # Enter a parse tree produced by JackParser#subroutineTarget.
    def enterSubroutineTarget(self, ctx:JackParser.SubroutineTargetContext):
        pass

    # Exit a parse tree produced by JackParser#subroutineTarget.
    def exitSubroutineTarget(self, ctx:JackParser.SubroutineTargetContext):
        pass


    # Enter a parse tree produced by JackParser#expressionList.
    def enterExpressionList(self, ctx:JackParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by JackParser#expressionList.
    def exitExpressionList(self, ctx:JackParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by JackParser#keywordConstant.
    def enterKeywordConstant(self, ctx:JackParser.KeywordConstantContext):
        pass

    # Exit a parse tree produced by JackParser#keywordConstant.
    def exitKeywordConstant(self, ctx:JackParser.KeywordConstantContext):
        pass


