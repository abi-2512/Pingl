class Interpreter:
    def __init__(self):
        self.variables = {}
        self.classes = {}

    def evaluate(self, ast):
        for statement in ast:
            self.execute(statement)

    def execute(self, node):
        if node[0] == 'assign':
            _, var_name, value = node
            self.variables[var_name] = self.evaluate_value(value)
        elif node[0] == 'display':
            _, value = node
            print(self.evaluate_value(value))
        elif node[0] == 'if':
            _, left, operator, right, body, else_body = node
            condition = self.evaluate_condition(left, operator, right)
            if condition:
                for stmt in body:
                    self.execute(stmt)
            else:
                for stmt in else_body:
                    self.execute(stmt)
        elif node[0] == 'repeat':
            _, times, body = node
            for _ in range(int(times)):
                for stmt in body:
                    self.execute(stmt)
        elif node[0] == 'class':
            _, class_name, body = node
            self.classes[class_name] = body

    def evaluate_value(self, value):
        if isinstance(value, tuple) and value[0] == 'concat':
            left = self.evaluate_value(value[1])
            right = self.evaluate_value(value[2])
            return str(left) + str(right)
        elif isinstance(value, tuple):
            raise RuntimeError(f"Unknown operation: {value[0]}")
        elif isinstance(value, str) and value.isdigit():
            return int(value)
        elif value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        return self.variables.get(value, value)

    def evaluate_condition(self, left, operator, right):
        left_val = self.variables.get(left, 0)
        right_val = int(right)
        if operator == 'GREATER':
            return left_val > right_val
        elif operator == 'LESS':
            return left_val < right_val
        return False