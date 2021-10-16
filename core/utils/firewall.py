import pyufw as ufw


def enable_firewall():
    """Enable Firewall.

    This function enable the UFW firewall.

    """
    try:
        ufw.enable()
        return True
    except:
        pass


def disable_firewall():
    """Disable Firewall.

    This function disable the UFW firewall.

    """
    try:
        ufw.disable()
        return True
    except:
        pass


def reset_firewall():
    """Reset Firewall.

    This function disable the UFW firewall.

    """
    try:
        ufw.reset()
        set_default_rules()
        return True
    except:
        pass


def set_default_rules():
    """Set default Rules.

    This function set the default rules for fastcp.

    """
    try:
        ufw.add("allow 22")
        ufw.add("allow 80")
        ufw.add("allow 443")
        ufw.add("allow 2050")
        return True
    except:
        pass
    return False


def add_rule(rule):
    """Add rule to firewall.

    This functions adds a rule to the firewall.

    """
    try:
        ufw.add(rule)
        return True
    except:
        pass
    return False

def delete_rule(rule):
    """Delete rule from firewall.

    This functions deletes a rule from the firewall.

    """
    try:
        ufw.delete(rule)
        return True
    except:
        pass
    return False

def delete_all():
    """Delete rule from firewall.

    This functions deletes a rule from the firewall.

    """
    try:
        reset_firewall()
        return True
    except:
        pass
    return False
