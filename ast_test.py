import ast
import astor
import astunparse
t = None

class v(ast.NodeVisitor):
    def generic_visit(self, node):
        if isinstance(node, ast.Call):
            if node.func.attr == "run":
                for x in node.args:
                    print(type(x))
                    print(x.__dict__)
                    print("astunparse: {}".format(astunparse.unparse(x)))
                    print("astor: {}".format(astor.to_source(x)))
                print(node.__dict__)
        ast.NodeVisitor.generic_visit(self, node)

x = v()
with open("samples/sample_01.py") as i:
    t = ast.parse(i.read())
x.visit(t)
