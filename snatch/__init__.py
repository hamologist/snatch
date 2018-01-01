import importlib
import pkgutil

from .commands import snatch as snatch_command

snatch_plugins = {
    name: importlib.import_module(name)
    for _, name, _
    in pkgutil.iter_modules()
    if name.startswith('snatch_')
}

for name, module in snatch_plugins.items():
    init_plugin = getattr(module, 'init_plugin', None)

    if init_plugin:
        try:
            init_plugin()
        except:
            pass
