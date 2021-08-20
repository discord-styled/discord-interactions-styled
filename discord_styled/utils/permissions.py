from typing import Union
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_permission

class Permissions:
    """Creates a slash command permissions template

    ### Args:
        `guild_id (int, list[int])`: List of guild ids
    
    ### Example: ::

        permissions = Permissions([123, 456, ...])
    """

    def __init__(self, guild_id:Union[int, list[int]]) -> None:
        self.guild_ids = [guild_id] if isinstance(guild_id, int) else guild_id
        self.permissions = {}
        for id in self.guild_ids:
            self.permissions[id] = []
    
    def everyone_permission(self, allow:bool=False) -> dict:
        """Allow or deny permission to @everyone

        ### Args:
            `allow (bool, optional)`: Whether to allow or deny permission. Defaults to False.
        
        ### Returns:
            `dict`: Permissions
        
        ### Example: ::

            permissions = Permissions(...)
            permissions.everyone_permission(False)
        """
        for id in self.guild_ids:
            permission = create_permission(id, SlashCommandPermissionType.ROLE, allow)
            if permission not in self.permissions[id]:
                self.permissions[id].append(permission)
        return self.permissions
    
    def allow_users(self, users:list[int], allow:bool=True) -> dict:
        """Allow or deny permissions to a list of user ids

        ### Args:
            `users (list[int])`: List of user ids
            `allow (bool, optional)`: Whether to allow or deny permission. Defaults to True.
        
        ### Returns:
            `dict`: Permissions
        
        ### Example: ::

            permissions = Permissions(...)
            permissions.allow_users([123, 456, ...])
        """
        for id in self.guild_ids:
            for user in users:
                self.permissions[id].append(create_permission(user, SlashCommandPermissionType.USER, allow))
        return self.permissions
    
    def allow_only_users(self, users:list[int]) -> dict:
        """Deny permissions for @everyone and allow them to a list of users ids

        ### Args:
            `users (list[int])`: List of users ids
        
        ### Returns:
            `dict`: Permissions

        ### Example: ::

            permissions = Permissions(...)
            permissions.allow_only_users([123, 456, ...])
        
        ### Equivalent to: ::

            permissions = Permissions(...)
            permissions.everyone_permission(False)
            permissions.allow_users([123, 456, ...])
        """
        self.everyone_permission(False)
        self.allow_users(users)
        return self.permissions
    
    def deny_users(self, users:list[int]) -> dict:
        """Deny permissions for a list of user ids, same as `allow_users(..., False)`

        ### Args:
            `users (list[int])`: List of user ids
        
        ### Returns:
            `dict`: Permissions
        
        ### Example: ::

            permissions = Permissions(...)
            permissions.deny_users([123, 456, ...])
        
        ### Equivalent to: ::

            permissions = Permissions(...)
            permissions.allow_users([123, 456, ...], False)
        """
        self.allow_users(users, False)
        return self.permissions
    
    def allow_roles(self, roles:list, allow:bool=True) -> dict:
        """Allow permissions for a list of role ids

        ### Args:
            `roles (list)`: List of role ids
            `allow (bool, optional)`: Whether to allow or deny permission. Defaults to True.
        
        ### Returns:
            `dict`: Permissions
        
        ### Example: ::

            permissions = Permissions(...)
            permissions.allow_roles([123, 456, ...])
        """
        for id in self.guild_ids:
            for role in roles:
                self.permissions[id].append(create_permission(role, SlashCommandPermissionType.ROLE, allow))
        return self.permissions
    
    def allow_only_roles(self, roles:list) -> dict:
        """Deny permissions for @everyone and allow them to a list of role ids

        ### Args:
            `roles (list)`: List of role ids
        
        ### Returns:
            `dict`: Permissions
        
        ### Example: ::

            permissions = Permissions(...)
            permissions.allow_only_roles([123, 456, ...])
        
        ### Equivalent to: ::

            permissions = Permissions(...)
            permissions.everyone_permission(False)
            permissions.allow_roles([123, 456, ...])
        """
        self.everyone_permission(False)
        self.allow_roles(roles)
        return self.permissions
    
    def deny_roles(self, roles:list[int]) -> dict:
        """Deny permissions to a list of role ids, same as `allow_roles(..., False)`

        ### Args:
            `roles (list[int])`: List of role ids
        
        ### Returns:
            `dict`: Permissions
        
        ### Example: ::

            permissions = Permissions(...)
            permissions.deny_roles([123, 456, ...])
        
        ### Equivalent to: ::

            permissions = Permissions(...)
            permissions.allow_roles([123, 456, ...], False)
        """
        self.allow_roles(roles, False)
        return self.permissions