from matplotlib.text import Text


class MainEvent:
    record_id: int
    text: Text

    def __init__(self, mat_text: Text, record_id: int):
        self._text = mat_text
        self.record_id = record_id
        self._event_type = None

    @property
    def text(self):
        return self._text

    def customise_text(self):
        self.text.set_color('red')

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, type_of_event: str):  # TODO change this to some namedtuple maybe to restric
        self._event_type = type


class GunEvent(MainEvent):
    def __init__(self, mat_text: Text, record_id: int, gunid: int):
        super().__init__(mat_text, record_id)
        self._gun_id = gunid
        self.customise_text()

    @property
    def gun_id(self):
        return self._gun_id

    def customise_text(self):
        self.text.set_color('blue') # TODO doesn't work - look for other method in Text class API
