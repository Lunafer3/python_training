class Project:

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return self.name == other.name

    def name_or_empty(self):
        if self.name:
            return self.name
        else:
            return ""


