
def load_ipython_extension(ipython):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.
    try:
        import settings
        import django.core.management
        import django
        django.core.management.setup_environ(settings)
        django.setup()
    except ImportError:
        pass

def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.
    pass
