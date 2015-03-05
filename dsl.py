
class Rules:
    assertion = {
        "else_whenever": False,
        "whenever": False,
        "otherwise": False,
    }

    called = {
        "else_whenever": False,
        "whenever": False,
        "otherwise": False,
    }

    results = None
    actionType = 'GET'
    execOrNot = True

    def __init__(self):
        pass

    def on_query(self):
        self.execOrNot = (self.actionType == 'GET')
        return self

    def on_create(self):
        self.execOrNot = (self.actionType == 'POST')
        return self

    def on_update(self):
        self.execOrNot = (self.actionType == 'PATCH')
        return self

    def on_delete(self):
        self.execOrNot = (self.actionType == 'PATCH')
        return self

    def whenever(self, assertion):
        if not self.execOrNot:
            return self

        self.assertion['whenever'] = assertion
        self.called['whenever'] = True
        self.execOrNot = True
        return self

    def else_whenever(self, assertion):
        if not self.execOrNot:
            return self

        self.assertion['else_whenever'] = assertion
        self.called['else_whenever'] = True
        self.execOrNot = True
        return self

    def otherwise(self):
        if not self.execOrNot:
            return self

        self.assertion['otherwise'] = \
            (self.assertion['whenever'] and self.assertion['else_whenever'])
        self.called['otherwise'] = True
        self.execOrNot = True
        return self