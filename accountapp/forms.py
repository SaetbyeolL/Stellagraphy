from django.contrib.auth.forms import PasswordChangeForm


class AccountUpdateForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].disabled = True
