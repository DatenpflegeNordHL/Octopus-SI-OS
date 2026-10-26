import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class SystemPythonContract(unittest.TestCase):
    def test_bundled_verifiers_ignore_shadow_python(self):
        registry = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shadow = root / "python3"
            shadow.write_text("#!/bin/sh\nexit 79\n")
            shadow.chmod(0o755)
            payload = root / "payload.json"
            payload.write_text("{}")
            environment = {**os.environ, "PATH": str(root) + os.pathsep + os.environ["PATH"]}
            for descriptor in sorted(registry.glob("*/verifier.json")):
                config = json.loads(descriptor.read_text())
                script = descriptor.parent / config["script"]
                with self.subTest(verifier=config["id"]):
                    request = {"params": {"tools": ["probe"]}, "payload_utf8": json.dumps({"tool": "probe", "arguments": {}}),
                               "payload_path": str(payload)}
                    result = subprocess.run([str(script)], input=json.dumps(request), text=True, capture_output=True, env=environment, timeout=10)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIsInstance(json.loads(result.stdout)["passed"], bool)
                    self.assertIn("/usr/bin/python3", config["authority"]["executable_commands"])
                    if config["id"] in ["tool_call_allowed", "payload_json_valid"]:
                        self.assertTrue(json.loads(result.stdout)["passed"])


if __name__ == "__main__":
    unittest.main()
