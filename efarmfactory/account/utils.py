from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class token_generator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))

generate_token=token_generator()