# vim: set ft=python ts=4 expandtab:

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError


def rotate(days, frequency):

    valid_frequencies = ['hourly', 'daily', 'weekly', 'monthly', 'yearly']
    if frequency not in valid_frequencies:
        raise AnsibleFilterError('Invalid frequency')

#    if int(days) != days:
#        raise AnsibleFilterError('not an Integer')

    divisor = {
        "hourly": 0.04167,
        "daily": 1,
        "weekly": 7,
        "monthly": 30,
        "yearly": 365
    }

    return int(days / divisor[frequency])


class FilterModule(object):
    def filters(self):
        return {
            'rotate': rotate
        }
