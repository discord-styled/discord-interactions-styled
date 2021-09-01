from typing import Union
from discord_slash.utils.manage_commands import create_choice, create_option


class Options:
    """Creates a slash command options template

    ### Example: ::

        my_options = Options()
    """
    
    def __init__(self) -> None:
        self.options = []
    
    def _prepare_choices(self, choices:list) -> list:
        """Convert list of choices to dictionaries

        ### Args:
            choices (`list`): List of choices

        ### Returns:
            `list`: List of dictionaries
        
        ### Example: ::

            my_options = Options()
            my_options.add("my_option", "This is my description")
        """
        for i, x in enumerate(choices):
            if isinstance(x, tuple):
                choices[i] = create_choice(x[0], x[1])
            else:
                choices[i] = create_choice(x, x)
        return choices
    
    def template(self) -> list:
        """Get the options template. Note: Don't do this until you've defined all your options.

        ### Returns:
            `list`: Template of options
        
        ### Example: ::

            my_options = Options()
            my_options.add("option1", "etc..")
            my_options = my_options.template()

            # Due to every method returns the template, if you have only one option you can do something like this:

            my_options = Options().add("option1", "etc...")
        """
        return self.options

    def add(self, name:str, description:str, type:Union[type, int]=3, required:bool=True, choices:list=[]) -> list:
        """Add option to template

        ### Args:
            name (`str`): Name of the option
            description (`str`): Description of the option
            type (`Union[type, int], optional`): Type of the option. Defaults to 3.
            required (`bool, optional`): Whether the option is disabled or not. Defaults to True.
            choices (`list, optional`): List of choices. Defaults to [].

        ### Returns:
            `dict`: Options list
        """
        choices = self._prepare_choices(choices)
        self.options.append(create_option(name, description, type, required, choices))
        return self.options
    
    def add_from_dict(self, option:dict) -> list:
        """Generate option from dictionary and add it to template

        ### Args:
            option (`dict`): Option's dict

        ### Returns:
            `dict`: Options list
        
        ### Example: ::

            my_options = Options()
            data = {"name": "my_option", "description": "My description"}
            my_options.add_from_dict(data)

            # Equivalent to:

            my_options = Options()
            my_options.add("my_option", "My description")
        """
        option_type = 3 if "type" not in option else option["type"]
        required = True if "required" not in option else option["required"]
        choices = [] if "choices" not in option else self._prepare_choices(option["choices"])
        self.options.append(create_option(option["name"], option["description"], option_type, required, choices))
        return self.options
    
    def add_from_dicts(self, options:list[dict]) -> list:
        """Generate options from a list of dicts and add them to template

        ### Args:
            options (`list`): List of dicts

        ### Returns:
            `dict`: Options list
        
        ### Example: ::

            data = [
                {"name": "option1", "description": "One option"},
                {"name": "option2", "description": "Two options", "type": int, "required": False},
                {"name": "option3", "description": "Three options", "choices": ["choice1"]}
            ]
            my_options = Options()
            my_options.add_from_dicts(data)
        
            # Equivalent to:

            my_options = Options()
            my_options.add("option1", "One option")
            my_options.add("option2", "Two options", int, False)
            my_options.add("option3", "Three options", choices=["choice1"])
        """
        for option in options:
            self.add_from_dict(option)
        return self.options