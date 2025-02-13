
import types

def user_function():
    pass

lambda_function = lambda x: x * 2

built_in_function = len

def is_user_defined(func):
    return isinstance(func, (types.FunctionType, types.LambdaType))

print("User Function:", is_user_defined(user_function))
print("Lambda Function:", is_user_defined(lambda_function))
print("Built-in Function:", is_user_defined(built_in_function))
