# Copyright (c) 2014, Matt Layman

import tempfile
import unittest

import mock

from tap import TAPTestRunner
from tap.runner import TAPTestResult


class TestTAPTestRunner(unittest.TestCase):

    def test_has_tap_test_result(self):
        runner = TAPTestRunner()
        self.assertEqual(runner.resultclass, TAPTestResult)

    @mock.patch('tap.runner.TAPTestResult')
    def test_runner_uses_outdir(self, test_result_cls):
        '''Test that the test runner sets the TAPTestResult OUTDIR so that TAP
        files will be written to that location.

        Setting class attributes to get the right behavior is a dirty hack, but
        the unittest classes aren't very extensible.
        '''
        outdir = tempfile.mkdtemp()

        TAPTestRunner.set_outdir(outdir)

        self.assertEqual(outdir, test_result_cls.OUTDIR)
