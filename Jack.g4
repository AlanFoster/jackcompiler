grammar Jack;

/**
 * Parser rules
 */
prog:
    classDec
    EOF
    ;

// Program structure

classDec:
    'class' className '{' classVarDec* subRoutineDec* '}'
    ;

className: IDENTIFIER ;

classVarDec:
    ('static' | 'field') typeName varName (',' varName)* ';'
    ;

varName: IDENTIFIER ;

subRoutineDec:
    ('constructor' | 'function' | 'method') ('void' | typeName)
        subroutineName '(' parameterList ')' subroutineBody ;

subroutineName: IDENTIFIER ;

parameterList: ((typeName varName) (',' typeName varName)*)? ;

subroutineBody: '{' varDec* statements '}' ;

varDec: 'var' typeName varName (',' varName)* ';' ;

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
    'let' varName('[' expression ']')? '=' expression ';' ;

ifStatement:
    'if' '(' expression ')' '{' statements '}'
    ('else' '{' statements '}')?
    ;

whileStatement:
    'while' '(' expression ')' '{' statements '}' ;

doStatement:
    'do' subroutineCall ';' ;

returnStatement:
    'return' expression? ';' ;

// Expressions

expression: term (op term)* ;
term:
    INTEGER
    | STRING
    | keywordConstant
    | varName
    | varName '[' expression ']'
    | subroutineCall
    | '(' expression ')'
    | unaryOp term
    ;

subroutineCall:
    subroutineName '(' expressionList ')'
    | (className | varName) '.' subroutineName '(' expressionList ')'
    ;

expressionList: (expression (',' expression)*)? ;
op: ADD | SUB | MUL | DIV | AND | OR | LT | GT | EQ ;
unaryOp: SUB | NOT ;

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
WS: [ \t\n] -> channel(HIDDEN);
