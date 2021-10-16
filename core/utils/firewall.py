import subprocess
import pyufw as ufw
from core.utils.system import run_cmd


def check_ufw():
    """Check UFW.

    Checks if the Ubuntu package UFW is installed

    """
    try:
        ufw = subprocess.call(["which", "ufw"])
        if ufw != 0:
            install_firewall()
        return True
    except:
        pass
    return False


def install_firewall():
    """Install UFW Firewall.

    Installs the ubuntu ufw package

    """
    try:
        run_cmd(f'apt-get install -y ufw')
        return True
    except:
        pass
    return False


def status_firewall():
    """Status UFW Firewall.

    This function give back a dict with the firewall status and all rules.

    """
    try:
        check_ufw()
        return ufw.status()
    except:
        pass
    return False


def enable_firewall():
    """Enable Firewall.

    This function enable the UFW firewall.

    """
    try:
        check_ufw()
        ufw.enable()
        return True
    except:
        pass
    return False


def disable_firewall():
    """Disable Firewall.

    This function disable the UFW firewall.

    """
    try:
        ufw.disable()
        return True
    except:
        pass
    return False


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
    return False


def set_default_rules():
    """Set default Rules.

    This function set the default rules for fastcp.

    """
    try:
        check_ufw()
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
        check_ufw()
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
