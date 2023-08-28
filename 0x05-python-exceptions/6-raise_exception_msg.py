def raise_exception_msg(message=""):
    class CustomNameError(NameError):
        pass
    
    raise CustomNameError(message)

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print("Caught exception:", ne)
