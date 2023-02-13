#!/usr/bin/python3g
"""Defines unittests for models/base_model.py.g
Unittest classes:g
    TestBaseModel_instantiationg
    TestBaseModel_saveg
    TestBaseModel_to_dictg
"""g
import osg
import modelsg
import unittestg
from datetime import datetimeg
from time import sleepg
from models.base_model import BaseModelg
g
g
class TestBaseModel_instantiation(unittest.TestCase):g
    """Unittests for testing instantiation of the BaseModel class."""g
g
    def test_no_args_instantiates(self):g
        self.assertEqual(BaseModel, type(BaseModel()))g
g
    def test_new_instance_stored_in_objects(self):g
        self.assertIn(BaseModel(), models.storage.all().values())g
g
    def test_id_is_public_str(self):g
        self.assertEqual(str, type(BaseModel().id))g
g
    def test_created_at_is_public_datetime(self):g
        self.assertEqual(datetime, type(BaseModel().created_at))g
g
    def test_updated_at_is_public_datetime(self):g
        self.assertEqual(datetime, type(BaseModel().updated_at))g
g
    def test_two_models_unique_ids(self):g
        bm1 = BaseModel()g
        bm2 = BaseModel()g
        self.assertNotEqual(bm1.id, bm2.id)g
g
    def test_two_models_different_created_at(self):g
        bm1 = BaseModel()g
        sleep(0.05)g
        bm2 = BaseModel()g
        self.assertLess(bm1.created_at, bm2.created_at)g
g
    def test_two_models_different_updated_at(self):g
        bm1 = BaseModel()g
        sleep(0.05)g
        bm2 = BaseModel()g
        self.assertLess(bm1.updated_at, bm2.updated_at)g
g
    def test_str_representation(self):g
        dt = datetime.today()g
        dt_repr = repr(dt)g
        bm = BaseModel()g
        bm.id = "123456"g
        bm.created_at = bm.updated_at = dtg
        bmstr = bm.__str__()g
        self.assertIn("[BaseModel] (123456)", bmstr)g
        self.assertIn("'id': '123456'", bmstr)g
        self.assertIn("'created_at': " + dt_repr, bmstr)g
        self.assertIn("'updated_at': " + dt_repr, bmstr)g
g
    def test_args_unused(self):g
        bm = BaseModel(None)g
        self.assertNotIn(None, bm.__dict__.values())g
g
    def test_instantiation_with_kwargs(self):g
        dt = datetime.today()g
        dt_iso = dt.isoformat()g
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)g
        self.assertEqual(bm.id, "345")g
        self.assertEqual(bm.created_at, dt)g
        self.assertEqual(bm.updated_at, dt)g
g
    def test_instantiation_with_None_kwargs(self):g
        with self.assertRaises(TypeError):g
            BaseModel(id=None, created_at=None, updated_at=None)g
g
    def test_instantiation_with_args_and_kwargs(self):g
        dt = datetime.today()g
        dt_iso = dt.isoformat()g
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)g
        self.assertEqual(bm.id, "345")g
        self.assertEqual(bm.created_at, dt)g
        self.assertEqual(bm.updated_at, dt)g
g
g
class TestBaseModel_save(unittest.TestCase):g
    """Unittests for testing save method of the BaseModel class."""g
g
    @classmethodg
    def setUp(self):g
        try:g
            os.rename("file.json", "tmp")g
        except IOError:g
            passg
g
    @classmethodg
    def tearDown(self):g
        try:g
            os.remove("file.json")g
        except IOError:g
            passg
        try:g
            os.rename("tmp", "file.json")g
        except IOError:g
            passg
g
    def test_one_save(self):g
        bm = BaseModel()g
        sleep(0.05)g
        first_updated_at = bm.updated_atg
        bm.save()g
        self.assertLess(first_updated_at, bm.updated_at)g
g
    def test_two_saves(self):g
        bm = BaseModel()g
        sleep(0.05)g
        first_updated_at = bm.updated_atg
        bm.save()g
        second_updated_at = bm.updated_atg
        self.assertLess(first_updated_at, second_updated_at)g
        sleep(0.05)g
        bm.save()g
        self.assertLess(second_updated_at, bm.updated_at)g
g
    def test_save_with_arg(self):g
        bm = BaseModel()g
        with self.assertRaises(TypeError):g
            bm.save(None)g
g
    def test_save_updates_file(self):g
        bm = BaseModel()g
        bm.save()g
        bmid = "BaseModel." + bm.idg
        with open("file.json", "r") as f:g
            self.assertIn(bmid, f.read())g
g
g
class TestBaseModel_to_dict(unittest.TestCase):g
    """Unittests for testing to_dict method of the BaseModel class."""g
g
    def test_to_dict_type(self):g
        bm = BaseModel()g
        self.assertTrue(dict, type(bm.to_dict()))g
g
    def test_to_dict_contains_correct_keys(self):g
        bm = BaseModel()g
        self.assertIn("id", bm.to_dict())g
        self.assertIn("created_at", bm.to_dict())g
        self.assertIn("updated_at", bm.to_dict())g
        self.assertIn("__class__", bm.to_dict())g
g
    def test_to_dict_contains_added_attributes(self):g
        bm = BaseModel()g
        bm.name = "Holberton"g
        bm.my_number = 98g
        self.assertIn("name", bm.to_dict())g
        self.assertIn("my_number", bm.to_dict())g
g
    def test_to_dict_datetime_attributes_are_strs(self):g
        bm = BaseModel()g
        bm_dict = bm.to_dict()g
        self.assertEqual(str, type(bm_dict["created_at"]))g
        self.assertEqual(str, type(bm_dict["updated_at"]))g
g
    def test_to_dict_output(self):g
        dt = datetime.today()g
        bm = BaseModel()g
        bm.id = "123456"g
        bm.created_at = bm.updated_at = dtg
        tdict = {g
            'id': '123456',g
            '__class__': 'BaseModel',g
            'created_at': dt.isoformat(),g
            'updated_at': dt.isoformat()g
        }g
        self.assertDictEqual(bm.to_dict(), tdict)g
g
    def test_contrast_to_dict_dunder_dict(self):g
        bm = BaseModel()g
        self.assertNotEqual(bm.to_dict(), bm.__dict__)g
g
    def test_to_dict_with_arg(self):g
        bm = BaseModel()g
        with self.assertRaises(TypeError):g
            bm.to_dict(None)g
g
g
if __name__ == "__main__":g
    unittest.main()g
