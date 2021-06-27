from app.session.models.session import Session


class ListSessionUseCase():
    def __init__(self, session_repo):
        self.session_repo = session_repo

    def run(self):
        return [s.as_dict() for s in self.session_repo.list()]


