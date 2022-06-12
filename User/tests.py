from rest_framework.test import APITestCase, APITransactionTestCase, APIClient
from rest_framework import status

from .models import Profile
from .serializer import CreateUserSerializer
from .api import UserViewSet


class CreateUserTestCase(APITestCase):

    def setUp(self):
        self.data = {"phone_number": '0913', "email": 'barch@gmail.com', "password": 'mmmm1234', "password2": "mmmm1234"}
        self.UserViewSet = UserViewSet()

    def test_only_phone_number_create(self):
        self.data["email"] = ''
        response = self.client.post("/users/users/user-viewset//", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_email_create(self):
        self.data['phone_number'] = ''
        response = self.client.post("/users/users/user-viewset//", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_none_email_phone(self):
    #     self.assertRaises(ValueError, self.UserViewSet.create)


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = Profile.objects.create(phone_number='0913', email='barch@gmail.com', password='mmmm1234')
        self.data = CreateUserSerializer(self.user).data


    def test_patch_user(self):
        self.data.update({'phone_number': '0914'})
        response1 = self.client.patch(f'/users/users/user-viewset//{self.user.id}/', self.data)
        self.data.update({'email': 'aa@bb.com'})
        response2 = self.client.patch(f'/users/users/user-viewset//{self.user.id}/', self.data)
        self.data.update({'password': '1234mmmm'})
        response3 = self.client.patch(f'/users/users/user-viewset//{self.user.id}/', self.data)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

    def test_put_user(self):
        self.data.update({"phone_number": '0915', "email": 'ch@gmail.com', "password": '123mm4mm'})
        response = self.client.put(f'/users/users/user-viewset//{self.user.id}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dont_allow_delete_user(self):
        response = self.client.delete(f'/users/users/user-viewset//{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_read_user_list(self):
        response = self.client.get('/users/users/user-viewset//')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        response = self.client.get('/users/users/user-viewset//')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#
# class FormulaValidationTestCase(APITestCase):
#
#     def setUp(self):
#         self.formula_validators = RawFormulaValidators()
#
#     def test_zero_division(self):
#         self.assertRaises(ZeroDivisionError, self.formula_validators.division_validators, '587/0')
#
#     def test_no_num_division(self):
#         self.assertRaisesMessage(ValueError, 'This error occurs when you try to divide anything other than numbers',
#                                  self.formula_validators.division_validators, '587/h')
#         self.assertRaisesMessage(ValueError, 'This error occurs when you try to divide anything other than numbers',
#                                  self.formula_validators.division_validators, 'f/8')
#
#
# class ModelTestCase(APITransactionTestCase):
#
#     reset_sequences = True
#
#     def test_calculator(self):
#         obj = Calculator.objects.create(name='test_name', formula='2/5', description= 'dis', variables=['a','b'])
#         self.assertEqual(1, obj.pk)  # database test
#         self.assertEqual('dis', obj.description)  # database test
#         self.assertEqual(['a','b'], obj.variables)  # database test
#         self.assertEqual('2/5', obj.formula)
# # -------------------------------------------------------------------------------------------------------------------
#
# class CalculatorIntegrationTest(APITestCase):
#
#     def setUp(self):
#         self.data = {"name": 'test_name', "formula": '896/8', "description": 'test description',
#                      "variables": ['a', 'b', 'c']}
#         create_response = self.client.post("/api/formula-viewset//", self.data)
#
#
#     def test_calculator_maker_formula_maker(self):
#         client = APIClient()
#         formula_response = client.get('/api/formula-viewset//', format='api')
#         formula_data = formula_response.data[0]
#         calculator_response = client.post('/api/calculator/calculator-viewset//get_formula/', data={'name': formula_data['name']})
#         self.assertEqual(len(formula_response.data), 1)
#         self.assertEqual(formula_response.status_code, status.HTTP_200_OK)
#         self.assertEqual(calculator_response.data['formula'], formula_data['formula'])
#         self.assertEqual(calculator_response.data['variables'], (formula_data['variables']))
#
#
# #------------------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#
