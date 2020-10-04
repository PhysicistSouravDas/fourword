from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Custom manager class for default User model.
    """

    def create_user(self, email, password, **kwargs):
        """Manager class method to create new User.

            Args:
                email (str): String object to represent email.
                password (str): String object to represent password.

            Returns:
                object: Returns Django User class's object.
        """
        if not email:
            raise ValueError('Email can not be blank.')

        if not password:
            raise ValueError('Password can not be blank.')

        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        """Manager class method to create new Superuser.

            Args:
                email (str): String object to represent email.
                password (str): String object to represent password.

            Returns:
                object: Returns Django User class's object.
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must be a Staff.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Only Superuser creation allowed.')
        if not (kwargs.get('first_name') and kwargs.get('last_name')):
            raise ValueError('First and Last name are mandatory.')

        return self.create_user(email, password, **kwargs)
