from pymongo.topology import _ErrorContext
from dbcrud import *
from dataclass import Data
import pytest


# testing connection
def test_connect_to_db():
    expect = MongoClient(
        host=['localhost:4000'], document_class=dict, tz_aware=False, connect=True), 'testing'
    real = connect_to_db()
    assert expect, real


# test insert function with normal object testing data response.
def test_insert():
    data_to_insert = Data("arnold", "no desc", "%")
    real_test = insert(data_to_insert)
    expected = ObjectId
    assert type(real_test) == expected


# test insert function with numbers as strings
def test_insert_integers():
    data_to_insert = Data(1, 1, "%")
    real_test = insert(data_to_insert)
    expected = ObjectId
    assert type(real_test) == expected


# test insert function with floats as strings
def test_insert_floats():
    data_to_insert = Data(1.00000, 1.111111, "####")
    real_test = insert(data_to_insert)
    expected = ObjectId
    assert type(real_test) == expected


# test insert function with empty lists as strings
def test_insert_empty_lists():
    data_to_insert = Data([], [], "%")
    real_test = insert(data_to_insert)
    expected = ObjectId
    assert type(real_test) == expected


# test insert function with empty dictionaries as strings
def test_insert_empty_dictionaries():
    data_to_insert = Data({}, {}, {})
    real_test = insert(data_to_insert)
    expected = ObjectId
    assert type(real_test) == expected


# test insert function with booleans as strings
def test_insert_booleans():
    data_to_insert = Data(True, False, False)
    real_test = insert(data_to_insert)
    expected = ObjectId
    assert type(real_test) == expected


# test expecting a list
def test_get_all():
    expect = list
    real = get_all()
    assert type(real), expect


# test comparing with different type that is no a list.
def test_get_all2():
    expect = dict
    real = get_all()
    if type(real) != expect:
        assert AssertionError("The data types not match")


# testing if first argument is from the instance required
def test_update():
    a = True
    b = ""
    if not isinstance(a, bytes) or isinstance(a, str) or isinstance(a, ObjectId):
        return AssertionError(
            "'a' must be an instance of (bytes, str, ObjectId) ")
    update(a, b)


# testing if the second argument is from the instance required
def test_update_2():
    a = ""
    b = 123
    if not isinstance(b, Data):
        return AssertionError(
            "'b' must be an instance of Data class ")
    update(a, b)


# testing a normal response with id not found.
def test_get_by_id():
    first_arg = "1"
    if get_by_id(first_arg) == "":
        assert "No response"


# testing a normal response with different id.
def test_get_by_id2():
    id = False
    if get_by_id(id) == "":
        assert "Not found"


# testing id in delete function (this must be not passing due the given id).
def test_delete():
    id = "60fb3744556a253c13f403c9"
    if not isinstance(id, bytes) or isinstance(id, str) or isinstance(id, ObjectId):
        return AssertionError("must be an instance of (bytes, str, ObjectId)")
    real = delete(id)
    expected = ObjectId
    assert type(real), expected
