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








