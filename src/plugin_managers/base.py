class Base ():
    def __init__(self):
        self.plugins = []

    def process (self, **kwargs):
        oldkwargs = kwargs
        try:
            for plugin in self.plugins:
                kwargs = plugin.do(**kwargs)
        except Exception,msg:
            self.log.critical("PLUGIN FAILURE (%s): %s" % (repr(plugin), repr(msg)))
            kwargs = oldkwargs
        return kwargs.get('data',None)
    


