from typing import Any, Coroutine, Union
import discord
from discord.emoji import Emoji
from discord.message import Message
from discord.partial_emoji import PartialEmoji
from discord_slash.context import ComponentContext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_actionrow, create_button, wait_for_component

def button(style:Union[int, str, ButtonStyle]="PRIMARY", label:Union[str, None]=None, emoji:Union[Emoji, PartialEmoji, str, None]=None, custom_id:Union[str, None]=None, url:Union[str, None]=None, disabled:bool=False) -> dict:
    """Creates a button for use within an action row

    ### Args:
        `style (Union[int, str, ButtonStyle], optional)`: The style of the button. Defaults to "PRIMARY".
        `label (Union[str, None], optional)`: The label of the button. Defaults to None.
        `emoji (Union[Emoji, PartialEmoji, str, None], optional)`: The emoji of the button. Defaults to None.
        `custom_id (Union[str, None], optional)`: The id of the button. Needed for non-link buttons. Defaults to None.
        `url (Union[str, None], optional)`: The URL of the button. Needed for link buttons. Defaults to None.
        `disabled (bool, optional)`: Whether the button is disabled or not. Defaults to False.

    ### Returns:
        dict: Button
    
    ### Example: ::

        my_buttons = buttons(
            button(label="Hi!")
        )
    
    ### Equivalent to: ::

        my_buttons = create_action_row(
            create_button(style=ButtonStyle.primary, label="Hi!")
        )
    """
    if isinstance(style, str):
        style = style.lower()
        if url:
            style = "URL"
        style = ButtonStyle.__dict__[style]
    return create_button(style, label, emoji, custom_id, url, disabled)

def buttons(*button_list:list[dict]) -> dict:
    """Creates an action row for buttons

    ### Args:
        `button_list`: List of buttons to go within the action row

    ### Returns:
        `dict`: Action row
    
    ### Example: ::

        my_buttons = buttons(
            button(label="Hi!")
        )
    
    ### Equivalent to: ::

        my_buttons = create_action_row(
            create_button(style=ButtonStyle.primary, label="Hi!")
        )
    """
    return create_actionrow(*button_list)

async def wait_button(client:discord.Client, buttons:Union[str, dict, list], messages:Union[Message, int, list, None]=None, check=None, timeout=None):
    """Waits for a button interaction. Alternative to `wait_for_component`.

    ### Args:
        `client (discord.Client)`: The client/bot object.
        `buttons (Union[str, dict, list])`: Custom ID to check for, or button dict (buttons or button) or list of previous two.
        `messages (Union[Message, int, list, None], optional)`: The message object to check for, or the message ID or list of the previous two. Defaults to None.
        `check ([type], optional)`: Optional check function. Must take `ComponentContext` as the first parameter. Defaults to None.
        `timeout ([type], optional)`: The number of seconds to wait before timing out and raising `asyncio.TimeoutError`. Defaults to None.

    ### Raises:
        `asyncio.TimeoutError`
    
    ### Example: ::

        button_ctx = await wait_button(bot, my_buttons)
    
    ### Equivalent to: ::

        button_ctx = await wait_for_component(bot, components=my_buttons)
    """
    return await wait_for_component(client, messages, buttons, check, timeout)
