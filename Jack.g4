grammar Jack;

/**
 * Parser rules
 */
program:
    classDec
    EOF
    ;

// Program structure

classDec:
    'class' className '{' classVarDec* subRoutineDec* '}'
    ;

className: IDENTIFIER ;

classVarDec:
    kind=('static' | 'field') typedVariable (',' varName)* ';'
    ;

varName: IDENTIFIER ;

subRoutineDec:
    kind=('constructor' | 'function' | 'method') ('void' | typeName)
        subroutineName '(' parameterList ')' subroutineBody ;

subroutineName: IDENTIFIER ;

parameterList: (params+=typedVariable (',' params+=typedVariable)*)? ;

subroutineBody: '{' varDec* statements '}' ;

varDec: 'var' typedVariable  (',' varName)* ';' ;

typedVariable: typeName varName ;

typeName:
    INT
    | CHAR
    | BOOLEAN
    | className
    ;

// Statements

statements: statement* ;

statement:
    letStatement
    | ifStatement
    | whileStatement
    | doStatement
    | returnStatement
    ;

letStatement:
    'let' varName('[' index=expression ']')? '=' value=expression ';' ;

ifStatement:
    'if' '(' expression ')' '{' true_statements=statements '}'
    ('else' '{' false_statements=statements '}')?
    ;

whileStatement:
    'while' '(' expression ')' '{' statements '}' ;

doStatement:
    'do' subroutineCall ';' ;

returnStatement:
    'return' expression? ';' ;

// Expressions

expression:
    operator=(SUB | NOT) expression                         # unaryExpression
    | left=expression operator=(MUL | DIV) right=expression # binaryExpression
    | left=expression operator=(ADD | SUB) right=expression # binaryExpression
    | left=expression operator=(LT | GT) right=expression   # binaryExpression
    | left=expression operator=AND right=expression         # binaryExpression
    | left=expression operator=OR right=expression          # binaryExpression
    | left=expression operator=EQ right=expression          # binaryExpression
    | INTEGER                                               # atom
    | STRING                                                # atom
    | keywordConstant                                       # atom
    | varName                                               # atom
    | varName '[' index=expression ']'                      # arrayReference
    | subroutineCall                                        # subroutineExpression
    | '(' expression ')'                                    # nestedExpression
    ;

subroutineCall:
    subroutineName '(' expressionList ')'
    | subroutineTarget '.' subroutineName '(' expressionList ')'
    ;

subroutineTarget: className | varName ;

expressionList: (expressions+=expression (',' expressions+=expression)*)? ;

keywordConstant: TRUE | FALSE | NULL | THIS ;

/**
 * Lexer rules
 */

// Keywords
CLASS: 'class' ;
CONSTRUCTOR: 'constructor' ;
FUNCTION: 'function' ;
METHOD: 'method' ;
FIELD: 'field' ;
STATIC: 'static' ;
VAR: 'var' ;
INT: 'int' ;
CHAR: 'char' ;
BOOLEAN: 'boolean' ;
VOID: 'void' ;
TRUE: 'true' ;
FALSE: 'false' ;
NULL: 'null' ;
THIS: 'this' ;
LET: 'let' ;
DO: 'do' ;
IF: 'if' ;
ELSE: 'else' ;
WHILE: 'while' ;
RETURN: 'return' ;

// Seperators
LBRACE : '{' ;
RBRACE : '}' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACK : '[' ;
RBRACK : ']' ;
DOT : '.' ;
COMMA : ',' ;
SEMI : ';' ;

// Operators
ADD : '+' ;
SUB : '-' ;
MUL: '*' ;
DIV: '/' ;
AND: '&' ;
OR: '|' ;
LT: '<' ;
GT: '>' ;
EQ: '=' ;
NOT: '~' ;

// Terms
INTEGER: [0-9]+ ;
STRING: '"' ~('\r' | '\n' | '\'')* '"' ;
IDENTIFIER: [a-zA-Z] [a-zA-Z0-9_]* ;

// Skip whitespaces and comments by default
API_COMMENT: ('/**' .*? '*/') -> channel(HIDDEN) ;
COMMENT: ('/*' .*? '*/') -> channel(HIDDEN) ;
LINE_COMMENT: ('//' ~( '\r' | '\n' )*) -> channel(HIDDEN) ;
WS: [ \t\n\r]+ -> channel(HIDDEN);
