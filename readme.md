# Jack Compiler

A compiler written with [Antlr](https://www.antlr.org/) for the Jack language, a language similar to Java, which will
run on the Hack platform.

## Notes

### Generate parser

```bash
docker-compose build
docker-compose run --rm service /bin/sh /usr/local/bin/antlr4 Jack.g4 -Dlanguage=Python3 -visitor -o parser
```

Unfortunately the generated method names are camel case, rather than snake case - as shown within the python3
codegen templates [here](https://github.com/antlr/antlr4/blob/837aa60e2c4736e242432c2ac93ed2de3b9eff3b/tool/resources/org/antlr/v4/tool/templates/codegen/Python3/Python3.stg#L104)

