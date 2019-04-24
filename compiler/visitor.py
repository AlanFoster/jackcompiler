from parser.JackParser import JackParser
from parser.JackVisitor import JackVisitor
from .symbol_table import Symbol, SymbolTable, EmptySymbolTable, SymbolType


class Visitor(JackVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable(EmptySymbolTable)
        self.label_count = 0

    def next_label(self, prefix):
        self.label_count = self.label_count + 1
        return f"{prefix}.{self.label_count}"

    # Visit a parse tree produced by JackParser#prog.
    def visitProgram(self, ctx: JackParser.ProgramContext):
        return self.visit(ctx.classDec())

    # Visit a parse tree produced by JackParser#classDec.
    def visitClassDec(self, ctx: JackParser.ClassDecContext):
        if ctx.className().getText() != "Main":
            raise TypeError("Class not supported")

        # class_declarations = self.visitChildren(ctx.classVarDec().ctx)
        statements = "".join([self.visit(child) for child in ctx.subRoutineDec()])

        return statements

    # Visit a parse tree produced by JackParser#className.
    def visitClassName(self, ctx: JackParser.ClassNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#classVarDec.
    def visitClassVarDec(self, ctx: JackParser.ClassVarDecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#varName.
    def visitVarName(self, ctx: JackParser.VarNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#subRoutineDec.
    def visitSubRoutineDec(self, ctx: JackParser.SubRoutineDecContext):
        kind = ctx.kind.text
        name = ctx.subroutineName().getText()
        # Note: The symbol table for methods must additionally contain an entry for "this"
        body = self.visit(ctx.subroutineBody())

        # Note: We must visit the subroutine body before knowing this value
        local_variable_count = self.symbol_table.local_variable_count()

        if kind == "function":
            comment = f"function Main.{name} {local_variable_count}\n"
            return comment + body

        raise ValueError(f"kind not handled correctly {kind}")

    # Visit a parse tree produced by JackParser#subroutineName.
    def visitSubroutineName(self, ctx: JackParser.SubroutineNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#parameterList.
    def visitParameterList(self, ctx: JackParser.ParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#subroutineBody.
    def visitSubroutineBody(self, ctx: JackParser.SubroutineBodyContext):
        var_decs = "".join([self.visit(var_dec) for var_dec in ctx.varDec()])
        statements = self.visit(ctx.statements())

        return var_decs + statements

    # Visit a parse tree produced by JackParser#varDec.
    def visitVarDec(self, ctx: JackParser.VarDecContext):
        typed_variable = ctx.typedVariable()
        var_name = typed_variable.varName().getText()
        type_name = typed_variable.typeName().getText()

        self.symbol_table.add(
            Symbol(name=var_name, type_name=type_name, kind=SymbolType.LOCAL)
        )
        for additional_var in ctx.varName():
            self.symbol_table.add(
                Symbol(
                    name=additional_var.getText(),
                    type_name=type_name,
                    kind=SymbolType.LOCAL,
                )
            )

        return ""

    # Visit a parse tree produced by JackParser#typedVariable.
    def visitTypedVariable(self, ctx: JackParser.TypedVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#typeName.
    def visitTypeName(self, ctx: JackParser.TypeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#statements.
    def visitStatements(self, ctx: JackParser.StatementsContext):
        statements = "".join([self.visit(child) for child in ctx.statement()])
        return statements

    # Visit a parse tree produced by JackParser#statement.
    def visitStatement(self, ctx: JackParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#letStatement.
    def visitLetStatement(self, ctx: JackParser.LetStatementContext):
        if ctx.index:
            raise ValueError(
                f"Array indexing not supported yet for expression {ctx.getText()}"
            )

        var_name = ctx.varName().getText()
        symbol = self.symbol_table.get(var_name)
        calculate_value = self.visit(ctx.value)
        store_result = f"pop {symbol.segment} {symbol.number}\n"

        return calculate_value + store_result

    # Visit a parse tree produced by JackParser#ifStatement.
    def visitIfStatement(self, ctx: JackParser.IfStatementContext):
        # return self.visitChildren(ctx)
        expression = self.visit(ctx.expression())
        true_statements = self.visit(ctx.true_statements)

        else_label = self.next_label("IF_ELSE")
        end_label = self.next_label("IF_END")

        if not ctx.false_statements:
            return (
                expression
                + "not\n"
                + f"if-goto {end_label}\n"
                + true_statements
                + f"label {end_label}\n"
            )
        else:
            false_statements = self.visit(ctx.false_statements)
            return (
                expression
                + "not\n"
                + f"if-goto {else_label}\n"
                + true_statements
                + f"goto {end_label}\n"
                f"label {else_label}\n" + false_statements + f"label {end_label}\n"
            )

    # Visit a parse tree produced by JackParser#whileStatement.
    def visitWhileStatement(self, ctx: JackParser.WhileStatementContext):
        expression = self.visit(ctx.expression())
        statements = self.visit(ctx.statements())

        start_label = self.next_label("LOOP_START")
        end_label = self.next_label("LOOP_END")

        return (
            f"label {start_label}\n"
            + expression
            + "not\n"
            + f"if-goto {end_label}\n"
            + statements
            + f"goto {start_label}\n"
            + f"label {end_label}\n"
        )

    # Visit a parse tree produced by JackParser#doStatement.
    def visitDoStatement(self, ctx: JackParser.DoStatementContext):
        return self.visit(ctx.subroutineCall()) + "pop temp 0\n"

    # Visit a parse tree produced by JackParser#returnStatement.
    def visitReturnStatement(self, ctx: JackParser.ReturnStatementContext):
        if ctx.expression():
            raise ValueError("Return expressions not handled yet")
        return_value = "push constant 0\n"
        return return_value + "return\n"

    # Visit a parse tree produced by JackParser#expression.
    def visitExpression(self, ctx: JackParser.ExpressionContext):
        first_term = self.visit(ctx.term()[0])
        op = self.visit(ctx.op()[0]) if ctx.op() else None
        second_term = self.visit(ctx.term()[1]) if len(ctx.term()) > 1 else None

        if second_term is not None:
            return first_term + second_term + op
        else:
            return first_term

    # Visit a parse tree produced by JackParser#atom.
    def visitAtom(self, ctx: JackParser.AtomContext):
        if ctx.INTEGER():
            return f"push constant {ctx.INTEGER().getText()}\n"
        elif ctx.keywordConstant():
            text = ctx.keywordConstant().getText()
            if text == "false":
                return "push constant 0\n"
            elif text == "true":
                return "push constant 0\nnot\n"
            else:
                raise ValueError(f"Unexpected literal value '{text}'")
        elif ctx.varName():
            symbol = self.symbol_table.get(ctx.varName().getText())
            return f"push {symbol.segment} {symbol.number}\n"
        else:
            raise ValueError(f"Could not handle atom {ctx.getText()}")

    # Visit a parse tree produced by JackParser#arrayReference.
    def visitArrayReference(self, ctx: JackParser.ArrayReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#subroutineExpression.
    def visitSubroutineExpression(self, ctx: JackParser.SubroutineExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#NestedExpression.
    def visitNestedExpression(self, ctx: JackParser.NestedExpressionContext):
        return self.visit(ctx.expression())

    # Visit a parse tree produced by JackParser#UnaryExpression.
    def visitUnaryExpression(self, ctx: JackParser.UnaryExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#subroutineCall.
    def visitSubroutineCall(self, ctx: JackParser.SubroutineCallContext):
        expressions = self.visitChildren(ctx.expressionList()) or ""
        arg_count = len(ctx.expressionList().expressions)

        routine_name = ctx.subroutineName().getText()
        if ctx.className():
            routine_name = ctx.className().getText() + "." + routine_name
        if ctx.varName():
            routine_name = ctx.className().getText() + "." + routine_name

        call = f"call {routine_name} {arg_count}\n"
        return expressions + call

    # Visit a parse tree produced by JackParser#expressionList.
    def visitExpressionList(self, ctx: JackParser.ExpressionListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#op.
    def visitOp(self, ctx: JackParser.OpContext):
        if ctx.ADD():
            return "add\n"
        elif ctx.SUB():
            return "sub\n"
        elif ctx.MUL():
            return "call Math.multiply 2\n"
        elif ctx.DIV():
            return "call Math.divide 2\n"
        if ctx.AND():
            return "and\n"
        elif ctx.OR():
            return "or\n"
        elif ctx.LT():
            return "lt\n"
        elif ctx.GT():
            return "gt\n"
        elif ctx.EQ():
            return "eq\n"
        else:
            raise TypeError(f"Could not handle expression {ctx.getText()}")

    # Visit a parse tree produced by JackParser#unaryOp.
    def visitUnaryOp(self, ctx: JackParser.UnaryOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by JackParser#keywordConstant.
    def visitKeywordConstant(self, ctx: JackParser.KeywordConstantContext):
        return self.visitChildren(ctx)
