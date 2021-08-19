from typing import Union
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_permission

def permissions(permissions:dict):
    """Apply a slash command permissions template.

    ### Args:
        `permissions (dict)`: Permissions template
    
    ### Example: ::

        @slash.slash(...)
        @permissions(my_permissions)

    """
    def wrapper(cmd):
        cmd.__permissions__ = permissions
        return cmd
    return wrapper

def prepare_command(cmd, guild_id:Union[int, list[int]]):
    """Prepare command adding permissions param and guild_id key if needed

    ### Args:
        `cmd`: Command to prepare
        `guild_id (int, list[int])`: Guild id(s) to prepare

    ### Returns:
        `cmd`: Command with `__permissions__` and `__permissions__[guild_id]`
    """
    if not getattr(cmd, "__permissions__", None):
        cmd.__permissions__ = {}
    if isinstance(guild_id, list):
        for id in guild_id:
            if id not in cmd.__permissions__:
                cmd.__permissions__[id] = []
    else:
        if guild_id not in cmd.__permissions__:
            cmd.__permissions__[guild_id] = []
    return cmd

def _set_everyone_permission(cmd, guild_id:Union[int, list[int]], allow:bool=False):
    """Deny permission for @everyone

    ### Args:
        `cmd`: Command
        `guild_id (int, list[int])`: Guild id(s) to apply permission
        `allow` (bool, optional): Allow or deny

    ### Returns:
        `cmd`: Command with @everyone denied permission
    """
    if isinstance(guild_id, list):
        for id in guild_id:
            cmd.__permissions__[id].append(create_permission(id, SlashCommandPermissionType.ROLE, False))
    else:
        cmd.__permissions__[guild_id].append(create_permission(guild_id, SlashCommandPermissionType.ROLE, allow))
    return cmd

def deny_all(guild_id:Union[int, list[int]]):
    """Decorator, deny permissions for @everyone

    ### Args:
        `guild_id (int, list[int])`: Id(s) of guild to apply permission

    ### Example: ::

        @slash.slash(...)
        @deny_all(123)
    
    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(123, SlashCommandPermissionType.ROLE, False)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        cmd = _set_everyone_permission(cmd, guild_id)
        return cmd
    return wrapper

def allow_all(guild_id:Union[int, list[int]]):
    """Decorator, allow permissions for @everyone

    ### Args:
        `guild_id (int, list[int])`: Id(s) of guild to apply permission

    ### Example: ::

        @slash.slash(...)
        @allow_all(123)
    
    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(123, SlashCommandPermissionType.ROLE, True)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        cmd = _set_everyone_permission(cmd, guild_id, True)
        return cmd
    return wrapper

# ROLE PERMISSIONS ------>

def _allow_role(cmd, guild_id:Union[int, list[int]], role_id:int, allow:bool=True):
    """Create ROLE type permission

    ### Args:
        `cmd`: Command
        `guild_id (int, list[int])`: Guild id to apply permission
        `role_id (int)`: Role id to apply permission
        `allow (bool, optional)`: Allow or deny permission. Defaults to True.

    ### Returns:
        `cmd`: Command with permission created
    """
    if isinstance(guild_id, list):
        for id in guild_id:
            cmd.__permissions__[id].append(
                create_permission(role_id, SlashCommandPermissionType.ROLE, allow)
            )
    else:
        cmd.__permissions__[guild_id].append(
            create_permission(role_id, SlashCommandPermissionType.ROLE, allow)
        )
    return cmd

def only_allow_roles(guild_id:Union[int, list[int]], roles:list[int]):
    """Decorator, deny permissions for @everyone and allow only for selected roles

    ### Args:
        `guild_id (int, list[int])`: Id(s) of guild to apply permissions
        `roles (list[int])`: List of role ids

    ### Example: ::

        @slash.slash(...)
        @only_allow_roles(123, [456, 654])
    
    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(123, SlashCommandPermissionType.ROLE, False),
                create_permission(456, SlashCommandPermissionType.ROLE, True),
                create_permission(654, SlashCommandPermissionType.ROLE, True)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        cmd = _set_everyone_permission(cmd, guild_id)
        for role in roles:
            cmd = _allow_role(cmd, guild_id, role)
        return cmd
    return wrapper

def allow_roles(guild_id:Union[int, list[int]], roles:list[int]):
    """Decorator, allow access for selected roles

    ### Args:
        `guild_id (int)`: Id(s) of guild to apply permissions
        `roles (list[int])`: List of role ids

    ### Example: ::

        @slash.slash(...)
        @just_allow_roles(123, [456, 654])
    
    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(456, SlashCommandPermissionType.ROLE, True),
                create_permission(654, SlashCommandPermissionType.ROLE, True)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        for role in roles:
            cmd = _allow_role(cmd, guild_id, role)
        return cmd
    return wrapper

def deny_roles(guild_id:Union[int, list[int]], roles:list[int]):
    """Decorator, deny permissions for selected roles

    ### Args:
        `guild_id (int, list[int])`: Id(s) of the guild to apply permission
        `roles (list[int])`: List of role ids

    ### Example: ::

        @slash.slash(...)
        @deny_roles(123, [456, 654])

    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(456, SlashCommandPermissionType.ROLE, False),
                create_permission(654, SlashCommandPermissionType.ROLE, False)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        for role in roles:
            cmd = _allow_role(cmd, guild_id, role, False)
        return cmd
    return wrapper

# USER PERMISSIONS ------>

def _allow_user(cmd, guild_id:Union[int, list[int]], user_id:int, allow:bool=True):
    """Create a USER type permission

    ### Args:
        `cmd`: Command
        `guild_id (int, list[int])`: Guild id(s) to apply permission
        `user_id (int)`: User id to apply permission
        `allow (bool, optional)`: Allow or deny permission. Defaults to True.

    Returns:
        `cmd`: Command with permission created
    """
    if isinstance(guild_id, list):
        for id in guild_id:
            cmd.__permissions__[id].append(
                create_permission(user_id, SlashCommandPermissionType.USER, allow)
            )
    else:
        cmd.__permissions__[guild_id].append(
            create_permission(user_id, SlashCommandPermissionType.USER, allow)
        )
    return cmd

def allow_users(guild_id:Union[int, list[int]], users:list[int]):
    """Decorator, Allow access for selected users

    ### Args:
        `guild_id (int, list[int])`: Guild id(s) to apply permission
        `users (list[int])`: List of user ids
    
    ### Example: ::

        @slash.slash(...)
        @allow_users(123, [456, 654])

    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(456, SlashCommandPermissionType.USER, True),
                create_permission(654, SlashCommandPermissionType.USER, True)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        for user in users:
            _allow_user(cmd, guild_id, user)
        return cmd
    return wrapper

def deny_users(guild_id:Union[int, list[int]], users:list[int]):
    """Decorator, Deny access for selected users

    ### Args:
        `guild_id (int)`: Guild id(s) to apply permission
        `users (list[int])`: List of user ids
    
    ### Example: ::

        @slash.slash(...)
        @deny_users(123, [456, 654])

    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(456, SlashCommandPermissionType.USER, False),
                create_permission(654, SlashCommandPermissionType.USER, False)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        for user in users:
            _allow_user(cmd, guild_id, user, False)
        return cmd
    return wrapper

def only_allow_users(guild_id:Union[int, list[int]], users:list[int]):
    """Decorator, Allow access for selected users

    ### Args:
        `guild_id (int, list[int])`: Guild id(s) to apply permission
        `users (list[int])`: List of user ids
    
    ### Example: ::

        @slash.slash(...)
        @only_allow_users(123, [456, 654])

    ### Equivalent to: ::

        @slash.slash(..., permissions={
            123: [
                create_permission(123, SlashCommandPermissionType.USER, False),
                create_permission(456, SlashCommandPermissionType.USER, True),
                create_permission(654, SlashCommandPermissionType.USER, True)
            ]
        })
    """
    def wrapper(cmd):
        cmd = prepare_command(cmd, guild_id)
        cmd = _set_everyone_permission(cmd, guild_id)
        for user in users:
            _allow_user(cmd, guild_id, user)
        return cmd
    return wrapper