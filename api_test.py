import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/api"
    PRODUCT_URL = "{}/products".format(API_URL)
    PRODUCT_OBJ = {
        "product_id": 3,
        "name": "Watch"
    }

    NEW_BOOK_OBJ = {
        "product_id": 3,
        "name": "T-Shit"
    }

    def _get_each_product_url(self, product_id):
        return "{}/{}".format(ApiTest.PRODUCT_URL, product_id)

    
    def test_1_get_all_product(self):
        r = requests.get(ApiTest.PRODUCT_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 2)

    def test_2_add_new_product(self):
        r = requests.post(ApiTest.PRODUCT_URL, json=ApiTest.PRODUCT_OBJ)
        self.assertEqual(r.status_code, 201)

    def test_3_get_new_product(self):
        product_id = 3
        r = requests.get(self._get_each_book_url(product_id))
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), ApiTest.PRODUCT_OBJ)

    def test_4_update_existing_product(self):
        product_id = 3
        r = requests.put(self._get_each_product_url(product_id),
                         json=ApiTest.PRODUCT_OBJ)
        self.assertEqual(r.status_code, 204)

    def test_5_get_new_product_after_update(self):
        product_id = 3
        r = requests.get(self._get_each_product_url(product_id))
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), ApiTest.PRODUCT_OBJ)

    def test_6_delete_product(self):
        product_id = 3
        r = requests.delete(self._get_each_product_url(product_id))
        self.assertEqual(r.status_code, 204)

    @unittest.expectedFailure
    def test_7_get_new_product_after_delete(self):
        product_id = 3
        r = requests.get(self._get_each_product_url(product_id))
        self.assertEqual(r.status_code, 200)
