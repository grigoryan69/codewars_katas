def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}" \
        if 'needle' in haystack else 0