from users.models import User, UsersRole
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField(allow_blank=False, allow_null=False)
    password = serializers.CharField(max_length=120, allow_blank=False, allow_null=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserDetailsSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    user_role = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.user_role = validated_data.get('user_role', instance.user_role)
        return instance

    def create(self, validated_data):
        pass


class UsersListSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    user_role = serializers.IntegerField()


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersRole
        fields = '__all__'


class UserRegistrationSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    user_role = serializers.IntegerField()
