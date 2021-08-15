<div align="center">
    <a><img src="https://cdn.discordapp.com/attachments/875651719088984125/875884861926285364/logo.gif" alt="discord-py-interactions" height="128"></a>
    <h2>Write easier code using <a href="https://github.com/discord-py-interactions/discord-py-interactions">discord-interactions</a> with <a href="https://github.com/discord-styled/discord-interactions-styled">interactions-styled</a>.</h2>
</div>

<p align="center">
    <a href="#about">About</a> |
    <a href="#installation">Installation</a> |
    <a href="#examples">Examples</a> |
    <a href="https://discord.gg/kNYjuz2Jjv">Discord</a> |
    <a href="https://pypi.org/project/discord-interactions-styled/">PyPI</a> |
    <a href="https://discord-styled.github.io/">Documentation</a>
</p>

# About
## What?
discord-interactions-styled is a set of already coded functions, decorators an more for the known <a href="https://github.com/discord-py-interactions/discord-py-interactions">discord-py-interactions</a> library.

## Why?
Well, discord-py-interactions is already pretty easy right? but, when you're working on a large-size bot it becomes repetitive to write always the same code to get results, it's redundant, that's when interactions-styled comes to the scene with a full set of functions to get results so much faster.

## How?
Just look at this example, we're denying permissions for `@everyone` and allowing them for two role ids `456` and `789`:
```py
# base library
@slash.slash(..., permissions={
    123: [
        create_permission(123, SlashCommandPermissionType.ROLE, False),
        create_permission(456, SlashCommandPermissionType.ROLE, True)
        create_permission(789, SlashCommandPermissionType.ROLE, True)
    ]
})

# With discord-interactions-styled
@slash.slash(...)
@only_allow_roles(123, [456, 789])

```
That's some *clean & pretty* code right there huh

# Installation
You can install this lib using pip, just type the following line below:

`pip install -U discord-interactions-styled`

# Examples
Creating options for a slash command
```py
from discord_slash.utils.manage_commands import create_option

# discord-py-interactions
@slash.slash(..., options=[
    create_option("option1", "my description", 3, True),
    create_option("option2", "another description", 4, True)
    create_option("option3", "and another", 3, False)
])

# discord-interactions-styled
from discord_styled.slash import option

@option("option1", "my description")
@option("option2", "another description", 4)
@option("option3", "and another", required=False)
@slash.slash(...)

```

Denying permissions for `@everyone` in a slash command
```py
# discord-py-interactions
from discord_slash.utils.manage_commands import create_permission

@slash.slash(..., permissions={
    123: [
        create_permission(123, SlashCommandPermissionType.ROLE, False)
    ]
})

# discord-interactions-styled
from discord_styled.permissions import deny_all

@slash.slash(...)
@deny_all()
```

## Documentation
These are just a few examples, we recommend you to go and visit the [official documentation](https://discord-styled.github.io/)

--------

- <a href="https://github.com/discord-styled/discord-interactions-styled">discord-interactions-styled</a> is not an independant library, all the logic comes from <a href="https://github.com/discord-py-interactions/discord-py-interactions">discord-py-interactions</a>, so this isn't an alternative to that lib, we're just providing a set of tools to use discord-py-interactions more easily.