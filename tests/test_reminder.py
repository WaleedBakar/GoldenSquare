import pytest
from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

    def test_raises_an_error_when_no_task_is_set():
        reminder =Reminder("Kay")
        with pytest.raises(Exeption) as err:
            reminder.remind()
        error_message = str(err.value)
        assert error_message == "No reminder set!"

