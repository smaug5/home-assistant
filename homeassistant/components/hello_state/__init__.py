"""The hello_state component."""

# from homeassistant.config import ConfigType
import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

CONFIG_SCHEMA = vol.Schema({}, extra=vol.ALLOW_EXTRA)
DOMAIN = "hello_state"


"""The hello_state setup process."""


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the hello_state component.

    Args:
        hass: Home Assistant core object.
        config: Configuration dictionary.

    Returns:
        bool: True if setup was successful.
    """
    hass.states.set("hello_state.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True
