# -*- coding:utf-8 -*-

class CPF(object):

    INVALID_CPF = [
        '00000000000', '11111111111', '22222222222', '33333333333',
        '44444444444', '55555555555', '66666666666', '77777777777',
        '88888888888', '99999999999'
    ]

    def __init__(self, cpf):
        self.cpf = cpf

    def validate_size(self):
        cpf = self.cleaning()
        if len(cpf) > 11 or len(cpf) < 11:
            return False
        return True

    def validate(self):
        if self.validate_size() and not self.cpf in self.INVALID_CPF:
            digit_1 = 0
            digit_2 = 0
            i = 0
            cpf = self.cleaning()
            while i < 10:
                digit_1 = ((digit_1 + (int(cpf[i]) * (11-i-1))) % 11
                    if i < 9 else digit_1)
                digit_2 = (digit_2 + (int(cpf[i]) * (11-i))) % 11
                i += 1
            return ((int(cpf[9]) == (11 - digit_1 if digit_1 > 1 else 0)) and
                    (int(cpf[10]) == (11 - digit_2 if digit_2 > 1 else 0)))
        return False

    def cleaning(self):
        return self.cpf.replace('.', '').replace('-', '')

    def format(self):
        return '%s.%s.%s-%s' % (
            self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])
