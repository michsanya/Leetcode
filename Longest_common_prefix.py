def longestCommonPrefix(strs) -> str:
    strs.sort(key=len)
    common_prefix = ""
    common_prefix_temp = ''
    if len(strs) == 1:
        return strs[0]
    for index, letter in enumerate(strs[0]):
        common_prefix = common_prefix + common_prefix_temp
        common_prefix_temp = ''
        for word in strs:
            if word[index] == letter:
                common_prefix_temp = letter
            else:
                return common_prefix
    common_prefix = common_prefix + common_prefix_temp
    return common_prefix
