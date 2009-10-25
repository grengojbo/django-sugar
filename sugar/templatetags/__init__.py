from django.template.context import Context
from functools import wraps

def private_context(f):
    """
    Simple decorator which avoids the need to a) copy-and-paste code to force
    context variables into inclusion_tag templates and b) carefully avoid
    inclusion tag variables conflicting with global variables.
    
    Instead each inclusion tag will be called with a *copy* of the provided
    context variable and its results will be merged in to avoid leaking into
    the global context


    """
    
    @wraps(f)
    def private_context_wrapper(context, *args, **kwargs):
        c = Context(context)
        rc = f(c, *args, **kwargs)
        c.update(rc)
        return c

    return private_context_wrapper