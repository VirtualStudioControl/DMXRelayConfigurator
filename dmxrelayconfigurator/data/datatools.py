__MESSAGE_ID = 0


def messageID() -> int:
    global __MESSAGE_ID
    __MESSAGE_ID = __MESSAGE_ID +1
    return __MESSAGE_ID
