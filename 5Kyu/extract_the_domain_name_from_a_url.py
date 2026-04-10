# https://www.codewars.com/kata/514a024011ea4fb54200004b

import re


def domain_name(url):
    return re.match(r"(?:https?://)?(?:www\.)?(.*?)\.", url).group(1)
