def concat_words(*args, separator="."):
    return separator.join(args)


print(concat_words("naha", "okinawa", "japan", separator=" "))
