import threading

import pytest

guest_list = pytest.importorskip("guest_list", reason="guest_list.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    A loop whose exit condition is never met would freeze the whole test run,
    so every call gets a time limit instead; the stuck thread is a daemon and
    dies with pytest.
    """
    func = getattr(guest_list, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")

    def limited(*args):
        result = {}

        def run():
            try:
                result["value"] = func(*args)
            except Exception as error:  # re-raised below, in the test itself
                result["error"] = error

        worker = threading.Thread(target=run, daemon=True)
        worker.start()
        worker.join(TIME_LIMIT)
        if worker.is_alive():
            pytest.fail(f"{name}{args} did not finish in {TIME_LIMIT}s: endless loop?")
        if "error" in result:
            raise result["error"]
        return result["value"]

    return limited


def test_add_new_guest():
    guests = {"Ali", "Sara"}
    assert function("add_guest")(guests, "Bek") is True
    assert guests == {"Ali", "Sara", "Bek"}


def test_add_existing_guest():
    guests = {"Ali", "Sara"}
    assert function("add_guest")(guests, "Ali") is False
    assert guests == {"Ali", "Sara"}


def test_add_to_empty_set():
    guests = set()
    assert function("add_guest")(guests, "Nilu") is True
    assert guests == {"Nilu"}


def test_remove_present_guest():
    guests = {"Ali", "Sara"}
    assert function("remove_guest")(guests, "Sara") is True
    assert guests == {"Ali"}


def test_remove_missing_guest():
    guests = {"Ali", "Sara"}
    assert function("remove_guest")(guests, "Timur") is False
    assert guests == {"Ali", "Sara"}


def test_remove_from_empty_set():
    guests = set()
    assert function("remove_guest")(guests, "Ali") is False
    assert guests == set()
