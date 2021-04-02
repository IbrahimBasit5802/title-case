def title_case(title, minor_words=''):
    # Convert both strings to lower case to avoid conflictions like In != IN
    
    title = title.lower()
    minor_words = minor_words.lower()
    
    # Convert both strings to array for comparisons further in code
    title_arr = title.split(" ")
    minor_arr = minor_words.split(" ")
    
    # Check for words from minor words and if not in minor words, capitalize them
    for x in range(0, len(title_arr)):
        if title_arr[x] not in minor_arr:
            title_arr[x] = title_arr[x].capitalize()
    result = ''
    
    # Capitalize the first word
    title_arr[0] = title_arr[0].capitalize()
    
    # Change the title array to a regular string
    for ele in range(0, len(title_arr)):
        result += title_arr[ele]
        if ele != len(title_arr) -1 :
            result = result + ' '
    return result