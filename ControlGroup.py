import ParticipantStatTools


class ControlGroup:

    def __init__(self, name: str):
        self.name = name
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def get_group_name(self):
        return self.name

    def get_group_score(self):
        return sum(ParticipantStatTools.build_summed_skills(self.participants))

    def __str__(self):
        group_str = self.get_group_name() + ": " + str(self.get_group_score())+"\n"
        for participant in self.participants:
            group_str += " * "+str(participant)+"\n"
        return group_str


