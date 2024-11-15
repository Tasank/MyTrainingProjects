class Doctor:
    def action(self):
        print('Я умею лечить')

    def _info(self):
        print('Я - врач')


    def play(self):
        self.action()
        self._info()

class Surgeon(Doctor):
    def action(self):
        print('Я занимаюсь хирургией')

    def _info(self):
        print('Я - хирург')


d = Surgeon()
d.play()