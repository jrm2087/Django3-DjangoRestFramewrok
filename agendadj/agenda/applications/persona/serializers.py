from rest_framework import serializers, pagination

from .models import Person, Reunion, Hobby


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            '__all__'
        )


class PersonaSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(required=False)


class PersonaSerializers2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = (
            '__all__'
        )


class ReunionSerializers(serializers.ModelSerializer):

    persona = PersonSerializers()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )


class HobbySerializers(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('id', 'hobby')


class PersonaSerializers3(serializers.ModelSerializer):

    hobbies = HobbySerializers(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created'
        )


class ReunionSerializers2(serializers.ModelSerializer):

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'
        )

    def get_fecha_hora(self, obj):
        return f'{str(obj.fecha)} - {str(obj.hora)}'


class ReunionSerializersLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )
        extra_kwargs = {
            'persona': {
                'view_name': 'persona_app:persona_detalle',
                'lookup_field': 'pk'
            }
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50


class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
