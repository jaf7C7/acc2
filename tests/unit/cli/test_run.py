from unittest.mock import Mock
from argparse import ArgumentError
import pytest
from acc.cli import run


def test_run_returns_1_if_argument_error_raised():
    # `argument.option_strings` is a required parameter for the `ArgumentError`
    # constructor.
    bad_argument = Mock(option_strings=['--foo'])
    argument_error = ArgumentError(argument=bad_argument, message='bar')
    run_app = Mock(side_effect=argument_error)
    assert run(app_runner=run_app) == 1


@pytest.mark.parametrize('exception', [BrokenPipeError, KeyboardInterrupt])
def test_run_returns_2_if_broken_pipe_or_kbd_interrupt(exception):
    run_app = Mock(side_effect=[exception])
    assert run(app_runner=run_app) == 2


def test_run_returns_0_if_no_errors():
    run_app = Mock()
    assert run(app_runner=run_app) == 0
