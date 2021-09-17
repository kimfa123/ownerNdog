from django.shortcuts import render

# Create your views here.
class OwnerListView(View):
    def get(self, request):
        owners = Owner.objects.all()
        
        result1  = []
        
        for owner in owners:

            dogs  = owner.dog_set.all()
            result10 = []
            
            for dog in dogs:

                list1 = {'dog_name': dog.name, "dog_age": dog.age}

                result10.append(list1)
                
            result3 = {'name': owner.name},{'email': owner.email}, {'age': owner.age}, {'dogs':result10}
            result1.append(result3)
        return JsonResponse({'result': result1}, status=200)

    def post(self, request):
        try:
            data   = json.loads(request.body)
            Owner.objects.create(name=data['name'], email=data['email'], age=data['age'])
            return JsonResponse({'result': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'INVELID_KEY'}, status=400)

class DogListView(View):
    def get(Self, request):
        dogs    = Dog.objects.all()
        result2 = []
        
        for dog in dogs:
            owners  = Owner.objects.get(name=dog.owners.name)
            result4 = {'name' : dog.name}, {'age': dog.age}, {'owner': owners.name}
            result2.append(result4)
        return JsonResponse({'result': result2}, status=200)

    def post(self, request):
        try:
            data   = json.loads(request.body)
            owner  = Owner.objects.get(name=data['owner']) # name=data['front key 값 아무 내용 가능']
            Dog.objects.create(name=data['name'], age=data['age'], owners=owner)
            return JsonResponse({'result': 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message' : 'INVELID_KEY'}, status=400)
        except Owner.DoesNotExist:
            return JsonResponse({'message' : 'USER DOES NOT EXIST'}, status=404) # get 들어있다면 except 2개 해줘야한다.