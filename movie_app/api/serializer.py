#django imports
from django.contrib.auth.models import User

#rest framework imports
from rest_framework import  serializers

#local imports
from movie_app.models import Collections, Generes, Movie

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],password = validated_data['password'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# Generes serializer
class GeneresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generes
        fields = '__all__'


# Movie serializer
class MovieSerializer(serializers.ModelSerializer):
    genres = GeneresSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


# Collections serializer
class GETRetriveCollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Collections
        #fields = ('title','description','movies','description')
        fields = '__all__'


 
class POSTPUTCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = '__all__'
        validators = []

    def run_validation(self, attrs):
        if self.partial: return attrs  # skip validation for PUT since the values in PUT body are optional as mentioned in the doc
        errors={}
        if not attrs.get('title'):
            errors['title'] = 'Title is required'
        if not attrs.get('description'):
            errors['description'] = 'Description is required'
        if not attrs.get('movies'):
            errors['movies'] = 'Movies are required'
        if attrs.get('movies'):
            movies_data = attrs.get('movies')
            for movie in movies_data:
                single_error = {}
                if not movie.get('title'):
                    single_error['title'] = 'Title is required'
                if not movie.get('description'):
                    single_error['description'] = 'Description is required'
                if not movie.get('genres'):
                    single_error['genres'] = 'Genres is required'
                if single_error:
                    if errors.get('movies'):
                        errors['movies'].append(single_error)
                    else: 
                        errors['movies'] = [single_error]
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        all_movies = handle_movies_and_geners(movies_data)
        collection_obj = Collections.objects.create(**validated_data)
        collection_obj.movies.set(all_movies)
        return collection_obj
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        if validated_data.get('movies'):
            movies_data = validated_data.get('movies')
            all_movies = handle_movies_and_geners(movies_data)
            instance.movies.set(all_movies)
        instance.save()
        return instance

def handle_movies_and_geners(movies_data):
        all_movies = []
        for movie in movies_data:
            all_gener = []
            geners_data = movie.pop('genres')
            for each_geners in geners_data:
                obj, created = Generes.objects.get_or_create(**each_geners)
                all_gener.append(obj)
            obj, created = Movie.objects.get_or_create(**movie)
            obj.genres.set(all_gener)
            obj.save()
            all_movies.append(obj)
        return all_movies
       
        
        
        