from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User
from events.models import Event
from line_up.models import LineUp

class DeleteLineupTest(APITestCase):
    fixtures = [
        'user-fixture.json',
        'event-fixture.json', 
        'address-fixture.json', 
        'category-fixture.json', 
        'lineup-fixture.json'
    ]

    @classmethod
    def setUpTestData(cls):
        cls.event      = Event.objects.all()[1]
        cls.admin_user = User.objects.filter(is_superuser=True)[0]
        cls.user       = User.objects.filter(is_staff=False)[0]
        cls.lineup     = LineUp.objects.filter(event_id=cls.event.id)[0]

        cls.client = APIClient()
    
    def test_should_not_accept_non_admin_user(self):
        token,_ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        try:
            response = self.client.delete(f"/api/events/{self.event.id}/lineup/{self.lineup.id}/")
        except Exception as e:
            self.fail(f'deletion is failing with message: {str(e)}')
            
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)        
        self.assertIn('detail', response_dict.keys())

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 1234')

        try:
            response = self.client.delete(f"/api/events/{self.event.id}/lineup/{self.lineup.id}/")
        except Exception as e:
            self.fail(f'deletion is failing with message: {str(e)}')

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)        
        self.assertIn('detail', response_dict.keys())
    
    def test_should_delete_lineup(self):
        token,_ = Token.objects.get_or_create(user_id=self.admin_user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        try:
            response = self.client.delete(f"/api/events/{self.event.id}/lineup/{self.lineup.id}/")
        except Exception as e:
            self.fail(f'deletion is failing with message: {str(e)}')
        
        try:
            LineUp.objects.get(id=self.lineup.id)
        except:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


