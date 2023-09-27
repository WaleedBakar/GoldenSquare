class GrammarStats:
    def __init__(self):
        self.total_checked = 0
        self.passed_checks = 0

    def check(self, text):
        starts_with_capital = text and text[0].isupper()
        ends_with_punctuation = text and text[-1] in ['.', '!', '?']
        if starts_with_capital and ends_with_punctuation:
            self.passed_checks += 1
        self.total_checked += 1

    def percentage_good(self):
        if self.total_checked == 0:
            return 0.0
        return (self.passed_checks / self.total_checked) * 100.0
