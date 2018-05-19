

class GroupChatPeer:

    def __init__(self, peer_id, name, status, role, public_key):
        self._peer_id = peer_id
        self._name = name
        self._status = status
        self._role = role
        self._public_key = public_key

    def get_id(self):
        return self._peer_id

    id = property(get_id)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    status = property(get_status, set_status)

    def get_role(self):
        return self._role

    def set_role(self, role):
        self._role = role

    role = property(get_role, set_role)

    def get_public_key(self):
        return self._public_key

    public_key = property(get_public_key)