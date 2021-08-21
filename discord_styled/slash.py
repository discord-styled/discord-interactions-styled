from typing import Union
from discord_slash.utils.manage_commands import create_choice, create_option

def option(name:str, description:str, type:Union[int, type]=3, required:bool=True, choices:list=[]):
    """Decorator to add an option to a slash command

    ### Example: ::

        @option("option1", "My option's description")
        @option("option2", "Another description", required=False)
        @slash.slash(...)
    
    ### Equivalent to: ::

        @slash.slash(..., options=[
            create_option("option1", "My option's description", 3, True),
            create_option("option2", "Another description", 3, False)
        ])
    
    ### Args:
        `name (str)`: Option's name
        `description (str)`: Option's description
        `type (Union[int, type], optional)`: Option's type. Defaults to 3.
        `required (bool, optional)`: Should require this option or not. Defaults to True.
        `choices (list, optional)`: Option's choices. Defaults to [].
    """
    def wrapper(cmd):
        for i, x in enumerate(choices):
            if isinstance(x, tuple):
                choices[i] = create_choice(x[0], x[1])
            else:
                choices[i] = create_choice(x, x)
        if not hasattr(cmd, "__options__"):
            cmd.__options__ = True
            cmd.options = []
        cmd.options.insert(0, create_option(name, description, type, required, choices))
        return cmd
    return wrapper