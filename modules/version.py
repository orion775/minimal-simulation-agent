def get_version():
    with open("version.txt") as f:
        return f.read().strip()