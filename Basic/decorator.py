def annaunce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper

@annaunce
def hello():
    print("hello world!")

hello()
