from data.randomizer import Randomizer


class UserDataRandomizer(Randomizer):

    def build_random_user_first_name(self):
        return super().create_random_string("First_name-")

    def build_random_user_last_name(self):
        return super().create_random_string("Last_name-")

    def build_random_email_name(self):
        return "test" + super().create_random_string("") + "@test.ua"



