class coercion:
    __slots__ = ['exact', 'type_match', 'removal']
    def __init__(self, exact={}, type_match={}, removal=[]):
        self.exact = exact
        self.type_match = type_match
        self.removal = removal

    def __call__(self, func):
        def decorated_function(*args, **kwargs):
            '''Does not affect kwargs yet'''
            parsed_args = args[:]
            parsed_args = self.type_coercion(parsed_args)
            parsed_args = self.exact_matches(parsed_args)

            # parsed_args = []
            # for arg in args:
            #     if arg in self.removals: continue
            #     if arg in self.coercion:
            #         parsed_args.append(self.coercion[arg])
            #     else:
            #         parsed_args.append(arg)
            # parsed_args = tuple(parsed_args)
            return func(*parsed_args, **kwargs)
        return decorated_function

    def type_coercion(self, args):
        return args

    def exact_matches(self, args):
        parsed_args = []
        for arg in args:
            if arg in self.exact:
                if self.exact[arg] == 'remove':
                    continue
                if self.exact[arg].__class__.__name__ in ['function', 'type']:
                    #TODO try/catch
                    parsed_args.append(self.exact[arg](arg))
                else:
                    parsed_args.append(self.exact[arg])
            else:
                parsed_args.append(arg)
        return tuple(parsed_args)

def coerce_builtin(builtin, exact={}, type_match={}, removal={}):
    constructor = coerce(coercion, exact, type_match, removal)
    return constructor(builtin)

def return_args(*args, **kwargs):
    pass



def test():
    state = False
    print()
