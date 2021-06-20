
# Prints the path as a single string
def get_path(path):
    arrow = "-->"

    if "|" in path:
        result = " ".join(path)
    else:
        result = arrow.join(path)

    return result