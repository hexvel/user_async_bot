from .commands.default import user_default_commands
from .commands.prefix import user_prefix_commands

from .script_controller import ScriptController
from .scripts.default import user_default_scripts

user_labelers = [
    user_default_commands,
    user_prefix_commands,
    user_default_scripts
]
