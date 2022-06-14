from .models import Profile


class PhoneNumberValidator:

    def __init__(self, phone_number, valid_digits):
        self.phone_number = phone_number
        self.valid_digits = valid_digits

    def phone_number_validator(self):

        if len(self.phone_number) == 10:
            self.phone_number = f'0{self.phone_number}'

        if (len(self.phone_number) != 11) or not self.phone_number[0] == '0' or\
                self.phone_number[1:4] not in str(self.valid_digits):
            raise ValueError('invalid phone number <09xx xxx xxxx>')
        return self.phone_number


class VerifyValidator:

    def __init__(self, phone_number=None, email=None):
        self.phone_number = phone_number
        self.email = email

    def phone_number_is_verified(self):
        user = Profile.objects.get(phone_number=self.phone_number)
        return True if user.phone_number_is_verified else False

    def email_is_verified(self):
        user = Profile.objects.get(email=self.email)
        return True if user.email_is_verified else False











