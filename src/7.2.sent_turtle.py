class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    """Read the inbox of a user, marking messages as read."""
    def read_inbox(self, username, count=None):
        user_box = self.boxes[username]
        ret = []
        for msg in user_box:
            if msg['unread']:
                ret.append(msg)
                msg['unread'] = False
                if count is not None and len(ret) == count:
                    break
        return ret

    """Search for messages containing a specific text in the user's inbox."""
    def search_inbox(self, username, message):
        user_box = self.boxes[username]
        ret = []
        for msg in user_box:
            if (message.lower() in msg['body'].lower()) or (message.lower() in msg['title'].lower()):
                ret.append(msg)
        return ret

    def send_message(self, sender, recipient, title, body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str title: The message title.
        :param str body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"No such recipient: {recipient}")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': body,
            'sender': sender,
            'unread': True
        }

        user_box = self.boxes[recipient]
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id
