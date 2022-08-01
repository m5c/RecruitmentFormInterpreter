import ParticipantStatTools
from Participant import Participant


class ControlGroup:

    def __init__(self, name: str, participants: []):
        self.name = name
        self.participants = participants

    def add_participant(self, participant):
        self.participants.append(participant)

    def get_participants(self) -> list[Participant]:
        return self.participants

    def get_group_name(self):
        return self.name

    def get_group_score(self):
        return sum(ParticipantStatTools.build_summed_skills(self.participants))

    def get_skill_amount(self):
        return self.participants[0].get_skill_amount()

    def get_group_size(self):
        return len(self.participants)

    def __str__(self):
        group_str = "Total score: " + str(self.get_group_score()) + "\n"
        for participant in self.participants:
            group_str += " * " + str(participant) + "\n"
        return group_str

    def mark_dropper(self, dropper_index: int):
        self.participants[dropper_index].set_dropper(True)
        return self.participants[dropper_index].get_name()
