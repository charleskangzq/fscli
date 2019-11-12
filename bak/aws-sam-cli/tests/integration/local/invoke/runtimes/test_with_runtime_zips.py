# coding=utf-8

import os
import tempfile

from subprocess import Popen, PIPE
from nose_parameterized import parameterized, param
import pytest

from tests.integration.local.invoke.invoke_integ_base import InvokeIntegBase
from pathlib import Path


class TestWithDifferentLambdaRuntimeZips(InvokeIntegBase):
    template = Path("runtimes", "template.yaml")

    def setUp(self):

        # Don't delete on close. Need the file to be present for tests to run.
        events_file = tempfile.NamedTemporaryFile(delete=False)
        events_file.write(b'"yolo"')  # Just empty event
        events_file.flush()
        events_file.close()

        self.events_file_path = events_file.name

    def tearDown(self):
        os.remove(self.events_file_path)

    @pytest.mark.timeout(timeout=300, method="thread")
    @parameterized.expand([param("Go1xFunction"), param("Java8Function")])
    def test_runtime_zip(self, function_name):
        command_list = self.get_command_list(
            function_name, template_path=self.template_path, event_path=self.events_file_path
        )

        process = Popen(command_list, stdout=PIPE)
        return_code = process.wait()

        self.assertEqual(return_code, 0)
        process_stdout = b"".join(process.stdout.readlines()).strip()
        self.assertEqual(process_stdout.decode("utf-8"), '"Hello World"')

    @pytest.mark.timeout(timeout=300, method="thread")
    def test_custom_provided_runtime(self):
        command_list = self.get_command_list(
            "CustomBashFunction", template_path=self.template_path, event_path=self.events_file_path
        )

        command_list = command_list + ["--skip-pull-image"]

        process = Popen(command_list, stdout=PIPE)
        return_code = process.wait()

        self.assertEqual(return_code, 0)
        process_stdout = b"".join(process.stdout.readlines()).strip()
        self.assertEqual(process_stdout.decode("utf-8"), '{"body":"hello 曰有冥 world 🐿","statusCode":200,"headers":{}}')