from contacts.friend import Friend


class FriendFactory:

    def __init__(self, history, profile_manager, settings, tox):
        self._history, self._profile_manager = history, profile_manager
        self._settings, self._tox = settings, tox

    def create_friend_by_number(self, friend_number):
        aliases = self._settings['friends_aliases']
        tox_id = self._tox.friend_get_public_key(friend_number)
        try:
            alias = list(filter(lambda x: x[0] == tox_id, aliases))[0][1]
        except:
            alias = ''
        item = self.create_friend_item()
        name = alias or self._tox.friend_get_name(friend_number) or tox_id
        status_message = self._tox.friend_get_status_message(friend_number)
        if not self._history.friend_exists_in_db(tox_id):
            self._history.add_friend_to_db(tox_id)
        message_getter = self._history.messages_getter(tox_id)
        friend = Friend(self._profile_manager, message_getter, friend_number, name, status_message, item, tox_id)
        friend.set_alias(alias)

        return friend

    def create_friend_by_public_key(self, public_key):
        friend_number = self._tox.friend_by_public_key(public_key)

        return self.create_friend_by_number(friend_number)

    def create_friend_item(self):
        """
        Method-factory
        :return: new widget for friend instance
        """
        return self._factory.friend_item()
